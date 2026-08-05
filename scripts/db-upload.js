const { createClient } = require("@supabase/supabase-js");
const fs = require("fs");
const path = require("path");
require("dotenv").config({ path: ".env.local" });

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL;
const supabaseServiceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;

if (!supabaseUrl || !supabaseServiceKey) {
  console.error("Error: Supabase credentials missing in .env.local");
  process.exit(1);
}

const supabase = createClient(supabaseUrl, supabaseServiceKey);

async function main() {
  const jsonPath = path.join(__dirname, "../src/app/preguntas.json");
  if (!fs.existsSync(jsonPath)) {
    console.error("Error: preguntas.json no encontrado en", jsonPath);
    process.exit(1);
  }

  const rawData = fs.readFileSync(jsonPath, "utf8");
  const questions = JSON.parse(rawData);

  console.log(`Leídas ${questions.length} preguntas de preguntas.json.`);
  console.log("Subiendo preguntas a Supabase...");

  // Primero limpiamos la tabla preguntas por si hay datos duplicados previos
  const { error: deleteError } = await supabase.from("preguntas").delete().neq("id", "00000000-0000-0000-0000-000000000000");
  if (deleteError) {
    console.error("Error al limpiar la tabla preguntas:", deleteError);
  } else {
    console.log("Tabla 'preguntas' limpiada con éxito.");
  }

  // Subida en lotes para evitar límites de tamaño de request
  const batchSize = 20;
  for (let i = 0; i < questions.length; i += batchSize) {
    const batch = questions.slice(i, i + batchSize);
    
    // Mapear campos al esquema de la tabla de base de datos
    const dbRows = batch.map(q => ({
      enunciado: q.enunciado,
      opcion_a: q.opcion_a,
      opcion_b: q.opcion_b,
      opcion_c: q.opcion_c,
      opcion_d: q.opcion_d,
      opcion_e: q.opcion_e || null,
      respuesta_correcta: q.respuesta_correcta,
      explicacion: q.explicacion,
      modelo_examen: q.modelo_examen
    }));

    const { error: insertError } = await supabase.from("preguntas").insert(dbRows);

    if (insertError) {
      console.error(`Error al insertar lote ${i / batchSize + 1}:`, insertError);
    } else {
      console.log(`Lote ${i / batchSize + 1} insertado con éxito (${batch.length} preguntas).`);
    }
  }

  console.log("¡Proceso de subida finalizado!");
}

main();
