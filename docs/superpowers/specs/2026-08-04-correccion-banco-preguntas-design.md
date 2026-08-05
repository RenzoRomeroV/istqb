# Diseño: Corrección del banco de preguntas ISTQB

## Problema

El banco de preguntas (`src/app/preguntas.json`, cargado también en Postgres vía `scripts/db-upload.js`) se genera con `scripts/extract_all.py` a partir de los DOCX/PDF de simulacros en `ISTQB/Simulacros/Simulacros/1. Simuladores tipo examen de certificación/`. La extracción actual tiene tres defectos confirmados:

1. **34 de 80 preguntas (42%) tienen `enunciado` vacío.** `process_question()` asume que las últimas 4 líneas de texto de cada bloque son siempre las opciones (`while idx >= 0 and text_count < 4`), sin verificar que empiecen con un marcador de opción (`a)`, `b)`, `c)`, `d)`, `e)`). Cuando el enunciado real termina pareciendo un párrafo más, se cuela como si fuera `opcion_a`, y la verdadera opción A se pierde.
2. **4 preguntas tienen una 5ª alternativa (E)** — su letra aparece en `respuesta_correcta` (ej. `"B,E"`) pero no existe columna `opcion_e` ni en el JSON ni en Postgres, así que el texto de esa opción no se guarda en ningún lado y la UI no la puede mostrar.
3. **El Examen B no se procesa en absoluto.** `main()` solo parsea Exam C y Exam D.

Esto es independiente del pipeline de voz: aunque la transcripción fuera perfecta, casi la mitad de las preguntas no se pueden matchear ni verificar correctamente porque su enunciado no existe donde se busca.

## Objetivo

Regenerar `preguntas.json` (y la tabla `preguntas` en Postgres) con:

- Enunciado correctamente separado de las opciones en el 100% de las preguntas incluidas en el banco final (79 de 80 preguntas parseadas de Exámenes C y D; ver excepción documentada en la sección de Diseño).
- Soporte para 4 o 5 alternativas (columna `opcion_e` opcional).
- Una validación automática que falle ruidosamente si algo queda incompleto, para no repetir este problema en silencio.

## Fuera de alcance

- **Examen B.** Se investigó incluirlo, pero `1.1 Preguntas - B.pdf` es un PDF escaneado sin texto extraíble (confirmado con `pypdf`: 0 de 31 páginas devuelven texto), y `1. Respuestas - B.docx` solo contiene la clave de respuestas y explicaciones, no el enunciado ni las opciones. Extraerlo requeriría OCR (Tesseract + Poppler, no instalados) y de todas formas necesitaría revisión manual pregunta por pregunta antes de confiar en él para un examen real. Queda como tarea futura separada (OCR o transcripción manual, a decidir).
- Los ~15 PDFs adicionales de "Simulacro de Examen ISTQB Foundation Level v4.0" en `ISTQB/Material de estudio` (números 9 al 23). Formato desconocido/no DOCX, se evalúa como expansión futura por separado.
- Cualquier cambio al pipeline de voz o a la UI del asistente (sub-proyecto aparte).

## Diseño

### 1. Reescritura del detector de opciones (`extract_all.py`)

**Corrección post-investigación (2026-08-04):** el diseño original de este documento asumía que cada alternativa empezaba con texto literal `a)`, `b)`, etc. Al ejecutar el parser contra los DOCX reales se comprobó que eso es falso: Word marca las alternativas con numeración automática de listas (elemento `numPr` en el XML del párrafo), que `python-docx` NO incluye en `.text` — el texto de una alternativa nunca contiene la letra. La señal confiable y verificada es `numPr`, no el texto.

Diseño corregido:

