# Diseño: Asistente de voz para iPhone (sub-proyecto 2a — Voz + Matching)

## Problema

El Asistente de voz actual (`src/app/page.tsx`) depende por completo de la Web Speech API del navegador (`window.SpeechRecognition` / `window.webkitSpeechRecognition`). Esa API **no existe en ningún navegador de iOS**: Apple nunca la implementó en Safari, y todos los navegadores de iOS (Safari, Chrome iOS, Edge iOS, Firefox iOS) están obligados por Apple a usar el motor WebKit de Safari como backend, así que ni instalando "otro navegador" se resuelve — es una limitación de la plataforma, no un bug de configuración. El dispositivo real del usuario para esta funcionalidad es un iPhone, así que el asistente de voz hoy no puede funcionar ahí en absoluto.

Además, incluso con una transcripción correcta, dos problemas adicionales impiden obtener siempre la respuesta correcta:

1. `src/app/api/search/route.ts` construye la búsqueda con `plainto_tsquery('spanish', $1)`, que une todas las palabras del texto dictado con **AND**. Si se dicta la pregunta completa más 4-5 alternativas (con muletillas o un solo error de transcripción), basta que una palabra no calce exacto con el texto guardado para que la fila entera no cumpla `@@ query` — cero resultados aunque el resto esté bien.
2. La interfaz solo maneja alternativas A-D con comparación de igualdad estricta (`respuesta_correcta === opt`). El banco de preguntas (corregido en el sub-proyecto 1) ya tiene preguntas con una 5ª alternativa (`opcion_e`) y preguntas con respuesta múltiple (ej. `"B,E"`), que hoy no se muestran ni se anuncian correctamente.

## Objetivo

Que el usuario pueda, en su iPhone, dictar una pregunta ISTQB completa junto con sus alternativas, y que el sistema transcriba con precisión, encuentre la pregunta correcta en el banco (tolerando pequeños errores de transcripción) y anuncie/muestre la(s) alternativa(s) correcta(s) sin importar si la pregunta tiene 4 o 5 alternativas o más de una respuesta correcta.

## Fuera de alcance (decisiones de alcance ya acordadas con el usuario)

- **Respaldo de IA anclado al temario oficial (RAG sobre los PDFs de `ISTQB/Material de estudio`)** para preguntas que no estén en el banco de datos. Se hace como sub-proyecto 2b, después de que esto funcione.
- **Selección múltiple interactiva en el modo Simulador** (examen cronometrado). El modo Simulador usa botones de opción única y comparación estricta, lo cual también está roto para las preguntas de respuesta múltiple — pero ahí el usuario *selecciona* una respuesta (no solo la ve), así que arreglarlo requiere cambiar la interacción a casillas de selección múltiple. Queda documentado como pendiente separado, no se toca en este sub-proyecto.
- Examen B y los ~15 PDFs adicionales de `ISTQB/Material de estudio` sin digitalizar (ya documentado como fuera de alcance en el sub-proyecto 1).

## Diseño

### 1. Grabación de voz (`src/app/page.tsx`)

Reemplazar por completo la inicialización y los handlers de `SpeechRecognition` por grabación con `MediaRecorder`:

- Un solo botón de micrófono, comportamiento "push-to-talk": primer toque llama a `navigator.mediaDevices.getUserMedia({ audio: true })` e inicia un `MediaRecorder` sobre ese stream; segundo toque llama a `recorder.stop()`.
- Al detener, se arma un `Blob` a partir de los chunks acumulados en `ondataavailable` y se envía a `/api/transcribe`.
- iOS Safari no soporta bien `audio/webm` en `MediaRecorder` (a diferencia de Chrome/Android) — usa `audio/mp4` (AAC) por defecto. Se elige el `mimeType` con `MediaRecorder.isTypeSupported(...)`, probando `audio/mp4` primero y con fallback a lo que el navegador soporte. Whisper acepta `mp4`/`m4a` directamente, así que no hace falta conversión de formato.
- Nuevo estado visual explícito para "Transcribiendo..." (distinto del actual `isProcessing`, que se usaba para el silencio de la Web Speech API y ya no aplica) mientras se espera la respuesta de `/api/transcribe`.
- Se elimina `recognitionRef`, el `useEffect` que inicializaba `SpeechRecognition`, y el mensaje de error específico de "tu navegador no soporta reconocimiento de voz" (ya no aplica con este enfoque).

### 2. Nueva ruta `/api/transcribe`

Nueva ruta (`src/app/api/transcribe/route.ts`) que:

- Recibe el audio como `multipart/form-data` (un `Blob`/`File`).
- Lo reenvía a `https://api.groq.com/openai/v1/audio/transcriptions` con `model: "whisper-large-v3-turbo"` y `language: "es"`.
- Usa la misma convención de API key que `/api/search`: header `x-groq-api-key` desde el cliente (localStorage), con fallback a `process.env.GROQ_API_KEY`.
- Devuelve `{ text: string }` en éxito, o un error claro (sin key configurada, error de Groq, audio vacío/no reconocible) para que el frontend lo muestre.

### 3. Matching tolerante a errores (`/api/search/route.ts`)

Reemplazar el `WHERE ... @@ plainto_tsquery(...)` (AND estricto) por una búsqueda por coincidencia de palabras clave con **OR**, con un umbral mínimo de coincidencia antes de aceptar el resultado — el mismo principio que ya usa el filtro de respaldo local en el frontend (contar cuántas palabras clave del texto dictado aparecen en la pregunta candidata), pero ejecutado en SQL contra toda la tabla en vez de en JS contra las preguntas ya cargadas en memoria:

- Extraer del texto dictado las palabras "significativas" (largo > 3, quitando palabras comunes que ya aparecen en casi cualquier pregunta: "cuál", "según", "durante", "opción", etc.) — la misma idea que ya usa el filtro de respaldo local en el frontend.
- Construir el tsquery uniendo esas palabras con `|` (OR) en vez de `&` (AND), para que ninguna palabra sea un punto único de fallo, y traer con `ts_rank` los 5 mejores candidatos (no solo 1) usando el índice GIN existente.
- Sobre esos 5 candidatos, calcular en el servidor qué fracción de las palabras clave aparece literalmente en el texto de cada uno (enunciado + opciones), igual que hace hoy el filtro de respaldo local pero aplicado a los candidatos ya acotados por el ranking en vez de a toda la tabla.
- Devolver como match el candidato con mayor fracción de coincidencia, solo si esa fracción es de al menos 50% (mismo umbral que ya usa el filtro de respaldo local, por consistencia) — así ninguna palabra mal transcrita anula la búsqueda, pero tampoco se acepta una coincidencia débil de una sola palabra suelta.
- Mantener el fallback a IA (Groq) cuando no hay match de base de datos, sin cambios en esta fase (el anclaje al temario oficial es el sub-proyecto 2b).

### 4. Confirmación visual (sin cambios de fondo, se mantiene)

El patrón actual ya es bueno para detectar errores de transcripción a tiempo: se sigue mostrando el texto transcrito formateado (pregunta/opciones separadas) y la pregunta encontrada con su % de confianza, antes/junto con el anuncio de la respuesta.

### 5. Soporte de 5ª alternativa y respuesta múltiple (vista Asistente únicamente)

- Las opciones a mostrar se calculan dinámicamente: `["A","B","C","D"]` más `"E"` si `matchedQuestion.opcion_e` existe.
- La alternativa correcta se determina con `matchedQuestion.respuesta_correcta.split(",").includes(opt)` en vez de `=== opt`, para soportar respuesta múltiple.
- `speakAnswer` se ajusta para construir el mensaje según la cantidad de letras en `respuesta_correcta`: una sola → "La respuesta correcta es la B."; varias → "Las respuestas correctas son la B y la E."

## Manejo de errores

- Permiso de micrófono denegado (`getUserMedia` rechaza la promesa) → mensaje claro pidiendo habilitar el micrófono para el sitio.
- Grabación sin audio útil / Blob vacío → mensaje pidiendo intentar de nuevo.
- Fallo de red o de Groq al transcribir → mensaje de error, se puede volver a grabar (no hace falta persistir el audio fallido).
- Sin coincidencia en base de datos ni IA → se mantiene el mensaje actual de "no encontré coincidencia".

## Testing

- La grabación real (permisos de micrófono, formato de audio, comportamiento de `MediaRecorder`) solo se puede validar manualmente en un iPhone real contra la app desplegada en Vercel (HTTPS) — no es automatizable de forma significativa.
- `/api/transcribe`: probar con un archivo de audio de muestra vía `curl`/script contra el endpoint real de Groq.
- `/api/search` con el matching corregido: casos de prueba con texto que tenga 1-2 palabras "mal transcritas" (sustituidas) respecto a una pregunta real de la base de datos, verificando que igual encuentra la pregunta correcta, y casos con texto irrelevante verificando que NO devuelve una coincidencia débil.
- Render de opciones y anuncio de voz: verificar manualmente contra al menos una de las 5 preguntas reales con `opcion_e` y una con respuesta múltiple ya existentes en la base de datos.
