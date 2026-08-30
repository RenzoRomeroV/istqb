# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")

import json
import os

PREGUNTAS_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "app", "preguntas.json")

SIMULACRO_7 = [
    {
        "enunciado": "¿Cuál de las siguientes NO es una actividad principal del proceso fundamental de prueba?",
        "opcion_a": "Planificación de las pruebas.",
        "opcion_b": "Diseño de las pruebas.",
        "opcion_c": "Corrección de defectos.",
        "opcion_d": "Ejecución de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Corregir defectos es una actividad de DESARROLLO, no del proceso de prueba.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de los siguientes es un principio fundamental de las pruebas?",
        "opcion_a": "Las pruebas exhaustivas son siempre posibles.",
        "opcion_b": "Las pruebas pueden demostrar la ausencia de defectos.",
        "opcion_c": "Las pruebas deben comenzar tan pronto como sea posible en el ciclo de vida del software.",
        "opcion_d": "Las pruebas no dependen del contexto.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Cuanto antes se detecta un defecto en el ciclo de vida, más barato resulta corregirlo (principio de pruebas tempranas).",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Qué nivel de pruebas se centra en probar el sistema completo como un todo?",
        "opcion_a": "Prueba de unidad.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de sistema.",
        "opcion_d": "Prueba de aceptación.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de sistema evalúa el comportamiento del sistema completo e integrado.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes técnicas es una técnica de prueba dinámica?",
        "opcion_a": "Revisión de código.",
        "opcion_b": "Inspección.",
        "opcion_c": "Prueba de caja negra.",
        "opcion_d": "Análisis estático.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de caja negra requiere ejecutar el software (dinámica). Las demás son técnicas estáticas.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe la técnica de análisis de valores límite?",
        "opcion_a": "Identificar grupos de entradas que se espera que se procesen de la misma manera.",
        "opcion_b": "Probar los valores en los límites de un rango de entrada válido.",
        "opcion_c": "Utilizar una tabla para definir las combinaciones de entradas y salidas esperadas.",
        "opcion_d": "Analizar el código fuente para identificar posibles defectos.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El análisis de valores límite prueba los valores justo en, por debajo y por encima de los límites de un rango de entrada.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Qué tipo de prueba se realiza para verificar que el sistema funciona correctamente después de ser migrado a un nuevo entorno?",
        "opcion_a": "Prueba de regresión.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de migración.",
        "opcion_d": "Prueba de aceptación.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de migración verifica que el sistema funcione correctamente tras ser migrado a un nuevo entorno.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la gestión de riesgos en las pruebas?",
        "opcion_a": "Controlar las versiones del software y los artefactos de prueba.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_c": "Identificar, analizar y controlar los riesgos que pueden afectar a las pruebas.",
        "opcion_d": "Evaluar los riesgos asociados con el uso del software.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La gestión de riesgos identifica, analiza y controla los riesgos que pueden afectar a las pruebas.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un tipo de informe de prueba?",
        "opcion_a": "Informe de incidente de prueba.",
        "opcion_b": "Informe de resumen de prueba.",
        "opcion_c": "Informe de progreso de prueba.",
        "opcion_d": "Informe de diseño de la interfaz de usuario.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Un informe de diseño de interfaz de usuario no es un artefacto del proceso de prueba.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes herramientas se utiliza para la automatización de pruebas?",
        "opcion_a": "Herramienta de gestión de pruebas.",
        "opcion_b": "Herramienta de análisis estático.",
        "opcion_c": "Herramienta de prueba de rendimiento.",
        "opcion_d": "Herramienta de ejecución de pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Una herramienta de ejecución de pruebas es la que automatiza específicamente la ejecución de casos de prueba.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el concepto de \"probabilidad\" de un defecto?",
        "opcion_a": "La frecuencia con la que se espera que ocurra un defecto.",
        "opcion_b": "El impacto del defecto en el funcionamiento del sistema.",
        "opcion_c": "La combinación de la probabilidad de un fallo y la gravedad de su impacto.",
        "opcion_d": "La dificultad de encontrar un defecto.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La probabilidad indica la frecuencia con la que se espera que ocurra un defecto.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes NO es una ventaja de las pruebas independientes?",
        "opcion_a": "Mayor objetividad en las pruebas.",
        "opcion_b": "Mayor probabilidad de encontrar defectos.",
        "opcion_c": "Reducción del coste de las pruebas.",
        "opcion_d": "Mayor confianza en la calidad del software.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La independencia no reduce el coste de las pruebas; sus beneficios reales son objetividad, mayor detección de defectos y confianza en la calidad.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de los siguientes es un ejemplo de prueba funcional?",
        "opcion_a": "Prueba de carga.",
        "opcion_b": "Prueba de usabilidad.",
        "opcion_c": "Prueba de seguridad.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de casos de uso evalúa el comportamiento funcional del sistema. Las demás son pruebas no funcionales.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes afirmaciones sobre la prueba de sistema es CORRECTA?",
        "opcion_a": "La prueba de sistema se realiza antes de la prueba de integración.",
        "opcion_b": "La prueba de sistema se centra en probar las interfaces entre los módulos.",
        "opcion_c": "La prueba de sistema se realiza en el entorno, en condiciones ideales, de producción.",
        "opcion_d": "La prueba de sistema no es necesaria si se ha realizado una prueba de integración exhaustiva.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de sistema evalúa el sistema completo e integrado en un entorno similar al de producción.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe la técnica de prueba de estado?",
        "opcion_a": "Identificar las condiciones y las acciones que se deben tomar en función de las combinaciones de condiciones.",
        "opcion_b": "Probar los valores en los límites de un rango de entrada.",
        "opcion_c": "Utilizar un grafo para representar los estados y las transiciones entre estados.",
        "opcion_d": "Analizar el código fuente para identificar posibles defectos.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de transición de estados modela el sistema como estados y las transiciones válidas/inválidas entre ellos.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes NO es una actividad típica de la ejecución de las pruebas?",
        "opcion_a": "Ejecutar los casos de prueba.",
        "opcion_b": "Registrar los resultados de las pruebas.",
        "opcion_c": "Estimar el esfuerzo de las pruebas.",
        "opcion_d": "Reportar los defectos encontrados.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Estimar el esfuerzo de las pruebas es una actividad de PLANIFICACIÓN, no de ejecución.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito del control de las pruebas?",
        "opcion_a": "Controlar el progreso de las pruebas en relación con el plan.",
        "opcion_b": "Tomar acciones correctivas cuando las pruebas se desvían del plan.",
        "opcion_c": "Evaluar la calidad del software.",
        "opcion_d": "Automatizar la ejecución de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El control de pruebas toma acciones correctivas cuando el progreso real se desvía de lo planificado.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un objetivo de las revisiones?",
        "opcion_a": "Encontrar defectos.",
        "opcion_b": "Mejorar la calidad del software.",
        "opcion_c": "Ejecutar el código.",
        "opcion_d": "Compartir conocimiento.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las revisiones son estáticas: no ejecutan el código.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba alfa?",
        "opcion_a": "Se realiza por usuarios reales en el entorno de producción.",
        "opcion_b": "Se realiza por testers internos en un entorno simulado.",
        "opcion_c": "Se realiza por testers externos en un entorno controlado.",
        "opcion_d": "Se realiza por desarrolladores en su propio entorno.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba alfa se realiza en el sitio del desarrollador, por un equipo interno pero independiente, en un entorno simulado.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre pruebas funcionales y no funcionales?",
        "opcion_a": "Las pruebas funcionales se centran en lo que el sistema debe hacer, mientras que las pruebas no funcionales se centran en cómo lo hace.",
        "opcion_b": "Las pruebas funcionales se realizan por el equipo de desarrollo, mientras que las pruebas no funcionales se realizan por el equipo de pruebas.",
        "opcion_c": "Las pruebas funcionales son más importantes que las pruebas no funcionales.",
        "opcion_d": "Las pruebas funcionales se realizan al principio del ciclo de vida del desarrollo, mientras que las pruebas no funcionales se realizan al final.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Las pruebas funcionales evalúan QUÉ hace el sistema; las no funcionales evalúan CÓMO lo hace.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un factor que influye en la priorización de las pruebas?",
        "opcion_a": "El riesgo asociado con la funcionalidad.",
        "opcion_b": "La complejidad de la funcionalidad.",
        "opcion_c": "La disponibilidad de las herramientas de prueba.",
        "opcion_d": "La importancia de la funcionalidad para el usuario.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La disponibilidad de herramientas no es un factor de priorización de pruebas.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes es una técnica de diseño de pruebas de caja blanca?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Prueba de casos de uso.",
        "opcion_d": "Prueba de condición.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de condición es una técnica de caja blanca. Las demás son técnicas de caja negra.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un objetivo típico de las pruebas de seguridad?",
        "opcion_a": "Evaluar la confidencialidad de los datos.",
        "opcion_b": "Evaluar la integridad de los datos.",
        "opcion_c": "Evaluar la disponibilidad del sistema.",
        "opcion_d": "Evaluar la facilidad de uso del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La facilidad de uso es objetivo de la prueba de usabilidad, no de seguridad.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de regresión?",
        "opcion_a": "Probar nuevas funcionalidades del sistema.",
        "opcion_b": "Verificar que los cambios en el sistema no han introducido nuevos defectos.",
        "opcion_c": "Probar el rendimiento del sistema bajo carga.",
        "opcion_d": "Evaluar la usabilidad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de regresión confirma que un cambio no ha afectado negativamente funcionalidad ya existente.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una tarea en la gestión de defectos?",
        "opcion_a": "Detectar defectos.",
        "opcion_b": "Corregir defectos.",
        "opcion_c": "Analizar la causa raíz de los defectos.",
        "opcion_d": "Prevenir defectos.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Detectar un defecto ocurre durante la ejecución de pruebas o revisiones, fuera del proceso de gestión de defectos propiamente dicho.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de un informe de incidente de prueba?",
        "opcion_a": "Controlar las versiones del software y los artefactos de prueba.",
        "opcion_b": "Documentar los detalles de un defecto encontrado durante las pruebas.",
        "opcion_c": "Planificar y controlar las actividades de prueba.",
        "opcion_d": "Evaluar los riesgos asociados con las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El informe de incidente de prueba documenta los detalles de un defecto encontrado durante las pruebas.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Qué técnica de prueba se centra en probar las respuestas del sistema a entradas inválidas o inesperadas?",
        "opcion_a": "Partición de equivalencia.",
        "opcion_b": "Prueba negativa.",
        "opcion_c": "Prueba de tabla de decisión.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba negativa evalúa cómo responde el sistema ante entradas inválidas o inesperadas.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar si un sistema puede funcionar en diferentes plataformas de hardware o software?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Prueba de compatibilidad.",
        "opcion_c": "Prueba de seguridad.",
        "opcion_d": "Prueba de usabilidad.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de compatibilidad verifica que el sistema funcione correctamente en distintas plataformas de hardware/software.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre un error y un fallo?",
        "opcion_a": "Un error es un problema reportado por el usuario, mientras que un fallo es un problema encontrado por el tester.",
        "opcion_b": "Un error es un problema menor, mientras que un fallo es un problema grave.",
        "opcion_c": "Un error es una acción humana que produce un resultado incorrecto, mientras que un fallo es una desviación del comportamiento esperado.",
        "opcion_d": "Un error es un problema en el software, mientras que un fallo es un problema en el hardware.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Un error humano puede introducir un defecto que, al ejecutarse, produce un fallo (desviación observable del comportamiento esperado).",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una responsabilidad típica del tester?",
        "opcion_a": "Diseñar casos de prueba.",
        "opcion_b": "Ejecutar casos de prueba.",
        "opcion_c": "Corregir defectos.",
        "opcion_d": "Reportar defectos.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Corregir defectos es responsabilidad del equipo de desarrollo, no del tester.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de componentes?",
        "opcion_a": "Probar las unidades individuales de código.",
        "opcion_b": "Probar la interacción entre diferentes módulos del sistema.",
        "opcion_c": "Probar un grupo de componentes relacionados que interactúan entre sí.",
        "opcion_d": "Probar la seguridad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Confirmado por resultados de exámenes previos: este banco de preguntas define la prueba de componentes como la prueba de un grupo de componentes relacionados que interactúan entre sí.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Qué técnica de prueba se centra en identificar las condiciones que deben cumplirse para que un sistema funcione correctamente?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Prueba de condición.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de condición diseña casos de prueba para ejercitar el resultado de condiciones lógicas individuales.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un beneficio de las pruebas independientes?",
        "opcion_a": "Mayor objetividad en las pruebas.",
        "opcion_b": "Mayor probabilidad de encontrar defectos.",
        "opcion_c": "Reducción del coste de las pruebas.",
        "opcion_d": "Mayor confianza en la calidad del software.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La independencia no reduce el coste de las pruebas.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de un informe de resumen de prueba?",
        "opcion_a": "Documentar los resultados de las pruebas.",
        "opcion_b": "Describir un defecto encontrado durante las pruebas.",
        "opcion_c": "Proporcionar una visión general de las actividades de prueba y los resultados.",
        "opcion_d": "Evaluar la calidad del software.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "El informe de resumen de prueba presenta una visión general de las actividades y los resultados de las pruebas.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar la cantidad de usuarios o transacciones que un sistema puede manejar simultáneamente?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Prueba de carga.",
        "opcion_c": "Prueba de estrés.",
        "opcion_d": "Prueba de concurrencia.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Confirmado por resultados de exámenes previos: cuando la pregunta enfatiza el manejo SIMULTÁNEO de usuarios/transacciones, este banco de preguntas espera 'prueba de concurrencia' como respuesta.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un principio de la gestión de la configuración?",
        "opcion_a": "Identificación.",
        "opcion_b": "Control de cambios.",
        "opcion_c": "Ejecución de pruebas.",
        "opcion_d": "Auditoría.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La ejecución de pruebas no es un principio de la gestión de la configuración.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de usabilidad?",
        "opcion_a": "Evaluar la facilidad con la que los usuarios pueden utilizar un sistema.",
        "opcion_b": "Probar el rendimiento del sistema bajo carga.",
        "opcion_c": "Verificar que el sistema puede recuperarse después de un fallo.",
        "opcion_d": "Probar la compatibilidad del sistema con diferentes plataformas.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba de usabilidad evalúa qué tan fácil e intuitivo es para los usuarios utilizar el sistema.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar el tiempo que tarda un sistema en realizar una tarea específica?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Prueba de tiempo de respuesta.",
        "opcion_c": "Prueba de carga.",
        "opcion_d": "Prueba de estrés.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Confirmado por resultados de exámenes previos: cuando la pregunta enfatiza el tiempo para una tarea específica, este banco de preguntas espera 'prueba de tiempo de respuesta' como respuesta.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una característica de un buen caso de prueba?",
        "opcion_a": "Preciso.",
        "opcion_b": "Repetible.",
        "opcion_c": "Complejo.",
        "opcion_d": "Trazable.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Un buen caso de prueba debe ser simple y conciso, no complejo.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de aceptación operativa?",
        "opcion_a": "Evaluar la facilidad con la que los usuarios pueden utilizar un sistema.",
        "opcion_b": "Probar el rendimiento del sistema bajo carga.",
        "opcion_c": "Verificar que el sistema cumple con los requisitos no funcionales.",
        "opcion_d": "Probar la seguridad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de aceptación operativa (OAT) verifica aspectos operativos y otros requisitos no funcionales antes de la puesta en producción.",
        "modelo_examen": "Simulacro 7"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una técnica de gestión de defectos?",
        "opcion_a": "Registro de defectos.",
        "opcion_b": "Clasificación de defectos.",
        "opcion_c": "Prueba de integración.",
        "opcion_d": "Priorización de defectos.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de integración es un nivel/tipo de prueba, no una técnica de gestión de defectos.",
        "modelo_examen": "Simulacro 7"
    },
]


def main():
    with open(PREGUNTAS_PATH, "r", encoding="utf-8") as f:
        existing = json.load(f)

    print(f"Preguntas existentes antes de agregar: {len(existing)}")

    existing.extend(SIMULACRO_7)

    with open(PREGUNTAS_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"Se agregaron {len(SIMULACRO_7)} preguntas del Simulacro 7.")
    print(f"Total de preguntas ahora: {len(existing)}")


if __name__ == "__main__":
    main()
