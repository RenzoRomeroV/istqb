const fs = require("fs");
const path = require("path");

const jsonPath = path.join(__dirname, "../src/app/preguntas.json");
const outPath = path.join(__dirname, "upload.sql");

function sqlString(value) {
  if (value === null || value === undefined || value === "") return "NULL";
  return "'" + String(value).replace(/'/g, "''") + "'";
}

const questions = JSON.parse(fs.readFileSync(jsonPath, "utf8"));

const lines = [];
lines.push("-- Generado automaticamente desde preguntas.json. Pegar completo en el SQL Editor de Supabase y ejecutar.");
lines.push("ALTER TABLE preguntas ADD COLUMN IF NOT EXISTS opcion_e TEXT;");
lines.push("TRUNCATE TABLE preguntas;");
lines.push("INSERT INTO preguntas (enunciado, opcion_a, opcion_b, opcion_c, opcion_d, opcion_e, respuesta_correcta, explicacion, modelo_examen) VALUES");

const valueRows = questions.map((q) => {
  return "  (" + [
    sqlString(q.enunciado),
    sqlString(q.opcion_a),
    sqlString(q.opcion_b),
    sqlString(q.opcion_c),
    sqlString(q.opcion_d),
    sqlString(q.opcion_e),
    sqlString(q.respuesta_correcta),
    sqlString(q.explicacion),
    sqlString(q.modelo_examen)
  ].join(", ") + ")";
});

lines.push(valueRows.join(",\n") + ";");

fs.writeFileSync(outPath, lines.join("\n"), "utf8");
console.log(`Generadas ${questions.length} filas en ${outPath}`);
