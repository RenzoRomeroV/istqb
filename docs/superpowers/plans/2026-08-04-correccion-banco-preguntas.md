# Corrección del banco de preguntas ISTQB — Plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Corregir `scripts/extract_all.py` para que el enunciado de cada pregunta nunca se confunda con una opción, agregar soporte para una 5ª alternativa (E), y validar automáticamente el resultado antes de subirlo a Postgres.

**Architecture:** Un script Python (`scripts/extract_all.py`) parsea DOCX/PDF de los Exámenes C y D a `src/app/preguntas.json`. Dos scripts Node (`scripts/db-init.js`, `scripts/db-upload.js`) crean/actualizan el esquema de Postgres (vía Supabase) y suben ese JSON. Dos rutas API de Next.js (`src/app/api/questions/route.ts`, `src/app/api/search/route.ts`) exponen esos datos al frontend.

**Tech Stack:** Python 3.12 (`python-docx`, `pypdf`, stdlib `unittest`), Node.js (`pg`, `@supabase/supabase-js`), Next.js API routes (TypeScript), Postgres (Supabase).

## Global Constraints

- Ejecutar Python en esta máquina Windows con el comando `py` (no `python3`, que no está disponible como alias).
- No agregar nuevas dependencias de Python: no hay `requirements.txt` en el proyecto, así que los tests usan solo `unittest` (stdlib).
- Los comandos `node scripts/*.js` deben correrse desde la raíz de `simulador-istq/` (los scripts cargan `.env.local` con una ruta relativa vía `dotenv`).
- El Examen B queda fuera de alcance de este plan (ver spec: PDF de preguntas escaneado sin texto extraíble).
- No modificar `src/app/page.tsx` ni ningún archivo de UI — ese trabajo es del sub-proyecto 2 (voz).

---

### Task 1: Función pura `split_enunciado_and_options` + tests unitarios

**Files:**
- Modify: `scripts/extract_all.py`
- Create: `scripts/test_extract_all.py`

**Interfaces:**
- Produces: `split_enunciado_and_options(items: list) -> tuple[list, list[str]]` en `scripts/extract_all.py`, definida a nivel de módulo (junto a `OPTION_MARKER_RE`). Recibe una lista de strings (y opcionalmente otros tipos, que cortan el escaneo), devuelve `(enunciado_items, options)`.

- [ ] **Step 1: Escribir el test que falla**

Crear `scripts/test_extract_all.py`:

```python
import unittest
from extract_all import split_enunciado_and_options


class TestSplitEnunciadoAndOptions(unittest.TestCase):
    def test_four_options_clean_split(self):
        items = [
            "¿Cuál de las siguientes es una técnica de caja negra?",
            "a) Análisis de valor límite",
            "b) Cobertura de sentencias",
            "c) Revisión por pares",
            "d) Análisis estático",
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(enunciado, ["¿Cuál de las siguientes es una técnica de caja negra?"])
        self.assertEqual(options, [
            "Análisis de valor límite",
            "Cobertura de sentencias",
            "Revisión por pares",
            "Análisis estático",
        ])

    def test_five_options_supported(self):
        items = [
            "¿Cuáles de las siguientes son actividades del proceso de pruebas?",
            "a) Planificación",
            "b) Análisis",
            "c) Diseño",
            "d) Implementación",
            "e) Ejecución",
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(len(options), 5)
        self.assertEqual(options[4], "Ejecución")

    def test_enunciado_paragraph_without_marker_is_not_swallowed(self):
        # Caso del bug real: el enunciado no tiene marcador de letra,
        # no debe tratarse como si fuera la opción A.
        items = [
            "¿Cuál de los siguientes es un objetivo típico de una prueba?",
            "a) Validación del cumplimiento de los requisitos documentados",
            "b) Causar fallos e identificar defectos",
            "c) Iniciación a los errores e identificación de las causas profundas",
            "d) Verificar que el objeto de ensayo cumple las expectativas del usuario",
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(len(enunciado), 1)
        self.assertIn("objetivo típico de una prueba", enunciado[0])
        self.assertEqual(len(options), 4)

    def test_stops_at_first_non_matching_line(self):
        items = [
            "Texto de enunciado",
            "más texto de enunciado que no es una opción",
            "a) Primera opción",
            "b) Segunda opción",
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(enunciado, ["Texto de enunciado", "más texto de enunciado que no es una opción"])
        self.assertEqual(options, ["Primera opción", "Segunda opción"])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Correr el test y verificar que falla**

Run: `py scripts/test_extract_all.py -v`
Expected: `ImportError: cannot import name 'split_enunciado_and_options' from 'extract_all'`

- [ ] **Step 3: Implementar la función en `scripts/extract_all.py`**

Agregar, antes de `def process_question(...)` (línea 72 actual):

```python
OPTION_MARKER_RE = re.compile(r'^([a-e])\)\s*', re.IGNORECASE)


