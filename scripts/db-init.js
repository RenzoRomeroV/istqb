const { Client } = require("pg");
require("dotenv").config({ path: ".env.local" });

const connectionString = process.env.DATABASE_URL;

if (!connectionString) {
  console.error("Error: DATABASE_URL no está definida en .env.local");
  process.exit(1);
}

const client = new Client({
  connectionString: connectionString,
  ssl: {
    rejectUnauthorized: false // Requerido para conexiones seguras con Supabase
  }
});

async function main() {
  try {
    await client.connect();
    console.log("Conectado con éxito a la base de datos de Supabase PostgreSQL.");

    // 1. Crear tabla de preguntas
    await client.query(`
      CREATE TABLE IF NOT EXISTS preguntas (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        enunciado TEXT NOT NULL,
        opcion_a TEXT NOT NULL,
        opcion_b TEXT NOT NULL,
        opcion_c TEXT NOT NULL,
        opcion_d TEXT NOT NULL,
        respuesta_correcta TEXT NOT NULL,
        explicacion TEXT,
        modelo_examen TEXT NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
      );
    `);
    console.log("Tabla 'preguntas' creada o ya existente.");

    // 1.1 Agregar columna opcion_e para preguntas con 5ta alternativa (no todas la tienen)
    await client.query(`ALTER TABLE preguntas ADD COLUMN IF NOT EXISTS opcion_e TEXT;`);
    console.log("Columna 'opcion_e' asegurada en la tabla 'preguntas'.");

    // 2. Crear un índice GIN para búsqueda de texto completo (Full Text Search) en español
    // Esto acelerará enormemente las búsquedas por voz.
    // Recreamos el índice porque cambió la expresión indexada (ahora incluye opcion_e)
    await client.query(`DROP INDEX IF EXISTS preguntas_fts_idx;`);
    await client.query(`
      CREATE INDEX preguntas_fts_idx ON preguntas
      USING gin(to_tsvector('spanish', enunciado || ' ' || opcion_a || ' ' || opcion_b || ' ' || opcion_c || ' ' || opcion_d || ' ' || COALESCE(opcion_e, '')));
    `);
    console.log("Índice de búsqueda por texto completo (FTS) en español configurado (incluye opcion_e).");

  } catch (err) {
    console.error("Error al inicializar la base de datos:", err);
    process.exitCode = 1;
  } finally {
    await client.end();
  }
}

main();
