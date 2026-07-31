const { createClient } = require("@supabase/supabase-js");
require("dotenv").config({ path: ".env.local" });

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL;
const supabaseServiceKey = process.env.SUPABASE_SERVICE_ROLE_KEY; // Requerido para operaciones administrativas

if (!supabaseUrl || !supabaseServiceKey) {
  console.error("Error: Supabase credentials missing in .env.local");
  process.exit(1);
}

const supabase = createClient(supabaseUrl, supabaseServiceKey);

async function main() {
  console.log("Conectando a Supabase vía API REST (HTTPS)...");
  
  // Vamos a intentar hacer un query simple a la tabla preguntas
  const { data, error } = await supabase.from("preguntas").select("*").limit(1);
  
  if (error) {
    console.error("Error al conectar o consultar la tabla preguntas:", error);
    console.log("Nota: Es probable que la tabla 'preguntas' aún no esté creada en la interfaz de Supabase.");
  } else {
    console.log("¡Conexión REST exitosa! Datos obtenidos:", data);
  }
}

main();
