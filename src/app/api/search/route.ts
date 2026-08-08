import { NextResponse } from "next/server";
import { Client } from "pg";

// Palabras que aparecen en casi cualquier pregunta y no ayudan a identificarla
const STOPWORDS = new Set([
  "cual", "cuales", "según", "durante", "opcion", "opción", "opciones",
  "para", "como", "cómo", "este", "esta", "esto", "estos", "estas",
  "desde", "hasta", "entre", "sobre", "cuando", "cuándo", "donde", "dónde",
  "porque", "respuesta", "pregunta", "siguiente", "siguientes",
  "mejor", "describe", "describen", "utiliza", "utilizan", "istqb", "foundation"
]);

function stripAccents(text: string): string {
  return text.normalize("NFD").replace(new RegExp("[\\u0300-\\u036f]", "g"), "");
}

function extractKeywords(text: string): string[] {
  return Array.from(new Set(
    text
      .toLowerCase()
      .split(/[^a-zñáéíóúü0-9]+/i)
      .filter((w) => w.length > 3 && !STOPWORDS.has(stripAccents(w)))
  ));
}

type PreguntaRow = {
  id: string;
  enunciado: string;
  opcion_a: string;
  opcion_b: string;
  opcion_c: string;
  opcion_d: string;
  opcion_e: string | null;
  respuesta_correcta: string;
  explicacion: string;
  modelo_examen: string;
};

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

    const cleanQuery = q.trim();
    const keywords = extractKeywords(cleanQuery);

    let dbMatchFound = false;
    let matchData: any = null;
    let confidenceVal = 0;

    if (keywords.length > 0) {
      // Unimos las palabras clave con OR: ninguna palabra mal transcrita anula la búsqueda.
      // Traemos varios candidatos por ranking y luego confirmamos el mejor por coincidencia real.
      const orQuery = keywords.join(" | ");

      const sql = `
        SELECT id, enunciado, opcion_a, opcion_b, opcion_c, opcion_d, opcion_e, respuesta_correcta, explicacion, modelo_examen,
               ts_rank(
                 to_tsvector('spanish', enunciado || ' ' || opcion_a || ' ' || opcion_b || ' ' || opcion_c || ' ' || opcion_d || ' ' || COALESCE(opcion_e, '')),
                 query
               ) as rank
        FROM preguntas,
             to_tsquery('spanish', $1) query
        WHERE to_tsvector('spanish', enunciado || ' ' || opcion_a || ' ' || opcion_b || ' ' || opcion_c || ' ' || opcion_d || ' ' || COALESCE(opcion_e, '')) @@ query
        ORDER BY rank DESC
        LIMIT 5;
      `;

      const res = await client.query<PreguntaRow>(sql, [orQuery]);

      let bestMatch: PreguntaRow | null = null;
      let bestOverlap = 0;

      for (const row of res.rows) {
        const rowText = stripAccents(
          `${row.enunciado} ${row.opcion_a} ${row.opcion_b} ${row.opcion_c} ${row.opcion_d} ${row.opcion_e || ""}`.toLowerCase()
        );
        const hits = keywords.filter((k) => rowText.includes(stripAccents(k))).length;
        const overlap = hits / keywords.length;

        if (overlap > bestOverlap) {
          bestOverlap = overlap;
          bestMatch = row;
        }
      }

      // Exigimos al menos 50% de las palabras clave para no aceptar coincidencias débiles
      if (bestMatch && bestOverlap >= 0.5) {
        dbMatchFound = true;
        confidenceVal = Math.round(bestOverlap * 100);
        matchData = {
          id: bestMatch.id,
          enunciado: bestMatch.enunciado,
          opcion_a: bestMatch.opcion_a,
          opcion_b: bestMatch.opcion_b,
          opcion_c: bestMatch.opcion_c,
          opcion_d: bestMatch.opcion_d,
          opcion_e: bestMatch.opcion_e,
          respuesta_correcta: bestMatch.respuesta_correcta,
          explicacion: bestMatch.explicacion,
          modelo_examen: bestMatch.modelo_examen
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
