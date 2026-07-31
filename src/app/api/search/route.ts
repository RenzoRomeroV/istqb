import { NextResponse } from "next/server";
import { Client } from "pg";

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const q = searchParams.get("q");

  if (!q || !q.trim()) {
    return NextResponse.json({ error: "Query parameter 'q' is required" }, { status: 400 });
  }

  const groqKey = request.headers.get("x-groq-api-key") || process.env.GROQ_API_KEY;
  const connectionString = process.env.DATABASE_URL;

  if (!connectionString) {
    return NextResponse.json({ error: "DATABASE_URL environment variable is missing" }, { status: 500 });
  }

  const client = new Client({
    connectionString,
    ssl: { rejectUnauthorized: false }
  });

  try {
    await client.connect();

    // Limpiamos la query del usuario para que sea apta para plainto_tsquery
    const cleanQuery = q.trim();

    // Búsqueda de texto completo con ranking de relevancia
    const sql = `
      SELECT id, enunciado, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta, explicacion, modelo_examen,
             ts_rank(
               to_tsvector('spanish', enunciado || ' ' || opcion_a || ' ' || opcion_b || ' ' || opcion_c || ' ' || opcion_d), 
               query
             ) as rank
      FROM preguntas, 
           plainto_tsquery('spanish', $1) query
      WHERE to_tsvector('spanish', enunciado || ' ' || opcion_a || ' ' || opcion_b || ' ' || opcion_c || ' ' || opcion_d) @@ query
      ORDER BY rank DESC
      LIMIT 1;
    `;

    const res = await client.query(sql, [cleanQuery]);

    let dbMatchFound = false;
    let matchData: any = null;
    let confidenceVal = 0;

    if (res.rows.length > 0) {
      const match = res.rows[0];
      const rankVal = parseFloat(match.rank);
      
      // Si la coincidencia es válida, la tomamos
      if (rankVal >= 0.05) {
        dbMatchFound = true;
        confidenceVal = Math.min(Math.round(rankVal * 100) + 40, 100);
        matchData = {
          id: match.id,
          enunciado: match.enunciado,
          opcion_a: match.opcion_a,
          opcion_b: match.opcion_b,
          opcion_c: match.opcion_c,
          opcion_d: match.opcion_d,
          respuesta_correcta: match.respuesta_correcta,
          explicacion: match.explicacion,
          modelo_examen: match.modelo_examen
        };
      }
    }

    if (dbMatchFound) {
      return NextResponse.json({
        match: matchData,
        confidence: confidenceVal
      });
    }

    // SI NO SE ENCONTRÓ EN BASE DE DATOS, RESPALDAR CON IA (GROQ) SI SE PROPORCIONÓ UNA CLAVE
    if (groqKey) {
      try {
        const groqRes = await fetch("https://api.groq.com/openai/v1/chat/completions", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${groqKey}`
          },
          body: JSON.stringify({
            model: "llama-3.1-8b-instant",
            messages: [
              {
                role: "system",
                content: "Eres un asistente experto en el examen de certificación ISTQB Foundation Level v4.0. Tu trabajo es analizar la pregunta de examen dictada por voz (que puede contener errores de transcripción o fonética) y sus opciones asociadas. Identifica cuál es la respuesta correcta basándote en el temario oficial del ISTQB. Debes responder EXCLUSIVAMENTE en formato JSON con la siguiente estructura (no agregues explicaciones fuera de ella, usa comillas dobles correctas):\n{\n  \"enunciado\": \"(enunciado corregido y limpio de la pregunta)\",\n  \"opcion_a\": \"(texto limpio de la opción A)\",\n  \"opcion_b\": \"(texto limpio de la opción B)\",\n  \"opcion_c\": \"(texto limpio de la opción C)\",\n  \"opcion_d\": \"(texto limpio de la opción D)\",\n  \"respuesta_correcta\": \"(A, B, C o D)\",\n  \"explicacion\": \"(justificación breve de por qué esa opción es correcta y las otras no)\"\n}"
              },
              {
                role: "user",
                content: `Pregunta dictada: ${cleanQuery}`
              }
            ],
            response_format: { type: "json_object" },
            temperature: 0.1
          })
        });

        if (groqRes.ok) {
          const groqData = await groqRes.json();
          const contentStr = groqData.choices?.[0]?.message?.content;
          if (contentStr) {
            const parsed = JSON.parse(contentStr);
            return NextResponse.json({
              match: {
                id: "ai-generated",
                enunciado: parsed.enunciado,
                opcion_a: parsed.opcion_a,
                opcion_b: parsed.opcion_b,
                opcion_c: parsed.opcion_c,
                opcion_d: parsed.opcion_d,
                respuesta_correcta: parsed.respuesta_correcta.toUpperCase(),
                explicacion: parsed.explicacion,
                modelo_examen: "IA (Groq Llama 3)"
              },
              confidence: 98 // Confianza de IA
            });
          }
        }
      } catch (groqErr) {
        console.error("Groq Fallback Error:", groqErr);
      }
    }

    // Si ni la base de datos ni la IA funcionaron, devolver null
    return NextResponse.json({ match: null, confidence: 0 });

  } catch (error: any) {
    console.error("Search API Error:", error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  } finally {
    await client.end();
  }
}
