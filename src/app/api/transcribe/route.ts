import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const groqKey = request.headers.get("x-groq-api-key") || process.env.GROQ_API_KEY;

  if (!groqKey) {
    return NextResponse.json(
      { error: "No hay una clave de Groq configurada. Agrégala en la pestaña de Ajustes BD." },
      { status: 400 }
    );
  }

  let incomingForm: FormData;
  try {
    incomingForm = await request.formData();
  } catch {
    return NextResponse.json({ error: "No se pudo leer el audio enviado." }, { status: 400 });
  }

  const audioFile = incomingForm.get("audio");

  if (!audioFile || !(audioFile instanceof Blob) || audioFile.size === 0) {
    return NextResponse.json({ error: "No se recibió ningún audio." }, { status: 400 });
  }

  const groqForm = new FormData();
  groqForm.append("file", audioFile, "grabacion.mp4");
  groqForm.append("model", "whisper-large-v3-turbo");
  groqForm.append("language", "es");

  try {
    const groqRes = await fetch("https://api.groq.com/openai/v1/audio/transcriptions", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${groqKey}`
      },
      body: groqForm
    });

    if (!groqRes.ok) {
      const errText = await groqRes.text();
      console.error("Groq transcription error:", errText);
      return NextResponse.json({ error: "Groq no pudo transcribir el audio. Intenta de nuevo." }, { status: 502 });
    }

    const data = await groqRes.json();
    return NextResponse.json({ text: data.text || "" });
  } catch (error) {
    console.error("Transcribe API Error:", error);
    const message = error instanceof Error ? error.message : "Error al transcribir el audio.";
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
