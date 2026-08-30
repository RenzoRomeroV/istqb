"use client";

import React, { useState, useEffect, useRef } from "react";
import { Mic, MicOff, BookOpen, CheckCircle2, Award, ShieldAlert, Sparkles, Volume2, VolumeX, HelpCircle, Database, Settings, Type, Search } from "lucide-react";

// Mock de preguntas ISTQB para demostración inmediata
const MOCK_PREGUNTAS = [
  {
    id: "1",
    enunciado: "¿Cuál de las siguientes opciones describe mejor la diferencia entre testing y depuración (debugging)?",
    opcion_a: "El testing muestra fallas causadas por defectos; la depuración encuentra, analiza y elimina la causa de las fallas en el código.",
    opcion_b: "El testing elimina los defectos; la depuración identifica las fallas.",
    opcion_c: "La depuración la realizan los testers; el testing lo realizan los desarrolladores.",
    opcion_d: "El testing busca la causa raíz; la depuración comprueba el correcto funcionamiento.",
    opcion_e: null as string | null,
    respuesta_correcta: "A",
    explicacion: "De acuerdo al Syllabus de ISTQB, el testing consiste en la ejecución de pruebas para mostrar fallos, mientras que la depuración (debugging) es la actividad de desarrollo que localiza, analiza y corrige las causas de dichos fallos (defectos)."
  },
  {
    id: "2",
    enunciado: "¿Cuál de los siguientes es un principio fundamental del testing de software?",
    opcion_a: "El testing completo es posible si se tiene suficiente tiempo y presupuesto.",
    opcion_b: "Las pruebas exhaustivas son imposibles; el testing muestra la presencia de defectos, no su ausencia.",
    opcion_c: "El testing debe comenzar lo más tarde posible en el ciclo de desarrollo.",
    opcion_d: "La paradoja del pesticida dice que si se repiten las mismas pruebas, se encontrarán más defectos nuevos.",
    opcion_e: null as string | null,
    respuesta_correcta: "B",
    explicacion: "El Principio 2 establece que las pruebas exhaustivas son imposibles debido a la infinidad de combinaciones. El Principio 1 establece que las pruebas muestran la presencia de defectos, no su ausencia."
  },
  {
    id: "3",
    enunciado: "Durante qué actividad del proceso de pruebas se definen los criterios de entrada y criterios de salida?",
    opcion_a: "Análisis de pruebas.",
    opcion_b: "Diseño de pruebas.",
    opcion_c: "Planificación de pruebas.",
    opcion_d: "Implementación de pruebas.",
    opcion_e: null as string | null,
    respuesta_correcta: "C",
    explicacion: "Los criterios de entrada y salida se definen durante la planificación de pruebas para establecer cuándo empezar y cuándo finalizar las actividades de prueba."
  },
  {
    id: "4",
    enunciado: "El objetivo principal del análisis de valor límite (Boundary Value Analysis) es:",
    opcion_a: "Probar todas las combinaciones posibles de entradas.",
    opcion_b: "Identificar defectos en los extremos de las particiones de equivalencia.",
    opcion_c: "Evaluar la estructura interna del código.",
    opcion_d: "Asegurar que el 100% de las sentencias del código sean ejecutadas.",
    opcion_e: null as string | null,
    respuesta_correcta: "B",
    explicacion: "El análisis de valores límite es una técnica de caja negra que se enfoca en probar los valores en las fronteras (límites) de las clases o particiones de equivalencia, ya que ahí es donde ocurren más errores."
  },
  {
    id: "5",
    enunciado: "¿Qué tipo de prueba se realiza para asegurar que los cambios recientes en el código no han introducido defectos en las partes no modificadas?",
    opcion_a: "Pruebas de confirmación (re-testing).",
    opcion_b: "Pruebas de regresión.",
    opcion_c: "Pruebas unitarias.",
    opcion_d: "Pruebas de integración.",
    opcion_e: null as string | null,
    respuesta_correcta: "B",
    explicacion: "Las pruebas de regresión se ejecutan de forma repetida para verificar que las partes del software que no han sido modificadas sigan funcionando correctamente después de aplicar cambios o correcciones."
  }
];

