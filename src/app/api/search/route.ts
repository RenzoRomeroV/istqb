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

type TemarioChunkRow = {
  fuente: string;
  contenido: string;
};

// Busca los fragmentos del temario oficial más relevantes para anclar la respuesta de la IA,
// usando la misma técnica de OR + coincidencia de palabras clave que la búsqueda de preguntas.
async function retrieveTemarioContext(client: Client, keywords: string[]): Promise<string> {
  if (keywords.length === 0) return "";

  const orQuery = keywords.join(" | ");

  const sql = `
    SELECT fuente, contenido
    FROM temario_chunks,
         to_tsquery('spanish', $1) query
    WHERE to_tsvector('spanish', contenido) @@ query
    ORDER BY ts_rank(to_tsvector('spanish', contenido), query) DESC
    LIMIT 10;
  `;

  const res = await client.query<TemarioChunkRow>(sql, [orQuery]);

  const scored = res.rows
    .map((row) => {
      const rowText = stripAccents(row.contenido.toLowerCase());
      const hits = keywords.filter((k) => rowText.includes(stripAccents(k))).length;
      return { ...row, overlap: hits / keywords.length };
    })
    .filter((c) => c.overlap > 0)
    .sort((a, b) => b.overlap - a.overlap);

  return scored
    .slice(0, 3)
    .map((c) => `[Fuente: ${c.fuente}]\n${c.contenido}`)
    .join("\n\n---\n\n");
}

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const q = searchParams.get("q");

  if (!q || !q.trim()) {
    return NextResponse.json({ error: "Query parameter 'q' is required" }, { status: 400 });
  }

  const geminiKey = request.headers.get("x-gemini-api-key") || process.env.GEMINI_API_KEY;
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

    // SI NO SE ENCONTRÓ EN BASE DE DATOS, RESPALDAR CON IA (GEMINI + BÚSQUEDA WEB) SI SE PROPORCIONÓ UNA CLAVE
    if (geminiKey) {
      try {
        const temarioContext = await retrieveTemarioContext(client, keywords);

        const systemPrompt = `Eres un asistente experto en el examen de certificación ISTQB Foundation Level v4.0. Tu trabajo es analizar la pregunta de examen (dictada por voz o escrita, puede contener errores de transcripción) y sus opciones asociadas, e identificar cuál es la respuesta correcta.

${temarioContext
            ? `Ancla tu respuesta PRINCIPALMENTE en los siguientes extractos del temario oficial de ISTQB. Si no alcanzan para responder con certeza, usa la búsqueda web para verificar contra fuentes oficiales de ISTQB antes de responder:\n\n${temarioContext}`
            : "No se encontró un extracto específico del temario oficial cargado para esta pregunta. Usa la búsqueda web para encontrar y verificar la respuesta contra fuentes oficiales de ISTQB (istqb.org, sílabos oficiales) antes de responder."
          }

Debes responder EXCLUSIVAMENTE en formato JSON con esta estructura exacta (sin texto ni markdown fuera del JSON, comillas dobles correctas). La pregunta puede tener 4 o 5 alternativas y puede tener más de una respuesta correcta:
{
  "enunciado": "(enunciado corregido y limpio de la pregunta)",
  "opcion_a": "(texto limpio de la opción A)",
  "opcion_b": "(texto limpio de la opción B)",
  "opcion_c": "(texto limpio de la opción C)",
  "opcion_d": "(texto limpio de la opción D)",
  "opcion_e": "(texto limpio de la opción E, o null si la pregunta solo tiene 4 opciones)",
  "respuesta_correcta": "(una o más letras en mayúscula separadas por coma, ej. \\"B\\" o \\"B,E\\")",
  "explicacion": "(justificación breve de por qué esa opción es correcta y las otras no)"
}`;

        const geminiRes = await fetch(
          `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${geminiKey}`,
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              systemInstruction: { parts: [{ text: systemPrompt }] },
              contents: [{ role: "user", parts: [{ text: `Pregunta: ${cleanQuery}` }] }],
              tools: [{ google_search: {} }],
              generationConfig: { temperature: 0.1 }
            })
          }
        );

        if (geminiRes.ok) {
          const geminiData = await geminiRes.json();
          const contentStr: string | undefined = geminiData.candidates?.[0]?.content?.parts
            ?.map((p: { text?: string }) => p.text)
            .filter(Boolean)
            .join("");

          if (contentStr) {
            const cleanJson = contentStr.replace(/^```(?:json)?\s*/i, "").replace(/```\s*$/, "").trim();
            const parsed = JSON.parse(cleanJson);
            const usedSearch = Boolean(geminiData.candidates?.[0]?.groundingMetadata?.webSearchQueries?.length);

            return NextResponse.json({
              match: {
                id: "ai-generated",
                enunciado: parsed.enunciado,
                opcion_a: parsed.opcion_a,
                opcion_b: parsed.opcion_b,
                opcion_c: parsed.opcion_c,
                opcion_d: parsed.opcion_d,
                opcion_e: parsed.opcion_e || null,
                respuesta_correcta: String(parsed.respuesta_correcta).toUpperCase(),
                explicacion: parsed.explicacion,
                modelo_examen: temarioContext
                  ? "IA anclada al temario oficial (Gemini)"
                  : usedSearch
                    ? "IA con búsqueda web (Gemini)"
                    : "IA (Gemini)"
              },
              confidence: temarioContext ? 90 : usedSearch ? 80 : 65
            });
          }
        } else {
          console.error("Gemini API respondió con error:", await geminiRes.text());
        }
      } catch (geminiErr) {
        console.error("Gemini Fallback Error:", geminiErr);
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