def split_enunciado_and_options(items):
    """Escanea `items` desde el final hacia el principio, tomando como opción cada
    línea de texto que empieza con un marcador de letra (a) a e)). Se detiene en
    cuanto encuentra un ítem que no matchea (o que no es texto) — ese ítem y todos
    los anteriores quedan como parte del enunciado. Devuelve (enunciado_items, options)."""
    remaining = list(items)
    opt_candidates = []
    while remaining:
        curr = remaining[-1]
        if not isinstance(curr, str):
            break
        match = OPTION_MARKER_RE.match(curr.strip())
        if not match:
            break
        clean_opt = OPTION_MARKER_RE.sub('', curr.strip(), count=1).strip()
        opt_candidates.insert(0, clean_opt)
        remaining.pop()
    return remaining, opt_candidates
```

- [ ] **Step 4: Correr el test y verificar que pasa**

Run: `py scripts/test_extract_all.py -v`
Expected: `OK` (4 tests pasan)

- [ ] **Step 5: Commit**

```bash
git add scripts/extract_all.py scripts/test_extract_all.py
git commit -m "feat: agregar split_enunciado_and_options con tests unitarios"
```

---

### Task 2: Conectar la función al parser real y soportar 5ª alternativa

**Files:**
- Modify: `scripts/extract_all.py`

**Interfaces:**
- Consumes: `split_enunciado_and_options` de Task 1.
- Produces: `process_question` ahora deja `q["opciones"]` con 4 o 5 elementos correctamente separados del enunciado. `compiled_questions` (dentro de `main()`) incluye la clave `"opcion_e"` (string o `None`) en cada dict.

- [ ] **Step 1: Reemplazar el cuerpo de `process_question`**

Reemplazar la función completa (actualmente líneas 72-116) por:

```python
def process_question(q, items, questions_list):
    if not items:
        return
    last_item = items[-1]
    has_selector_last = isinstance(last_item, str) and ("seleccione" in last_item.lower() and "opci" in last_item.lower())
    if has_selector_last:
        items.pop()

    options = []
    enunciado_parts = []

    if items and isinstance(items[-1], Table):
        opt_table = items.pop()
        for row in opt_table.rows:
            row_text = " ".join([cell.text.strip() for cell in row.cells])
            clean_opt = re.sub(r'^[a-e]\)\s*', '', row_text, flags=re.IGNORECASE).strip()
            options.append(clean_opt)
    else:
        if items and isinstance(items[-1], str):
            last_p = items[-1]
            clean_last = re.sub(r'\s*Seleccione\s+(?:UNA|DOS)\s+opci(?:ó|o)nes?\.?$', '', last_p, flags=re.IGNORECASE).strip()
            items[-1] = clean_last

        items, options = split_enunciado_and_options(items)

    for item in items:
        if isinstance(item, str):
            enunciado_parts.append(item)
        elif isinstance(item, Table):
            enunciado_parts.append(format_table_as_text(item))

    q["enunciado"] = "\n".join(enunciado_parts)
    q["opciones"] = options
    questions_list.append(q)