- `parse_docx_questions` deja de acumular `str` planos; acumula tuplas `(texto, es_opcion)`, donde `es_opcion = paragraph._p.find('.//{...}numPr') is not None`.
- Antes de acumular cada párrafo, se le quita la frase "Seleccione UNA/DOS opción(es)." si aparece al final (a veces es un párrafo propio, a veces viene pegada al texto de la última alternativa). Si tras quitarla el párrafo queda vacío, se descarta por completo. Esto reemplaza la lógica anterior de `has_selector_last`, que borraba el ítem completo aunque contuviera texto real de una alternativa.
- `split_enunciado_and_options` recorre `items` de atrás hacia adelante tomando como opción cada tupla con `es_opcion=True`, y se detiene en el primer ítem que no lo sea **o** al llegar a 5 opciones (tope duro: ISTQB Foundation nunca ofrece más de 5 alternativas). El tope es necesario porque algunas preguntas tienen listas numeradas dentro del propio enunciado (p. ej. los pasos de un escenario), que también llevan `numPr` — sin tope, esas líneas se colarían como alternativas falsas.
- Verificado contra los 80 DOCX reales (Exam C + D): 79/80 preguntas quedan con el enunciado y las opciones perfectamente separados. La única excepción (Examen D, pregunta 29) tiene una alternativa tan larga que Word la partió en varios párrafos, y solo el primero conserva `numPr` — un caso genuino y raro (afecta a 1 de 80 preguntas) que no vale la pena perseguir con más heurísticas, porque cualquier regla que lo cubra arriesga romper los otros 79. Esa pregunta queda excluida del banco final (ya lo hace el filtro existente `if len(opciones) >= 4`, con su `ADVERTENCIA` impresa) — el banco final queda en 79 preguntas 100% correctas en vez de 80 con 34 corruptas.
- Mantener el manejo de tablas (`Table` de docx) igual que hoy: ahí las alternativas SÍ tienen el prefijo literal `a)`/`b)`/etc. dentro de cada celda (confirmado inspeccionando la pregunta 21), solo se amplía el regex de `[a-d]` a `[a-e]`.

### 2. Esquema de datos

- `scripts/db-init.js`: agregar `opcion_e TEXT` (sin `NOT NULL`, ya que la mayoría de preguntas no la tienen) a `CREATE TABLE preguntas`, y actualizar el índice GIN de FTS para incluir `COALESCE(opcion_e, '')`.
- `compiled_questions` en `extract_all.py`: incluir `"opcion_e": q["opciones"][4] if len(q["opciones"]) == 5 else None`.
- `scripts/db-upload.js`: actualizar el INSERT para incluir la columna `opcion_e`.

### 3. Validación automática post-extracción

Al final de `extract_all.py`, antes de escribir el JSON, recorrer `compiled_questions` y acumular errores:

- `enunciado` vacío o menor a 10 caracteres.
- Alguna letra en `respuesta_correcta` sin opción de texto correspondiente (ej. respuesta "E" pero `opcion_e` es `None`).
- Menos de 4 opciones capturadas.

Si hay errores, imprimir la lista completa (número de pregunta + examen + motivo) y terminar con código de salida distinto de cero, en vez de escribir un JSON parcialmente corrupto silenciosamente como ocurre hoy.

### 4. Regeneración de datos

1. Correr `extract_all.py` corregido → nuevo `preguntas.json` (Exam C + D, ~80 preguntas esperadas, ahora con enunciados completos y `opcion_e` donde aplique).
2. Correr `db-init.js` (agrega `opcion_e` si la tabla ya existe — usar `ALTER TABLE ADD COLUMN IF NOT EXISTS` en vez de solo `CREATE TABLE IF NOT EXISTS`, porque la tabla ya existe en producción).
3. Correr `db-upload.js` para repoblar Postgres.

## Manejo de errores

- Si el validador post-extracción encuentra problemas: el script termina sin escribir el JSON final (evita dejar datos a medio corregir reemplazando los que sí funcionaban).
- `db-upload.js` ya borra toda la tabla (`delete().neq("id", ...)`) antes de insertar el lote nuevo, así que ya es idempotente frente al nuevo `preguntas.json` — solo hay que sumar `opcion_e` al mapeo de columnas que inserta.

## Testing

- Correr el script contra los 2 exámenes (C y D) y verificar manualmente 5-6 preguntas al azar de cada uno contra el DOCX/PDF original (incluyendo al menos una de las 4 preguntas con 5 alternativas).
- Confirmar que el validador automático reporta 0 errores antes de subir a Postgres.
- Contar preguntas totales esperadas (Exam C + D) y compararlo con el número de preguntas real en cada documento fuente.
- Verificar en la UI (`/api/questions`) que las preguntas con 5 alternativas ahora traen `opcion_e` en la respuesta JSON (aunque el render de una 5ª opción en la interfaz se hace en el sub-proyecto 2, de voz).
