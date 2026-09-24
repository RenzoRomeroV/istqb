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

// Devuelve solo la parte del texto dictado ANTES de la primera opción ("opción A", "la B",
// "respuesta C", "d)", etc.) — es decir, el enunciado propiamente dicho, sin las alternativas.
// Si no se detecta ningún marcador de opción, devolvemos "" en vez del texto completo: si
// tratáramos todo el texto como "enunciado" (opciones incluidas) y lo comparáramos solo contra
// el campo enunciado (corto) de la fila candidata, el chequeo fallaría casi siempre incluso
// para una coincidencia exacta real, porque la mayoría de esas palabras clave vienen de las
// opciones y nunca aparecen en el enunciado corto. Sin marcador, confiamos solo en el
// solapamiento total (85%) en vez de arriesgarnos a este falso negativo.
function extractEnunciadoPortion(text: string): string {
  const marker = /\b(?:opci[oó]n\s+[a-e]\b|la\s+(?:opci[oó]n\s+)?[a-e]\b|respuesta\s+[a-e]\b|[a-e]\))/i;
  const match = marker.exec(text);
  return match ? text.slice(0, match.index) : "";
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

type TavilyResult = {
  title: string;
  url: string;
  content: string;
};

// Busca en internet vía Tavily cuando la pregunta no está en la base de datos,
// para anclar la respuesta de la IA en resultados reales en vez de solo su conocimiento entrenado.
async function searchTavily(apiKey: string, query: string): Promise<string> {
  try {
    const res = await fetch("https://api.tavily.com/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        api_key: apiKey,
        query: `ISTQB Foundation Level Syllabus v4.0: ${query}`,
        search_depth: "advanced",
        max_results: 5,
        include_answer: true
      })
    });

    if (!res.ok) {
      console.error("Tavily API respondió con error:", await res.text());
      return "";
    }

    const data = await res.json();
    const parts: string[] = [];

    if (data.answer) {
      parts.push(`Resumen de la búsqueda: ${data.answer}`);
    }

    for (const r of (data.results || []) as TavilyResult[]) {
      parts.push(`[${r.title}](${r.url})\n${r.content}`);
    }

    return parts.join("\n\n---\n\n");
  } catch (err) {
    console.error("Tavily Search Error:", err);
    return "";
  }
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
    // Palabras clave SOLO del enunciado (sin las opciones): distintas preguntas a veces
    // reciclan el mismo set de 4 opciones (ej. "gestión de defectos" y "automatización de
    // pruebas" comparten exactamente las mismas 4 herramientas como alternativas). En esos
    // casos el solapamiento combinado puede ser altísimo aunque la pregunta sea otra —
    // por eso exigimos, además, que el enunciado en sí coincida con el de la fila candidata.
    const enunciadoKeywords = extractKeywords(extractEnunciadoPortion(cleanQuery));

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
      let bestEnunciadoOverlap = 1;

      for (const row of res.rows) {
        const rowText = stripAccents(
          `${row.enunciado} ${row.opcion_a} ${row.opcion_b} ${row.opcion_c} ${row.opcion_d} ${row.opcion_e || ""}`.toLowerCase()
        );
        const hits = keywords.filter((k) => rowText.includes(stripAccents(k))).length;
        const overlap = hits / keywords.length;

        if (overlap > bestOverlap) {
          bestOverlap = overlap;
          bestMatch = row;

          if (enunciadoKeywords.length > 0) {
            const rowEnunciado = stripAccents(row.enunciado.toLowerCase());
            const enunciadoHits = enunciadoKeywords.filter((k) => rowEnunciado.includes(stripAccents(k))).length;
            bestEnunciadoOverlap = enunciadoHits / enunciadoKeywords.length;
          } else {
            bestEnunciadoOverlap = 1;
          }
        }
      }

      // Exigimos coincidencia casi exacta (85%+) en el total, Y que el enunciado (sin las
      // opciones) coincida al menos 60% con el de la fila candidata. Con varios simulacros
      // casi idénticos guardados, y varias preguntas distintas que reciclan el mismo set de
      // opciones, un umbral bajo o solo el solapamiento combinado acepta la variante
      // equivocada en vez de caer al respaldo de IA.
      if (bestMatch && bestOverlap >= 0.85 && bestEnunciadoOverlap >= 0.6) {
        dbMatchFound = true;
        // Si pasó el umbral estricto, la tratamos como encontrada al 100%: ya no tiene
        // sentido mostrar el porcentaje bruto de solapamiento (85%, 92%...) cuando el
        // sistema está seguro de que es la pregunta correcta de tu banco.
        confidenceVal = 100;
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

    // SI NO SE ENCONTRÓ EN BASE DE DATOS, RESPALDAR CON IA (GEMINI) SI SE PROPORCIONÓ UNA CLAVE
    // Antes de preguntarle a Gemini, buscamos en internet vía Tavily para anclar la respuesta
    // en resultados reales en vez de depender solo del conocimiento entrenado del modelo.
    const tavilyKey = request.headers.get("x-tavily-api-key") || process.env.TAVILY_API_KEY;

    if (geminiKey) {
      try {
        const temarioContext = await retrieveTemarioContext(client, keywords);
        const webContext = tavilyKey ? await searchTavily(tavilyKey, cleanQuery) : "";

        const groundingSections: string[] = [];
        if (webContext) {
          groundingSections.push(`RESULTADOS DE BÚSQUEDA EN INTERNET (prioridad más alta, son información real y actual):\n\n${webContext}`);
        }
        if (temarioContext) {
          groundingSections.push(`EXTRACTOS DEL TEMARIO OFICIAL DE ISTQB:\n\n${temarioContext}`);
        }

        const systemPrompt = `Eres un asistente experto en el examen de certificación ISTQB Foundation Level v4.0. Tu trabajo es analizar la pregunta de examen (dictada por voz o escrita, puede contener errores de transcripción) y sus opciones asociadas, e identificar cuál es la respuesta correcta.

REGLAS DE FIDELIDAD AL ENUNCIADO DEL USUARIO (OBLIGATORIAS: tienen prioridad sobre cualquier fuente de referencia citada más abajo):
1. El campo "enunciado" y las opciones ("opcion_a" a "opcion_e") deben reproducir EXACTAMENTE lo que el usuario dictó o escribió. Las ÚNICAS correcciones permitidas son errores obvios y puntuales de transcripción de voz: una palabra suelta mal oída por homófono (ej. "opción de" -> "opción D"), separar dos opciones que quedaron pegadas sin pausa, y ajustes de puntuación/mayúsculas. Nunca agregues, quites, resumas ni reformules ideas.
2. PROHIBIDO TERMINANTEMENTE cambiar el sentido o la polaridad de una afirmación: no conviertas "es correcta" en "NO es correcta" (ni viceversa), no agregues ni quites negaciones, no inviertas relaciones temporales ("antes de" <-> "después de"), y no sustituyas conceptos por otros aunque sean del mismo dominio (p. ej. "entorno de producción" por "entorno de prueba representativo"). Esto aplica AUNQUE reconozcas la pregunta y sepas que existe una versión "canónica" distinta con otra redacción en tu entrenamiento o en las fuentes de abajo: esa versión NO es la que te está preguntando este usuario.
3. Las fuentes de referencia (búsqueda web / temario oficial), si existen, se usan EXCLUSIVAMENTE para decidir "respuesta_correcta" y redactar "explicacion". JAMÁS copies o tomes prestado el texto de "enunciado" ni de ninguna opción desde esas fuentes. Si lo que dictó el usuario no coincide con la redacción de las fuentes, transcribe fielmente al usuario, no a la fuente.
4. Si detectas que dos opciones llegaron mezcladas en un solo bloque de texto (error típico de transcripción), sepáralas conservando cada palabra dicha por el usuario en el orden original; no inventes texto nuevo para completar una opción incompleta o ambigua.
5. Para decidir "respuesta_correcta", vuelve a leer la polaridad EXACTA del "enunciado" que fijaste según las reglas 1-4 (si pregunta cuál opción ES correcta, o cuál NO es correcta) y evalúa cada opción respondiendo esa pregunta concreta. Si las fuentes de referencia contienen una versión de esta pregunta con otra polaridad o redacción, NO reutilices su respuesta ni su razonamiento tal cual: la letra correcta para la pregunta con polaridad opuesta puede ser distinta (incluso la inversa) a la de esa fuente. Razona sobre las opciones tal como las dictó el usuario, no sobre las de la fuente.

${groundingSections.length > 0
            ? `Usa las siguientes fuentes SOLO para determinar cuál de las opciones dictadas por el usuario es la correcta y para redactar la explicación (en orden de prioridad). No son una fuente del texto del enunciado ni de las opciones:\n\n${groundingSections.join("\n\n---\n\n")}`
            : "No se encontró un extracto del temario oficial ni resultados de búsqueda para esta pregunta. Respóndela con tu mejor criterio experto en ISTQB Foundation Level v4.0, sin alterar el enunciado ni las opciones dictadas por el usuario."
          }

Debes responder EXCLUSIVAMENTE en formato JSON con esta estructura exacta (sin texto ni markdown fuera del JSON, comillas dobles correctas). La pregunta puede tener 4 o 5 alternativas y puede tener más de una respuesta correcta:
{
  "enunciado": "(enunciado EXACTO dictado por el usuario, solo con corrección de homófonos/puntuación obvios; SIN reescritura de contenido ni cambio de polaridad)",
  "opcion_a": "(texto EXACTO de la opción A tal como la dictó el usuario, con la misma corrección mínima)",
  "opcion_b": "(texto EXACTO de la opción B tal como la dictó el usuario, con la misma corrección mínima)",
  "opcion_c": "(texto EXACTO de la opción C tal como la dictó el usuario, con la misma corrección mínima)",
  "opcion_d": "(texto EXACTO de la opción D tal como la dictó el usuario, con la misma corrección mínima)",
  "opcion_e": "(texto EXACTO de la opción E tal como la dictó el usuario, o null si la pregunta solo tiene 4 opciones)",
  "respuesta_correcta": "(una o más letras en mayúscula separadas por coma, ej. \\"B\\" o \\"B,E\\")",
  "explicacion": "(justificación breve de por qué esa opción es correcta y las otras no)"
}`;

        const geminiRes = await fetch(
          `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=${geminiKey}`,
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              systemInstruction: { parts: [{ text: systemPrompt }] },
              contents: [{ role: "user", parts: [{ text: `Pregunta: ${cleanQuery}` }] }],
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

            // GUARDRAIL DE FIDELIDAD: verificamos que lo que Gemini devolvió realmente
            // corresponda a la pregunta que dictó el usuario, y no a una versión "canónica"
            // distinta que haya encontrado en la búsqueda web o en su propio entrenamiento
            // (el bug real que motivó esta verificación: misma temática, enunciado y opciones
            // reescritas por completo, incluyendo la polaridad de la pregunta).
            const aiCombinedText = [
              parsed.enunciado,
              parsed.opcion_a,
              parsed.opcion_b,
              parsed.opcion_c,
              parsed.opcion_d,
              parsed.opcion_e
            ].filter(Boolean).join(" ");
            const aiKeywords = new Set(extractKeywords(aiCombinedText).map((k) => stripAccents(k)));
            const fidelityHits = keywords.filter((k) => aiKeywords.has(stripAccents(k))).length;
            const fidelityOverlap = keywords.length > 0 ? fidelityHits / keywords.length : 1;

            if (fidelityOverlap < 0.4) {
              console.error(
                "Guardrail de fidelidad: la respuesta de Gemini fue rechazada porque su enunciado/opciones " +
                "no coinciden con lo dictado por el usuario (posible sustitución por una versión distinta " +
                "de la pregunta encontrada en la web o en el entrenamiento del modelo).",
                { fidelityOverlap, cleanQuery, aiEnunciado: parsed.enunciado, keywords }
              );
              // No devolvemos este match: dejamos que el flujo caiga al `return` final de
              // `match: null` en vez de mostrarle al usuario, con falsa confianza, la
              // respuesta a una pregunta que no es la que hizo.
            } else {
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
                  modelo_examen: webContext
                    ? "IA con búsqueda web (Gemini)"
                    : temarioContext
                      ? "IA anclada al temario oficial (Gemini)"
                      : "IA (Gemini)"
                },
                confidence: webContext ? 95 : temarioContext ? 90 : 65
              });
            }
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
