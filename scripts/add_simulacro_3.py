# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")

import json
import os

PREGUNTAS_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "app", "preguntas.json")

SIMULACRO_3 = [
    {
        "enunciado": "¿Cuál de las siguientes NO es una de las siete pruebas de principios de software?",
        "opcion_a": "Las pruebas exhaustivas son imposibles.",
        "opcion_b": "La detección temprana de defectos es económicamente beneficiosa.",
        "opcion_c": "Las pruebas deben ser realizadas únicamente por testers independientes.",
        "opcion_d": "Las pruebas dependen del contexto.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "No es uno de los 7 principios de las pruebas. Las pruebas exhaustivas son imposibles, la detección temprana reduce costes y las pruebas son dependientes del contexto sí son principios reconocidos; la independencia de los testers es una consideración de organización, no un principio.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes afirmaciones sobre las pruebas es INCORRECTA?",
        "opcion_a": "Las pruebas pueden mostrar la presencia de defectos.",
        "opcion_b": "Las pruebas reducen el riesgo de que los defectos causen fallos en el software.",
        "opcion_c": "Las pruebas pueden garantizar que el software esté completamente libre de defectos.",
        "opcion_d": "Las pruebas ayudan a construir confianza en la calidad del software.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las pruebas muestran la PRESENCIA de defectos, nunca pueden garantizar su ausencia total (uno de los 7 principios fundamentales).",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Qué nivel de pruebas se centra en la verificación de los requisitos no funcionales, como el rendimiento, la seguridad y la usabilidad?",
        "opcion_a": "Prueba de unidad.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de sistema.",
        "opcion_d": "Prueba de aceptación.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de sistema evalúa el comportamiento del sistema completo, incluyendo requisitos funcionales y no funcionales como rendimiento, seguridad y usabilidad.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes es una técnica de prueba estática?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de valores límite.",
        "opcion_c": "Prueba de tabla de decisión.",
        "opcion_d": "Revisión formal.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La revisión formal (inspección) es una técnica de prueba estática. Las demás son técnicas dinámicas de caja negra.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe la técnica de prueba de casos de uso?",
        "opcion_a": "Identificar grupos de entradas que se espera que se procesen de la misma manera.",
        "opcion_b": "Probar los valores en los límites de un rango de entrada válido.",
        "opcion_c": "Derivar casos de prueba basados en las historias de usuario.",
        "opcion_d": "Analizar el código fuente para identificar posibles defectos.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de casos de uso deriva casos de prueba a partir de las interacciones definidas entre el usuario (actor) y el sistema.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Qué tipo de prueba se realiza para verificar que los cambios en el sistema no han afectado negativamente a la funcionalidad existente?",
        "opcion_a": "Prueba de regresión.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de migración.",
        "opcion_d": "Prueba de aceptación.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba de regresión confirma que un cambio no ha afectado negativamente funcionalidad ya existente.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la gestión de la configuración?",
        "opcion_a": "Controlar las versiones del software, los datos de prueba y los entornos de prueba.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_c": "Planificar y controlar las actividades de prueba.",
        "opcion_d": "Evaluar los riesgos asociados con las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La gestión de la configuración controla y mantiene la integridad de las versiones de software, datos y entornos de prueba a lo largo del proyecto.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes métricas se utiliza para medir la cantidad de código que se ha ejercitado durante las pruebas?",
        "opcion_a": "Número de casos de prueba ejecutados.",
        "opcion_b": "Número de defectos encontrados.",
        "opcion_c": "Cobertura de código.",
        "opcion_d": "Número de líneas de código escritas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La cobertura de código mide qué porcentaje del código fuente ha sido ejercitado por las pruebas ejecutadas.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes herramientas NO se utiliza en las pruebas de software?",
        "opcion_a": "Herramienta de gestión de pruebas.",
        "opcion_b": "Herramienta de análisis estático.",
        "opcion_c": "Herramienta de diseño gráfico.",
        "opcion_d": "Herramienta de seguimiento de errores.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Una herramienta de diseño gráfico no está relacionada con el proceso de pruebas de software.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el concepto de \"mitigación de riesgos\"?",
        "opcion_a": "La probabilidad de que un defecto cause un fallo.",
        "opcion_b": "El impacto del defecto en el funcionamiento del sistema.",
        "opcion_c": "Tomar medidas para reducir la probabilidad o el impacto de un riesgo.",
        "opcion_d": "La dificultad de encontrar un defecto.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La mitigación de riesgos consiste en tomar acciones preventivas o correctivas para reducir la probabilidad de ocurrencia o el impacto de un riesgo.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes NO es una característica de un buen caso de prueba?",
        "opcion_a": "Preciso.",
        "opcion_b": "Repetible.",
        "opcion_c": "Ambiguo.",
        "opcion_d": "Trazable.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Un buen caso de prueba debe ser claro y sin ambigüedad; la ambigüedad es justamente lo opuesto a una buena característica.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de los siguientes es un ejemplo de prueba no funcional?",
        "opcion_a": "Prueba de seguridad.",
        "opcion_b": "Prueba de casos de uso.",
        "opcion_c": "Prueba de tabla de decisión.",
        "opcion_d": "Prueba de partición de equivalencia.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba de seguridad evalúa un atributo de calidad no funcional. Las demás opciones son técnicas de diseño de pruebas funcionales.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes afirmaciones sobre la prueba de unidad es CORRECTA?",
        "opcion_a": "La prueba de unidad se realiza después de la prueba de integración.",
        "opcion_b": "La prueba de unidad se centra en probar las unidades individuales de código.",
        "opcion_c": "La prueba de unidad solo se puede realizar por los testers.",
        "opcion_d": "La prueba de unidad no es necesaria si se ha realizado una prueba de integración exhaustiva.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de unidad (componentes) verifica de forma aislada las unidades individuales de código, antes de la integración.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe la técnica de prueba de tabla de decisión?",
        "opcion_a": "Identificar las condiciones y las acciones que se deben tomar en función de las combinaciones de condiciones.",
        "opcion_b": "Probar los valores en los límites de un rango de entrada.",
        "opcion_c": "Utilizar un grafo para representar los estados y las transiciones entre estados.",
        "opcion_d": "Analizar el código fuente para identificar posibles defectos.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La tabla de decisión modela combinaciones de condiciones (causas) y las acciones (efectos) resultantes.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes NO es una actividad típica de la planificación de las pruebas?",
        "opcion_a": "Definir los objetivos de las pruebas.",
        "opcion_b": "Estimar el esfuerzo de las pruebas.",
        "opcion_c": "Ejecutar los casos de prueba.",
        "opcion_d": "Identificar los riesgos de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Ejecutar los casos de prueba es una actividad de EJECUCIÓN, no de planificación.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito del informe de progreso de las pruebas?",
        "opcion_a": "Controlar el progreso de las pruebas en relación con el plan.",
        "opcion_b": "Informar a las partes interesadas sobre el estado actual de las pruebas.",
        "opcion_c": "Evaluar la calidad del software.",
        "opcion_d": "Automatizar la ejecución de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El informe de progreso comunica periódicamente a las partes interesadas el estado actual de las actividades de prueba.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un tipo de prueba de mantenimiento?",
        "opcion_a": "Prueba de regresión.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de migración.",
        "opcion_d": "Prueba de mantenimiento correctivo.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de integración es un nivel de prueba general, no un tipo específico de prueba de mantenimiento.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de aceptación?",
        "opcion_a": "Verificar que el sistema cumple con los requisitos del usuario.",
        "opcion_b": "Encontrar tantos defectos como sea posible.",
        "opcion_c": "Probar el rendimiento del sistema bajo carga.",
        "opcion_d": "Evaluar la usabilidad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba de aceptación busca establecer confianza en que el sistema cumple con las necesidades y requisitos del usuario/negocio.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre pruebas de caja blanca y pruebas de caja negra?",
        "opcion_a": "Las pruebas de caja blanca se realizan al principio del ciclo de vida del desarrollo, mientras que las pruebas de caja negra se realizan al final.",
        "opcion_b": "Las pruebas de caja blanca se basan en el código fuente, mientras que las pruebas de caja negra se basan en las especificaciones de los requisitos.",
        "opcion_c": "Las pruebas de caja blanca son más importantes que las pruebas de caja negra.",
        "opcion_d": "Las pruebas de caja blanca se realizan por el equipo de desarrollo, mientras que las pruebas de caja negra se realizan por el equipo de pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Las técnicas de caja blanca (estructurales) se basan en la estructura interna del código; las de caja negra se basan en las especificaciones, sin conocer la implementación interna.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un factor que influye en la selección de las herramientas de prueba?",
        "opcion_a": "El presupuesto del proyecto.",
        "opcion_b": "La complejidad del sistema.",
        "opcion_c": "Las habilidades del equipo de pruebas.",
        "opcion_d": "La ubicación geográfica del equipo de pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La ubicación geográfica del equipo no es un factor típico de selección de herramientas.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes es una técnica de diseño de pruebas de caja blanca?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Prueba de condición.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de condición es una técnica de caja blanca (basada en la estructura interna del código). Las demás son técnicas de caja negra.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un objetivo típico de las pruebas de rendimiento?",
        "opcion_a": "Medir el tiempo de respuesta del sistema.",
        "opcion_b": "Identificar los cuellos de botella en el sistema.",
        "opcion_c": "Verificar que el sistema cumple con los requisitos de seguridad.",
        "opcion_d": "Evaluar la escalabilidad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Verificar requisitos de seguridad es objetivo de la prueba de seguridad, no de la prueba de rendimiento.",
        "modelo_examen": "Simulacro 3"
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
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una tarea en la gestión de defectos?",
        "opcion_a": "Detectar defectos.",
        "opcion_b": "Corregir defectos.",
        "opcion_c": "Analizar la causa raíz de los defectos.",
        "opcion_d": "Prevenir defectos.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Detectar un defecto ocurre durante la ejecución de pruebas o revisiones (fuera del proceso de gestión de defectos). La gestión de defectos abarca lo que sucede después de detectado: registrar, clasificar, corregir, analizar causa raíz y prevenir recurrencias.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de un informe de incidente de prueba?",
        "opcion_a": "Controlar las versiones del software y los artefactos de prueba.",
        "opcion_b": "Documentar los detalles de un defecto encontrado durante las pruebas.",
        "opcion_c": "Planificar y controlar las actividades de prueba.",
        "opcion_d": "Evaluar los riesgos asociados con las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El informe de incidente de prueba documenta los detalles de un defecto/incidente encontrado durante las pruebas.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Qué técnica de prueba se centra en probar las combinaciones de entradas y salidas utilizando una tabla?",
        "opcion_a": "Partición de equivalencia.",
        "opcion_b": "Análisis de valores límite.",
        "opcion_c": "Prueba de tabla de decisión.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La tabla de decisión modela combinaciones de entradas (condiciones) y salidas (acciones).",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar si un sistema cumple con los estándares de accesibilidad?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Pruebas no funcionales.",
        "opcion_c": "Prueba de seguridad.",
        "opcion_d": "Prueba funcionales.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de accesibilidad se clasifica dentro de las pruebas no funcionales, junto con usabilidad, rendimiento y seguridad.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre un error y un fallo?",
        "opcion_a": "Un error es un problema reportado por el usuario, mientras que un fallo es un problema encontrado por el tester.",
        "opcion_b": "Un error es un problema menor, mientras que un fallo es un problema grave.",
        "opcion_c": "Un error es una acción humana que produce un resultado incorrecto, mientras que un fallo es una desviación del comportamiento esperado.",
        "opcion_d": "Un error es un problema en el software, mientras que un fallo es un problema en el hardware.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Un error (equivocación humana) puede introducir un defecto que, al ejecutarse, produce un fallo (desviación observable del comportamiento esperado).",
        "modelo_examen": "Simulacro 3"
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
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de componentes?",
        "opcion_a": "Probar las unidades individuales de código.",
        "opcion_b": "Probar la interacción entre diferentes módulos del sistema.",
        "opcion_c": "Probar un grupo de componentes relacionados que interactúan entre sí.",
        "opcion_d": "Probar la seguridad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Confirmado por resultados de exámenes previos: este banco de preguntas define la prueba de componentes como la prueba de un grupo de componentes relacionados que interactúan entre sí, distinguiéndola de la prueba de unidad aislada.",
        "modelo_examen": "Simulacro 3"
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
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un beneficio de las pruebas independientes?",
        "opcion_a": "Mayor objetividad en las pruebas.",
        "opcion_b": "Mayor probabilidad de encontrar defectos.",
        "opcion_c": "Reducción del coste de las pruebas.",
        "opcion_d": "Mayor confianza en la calidad del software.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La independencia no reduce el coste de las pruebas; de hecho puede añadir coordinación adicional. Sus beneficios reales son objetividad, mayor detección de defectos y confianza en la calidad.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de un informe de resumen de prueba?",
        "opcion_a": "Documentar los resultados de las pruebas.",
        "opcion_b": "Describir un defecto encontrado durante las pruebas.",
        "opcion_c": "Proporcionar una visión general de las actividades de prueba y los resultados.",
        "opcion_d": "Evaluar la calidad del software.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "El informe de resumen de prueba (test summary report) presenta una visión general de las actividades y los resultados de las pruebas al final de una fase o proyecto.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar la cantidad de usuarios o transacciones que un sistema puede manejar simultáneamente?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Prueba de carga.",
        "opcion_c": "Prueba de estrés.",
        "opcion_d": "Prueba de concurrencia.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Confirmado por resultados de exámenes previos: cuando la pregunta enfatiza el manejo SIMULTÁNEO de usuarios/transacciones, este banco de preguntas espera 'prueba de concurrencia' como respuesta, distinguiéndola de la prueba de carga.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un principio de la gestión de la configuración?",
        "opcion_a": "Identificación.",
        "opcion_b": "Control de cambios.",
        "opcion_c": "Ejecución de pruebas.",
        "opcion_d": "Auditoría.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La ejecución de pruebas no es un principio de la gestión de la configuración (identificación, control de cambios, informe de estado y auditoría).",
        "modelo_examen": "Simulacro 3"
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
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar el tiempo que tarda un sistema en realizar una tarea específica?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Prueba de tiempo de respuesta.",
        "opcion_c": "Prueba de carga.",
        "opcion_d": "Prueba de estrés.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Confirmado por resultados de exámenes previos: cuando la pregunta enfatiza el tiempo para una tarea específica, este banco de preguntas espera 'prueba de tiempo de respuesta' como respuesta, distinguiéndola de la prueba de rendimiento general.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes NO es una característica de un buen caso de prueba?",
        "opcion_a": "Preciso.",
        "opcion_b": "Repetible.",
        "opcion_c": "Complejo.",
        "opcion_d": "Trazable.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Un buen caso de prueba debe ser simple y conciso, no complejo.",
        "modelo_examen": "Simulacro 3"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de aceptación operativa?",
        "opcion_a": "Evaluar la facilidad con la que los usuarios pueden utilizar un sistema.",
        "opcion_b": "Probar el rendimiento del sistema bajo carga.",
        "opcion_c": "Verificar que el sistema cumple con los requisitos no funcionales.",
        "opcion_d": "Probar la seguridad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de aceptación operativa (OAT) verifica aspectos operativos como respaldo/recuperación, mantenimiento y otros requisitos no funcionales, realizada por administradores del sistema antes de su puesta en producción.",
        "modelo_examen": "Simulacro 3"
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
        "modelo_examen": "Simulacro 3"
    },
]


def main():
    with open(PREGUNTAS_PATH, "r", encoding="utf-8") as f:
        existing = json.load(f)

    print(f"Preguntas existentes antes de agregar: {len(existing)}")

    existing.extend(SIMULACRO_3)

    with open(PREGUNTAS_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"Se agregaron {len(SIMULACRO_3)} preguntas del Simulacro 3.")
    print(f"Total de preguntas ahora: {len(existing)}")


if __name__ == "__main__":
    main()