```

Nota: el único cambio en la rama de `Table` es el regex `[a-d]` → `[a-e]`; el resto es igual a hoy.

- [ ] **Step 2: Actualizar la compilación de resultados para Exam C**

En `main()`, reemplazar el bloque del Exam C (actualmente):

```python
    for q in questions_c:
        num = q["num"]
        if len(q["opciones"]) == 4:
            compiled_questions.append({
                "enunciado": q["enunciado"],
                "opcion_a": q["opciones"][0],
                "opcion_b": q["opciones"][1],
                "opcion_c": q["opciones"][2],
                "opcion_d": q["opciones"][3],
                "respuesta_correcta": answers_c.get(num, ""),
                "explicacion": explanations_c.get(num, ""),
                "modelo_examen": "C"
            })
```

por:

```python
    for q in questions_c:
        num = q["num"]
        if len(q["opciones"]) >= 4:
            compiled_questions.append({
                "enunciado": q["enunciado"],
                "opcion_a": q["opciones"][0],
                "opcion_b": q["opciones"][1],
                "opcion_c": q["opciones"][2],
                "opcion_d": q["opciones"][3],
                "opcion_e": q["opciones"][4] if len(q["opciones"]) >= 5 else None,
                "respuesta_correcta": answers_c.get(num, ""),
                "explicacion": explanations_c.get(num, ""),
                "modelo_examen": "C"
            })
        else:
            print(f"ADVERTENCIA: Examen C Pregunta {num} descartada, solo se detectaron {len(q['opciones'])} opciones")
```

- [ ] **Step 3: Aplicar el mismo cambio al bloque del Exam D**

Reemplazar el bloque equivalente de `questions_d` con la misma estructura (mismo patrón, cambiando `answers_c`/`explanations_c`/`"C"` por `answers_d`/`explanations_d`/`"D"`, y el mensaje de advertencia a `"Examen D"`).

- [ ] **Step 4: Correr el script completo contra los archivos reales**

Run: `cd simulador-istq && py scripts/extract_all.py`
Expected: imprime `Exam C: Parsed N questions...` y `Exam D: Parsed M questions...`, sin excepciones. Un examen ISTQB Foundation estándar tiene 40 preguntas — si N o M no es 40, cuenta manualmente las preguntas en el DOCX correspondiente (`2. Preguntas - C.docx` / `3. Preguntas - D.docx`) para confirmar si son menos en la fuente o si el parser descartó alguna. Anota si aparece alguna línea `ADVERTENCIA:` (indicaría una pregunta con menos de 4 opciones detectadas — investigar esa pregunta puntual en el DOCX original antes de continuar).

- [ ] **Step 5: Verificar manualmente el caso conocido del bug**

Run:
```bash
node -e "
const data = require('./src/app/preguntas.json');
const q = data.find(q => q.enunciado.includes('objetivo típico de una prueba'));
console.log(JSON.stringify(q, null, 2));
"
```
Expected: `enunciado` es `"¿Cuál de los siguientes es un objetivo típico de una prueba?"`, y `opcion_a` es `"Validación del cumplimiento de los requisitos documentados"` (ya NO el enunciado). Confirma también que el conteo de `enunciado` vacíos bajó a 0:
```bash
node -e "
const data = require('./src/app/preguntas.json');
console.log('vacios:', data.filter(q => !q.enunciado || !q.enunciado.trim()).length);
console.log('con opcion_e:', data.filter(q => q.opcion_e).length);
"
```
Expected: `vacios: 0`, `con opcion_e: 4` (o el número real de preguntas de 5 alternativas detectadas).

- [ ] **Step 6: Commit**

```bash
git add scripts/extract_all.py src/app/preguntas.json
git commit -m "fix: separar enunciado de opciones por marcador de letra, soportar 5ta alternativa"
```

---

### Task 3: Validación automática post-extracción

**Files:**
- Modify: `scripts/extract_all.py`
- Modify: `scripts/test_extract_all.py`

**Interfaces:**
- Produces: `validate_questions(compiled_questions: list[dict]) -> list[str]` en `scripts/extract_all.py`. `main()` llama a esta función antes de escribir el JSON; si la lista de errores no está vacía, imprime cada error y termina con `sys.exit(1)` sin escribir el archivo.

- [ ] **Step 1: Escribir los tests que fallan**

Agregar a `scripts/test_extract_all.py`:

```python
from extract_all import split_enunciado_and_options, validate_questions


