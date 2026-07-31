import { NextResponse } from "next/server";
import { Client } from "pg";

export async function GET() {
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

    // Obtener todas las preguntas de la base de datos
    const res = await client.query(`
      SELECT id, enunciado, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta, explicacion, modelo_examen
      FROM preguntas
      ORDER BY modelo_examen ASC, id ASC;
    `);

    return NextResponse.json({ questions: res.rows });

  } catch (error: any) {
    console.error("Questions API Error:", error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  } finally {
    await client.end();
  }
}
