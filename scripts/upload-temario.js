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
  const jsonPath = path.join(__dirname, "temario_chunks.json");
  if (!fs.existsSync(jsonPath)) {
    console.error("Error: temario_chunks.json no encontrado en", jsonPath, "- corre primero: py scripts/extract_temario.py");
    process.exit(1);
  }

  const rawData = fs.readFileSync(jsonPath, "utf8");
  const chunks = JSON.parse(rawData);

  console.log(`Leídos ${chunks.length} fragmentos de temario_chunks.json.`);
  console.log("Subiendo fragmentos del temario a Supabase...");

  const { error: deleteError } = await supabase.from("temario_chunks").delete().neq("id", "00000000-0000-0000-0000-000000000000");
  if (deleteError) {
    console.error("Error al limpiar la tabla temario_chunks:", deleteError);
    process.exitCode = 1;
    return;
  } else {
    console.log("Tabla 'temario_chunks' limpiada con éxito.");
  }

  const batchSize = 20;
  for (let i = 0; i < chunks.length; i += batchSize) {
    const batch = chunks.slice(i, i + batchSize);

    const dbRows = batch.map(c => ({
      fuente: c.fuente,
      orden: c.orden,
      contenido: c.contenido
    }));

    const { error: insertError } = await supabase.from("temario_chunks").insert(dbRows);

    if (insertError) {
      console.error(`Error al insertar lote ${i / batchSize + 1}:`, insertError);
      process.exitCode = 1;
    } else {
      console.log(`Lote ${i / batchSize + 1} insertado con éxito (${batch.length} fragmentos).`);
    }
  }

  console.log("¡Proceso de subida del temario finalizado!");
}

main();