class TestValidateQuestions(unittest.TestCase):
    def _valid_question(self, **overrides):
        q = {
            "enunciado": "¿Cuál de las siguientes es una técnica de caja negra?",
            "opcion_a": "Análisis de valor límite",
            "opcion_b": "Cobertura de sentencias",
            "opcion_c": "Revisión por pares",
            "opcion_d": "Análisis estático",
            "opcion_e": None,
            "respuesta_correcta": "A",
            "explicacion": "Porque sí.",
            "modelo_examen": "C",
        }
        q.update(overrides)
        return q

    def test_valid_question_has_no_errors(self):
        errors = validate_questions([self._valid_question()])
        self.assertEqual(errors, [])

    def test_empty_enunciado_is_flagged(self):
        errors = validate_questions([self._valid_question(enunciado="")])
        self.assertEqual(len(errors), 1)
        self.assertIn("enunciado", errors[0])

    def test_missing_option_text_for_correct_answer_letter_is_flagged(self):
        errors = validate_questions([self._valid_question(respuesta_correcta="E", opcion_e=None)])
        self.assertEqual(len(errors), 1)
        self.assertIn("E", errors[0])

    def test_multi_letter_answer_with_all_options_present_is_valid(self):
        q = self._valid_question(respuesta_correcta="B,E", opcion_e="Quinta opción")
        errors = validate_questions([q])
        self.assertEqual(errors, [])
```

(Actualizar el `import` al inicio del archivo para incluir `validate_questions` junto a `split_enunciado_and_options`, como se muestra arriba.)

- [ ] **Step 2: Correr los tests y verificar que fallan**

Run: `py scripts/test_extract_all.py -v`
Expected: `ImportError: cannot import name 'validate_questions' from 'extract_all'`

- [ ] **Step 3: Implementar `validate_questions` en `scripts/extract_all.py`**

Agregar la función justo antes de `def main():`:

```python
def validate_questions(compiled_questions):
    errors = []
    opt_fields = {"A": "opcion_a", "B": "opcion_b", "C": "opcion_c", "D": "opcion_d", "E": "opcion_e"}

    for q in compiled_questions:
        label = f"Examen {q.get('modelo_examen', '?')} - {q.get('enunciado', '')[:50]!r}"

        if not q.get("enunciado") or len(q["enunciado"].strip()) < 10:
            errors.append(f"{label}: enunciado vacío o demasiado corto")

        respuestas = [r.strip().upper() for r in q.get("respuesta_correcta", "").split(",") if r.strip()]
        for letra in respuestas:
            field = opt_fields.get(letra)
            if field is None or not q.get(field):
                errors.append(f"{label}: respuesta_correcta incluye '{letra}' pero {field or 'esa letra'} está vacío")

        num_opciones = sum(1 for f in ("opcion_a", "opcion_b", "opcion_c", "opcion_d", "opcion_e") if q.get(f))
        if num_opciones < 4:
            errors.append(f"{label}: solo se capturaron {num_opciones} opciones (se esperaban al menos 4)")

    return errors
```

- [ ] **Step 4: Correr los tests y verificar que pasan**

Run: `py scripts/test_extract_all.py -v`
Expected: `OK` (8 tests en total pasan)

- [ ] **Step 5: Integrar la validación en `main()`**

En `scripts/extract_all.py`, justo antes del bloque `# Output to preguntas.json` (dentro de `main()`), agregar:

```python
    validation_errors = validate_questions(compiled_questions)
    if validation_errors:
        print(f"\nSe encontraron {len(validation_errors)} problema(s) de validación. No se escribirá preguntas.json:")
        for err in validation_errors:
            print(f"  - {err}")
        sys.exit(1)
```

- [ ] **Step 6: Correr el script completo end-to-end**

Run: `py scripts/extract_all.py`
Expected: `Successfully compiled and saved N questions to ...` sin bloque de errores de validación. Si aparecen errores, investigar la pregunta señalada en el DOCX/PDF original y ajustar `split_enunciado_and_options` o los datos fuente según corresponda antes de continuar a la Task 4.

- [ ] **Step 7: Commit**

```bash
git add scripts/extract_all.py scripts/test_extract_all.py src/app/preguntas.json
git commit -m "feat: validar automáticamente el banco de preguntas antes de escribir el JSON"
```