export default function Home() {
  const [activeTab, setActiveTab] = useState<"assistant" | "write" | "simulator" | "db">("assistant");

  // DB Questions Bank
  const [dbQuestions, setDbQuestions] = useState<typeof MOCK_PREGUNTAS>(MOCK_PREGUNTAS);

  // Voice Assistant States
  const [isListening, setIsListening] = useState(false);
  const [isTranscribing, setIsTranscribing] = useState(false);
  const [spokenText, setSpokenText] = useState("");
  const [matchedQuestion, setMatchedQuestion] = useState<typeof MOCK_PREGUNTAS[0] | null>(null);
  const [confidence, setConfidence] = useState(0);
  const [isAudioEnabled, setIsAudioEnabled] = useState(true);
  const [showJustification, setShowJustification] = useState(false); // Oculto por defecto
  const [recognitionError, setRecognitionError] = useState("");

  // Write Module States
  const [typedText, setTypedText] = useState("");
  const [isSearchingTyped, setIsSearchingTyped] = useState(false);
  const [searchedTypedText, setSearchedTypedText] = useState("");

  // Simulator States
  const [simQuestions, setSimQuestions] = useState<typeof MOCK_PREGUNTAS>([]);
  const [currentSimIdx, setCurrentSimIdx] = useState(0);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [showSimResults, setShowSimResults] = useState(false);
  const [timer, setTimer] = useState(3600); // 60 minutos
  const [isTimerActive, setIsTimerActive] = useState(false);

  // DB States
  const [supabaseConnected, setSupabaseConnected] = useState(true); // Conectado por defecto a la API local
  const [supabaseUrl, setSupabaseUrl] = useState("");
  const [supabaseKey, setSupabaseKey] = useState("");
  const [groqApiKey, setGroqApiKey] = useState("");
  const [geminiApiKey, setGeminiApiKey] = useState("");
  const [tavilyApiKey, setTavilyApiKey] = useState("");

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);

  // Cargar preguntas y API keys de la base de datos y localStorage al iniciar
  useEffect(() => {
    async function loadQuestions() {
      try {
        const res = await fetch("/api/questions");
        const data = await res.json();
        if (data.questions && data.questions.length > 0) {
          setDbQuestions(data.questions);
          setSupabaseConnected(true);
        }
      } catch (err) {
        console.error("No se pudieron cargar preguntas de Supabase, usando locales:", err);
        setSupabaseConnected(false);
      }
    }
    loadQuestions();

    if (typeof window !== "undefined") {
      const savedGroqKey = localStorage.getItem("groq_api_key");
      if (savedGroqKey) {
        setGroqApiKey(savedGroqKey);
      }
      const savedGeminiKey = localStorage.getItem("gemini_api_key");
      if (savedGeminiKey) {
        setGeminiApiKey(savedGeminiKey);
      }
      const savedTavilyKey = localStorage.getItem("tavily_api_key");
      if (savedTavilyKey) {
        setTavilyApiKey(savedTavilyKey);
      }
    }
  }, []);

  // Controlar el temporizador del simulador
  useEffect(() => {
    let interval: any = null;
    if (isTimerActive && timer > 0 && !showSimResults) {
      interval = setInterval(() => {
        setTimer((prev) => prev - 1);
      }, 1000);
    } else if (timer === 0) {
      setShowSimResults(true);
      setIsTimerActive(false);
    }
    return () => clearInterval(interval);
  }, [isTimerActive, timer, showSimResults]);

  // Formatear tiempo del cronómetro
  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
  };

  // Formatear texto dictado para ordenarlo por líneas de preguntas y alternativas
  const renderFormattedSpokenText = (text: string) => {
    if (!text) return null;

    // Marcador de pregunta
    let formatted = text;
    formatted = formatted.replace(/(?:pregunta\s+istqb\s+foundation|pregunta\s+istqb|pregunta)\s*/i, "\n[PREGUNTA]\n");

    // Marcadores de opciones (la a, la b, la c, la d, la e, la f, respuesta a, etc.)
    formatted = formatted.replace(/\b(?:la\s+a|opción\s+a|opcion\s+a|respuesta\s+a|a\))\s*/gi, "\n[OP_A] ");
    formatted = formatted.replace(/\b(?:la\s+b|opción\s+b|opcion\s+b|respuesta\s+b|b\))\s*/gi, "\n[OP_B] ");
    formatted = formatted.replace(/\b(?:la\s+c|opción\s+c|opcion\s+c|respuesta\s+c|c\))\s*/gi, "\n[OP_C] ");
    formatted = formatted.replace(/\b(?:la\s+d|opción\s+d|opcion\s+d|respuesta\s+d|d\))\s*/gi, "\n[OP_D] ");
    formatted = formatted.replace(/\b(?:la\s+e|opción\s+e|opcion\s+e|respuesta\s+e|e\))\s*/gi, "\n[OP_E] ");

    const lines = formatted.split("\n").map(l => l.trim()).filter(Boolean);

    return (
      <div className="flex flex-col gap-1.5 text-xs text-zinc-300 leading-relaxed font-sans mt-1">
        {lines.map((line, idx) => {
          if (line.startsWith("[PREGUNTA]")) {
            const content = line.replace("[PREGUNTA]", "").trim();
            return (
              <div key={idx} className="mt-1">
                <strong className="text-amber-400 block font-semibold">Pregunta:</strong>
                {content && <span className="italic">"{content}"</span>}
              </div>
            );
          }
          if (line.startsWith("[OP_A]")) {
            return <div key={idx} className="pl-3 flex items-start gap-1"><span className="text-amber-400/80 font-bold shrink-0">la A:</span> <span className="italic">"{line.replace("[OP_A]", "").trim()}"</span></div>;
          }
          if (line.startsWith("[OP_B]")) {
            return <div key={idx} className="pl-3 flex items-start gap-1"><span className="text-amber-400/80 font-bold shrink-0">la B:</span> <span className="italic">"{line.replace("[OP_B]", "").trim()}"</span></div>;
          }
          if (line.startsWith("[OP_C]")) {
            return <div key={idx} className="pl-3 flex items-start gap-1"><span className="text-amber-400/80 font-bold shrink-0">la C:</span> <span className="italic">"{line.replace("[OP_C]", "").trim()}"</span></div>;
          }
          if (line.startsWith("[OP_D]")) {
            return <div key={idx} className="pl-3 flex items-start gap-1"><span className="text-amber-400/80 font-bold shrink-0">la D:</span> <span className="italic">"{line.replace("[OP_D]", "").trim()}"</span></div>;
          }
          if (line.startsWith("[OP_E]")) {
            return <div key={idx} className="pl-3 flex items-start gap-1"><span className="text-amber-400/80 font-bold shrink-0">la E:</span> <span className="italic">"{line.replace("[OP_E]", "").trim()}"</span></div>;
          }
          return <p key={idx} className="italic">"{line}"</p>;
        })}
      </div>
    );
  };

  // Tarjeta de respuesta encontrada, reutilizada por el Asistente de voz y el módulo Escribir
  const renderAnswerCard = () => {
    if (!matchedQuestion) return null;

    return (
      <div className="bg-gradient-to-b from-zinc-900 to-zinc-950 border border-emerald-500/30 rounded-2xl p-5 shadow-[0_4px_20px_rgba(16,185,129,0.05)] flex flex-col gap-4">
        <div className="flex items-center justify-between border-b border-zinc-800/80 pb-2.5">
          <div className="flex items-center gap-2">
            <span className="bg-emerald-500/10 text-emerald-400 text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full border border-emerald-500/20">
              Coincidencia encontrada
            </span>
            <span className="text-zinc-500 text-xs">{confidence}% Confianza</span>
          </div>
          <HelpCircle className="w-4 h-4 text-zinc-400" />
        </div>

        <div>
          <h3 className="font-semibold text-white text-sm leading-relaxed mb-3">
            {matchedQuestion.enunciado}
          </h3>

          {/* Lista de Opciones */}
          <div className="flex flex-col gap-2">
            {(matchedQuestion.opcion_e ? ["A", "B", "C", "D", "E"] : ["A", "B", "C", "D"]).map((opt) => {
              const text =
                opt === "A" ? matchedQuestion.opcion_a :
                  opt === "B" ? matchedQuestion.opcion_b :
                    opt === "C" ? matchedQuestion.opcion_c :
                      opt === "D" ? matchedQuestion.opcion_d : matchedQuestion.opcion_e;
              const isCorrect = matchedQuestion.respuesta_correcta
                .split(",")
                .map(l => l.trim())
                .includes(opt);

              return (
                <div
                  key={opt}
                  className={`flex items-start gap-2.5 p-3 rounded-xl border text-xs transition-all ${isCorrect
                      ? "bg-emerald-950/30 border-emerald-500/50 text-emerald-100 shadow-[0_0_15px_rgba(16,185,129,0.03)]"
                      : "bg-zinc-900/20 border-zinc-800/50 text-zinc-400"
                    }`}
                >
                  <span className={`w-5 h-5 flex items-center justify-center rounded-md font-bold ${isCorrect ? "bg-emerald-500 text-zinc-950" : "bg-zinc-800 text-zinc-400"
                    }`}>
                    {opt}
                  </span>
                  <span className="flex-1 leading-relaxed">{text}</span>
                </div>
              );
            })}
          </div>
        </div>

        {/* Explicación Justificación (Colapsable) */}
        <div className="flex flex-col gap-1.5 mt-1">
          <button
            onClick={() => setShowJustification(!showJustification)}
            className="self-start text-[10px] text-zinc-500 hover:text-zinc-300 underline font-medium transition-colors"
          >
            {showJustification ? "Ocultar justificación oficial" : "Ver justificación oficial"}
          </button>
          {showJustification && (
            <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl p-3 text-[11px] text-zinc-400 leading-relaxed">
              {matchedQuestion.explicacion}
            </div>
          )}
        </div>
      </div>
    );
  };

  // Buscar pregunta por texto hablado
  const searchQuestion = async (text: string) => {
    if (!text.trim()) return;

    // Primero intentamos buscar en la base de datos de Supabase a través de nuestra API
    try {
      const savedGeminiKey = typeof window !== "undefined" ? localStorage.getItem("gemini_api_key") || "" : "";
      const savedTavilyKey = typeof window !== "undefined" ? localStorage.getItem("tavily_api_key") || "" : "";
      const headers: Record<string, string> = {};
      if (savedGeminiKey) {
        headers["x-gemini-api-key"] = savedGeminiKey;
      }
      if (savedTavilyKey) {
        headers["x-tavily-api-key"] = savedTavilyKey;
      }

      const res = await fetch(`/api/search?q=${encodeURIComponent(text)}`, { headers });
      if (res.ok) {
        const data = await res.json();
        if (data.match) {
          setMatchedQuestion(data.match);
          setConfidence(data.confidence || 95);
          setShowJustification(false); // Resetear visibilidad de justificación
          if (isAudioEnabled) {
            speakAnswer(data.match);
          }
        } else {
          // Si el servidor resolvió con éxito pero no encontró coincidencia, detenemos la búsqueda aquí
          setMatchedQuestion(null);
          setConfidence(0);
        }
        return;
      }
    } catch (err) {
      console.warn("Búsqueda en base de datos falló, usando búsqueda local:", err);
    }

    // Algoritmo de respaldo local (Fuzzy Match offline)
    const cleanText = text.toLowerCase();
    let bestMatch: typeof MOCK_PREGUNTAS[0] | null = null;
    let maxMatches = 0;

    dbQuestions.forEach((q) => {
      let matches = 0;
      const questionText = `${q.enunciado} ${q.opcion_a} ${q.opcion_b} ${q.opcion_c} ${q.opcion_d} ${q.opcion_e || ""}`.toLowerCase();

      const words = cleanText.split(/\s+/).filter(w => w.length > 3);
      words.forEach((word) => {
        if (questionText.includes(word)) {
          matches++;
        }
      });

      if (matches > maxMatches) {
        maxMatches = matches;
        bestMatch = q;
      }
    });

    // Exigir al menos un 50% de coincidencia de palabras clave para evitar falsos positivos locales
    const wordCount = cleanText.split(/\s+/).filter(w => w.length > 3).length;
    const calculatedConfidence = wordCount > 0 ? Math.min(Math.round((maxMatches / wordCount) * 100), 100) : 0;

    if (bestMatch && maxMatches >= 2 && calculatedConfidence >= 50) {
      setMatchedQuestion(bestMatch);
      setConfidence(calculatedConfidence);
      setShowJustification(false);

      if (isAudioEnabled && typeof window !== "undefined") {
        speakAnswer(bestMatch);
      }
    } else {
      setMatchedQuestion(null);
      setConfidence(0);
    }
  };

  // Leer respuesta correcta en voz alta (De forma abreviada y concisa como pidió el usuario)
  const speakAnswer = (question: typeof MOCK_PREGUNTAS[0]) => {
    if (!isAudioEnabled || !question) return;

    window.speechSynthesis.cancel(); // Detener cualquier reproducción previa
    const letters = question.respuesta_correcta.split(",").map(l => l.trim()).filter(Boolean);

    const message = letters.length > 1
      ? `Las respuestas correctas son la ${letters.slice(0, -1).join(", la ")} y la ${letters[letters.length - 1]}.`
      : `La respuesta correcta es la ${letters[0]}.`;

    const utterance = new SpeechSynthesisUtterance(message);
    utterance.lang = "es-ES";
    utterance.rate = 1.0;
    window.speechSynthesis.speak(utterance);
  };

  // Transcribir el audio grabado y buscar la pregunta correspondiente
  const transcribeAndSearch = async (blob: Blob) => {
    setIsTranscribing(true);
    try {
      const savedKey = typeof window !== "undefined" ? localStorage.getItem("groq_api_key") || "" : "";
      const formData = new FormData();
      formData.append("audio", blob, "grabacion.mp4");

      const headers: Record<string, string> = {};
      if (savedKey) {
        headers["x-groq-api-key"] = savedKey;
      }

      const res = await fetch("/api/transcribe", { method: "POST", body: formData, headers });
      const data = await res.json();

      if (!res.ok || !data.text) {
        setRecognitionError(data.error || "No se pudo transcribir el audio. Intenta de nuevo.");
        return;
      }

      setRecognitionError("");
      setSpokenText(data.text);
      await searchQuestion(data.text);
    } catch (err) {
      console.error("Transcribe error", err);
      setRecognitionError("Error al transcribir. Verifica tu conexión e intenta de nuevo.");
    } finally {
      setIsTranscribing(false);
    }
  };

  // Alternar la grabación (push-to-talk): un toque para empezar, otro para terminar
  const toggleListening = async () => {
    if (isListening) {
      mediaRecorderRef.current?.stop();
      return;
    }

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const preferredTypes = ["audio/mp4", "audio/webm", "audio/ogg"];
      const mimeType = preferredTypes.find(t => typeof MediaRecorder !== "undefined" && MediaRecorder.isTypeSupported(t));
      const recorder = mimeType ? new MediaRecorder(stream, { mimeType }) : new MediaRecorder(stream);

      audioChunksRef.current = [];
      recorder.ondataavailable = (e) => {
        if (e.data.size > 0) {
          audioChunksRef.current.push(e.data);
        }
      };
      recorder.onstop = () => {
        stream.getTracks().forEach(track => track.stop());
        const blob = new Blob(audioChunksRef.current, { type: recorder.mimeType || "audio/mp4" });
        setIsListening(false);
        transcribeAndSearch(blob);
      };

      mediaRecorderRef.current = recorder;
      setSpokenText("");
      setMatchedQuestion(null);
      setRecognitionError("");
      recorder.start();
      setIsListening(true);
    } catch (err) {
      console.error("Mic error", err);
      setRecognitionError("No se pudo acceder al micrófono. Verifica los permisos del navegador para este sitio.");
    }
  };

  // Buscar la respuesta a partir del texto escrito a mano (módulo Escribir)
  const handleTypedSearch = async () => {
    const text = typedText.trim();
    if (!text || isSearchingTyped) return;

    setIsSearchingTyped(true);
    setMatchedQuestion(null);
    setSpokenText("");
    setSearchedTypedText(text);
    try {
      await searchQuestion(text);
    } finally {
      setIsSearchingTyped(false);
    }
  };

  // Inicializar examen de simulacro
  const startSimulator = () => {
    // Mezclar preguntas de la base de datos
    const shuffled = [...dbQuestions].sort(() => 0.5 - Math.random());
    // Examen de 40 preguntas reales
    setSimQuestions(shuffled.slice(0, 40));
    setCurrentSimIdx(0);
    setAnswers({});
    setShowSimResults(false);
    setTimer(3600); // 60 minutos
    setIsTimerActive(true);
  };

  // Guardar respuesta del simulacro
  const selectOption = (questionId: string, option: string) => {
    setAnswers(prev => ({
      ...prev,
      [questionId]: option
    }));
  };

  // Calcular puntaje
  const calculateScore = () => {
    let correct = 0;
    simQuestions.forEach((q) => {
      if (answers[q.id] === q.respuesta_correcta) {
        correct++;
      }
    });
    const percentage = Math.round((correct / simQuestions.length) * 100);
    return {
      correct,
      total: simQuestions.length,
      percentage,
      passed: percentage >= 65
    };
  };

  return (
    <div className="flex-1 flex flex-col bg-zinc-950 text-zinc-100 font-sans min-h-screen">
      {/* Header Premium */}
      <header className="sticky top-0 z-50 bg-zinc-900/80 backdrop-blur-md border-b border-zinc-800/80 px-4 py-3 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="bg-gradient-to-tr from-amber-500 to-amber-300 p-2 rounded-xl text-zinc-950 font-bold shadow-[0_0_15px_rgba(245,158,11,0.2)]">
            <Sparkles className="w-5 h-5" />
          </div>
          <div>
            <h1 className="text-md font-bold tracking-tight text-white flex items-center gap-1.5">
              ISTQB <span className="text-amber-400 font-normal">Copiloto</span>
            </h1>
            <p className="text-[10px] text-zinc-400">Asistente Inteligente de Certificación</p>
          </div>
        </div>

        {/* Indicador de Conexión Supabase */}
        <div className="flex items-center gap-1.5 bg-zinc-800/60 border border-zinc-700/50 px-2.5 py-1 rounded-full text-xs">
          <Database className={`w-3.5 h-3.5 ${supabaseConnected ? "text-emerald-400" : "text-zinc-500 animate-pulse"}`} />
          <span className="text-[10px] text-zinc-300 font-medium">
            {supabaseConnected ? "Supabase Listo" : "Modo Local"}
          </span>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 max-w-md w-full mx-auto px-4 py-6 flex flex-col gap-6">

        {/* Navigation Tabs */}
        <div className="grid grid-cols-4 gap-1 bg-zinc-900 p-1 rounded-xl border border-zinc-800/80">
          <button
            onClick={() => setActiveTab("assistant")}
            className={`flex flex-col items-center gap-1 py-2 px-3 rounded-lg text-xs font-medium transition-all ${activeTab === "assistant"
                ? "bg-gradient-to-r from-amber-500 to-amber-600 text-white shadow-md shadow-amber-600/10"
                : "text-zinc-400 hover:text-white"
              }`}
          >
            <Mic className="w-4 h-4" />
            <span>Asistente</span>
          </button>
          <button
            onClick={() => setActiveTab("write")}
            className={`flex flex-col items-center gap-1 py-2 px-3 rounded-lg text-xs font-medium transition-all ${activeTab === "write"
                ? "bg-gradient-to-r from-amber-500 to-amber-600 text-white shadow-md shadow-amber-600/10"
                : "text-zinc-400 hover:text-white"
              }`}
          >
            <Type className="w-4 h-4" />
            <span>Escribir</span>
          </button>
          <button
            onClick={() => {
              setActiveTab("simulator");
              if (simQuestions.length === 0) startSimulator();
            }}
            className={`flex flex-col items-center gap-1 py-2 px-3 rounded-lg text-xs font-medium transition-all ${activeTab === "simulator"
                ? "bg-gradient-to-r from-amber-500 to-amber-600 text-white shadow-md shadow-amber-600/10"
                : "text-zinc-400 hover:text-white"
              }`}
          >
            <BookOpen className="w-4 h-4" />
            <span>Simulador</span>
          </button>
          <button
            onClick={() => setActiveTab("db")}
            className={`flex flex-col items-center gap-1 py-2 px-3 rounded-lg text-xs font-medium transition-all ${activeTab === "db"
                ? "bg-gradient-to-r from-amber-500 to-amber-600 text-white shadow-md shadow-amber-600/10"
                : "text-zinc-400 hover:text-white"
              }`}
          >
            <Settings className="w-4 h-4" />
            <span>Ajustes BD</span>
          </button>
        </div>

        {/* --- VIEW 1: VOICE ASSISTANT --- */}
        {activeTab === "assistant" && (
          <div className="flex-1 flex flex-col gap-5">
            {/* Mic and Listening Panel */}
            <div className="bg-zinc-900/50 border border-zinc-800/80 rounded-2xl p-6 flex flex-col items-center gap-4 text-center">
              <h2 className="text-sm font-semibold text-zinc-300">Toca para grabar la pregunta y las alternativas, toca de nuevo para terminar</h2>

              {/* Pulsing Mic Button */}
              <button
                onClick={toggleListening}
                disabled={isTranscribing}
                className={`relative w-24 h-24 rounded-full flex items-center justify-center transition-all disabled:opacity-50 disabled:cursor-not-allowed ${isListening
                    ? "bg-rose-500 shadow-[0_0_30px_rgba(244,63,94,0.4)] animate-pulse"
                    : "bg-gradient-to-tr from-amber-500 to-amber-400 text-zinc-950 shadow-[0_0_20px_rgba(245,158,11,0.2)] hover:scale-105"
                  }`}
              >
                {isListening ? (
                  <MicOff className="w-10 h-10 text-white" />
                ) : (
                  <Mic className="w-10 h-10 text-zinc-950" />
                )}
                {isListening && (
                  <span className="absolute -inset-2 rounded-full border-2 border-rose-500 animate-ping opacity-75"></span>
                )}
              </button>

              <div className="flex items-center justify-center gap-4 mt-2">
                <button
                  onClick={() => setIsAudioEnabled(!isAudioEnabled)}
                  className="flex items-center gap-1.5 px-3 py-1 bg-zinc-800/80 hover:bg-zinc-700/80 rounded-full text-xs text-zinc-400 hover:text-white transition-colors"
                >
                  {isAudioEnabled ? (
                    <>
                      <Volume2 className="w-3.5 h-3.5 text-amber-400" />
                      <span>Voz Activada</span>
                    </>
                  ) : (
                    <>
                      <VolumeX className="w-3.5 h-3.5" />
                      <span>Voz Silenciada</span>
                    </>
                  )}
                </button>
              </div>

              {recognitionError && (
                <div className="bg-rose-950/40 border border-rose-900/60 p-3 rounded-xl text-xs text-rose-300 flex items-start gap-2 text-left">
                  <ShieldAlert className="w-4 h-4 shrink-0 text-rose-400" />
                  <span>{recognitionError}</span>
                </div>
              )}
            </div>

            {/* Transcribiendo audio (sin transcripción todavía) */}
            {isTranscribing && !spokenText && (
              <div className="bg-zinc-900/20 border border-zinc-800/60 rounded-2xl p-6 text-center text-zinc-400 text-xs flex flex-col items-center gap-2 py-10">
                <Sparkles className="w-6 h-6 text-amber-500 animate-spin" />
                <span>Transcribiendo tu audio...</span>
              </div>
            )}

            {/* Realtime Spoken Transcript */}
            {spokenText && (
              <div className="bg-zinc-900/30 border border-zinc-800/50 rounded-xl p-4 flex flex-col gap-2">
                <div className="text-[10px] uppercase font-bold tracking-wider text-zinc-500 flex items-center gap-1.5">
                  {isTranscribing ? (
                    <>
                      <span className="w-2 h-2 rounded-full bg-amber-500 animate-pulse shrink-0"></span>
                      <span className="text-amber-400">Buscando la pregunta...</span>
                    </>
                  ) : (
                    <>
                      <span className="w-2 h-2 rounded-full bg-emerald-500 shrink-0"></span>
                      <span className="text-emerald-400">Transcripción lista</span>
                    </>
                  )}
                </div>
                {renderFormattedSpokenText(spokenText)}
              </div>
            )}

            {/* Answer Display Card */}
            {matchedQuestion ? renderAnswerCard() : spokenText && (
              <div className="bg-zinc-900/20 border border-zinc-800/60 rounded-2xl p-6 text-center text-zinc-400 text-xs flex flex-col items-center gap-2 py-10">
                {isTranscribing ? (
                  <>
                    <Sparkles className="w-6 h-6 text-amber-500 animate-spin" />
                    <span>Buscando la pregunta...</span>
                  </>
                ) : (
                  <>
                    <ShieldAlert className="w-5 h-5 text-rose-500" />
                    <span>No se encontró ninguna coincidencia exacta en el banco de preguntas. Intenta grabando de nuevo, dictando términos más específicos del ISTQB.</span>
                  </>
                )}
              </div>
            )}
          </div>
        )}

        {/* --- VIEW 1.5: WRITE MODULE --- */}
        {activeTab === "write" && (
          <div className="flex-1 flex flex-col gap-5">
            <div className="bg-zinc-900/50 border border-zinc-800/80 rounded-2xl p-6 flex flex-col gap-4">
              <h2 className="text-sm font-semibold text-zinc-300">Escribe la pregunta y las alternativas</h2>
              <textarea
                value={typedText}
                onChange={(e) => setTypedText(e.target.value)}
                placeholder='Ej: la pregunta es... la A es... la B es... la C es... la D es...'
                rows={6}
                className="bg-zinc-950 border border-zinc-800 focus:border-amber-500 focus:outline-none rounded-xl px-3 py-2.5 text-xs text-white transition-colors resize-none"
              />
              <button
                onClick={handleTypedSearch}
                disabled={!typedText.trim() || isSearchingTyped}
                className="w-full py-3 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 disabled:opacity-50 disabled:cursor-not-allowed text-zinc-950 rounded-xl text-xs font-bold transition-all"
              >
                {isSearchingTyped ? "Buscando..." : "Buscar respuesta"}
              </button>

              {recognitionError && (
                <div className="bg-rose-950/40 border border-rose-900/60 p-3 rounded-xl text-xs text-rose-300 flex items-start gap-2 text-left">
                  <ShieldAlert className="w-4 h-4 shrink-0 text-rose-400" />
                  <span>{recognitionError}</span>
                </div>
              )}
            </div>

            {matchedQuestion ? renderAnswerCard() : isSearchingTyped ? (
              <div className="bg-zinc-900/20 border border-zinc-800/60 rounded-2xl p-6 text-center text-zinc-400 text-xs flex flex-col items-center gap-2 py-10">
                <Sparkles className="w-6 h-6 text-amber-500 animate-spin" />
                <span>Buscando la pregunta...</span>
              </div>
            ) : searchedTypedText && (
              <div className="bg-zinc-900/20 border border-zinc-800/60 rounded-2xl p-6 text-center text-zinc-400 text-xs flex flex-col items-center gap-2 py-10">
                <ShieldAlert className="w-5 h-5 text-rose-500" />
                <span>No se encontró ninguna coincidencia. Intenta con términos más específicos del ISTQB.</span>
              </div>
            )}
          </div>
        )}

        {/* --- VIEW 2: EXAM SIMULATOR --- */}
        {activeTab === "simulator" && (
          <div className="flex-1 flex flex-col gap-4">

            {/* Simulacro en progreso */}
            {!showSimResults && simQuestions.length > 0 && (
              <>
                {/* Stats y Cronómetro */}
                <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-3 flex items-center justify-between text-xs">
                  <div className="flex items-center gap-1.5">
                    <span className="font-semibold text-white">Pregunta {currentSimIdx + 1}/{simQuestions.length}</span>
                  </div>
                  <div className="bg-zinc-800 px-3 py-1 rounded-full text-amber-400 font-mono font-bold tracking-wider">
                    {formatTime(timer)}
                  </div>
                </div>

                {/* Card de la Pregunta */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-5 flex flex-col gap-4">
                  <p className="text-sm font-medium text-white leading-relaxed">
                    {simQuestions[currentSimIdx]?.enunciado}
                  </p>

                  <div className="flex flex-col gap-2">
                    {["A", "B", "C", "D"].map((opt) => {
                      const text =
                        opt === "A" ? simQuestions[currentSimIdx]?.opcion_a :
                          opt === "B" ? simQuestions[currentSimIdx]?.opcion_b :
                            opt === "C" ? simQuestions[currentSimIdx]?.opcion_c : simQuestions[currentSimIdx]?.opcion_d;
                      const qId = simQuestions[currentSimIdx]?.id;
                      const isSelected = answers[qId] === opt;

                      return (
                        <button
                          key={opt}
                          onClick={() => selectOption(qId, opt)}
                          className={`flex items-start gap-2.5 p-3 rounded-xl border text-xs text-left transition-all ${isSelected
                              ? "bg-amber-500/10 border-amber-500 text-amber-100 shadow-[0_0_15px_rgba(245,158,11,0.05)]"
                              : "bg-zinc-900/30 border-zinc-800 hover:border-zinc-700 text-zinc-300"
                            }`}
                        >
                          <span className={`w-5 h-5 flex items-center justify-center rounded-md font-bold shrink-0 ${isSelected ? "bg-amber-500 text-zinc-950" : "bg-zinc-800 text-zinc-400"
                            }`}>
                            {opt}
                          </span>
                          <span className="leading-relaxed">{text}</span>
                        </button>
                      );
                    })}
                  </div>
                </div>

                {/* Navegación del Simulacro */}
                <div className="flex items-center justify-between gap-4 mt-2">
                  <button
                    disabled={currentSimIdx === 0}
                    onClick={() => setCurrentSimIdx(prev => prev - 1)}
                    className="flex-1 py-2.5 px-4 bg-zinc-800 hover:bg-zinc-700 disabled:opacity-40 rounded-xl text-xs font-semibold text-white transition-colors"
                  >
                    Anterior
                  </button>
                  {currentSimIdx < simQuestions.length - 1 ? (
                    <button
                      onClick={() => setCurrentSimIdx(prev => prev + 1)}
                      className="flex-1 py-2.5 px-4 bg-zinc-800 hover:bg-zinc-700 rounded-xl text-xs font-semibold text-white transition-colors"
                    >
                      Siguiente
                    </button>
                  ) : (
                    <button
                      onClick={() => {
                        setShowSimResults(true);
                        setIsTimerActive(false);
                      }}
                      className="flex-1 py-2.5 px-4 bg-gradient-to-r from-emerald-600 to-emerald-500 hover:from-emerald-500 hover:to-emerald-400 rounded-xl text-xs font-bold text-white transition-all shadow-md shadow-emerald-500/10"
                    >
                      Finalizar Examen
                    </button>
                  )}
                </div>
              </>
            )}

            {/* Resultados del simulacro */}
            {showSimResults && (
              <div className="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-5 flex flex-col gap-6 text-center items-center">
                <div className="bg-gradient-to-tr from-amber-500 to-amber-300 p-3.5 rounded-2xl text-zinc-950 font-bold shadow-[0_0_20px_rgba(245,158,11,0.15)] mt-2">
                  <Award className="w-8 h-8" />
                </div>

                <div>
                  <h3 className="text-lg font-bold text-white">Examen Finalizado</h3>
                  <p className="text-xs text-zinc-400 mt-1">Resultados calculados sobre el estándar ISTQB (mínimo 65% para aprobar)</p>
                </div>

                {/* Score Circular / Caja */}
                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 w-full flex items-center justify-around">
                  <div>
                    <div className="text-2xl font-black text-white">{calculateScore().correct} / {calculateScore().total}</div>
                    <div className="text-[10px] uppercase font-bold text-zinc-500 tracking-wider">Correctas</div>
                  </div>
                  <div className="h-8 w-px bg-zinc-800"></div>
                  <div>
                    <div className={`text-2xl font-black ${calculateScore().passed ? "text-emerald-400" : "text-rose-400"}`}>
                      {calculateScore().percentage}%
                    </div>
                    <div className="text-[10px] uppercase font-bold text-zinc-500 tracking-wider">Puntuación</div>
                  </div>
                </div>

                {/* Aprobado / Reprobado Alert */}
                {calculateScore().passed ? (
                  <div className="bg-emerald-950/30 border border-emerald-500/50 p-4 rounded-xl text-xs text-emerald-300 flex items-start gap-2.5 text-left w-full">
                    <CheckCircle2 className="w-5 h-5 shrink-0 text-emerald-400" />
                    <div>
                      <strong className="block font-semibold text-emerald-200">¡Aprobaste el examen!</strong>
                      Has superado el umbral del 65% requerido para la certificación de Tester Fundamento.
                    </div>
                  </div>
                ) : (
                  <div className="bg-rose-950/30 border border-rose-500/50 p-4 rounded-xl text-xs text-rose-300 flex items-start gap-2.5 text-left w-full">
                    <ShieldAlert className="w-5 h-5 shrink-0 text-rose-400" />
                    <div>
                      <strong className="block font-semibold text-rose-200">Examen No Aprobado</strong>
                      Necesitas al menos 65% de respuestas correctas. Sigue entrenando y repasando tus materiales.
                    </div>
                  </div>
                )}

                <button
                  onClick={startSimulator}
                  className="w-full py-3 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-zinc-950 rounded-xl text-xs font-bold transition-all"
                >
                  Iniciar Nuevo Simulacro
                </button>
              </div>
            )}
          </div>
        )}

        {/* --- VIEW 3: SETTINGS & DATABASE --- */}
        {activeTab === "db" && (
          <div className="flex-1 flex flex-col gap-4">
            <div className="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-5 flex flex-col gap-4">
              <div className="flex items-center gap-2 border-b border-zinc-800/80 pb-3">
                <Database className="w-5 h-5 text-amber-400" />
                <h3 className="font-semibold text-white text-sm">Conectar Base de Datos Supabase</h3>
              </div>

              <p className="text-xs text-zinc-400 leading-relaxed">
                Ingresa los datos de tu proyecto Supabase para poder almacenar y consultar miles de preguntas reales del examen ISTQB.
              </p>

              <div className="flex flex-col gap-3.5 mt-2">
                <div className="flex flex-col gap-1.5">
                  <label className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Supabase URL</label>
                  <input
                    type="text"
                    value={supabaseUrl}
                    onChange={(e) => setSupabaseUrl(e.target.value)}
                    placeholder="https://xxxxxx.supabase.co"
                    className="bg-zinc-950 border border-zinc-800 focus:border-amber-500 focus:outline-none rounded-xl px-3 py-2.5 text-xs text-white transition-colors"
                  />
                </div>
                <div className="flex flex-col gap-1.5">
                  <label className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Anon Key / API Key</label>
                  <input
                    type="password"
                    value={supabaseKey}
                    onChange={(e) => setSupabaseKey(e.target.value)}
                    placeholder="eyJhbGciOi..."
                    className="bg-zinc-950 border border-zinc-800 focus:border-amber-500 focus:outline-none rounded-xl px-3 py-2.5 text-xs text-white transition-colors"
                  />
                </div>
              </div>

              <button
                onClick={() => {
                  if (supabaseUrl && supabaseKey) {
                    setSupabaseConnected(true);
                    alert("¡Conexión guardada exitosamente (Modo Simulado)!");
                  } else {
                    alert("Por favor ingresa tanto la URL como la clave.");
                  }
                }}
                className="w-full mt-2 py-3 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-zinc-950 rounded-xl text-xs font-bold transition-all"
              >
                Guardar y Conectar Supabase
              </button>
            </div>

            {/* Panel de Configuración de voz (Groq Whisper) */}
            <div className="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-5 flex flex-col gap-4">
              <div className="flex items-center gap-2 border-b border-zinc-800/80 pb-3">
                <Mic className="w-5 h-5 text-amber-400" />
                <h3 className="font-semibold text-white text-sm">Transcripción de Voz (Groq)</h3>
              </div>

              <p className="text-xs text-zinc-400 leading-relaxed">
                Esta clave se usa únicamente para convertir tu voz grabada en texto (Whisper). Genera una API Key gratuita en console.groq.com.
              </p>

              <div className="flex flex-col gap-3.5 mt-2">
                <div className="flex flex-col gap-1.5">
                  <label className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Groq API Key</label>
                  <input
                    type="password"
                    value={groqApiKey}
                    onChange={(e) => setGroqApiKey(e.target.value)}
                    placeholder="gsk_xxxxxxxxxxxxxx"
                    className="bg-zinc-950 border border-zinc-800 focus:border-amber-500 focus:outline-none rounded-xl px-3 py-2.5 text-xs text-white transition-colors"
                  />
                </div>
              </div>

              <button
                onClick={() => {
                  if (groqApiKey.trim()) {
                    localStorage.setItem("groq_api_key", groqApiKey.trim());
                    alert("¡Clave de Groq guardada exitosamente!");
                  } else {
                    localStorage.removeItem("groq_api_key");
                    alert("Clave de Groq eliminada.");
                  }
                }}
                className="w-full mt-2 py-3 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-zinc-950 rounded-xl text-xs font-bold transition-all"
              >
                Guardar Clave de Groq
              </button>
            </div>

            {/* Panel de Configuración de IA (Gemini + búsqueda web) */}
            <div className="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-5 flex flex-col gap-4">
              <div className="flex items-center gap-2 border-b border-zinc-800/80 pb-3">
                <Sparkles className="w-5 h-5 text-amber-400" />
                <h3 className="font-semibold text-white text-sm">Respaldo Inteligente (Gemini)</h3>
              </div>

              <p className="text-xs text-zinc-400 leading-relaxed">
                Si una pregunta no se encuentra en el banco de preguntas, el sistema usará Gemini (con el temario oficial ya cargado y, si configuras Tavily abajo, resultados reales de internet) para analizarla y responder. Genera una API Key gratuita en aistudio.google.com.
              </p>

              <div className="flex flex-col gap-3.5 mt-2">
                <div className="flex flex-col gap-1.5">
                  <label className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Gemini API Key</label>
                  <input
                    type="password"
                    value={geminiApiKey}
                    onChange={(e) => setGeminiApiKey(e.target.value)}
                    placeholder="AIzaSyxxxxxxxxxxxxxx"
                    className="bg-zinc-950 border border-zinc-800 focus:border-amber-500 focus:outline-none rounded-xl px-3 py-2.5 text-xs text-white transition-colors"
                  />
                </div>
              </div>

              <button
                onClick={() => {
                  if (geminiApiKey.trim()) {
                    localStorage.setItem("gemini_api_key", geminiApiKey.trim());
                    alert("¡Clave de Gemini guardada exitosamente!");
                  } else {
                    localStorage.removeItem("gemini_api_key");
                    alert("Clave de Gemini eliminada.");
                  }
                }}
                className="w-full mt-2 py-3 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-zinc-950 rounded-xl text-xs font-bold transition-all"
              >
                Guardar Clave de Gemini
              </button>
            </div>

            {/* Panel de Configuración de Búsqueda Web (Tavily) */}
            <div className="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-5 flex flex-col gap-4">
              <div className="flex items-center gap-2 border-b border-zinc-800/80 pb-3">
                <Search className="w-5 h-5 text-amber-400" />
                <h3 className="font-semibold text-white text-sm">Búsqueda Web (Tavily)</h3>
              </div>

              <p className="text-xs text-zinc-400 leading-relaxed">
                Cuando Gemini responde una pregunta que no está en tu banco, esta clave le permite buscar en internet primero y anclar la respuesta en resultados reales en vez de solo su conocimiento entrenado. Genera una API Key gratuita en tavily.com.
              </p>

              <div className="flex flex-col gap-3.5 mt-2">
                <div className="flex flex-col gap-1.5">
                  <label className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Tavily API Key</label>
                  <input
                    type="password"
                    value={tavilyApiKey}
                    onChange={(e) => setTavilyApiKey(e.target.value)}
                    placeholder="tvly-xxxxxxxxxxxxxx"
                    className="bg-zinc-950 border border-zinc-800 focus:border-amber-500 focus:outline-none rounded-xl px-3 py-2.5 text-xs text-white transition-colors"
                  />
                </div>
              </div>

              <button
                onClick={() => {
                  if (tavilyApiKey.trim()) {
                    localStorage.setItem("tavily_api_key", tavilyApiKey.trim());
                    alert("¡Clave de Tavily guardada exitosamente!");
                  } else {
                    localStorage.removeItem("tavily_api_key");
                    alert("Clave de Tavily eliminada.");
                  }
                }}
                className="w-full mt-2 py-3 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-zinc-950 rounded-xl text-xs font-bold transition-all"
              >
                Guardar Clave de Tavily
              </button>
            </div>

            {/* Nota de Ayuda */}
            <div className="bg-zinc-900/30 border border-zinc-800/80 rounded-xl p-4 text-[11px] text-zinc-400 leading-relaxed">
              <strong className="text-zinc-300 block mb-1">Nota:</strong>
              Para un entorno de producción, guardaremos estas credenciales directamente en un archivo de configuración `.env.local` de Next.js para proteger tu clave secreta de forma segura en el servidor.
            </div>
          </div>
        )}
      </main>

      {/* Footer minimalista */}
      <footer className="text-center py-5 text-[10px] text-zinc-600 border-t border-zinc-900 mt-auto">
        Diseñado para estudio inteligente del ISTQB &copy; {new Date().getFullYear()}
      </footer>
    </div>
  );
}
