# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")

import json
import os

PREGUNTAS_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "app", "preguntas.json")

SIMULACRO_10 = [
    {
        "enunciado": "¿Cuál de las siguientes NO es una razón común para realizar pruebas?",
        "opcion_a": "Demostrar que el software está 100% libre de defectos.",
        "opcion_b": "Aumentar la confianza en el software.",
        "opcion_c": "Reducir el riesgo.",
        "opcion_d": "Encontrar defectos.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Las pruebas nunca pueden demostrar que el software esté completamente libre de defectos.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de los siguientes NO es un objetivo principal de las pruebas?",
        "opcion_a": "Prevenir defectos.",
        "opcion_b": "Ganar más dinero.",
        "opcion_c": "Mejorar la confianza en el software.",
        "opcion_d": "Encontrar defectos.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "\"Ganar más dinero\" no es un objetivo de las pruebas reconocido por ISTQB.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Qué nivel de pruebas se centra en probar la interacción entre diferentes sistemas?",
        "opcion_a": "Prueba de integración.",
        "opcion_b": "Prueba de aceptación.",
        "opcion_c": "Prueba de unidad.",
        "opcion_d": "Prueba de sistema",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Sin la opción especializada de \"Integración de Sistema\", la prueba de integración es la que mejor cubre la interacción entre sistemas/componentes.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes es una técnica de prueba estática?",
        "opcion_a": "Prueba de tabla de decisión.",
        "opcion_b": "Prueba de partición de equivalencia.",
        "opcion_c": "Prueba de valores límite.",
        "opcion_d": "Revisión de código.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La revisión de código es una técnica de prueba estática. Las demás son técnicas dinámicas de caja negra.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe la técnica de análisis de valores límite?",
        "opcion_a": "Utilizar una tabla para definir las combinaciones de entradas y salidas esperadas.",
        "opcion_b": "Analizar el código fuente para identificar posibles defectos.",
        "opcion_c": "Probar los valores en los límites de un rango de entrada válido.",
        "opcion_d": "Identificar grupos de entradas que se espera que se procesen de la misma manera.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "El análisis de valores límite prueba los valores justo en, por debajo y por encima de los límites de un rango de entrada.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Qué tipo de prueba se realiza para verificar que los cambios en el sistema no han afectado negativamente a la funcionalidad existente?",
        "opcion_a": "Prueba de aceptación.",
        "opcion_b": "Prueba de migración.",
        "opcion_c": "Prueba de integración.",
        "opcion_d": "Prueba de regresión.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de regresión confirma que un cambio no ha afectado negativamente funcionalidad ya existente.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la gestión de riesgos en las pruebas?",
        "opcion_a": "Controlar las versiones del software y los artefactos de prueba.",
        "opcion_b": "Evaluar los riesgos asociados con el uso del software.",
        "opcion_c": "Identificar, analizar y controlar los riesgos que pueden afectar a las pruebas.",
        "opcion_d": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La gestión de riesgos identifica, analiza y controla los riesgos que pueden afectar a las pruebas.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un tipo de informe de prueba?",
        "opcion_a": "Informe de resumen de prueba.",
        "opcion_b": "Informe de diseño de la interfaz de usuario.",
        "opcion_c": "Informe de incidente de prueba.",
        "opcion_d": "Informe de progreso de prueba.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Un informe de diseño de interfaz de usuario no es un artefacto del proceso de prueba.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes herramientas se utiliza para la automatización de pruebas?",
        "opcion_a": "Herramienta de prueba de rendimiento.",
        "opcion_b": "Herramienta de gestión de pruebas.",
        "opcion_c": "Herramienta de ejecución de pruebas.",
        "opcion_d": "Herramienta de análisis estático.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Una herramienta de ejecución de pruebas es la que automatiza específicamente la ejecución de casos de prueba.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el concepto de 'probabilidad' de un defecto?",
        "opcion_a": "El impacto del defecto en el funcionamiento del sistema.",
        "opcion_b": "La dificultad de encontrar un defecto.",
        "opcion_c": "La frecuencia con la que se espera que ocurra un defecto.",
        "opcion_d": "La combinación de la probabilidad de un fallo y la gravedad de su impacto.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La probabilidad indica la frecuencia con la que se espera que ocurra un defecto.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes NO es una ventaja de las pruebas independientes?",
        "opcion_a": "Mayor confianza en la calidad del software.",
        "opcion_b": "Reducción del coste de las pruebas.",
        "opcion_c": "Mayor objetividad en las pruebas.",
        "opcion_d": "Mayor probabilidad de encontrar defectos.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La independencia no reduce el coste de las pruebas; sus beneficios reales son objetividad, mayor detección de defectos y confianza en la calidad.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de los siguientes es un ejemplo de prueba no funcional?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de rendimiento.",
        "opcion_c": "Prueba de tabla de decisión.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de rendimiento evalúa un atributo de calidad no funcional. Las demás son técnicas de diseño de pruebas funcionales.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes afirmaciones sobre la prueba de integración es CORRECTA?",
        "opcion_a": "La prueba de integración no es necesaria si se ha realizado una prueba de unidad exhaustiva.",
        "opcion_b": "La prueba de integración se realiza después de la prueba de sistema.",
        "opcion_c": "La prueba de integración se centra en probar las interfaces entre los módulos.",
        "opcion_d": "La prueba de integración solo se puede realizar utilizando el enfoque de arriba hacia abajo.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de integración se enfoca en las interfaces y la interacción entre componentes o sistemas.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe la técnica de prueba de transición de estados?",
        "opcion_a": "Utilizar un grafo para representar los estados y las transiciones entre estados.",
        "opcion_b": "Probar los valores en los límites de un rango de entrada.",
        "opcion_c": "Identificar las condiciones y las acciones que se deben tomar en función de las combinaciones de condiciones.",
        "opcion_d": "Analizar el código fuente para identificar posibles defectos.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba de transición de estados modela el sistema como estados y las transiciones válidas/inválidas entre ellos.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes NO es una actividad típica de la ejecución de las pruebas?",
        "opcion_a": "Estimar el esfuerzo de las pruebas.",
        "opcion_b": "Reportar los defectos encontrados.",
        "opcion_c": "Ejecutar los casos de prueba.",
        "opcion_d": "Registrar los resultados de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Estimar el esfuerzo de las pruebas es una actividad de PLANIFICACIÓN, no de ejecución.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito del control de las pruebas?",
        "opcion_a": "Automatizar la ejecución de las pruebas.",
        "opcion_b": "Tomar acciones correctivas cuando las pruebas se desvían del plan.",
        "opcion_c": "Evaluar la calidad del software.",
        "opcion_d": "Controlar el progreso de las pruebas en relación con el plan.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El control de pruebas toma acciones correctivas cuando el progreso real se desvía de lo planificado.",
        "modelo_examen": "Simulacro 10"
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
        "modelo_examen": "Simulacro 10"
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
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre pruebas funcionales y no funcionales?",
        "opcion_a": "Las pruebas funcionales se centran en lo que el sistema debe hacer, mientras que las pruebas no funcionales se centran en cómo lo hace.",
        "opcion_b": "Las pruebas funcionales se realizan por el equipo de desarrollo, mientras que las pruebas no funcionales se realizan por el equipo de pruebas.",
        "opcion_c": "Las pruebas funcionales se realizan al principio del ciclo de vida del desarrollo, mientras que las pruebas no funcionales se realizan al final.",
        "opcion_d": "Las pruebas funcionales son más importantes que las pruebas no funcionales.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Las pruebas funcionales evalúan QUÉ hace el sistema; las no funcionales evalúan CÓMO lo hace.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un factor que influye en la priorización de las pruebas?",
        "opcion_a": "La complejidad de la funcionalidad.",
        "opcion_b": "La importancia de la funcionalidad para el usuario.",
        "opcion_c": "El riesgo asociado con la funcionalidad.",
        "opcion_d": "La disponibilidad de las herramientas de prueba.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La disponibilidad de herramientas no es un factor de priorización de pruebas.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes es una técnica de diseño de pruebas de caja negra?",
        "opcion_a": "Prueba de caminos básicos.",
        "opcion_b": "Prueba de condición.",
        "opcion_c": "Prueba de bucle.",
        "opcion_d": "Prueba de tabla de decisión.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La tabla de decisión es una técnica de caja negra. Las demás son técnicas de caja blanca.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un objetivo típico de las pruebas de seguridad?",
        "opcion_a": "Evaluar la integridad de los datos.",
        "opcion_b": "Evaluar la facilidad de uso del sistema.",
        "opcion_c": "Evaluar la disponibilidad del sistema.",
        "opcion_d": "Evaluar la confidencialidad de los datos.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La facilidad de uso es objetivo de la prueba de usabilidad, no de seguridad.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de regresión?",
        "opcion_a": "Probar el rendimiento del sistema bajo carga.",
        "opcion_b": "Evaluar la usabilidad del sistema.",
        "opcion_c": "Probar nuevas funcionalidades del sistema.",
        "opcion_d": "Verificar que los cambios en el sistema no han introducido nuevos defectos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de regresión confirma que un cambio no ha afectado negativamente funcionalidad ya existente.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una tarea en la gestión de defectos?",
        "opcion_a": "Detectar defectos.",
        "opcion_b": "Prevenir defectos.",
        "opcion_c": "Corregir defectos.",
        "opcion_d": "Analizar la causa raíz de los defectos.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Detectar un defecto ocurre durante la ejecución de pruebas o revisiones, fuera del proceso de gestión de defectos propiamente dicho.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de un informe de incidente de prueba?",
        "opcion_a": "Evaluar los riesgos asociados con las pruebas.",
        "opcion_b": "Planificar y controlar las actividades de prueba.",
        "opcion_c": "Controlar las versiones del software y los artefactos de prueba.",
        "opcion_d": "Documentar los detalles de un defecto encontrado durante las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "El informe de incidente de prueba documenta los detalles de un defecto encontrado durante las pruebas.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Qué técnica de prueba se centra en probar las respuestas del sistema a entradas inválidas o inesperadas?",
        "opcion_a": "Prueba negativa.",
        "opcion_b": "Prueba de casos de uso.",
        "opcion_c": "Partición de equivalencia.",
        "opcion_d": "Prueba de tabla de decisión.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba negativa evalúa cómo responde el sistema ante entradas inválidas o inesperadas.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar si un sistema puede funcionar en diferentes plataformas de hardware o software?",
        "opcion_a": "Prueba de seguridad.",
        "opcion_b": "Prueba de compatibilidad.",
        "opcion_c": "Prueba de rendimiento.",
        "opcion_d": "Prueba de usabilidad.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de compatibilidad verifica que el sistema funcione correctamente en distintas plataformas de hardware/software.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre un defecto y un fallo?",
        "opcion_a": "Un defecto es un problema reportado por el usuario, mientras que un fallo es un problema encontrado por el tester.",
        "opcion_b": "Un defecto es un problema menor, mientras que un fallo es un problema grave.",
        "opcion_c": "Un defecto es un problema en el software, mientras que un fallo es un problema en el hardware.",
        "opcion_d": "Un defecto es una imperfección en el software, mientras que un fallo es una desviación del comportamiento esperado.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Un defecto es una imperfección en el producto de trabajo; un fallo es la desviación observable del comportamiento esperado cuando ese defecto se ejecuta.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una responsabilidad típica del líder de pruebas?",
        "opcion_a": "Planificar las actividades de prueba.",
        "opcion_b": "Monitorear el progreso de las pruebas.",
        "opcion_c": "Asignar tareas al equipo de pruebas.",
        "opcion_d": "Corregir defectos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Corregir defectos es responsabilidad del equipo de desarrollo, no del líder de pruebas.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de aceptación del usuario?",
        "opcion_a": "Probar la seguridad del sistema.",
        "opcion_b": "Probar las unidades individuales de código.",
        "opcion_c": "Verificar que el sistema cumple con las necesidades del usuario en su entorno real.",
        "opcion_d": "Probar la interacción entre diferentes módulos del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de aceptación del usuario (UAT) verifica que el sistema cumple con las necesidades del usuario en un entorno real.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Qué técnica de prueba se centra en probar las transiciones entre diferentes estados de un sistema?",
        "opcion_a": "Prueba de casos de uso.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Prueba de partición de equivalencia.",
        "opcion_d": "Prueba de transición de estados.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de transición de estados modela el sistema como estados y las transiciones válidas/inválidas entre ellos.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un beneficio de la automatización de pruebas?",
        "opcion_a": "Eliminación de la necesidad de pruebas manuales.",
        "opcion_b": "Mayor eficiencia de las pruebas.",
        "opcion_c": "Mayor cobertura de pruebas.",
        "opcion_d": "Mayor repetibilidad de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La automatización NO elimina la necesidad de pruebas manuales (exploratorias, de usabilidad, etc.).",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de un plan de pruebas?",
        "opcion_a": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_b": "Guiar las actividades de prueba.",
        "opcion_c": "Evaluar la calidad del software.",
        "opcion_d": "Documentar los resultados de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El plan de pruebas documenta el enfoque, alcance, recursos y cronograma, y sirve para guiar las actividades de prueba.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar si un sistema puede manejar grandes volúmenes de datos o usuarios?",
        "opcion_a": "Prueba de estrés.",
        "opcion_b": "Prueba de volumen.",
        "opcion_c": "Prueba de rendimiento.",
        "opcion_d": "Prueba de carga.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de volumen evalúa específicamente el manejo de grandes volúmenes de datos/usuarios por parte del sistema (confirmado en exámenes previos con resultados reales).",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un atributo de calidad del software según la norma ISO 25010?",
        "opcion_a": "Fiabilidad.",
        "opcion_b": "Coste.",
        "opcion_c": "Usabilidad.",
        "opcion_d": "Funcionalidad.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El coste es una restricción de proyecto/negocio, no una característica de calidad del producto según ISO 25010.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de seguridad?",
        "opcion_a": "Probar el rendimiento del sistema bajo carga.",
        "opcion_b": "Evaluar la facilidad con la que los usuarios pueden utilizar un sistema.",
        "opcion_c": "Verificar que el sistema está protegido contra accesos no autorizados.",
        "opcion_d": "Probar la compatibilidad del sistema con diferentes plataformas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de seguridad verifica la protección de datos y funcionalidad ante accesos, usos o modificaciones no autorizadas.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Qué tipo de revisión implica una reunión formal con un equipo de revisores?",
        "opcion_a": "Recorrido.",
        "opcion_b": "Revisión informal.",
        "opcion_c": "Inspección.",
        "opcion_d": "Revisión técnica.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La inspección es el tipo de revisión más formal: proceso definido, moderador entrenado, checklists, métricas y una reunión formal de revisión.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un tipo de defecto?",
        "opcion_a": "Error de codificación.",
        "opcion_b": "Error de diseño.",
        "opcion_c": "Error de documentación.",
        "opcion_d": "Error de ejecución.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Un \"error de ejecución\" describe un fallo (failure) en tiempo de ejecución, no un tipo de defecto estático en un producto de trabajo.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de compatibilidad?",
        "opcion_a": "Probar la seguridad del sistema.",
        "opcion_b": "Evaluar la facilidad con la que los usuarios pueden utilizar un sistema.",
        "opcion_c": "Verificar que el sistema funciona correctamente en diferentes entornos.",
        "opcion_d": "Probar el rendimiento del sistema bajo carga.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de compatibilidad verifica que el sistema funcione correctamente en distintos entornos.",
        "modelo_examen": "Simulacro 10"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una técnica de gestión de pruebas?",
        "opcion_a": "Gestión de la configuración.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Planificación de pruebas.",
        "opcion_d": "Seguimiento de pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de integración es un nivel/tipo de prueba, no una técnica de gestión de pruebas.",
        "modelo_examen": "Simulacro 10"
    },
]


def main():
    with open(PREGUNTAS_PATH, "r", encoding="utf-8") as f:
        existing = json.load(f)

    print(f"Preguntas existentes antes de agregar: {len(existing)}")

    existing.extend(SIMULACRO_10)

    with open(PREGUNTAS_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"Se agregaron {len(SIMULACRO_10)} preguntas del Simulacro 10.")
    print(f"Total de preguntas ahora: {len(existing)}")


if __name__ == "__main__":
    main()