---

### Task 4: Agregar columna `opcion_e` y actualizar el índice FTS en Postgres

**Files:**
- Modify: `scripts/db-init.js`

**Interfaces:**
- Produces: tabla `preguntas` en Postgres con columna `opcion_e TEXT` (nullable), e índice `preguntas_fts_idx` reconstruido incluyéndola.

- [ ] **Step 1: Modificar `scripts/db-init.js`**

Después del bloque `CREATE TABLE IF NOT EXISTS preguntas (...)` (línea 37 actual, `console.log("Tabla 'preguntas' creada o ya existente.");`), agregar:

```js
    // 1.1 Agregar columna opcion_e para preguntas con 5ta alternativa (no todas la tienen)
    await client.query(`ALTER TABLE preguntas ADD COLUMN IF NOT EXISTS opcion_e TEXT;`);
    console.log("Columna 'opcion_e' asegurada en la tabla 'preguntas'.");
```

Luego reemplazar el bloque del índice FTS (actualmente):

```js
    await client.query(`
      CREATE INDEX IF NOT EXISTS preguntas_fts_idx ON preguntas 
      USING gin(to_tsvector('spanish', enunciado || ' ' || opcion_a || ' ' || opcion_b || ' ' || opcion_c || ' ' || opcion_d));
    `);
    console.log("Índice de búsqueda por texto completo (FTS) en español configurado.");
```

por:

```js
    // Recreamos el índice porque cambió la expresión indexada (ahora incluye opcion_e)
    await client.query(`DROP INDEX IF EXISTS preguntas_fts_idx;`);
    await client.query(`
      CREATE INDEX preguntas_fts_idx ON preguntas 
      USING gin(to_tsvector('spanish', enunciado || ' ' || opcion_a || ' ' || opcion_b || ' ' || opcion_c || ' ' || opcion_d || ' ' || COALESCE(opcion_e, '')));
    `);
    console.log("Índice de búsqueda por texto completo (FTS) en español configurado (incluye opcion_e).");
```

- [ ] **Step 2: Correr el script contra la base de datos real**

Run: `node scripts/db-init.js`
Expected: `Conectado con éxito...`, `Tabla 'preguntas' creada o ya existente.`, `Columna 'opcion_e' asegurada en la tabla 'preguntas'.`, `Índice de búsqueda por texto completo (FTS) en español configurado (incluye opcion_e).`, sin errores.

- [ ] **Step 3: Verificar la columna en la base de datos**

Run:
```bash
node -e "
require('dotenv').config({ path: '.env.local' });
const { Client } = require('pg');
const c = new Client({ connectionString: process.env.DATABASE_URL, ssl: { rejectUnauthorized: false } });
c.connect().then(() => c.query(\"SELECT column_name FROM information_schema.columns WHERE table_name='preguntas' ORDER BY column_name\"))
  .then(r => { console.log(r.rows.map(x => x.column_name)); return c.end(); });
"
```
Expected: la lista incluye `opcion_e` junto a `opcion_a`, `opcion_b`, `opcion_c`, `opcion_d`.

- [ ] **Step 4: Commit**

```bash
git add scripts/db-init.js
git commit -m "feat: agregar columna opcion_e y reconstruir índice FTS en Postgres"
```

---

### Task 5: Incluir `opcion_e` al subir preguntas a Supabase

**Files:**
- Modify: `scripts/db-upload.js`

**Interfaces:**
- Consumes: columna `opcion_e` de Task 4, campo `opcion_e` en `preguntas.json` de Task 2.
- Produces: filas de Postgres con `opcion_e` poblado para las preguntas que la tienen.

- [ ] **Step 1: Modificar el mapeo de columnas**

En `scripts/db-upload.js`, reemplazar:

```js
    const dbRows = batch.map(q => ({
      enunciado: q.enunciado,
      opcion_a: q.opcion_a,
      opcion_b: q.opcion_b,
      opcion_c: q.opcion_c,
      opcion_d: q.opcion_d,
      respuesta_correcta: q.respuesta_correcta,
      explicacion: q.explicacion,
      modelo_examen: q.modelo_examen
    }));
```

por:

```js
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
```

- [ ] **Step 2: Correr la subida contra Supabase**

Run: `node scripts/db-upload.js`
Expected: `Tabla 'preguntas' limpiada con éxito.`, luego un `Lote N insertado con éxito...` por cada lote de 20, sin `Error al insertar lote`.

- [ ] **Step 3: Verificar una pregunta de 5 alternativas en la base de datos**

Run:
```bash
node -e "
require('dotenv').config({ path: '.env.local' });
const { createClient } = require('@supabase/supabase-js');
const s = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY);
s.from('preguntas').select('enunciado, opcion_e, respuesta_correcta').not('opcion_e', 'is', null).then(({data, error}) => {
  console.log(error || data);
});
"
```
Expected: devuelve las filas cuya `respuesta_correcta` incluye "E", con `opcion_e` poblado (no `null`).

- [ ] **Step 4: Commit**

```bash
git add scripts/db-upload.js
git commit -m "feat: incluir opcion_e al subir preguntas a Supabase"
```

---

### Task 6: Exponer `opcion_e` en las rutas API

**Files:**
- Modify: `src/app/api/questions/route.ts`
- Modify: `src/app/api/search/route.ts`

**Interfaces:**
- Consumes: columna `opcion_e` de Postgres (Task 4/5).
- Produces: `GET /api/questions` y `GET /api/search` devuelven `opcion_e` (string o `null`) en cada pregunta.

- [ ] **Step 1: Actualizar el SELECT de `/api/questions`**

En `src/app/api/questions/route.ts`, reemplazar:

```ts
    const res = await client.query(`
      SELECT id, enunciado, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta, explicacion, modelo_examen
      FROM preguntas
      ORDER BY modelo_examen ASC, id ASC;
    `);
```

por:

```ts
    const res = await client.query(`
      SELECT id, enunciado, opcion_a, opcion_b, opcion_c, opcion_d, opcion_e, respuesta_correcta, explicacion, modelo_examen
      FROM preguntas
      ORDER BY modelo_examen ASC, id ASC;
    `);
```

- [ ] **Step 2: Actualizar `/api/search`**

En `src/app/api/search/route.ts`, reemplazar el SQL de búsqueda:

```ts
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
```

por (agrega `opcion_e` al SELECT y al `to_tsvector` de ambos lugares, para que coincida con el índice de Task 4):

```ts
    const sql = `
      SELECT id, enunciado, opcion_a, opcion_b, opcion_c, opcion_d, opcion_e, respuesta_correcta, explicacion, modelo_examen,
             ts_rank(
               to_tsvector('spanish', enunciado || ' ' || opcion_a || ' ' || opcion_b || ' ' || opcion_c || ' ' || opcion_d || ' ' || COALESCE(opcion_e, '')),
               query
             ) as rank
      FROM preguntas, 
           plainto_tsquery('spanish', $1) query
      WHERE to_tsvector('spanish', enunciado || ' ' || opcion_a || ' ' || opcion_b || ' ' || opcion_c || ' ' || opcion_d || ' ' || COALESCE(opcion_e, '')) @@ query
      ORDER BY rank DESC
      LIMIT 1;
    `;
```

Y en el objeto `matchData` un poco más abajo en el mismo archivo, agregar `opcion_e: match.opcion_e,` junto a `opcion_d: match.opcion_d,`.

- [ ] **Step 3: Probar contra el servidor de desarrollo**

Run: `npm run dev` (dejarlo corriendo), en otra terminal:
```bash
curl -s "http://localhost:3000/api/questions" | node -e "
let data = '';
process.stdin.on('data', d => data += d);
process.stdin.on('end', () => {
  const json = JSON.parse(data);
  const conE = json.questions.filter(q => q.opcion_e);
  console.log('preguntas con opcion_e:', conE.length);
  console.log(conE[0]);
});
"
```
Expected: `preguntas con opcion_e` es mayor a 0, y la pregunta de ejemplo impresa tiene `opcion_e` como string no vacío.

- [ ] **Step 4: Commit**

```bash
git add src/app/api/questions/route.ts src/app/api/search/route.ts
git commit -m "feat: exponer opcion_e en las rutas /api/questions y /api/search"
```
