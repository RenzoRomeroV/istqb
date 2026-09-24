# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")

import json
import os

PREGUNTAS_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "app", "preguntas.json")

SIMULACRO_9 = [
    {
        "enunciado": "¿Cuál de las siguientes NO es una de las siete pruebas de principios de software?",
        "opcion_a": "Las pruebas exhaustivas son imposibles.",
        "opcion_b": "Las pruebas deben comenzar lo antes posible en el ciclo de vida del software.",
        "opcion_c": "Las pruebas demuestran que el software está libre de defectos.",
        "opcion_d": "Las pruebas dependen del contexto.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las pruebas muestran la PRESENCIA de defectos, nunca pueden demostrar que el software esté completamente libre de ellos.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de los siguientes NO es un objetivo principal de las pruebas?",
        "opcion_a": "Encontrar defectos.",
        "opcion_b": "Prevenir defectos.",
        "opcion_c": "Ganar más dinero.",
        "opcion_d": "Mejorar la confianza en el software.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "\"Ganar más dinero\" no es un objetivo de las pruebas reconocido por ISTQB; los objetivos incluyen encontrar y prevenir defectos, y aumentar la confianza en el software.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Qué nivel de pruebas se centra en probar la interacción entre diferentes sistemas?",
        "opcion_a": "Prueba de unidad.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de sistema.",
        "opcion_d": "Prueba de Integración de Sistema",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de integración de sistemas evalúa específicamente la interacción entre distintos SISTEMAS, a diferencia de la prueba de integración genérica (entre componentes/módulos de un mismo sistema).",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes es una técnica de prueba estática?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de valores límite.",
        "opcion_c": "Prueba de tabla de decisión.",
        "opcion_d": "Revisión técnica.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La revisión técnica es una técnica de prueba estática. Las demás son técnicas dinámicas de caja negra.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe la técnica de prueba de casos de uso?",
        "opcion_a": "Identificar grupos de entradas que se espera que se procesen de la misma manera.",
        "opcion_b": "Probar los valores en los límites de un rango de entrada válido.",
        "opcion_c": "Utilizar una tabla para definir las combinaciones de entradas y salidas esperadas.",
        "opcion_d": "Derivar casos de prueba basados en las interacciones típicas de los usuarios con el sistema.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de casos de uso deriva casos de prueba a partir de las interacciones típicas entre el usuario (actor) y el sistema.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Qué tipo de prueba se realiza después de corregir un defecto para verificar que se ha solucionado?",
        "opcion_a": "Prueba de confirmación.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de sistema.",
        "opcion_d": "Prueba de aceptación.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba de confirmación (re-testing) verifica que un defecto previamente corregido efectivamente se solucionó.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la gestión de la configuración?",
        "opcion_a": "Controlar las versiones del software, los datos de prueba y los entornos de prueba.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_c": "Planificar y controlar las actividades de prueba.",
        "opcion_d": "Evaluar los riesgos asociados con las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La gestión de la configuración controla las versiones del software, los datos de prueba y los entornos de prueba a lo largo del proyecto.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes métricas se utiliza para medir la cantidad de código que se ha ejercitado durante las pruebas?",
        "opcion_a": "Número de casos de prueba ejecutados.",
        "opcion_b": "Número de defectos encontrados.",
        "opcion_c": "Cobertura de código.",
        "opcion_d": "Número de líneas de código escritas",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La cobertura de código mide qué porcentaje del código fuente ha sido ejercitado por las pruebas ejecutadas.",
        "modelo_examen": "Simulacro 9"
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
        "modelo_examen": "Simulacro 9"
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
        "modelo_examen": "Simulacro 9"
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
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de los siguientes es un ejemplo de prueba no funcional?",
        "opcion_a": "Prueba de seguridad.",
        "opcion_b": "Prueba de casos de uso.",
        "opcion_c": "Prueba de tabla de decisión.",
        "opcion_d": "Prueba de partición de equivalencia",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba de seguridad evalúa un atributo de calidad no funcional. Las demás son técnicas de diseño de pruebas funcionales.",
        "modelo_examen": "Simulacro 9"
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
        "modelo_examen": "Simulacro 9"
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
        "modelo_examen": "Simulacro 9"
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
        "modelo_examen": "Simulacro 9"
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
        "modelo_examen": "Simulacro 9"
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
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de aceptación?",
        "opcion_a": "Verificar que el sistema cumple con los requisitos del usuario.",
        "opcion_b": "Encontrar tantos defectos como sea posible.",
        "opcion_c": "Probar el rendimiento del sistema bajo carga.",
        "opcion_d": "Evaluar la usabilidad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba de aceptación establece confianza en que el sistema cumple con las necesidades y requisitos del usuario/negocio.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre pruebas de caja blanca y pruebas de caja negra?",
        "opcion_a": "Las pruebas de caja blanca se realizan al principio del ciclo de vida del desarrollo, mientras que las pruebas de caja negra se realizan al final.",
        "opcion_b": "Las pruebas de caja blanca se basan en el código fuente, mientras que las pruebas de caja negra se basan en las especificaciones de los requisitos.",
        "opcion_c": "Las pruebas de caja blanca son más importantes que las pruebas de caja negra.",
        "opcion_d": "Las pruebas de caja blanca se realizan por el equipo de desarrollo, mientras que las pruebas de caja negra se realizan por el equipo de pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Las técnicas de caja blanca (estructurales) se basan en la estructura interna del código; las de caja negra se basan en las especificaciones.",
        "modelo_examen": "Simulacro 9"
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
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes es una técnica de diseño de pruebas de caja blanca?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Prueba de caminos.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de caminos es una técnica de caja blanca (estructural). Las demás son técnicas de caja negra.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un objetivo típico de las pruebas de usabilidad?",
        "opcion_a": "Evaluar la facilidad de aprendizaje del sistema.",
        "opcion_b": "Medir el tiempo de respuesta del sistema.",
        "opcion_c": "Evaluar la eficiencia del sistema.",
        "opcion_d": "Evaluar la satisfacción del usuario.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Medir el tiempo de respuesta es objetivo de la prueba de rendimiento, no de usabilidad.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de migración?",
        "opcion_a": "Probar nuevas funcionalidades del sistema.",
        "opcion_b": "Verificar que los datos se transfieren correctamente a un nuevo entorno.",
        "opcion_c": "Probar el rendimiento del sistema bajo carga.",
        "opcion_d": "Evaluar la usabilidad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de migración verifica que los datos se transfieren correctamente a un nuevo entorno o formato.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una actividad típica de la planificación de las pruebas?",
        "opcion_a": "Definir los objetivos de las pruebas.",
        "opcion_b": "Estimar el esfuerzo de las pruebas.",
        "opcion_c": "Ejecutar los casos de prueba.",
        "opcion_d": "Identificar los riesgos de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Ejecutar los casos de prueba es una actividad de EJECUCIÓN, no de planificación.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la gestión de la configuración en las pruebas?",
        "opcion_a": "Controlar las versiones del software y los artefactos de prueba.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_c": "Planificar y controlar las actividades de prueba.",
        "opcion_d": "Evaluar los riesgos asociados con las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La gestión de la configuración controla las versiones del software y los artefactos de prueba a lo largo del proyecto.",
        "modelo_examen": "Simulacro 9"
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
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar si un sistema cumple con los estándares y regulaciones?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Prueba de cumplimiento.",
        "opcion_c": "Prueba de seguridad.",
        "opcion_d": "Prueba de compatibilidad.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de cumplimiento evalúa si el sistema cumple con estándares y regulaciones aplicables.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre un defecto y un fallo?",
        "opcion_a": "Un defecto es un problema reportado por el usuario, mientras que un fallo es un problema encontrado por el tester.",
        "opcion_b": "Un defecto es un problema menor, mientras que un fallo es un problema grave.",
        "opcion_c": "Un defecto es una imperfección en el software, mientras que un fallo es una desviación del comportamiento esperado.",
        "opcion_d": "Un defecto es un problema en el software, mientras que un fallo es un problema en el hardware.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Un defecto es una imperfección en el producto de trabajo; un fallo es la desviación observable del comportamiento esperado cuando ese defecto se ejecuta.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una responsabilidad típica del líder de pruebas?",
        "opcion_a": "Planificar las actividades de prueba.",
        "opcion_b": "Asignar tareas al equipo de pruebas.",
        "opcion_c": "Corregir defectos.",
        "opcion_d": "Monitorear el progreso de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Corregir defectos es responsabilidad del equipo de desarrollo, no del líder de pruebas.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de aceptación del usuario?",
        "opcion_a": "Probar las unidades individuales de código.",
        "opcion_b": "Probar la interacción entre diferentes módulos del sistema.",
        "opcion_c": "Verificar que el sistema cumple con las necesidades del usuario en su entorno real.",
        "opcion_d": "Probar la seguridad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de aceptación del usuario (UAT) verifica que el sistema cumple con las necesidades del usuario en un entorno real.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Qué técnica de prueba se centra en probar las respuestas del sistema a entradas inválidas o inesperadas?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Pruebas negativas.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las pruebas negativas evalúan cómo responde el sistema ante entradas inválidas o inesperadas.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un desafío común en la automatización de pruebas?",
        "opcion_a": "La selección de las herramientas adecuadas.",
        "opcion_b": "La creación y mantenimiento de los scripts de prueba.",
        "opcion_c": "La identificación de los casos de prueba adecuados para automatizar.",
        "opcion_d": "La eliminación completa de las pruebas manuales.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La automatización no elimina completamente la necesidad de pruebas manuales; eso no es un desafío real sino un mito.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de un informe de incidente de prueba?",
        "opcion_a": "Documentar los resultados de las pruebas.",
        "opcion_b": "Describir un defecto encontrado durante las pruebas.",
        "opcion_c": "Guiar las actividades de prueba.",
        "opcion_d": "Evaluar la calidad del software.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El informe de incidente de prueba documenta los detalles de un defecto encontrado durante las pruebas.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar el comportamiento del sistema cuando se somete a una carga extrema?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Prueba de carga.",
        "opcion_c": "Prueba de estrés.",
        "opcion_d": "Prueba de volumen.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de estrés evalúa el comportamiento del sistema al someterlo a una carga extrema, más allá de su capacidad máxima.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un tipo de revisión?",
        "opcion_a": "Revisión informal.",
        "opcion_b": "Revisión técnica.",
        "opcion_c": "Prueba de regresión.",
        "opcion_d": "Inspección.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de regresión es un tipo de prueba dinámica, no un tipo de revisión (técnica estática).",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de recuperación?",
        "opcion_a": "Evaluar la facilidad con la que los usuarios pueden utilizar un sistema.",
        "opcion_b": "Probar el rendimiento del sistema bajo carga.",
        "opcion_c": "Verificar que el sistema puede recuperarse después de un fallo.",
        "opcion_d": "Probar la compatibilidad del sistema con diferentes plataformas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de recuperación verifica la capacidad del sistema para recuperarse tras un fallo.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar el impacto de los cambios en una parte del sistema en otras partes del sistema?",
        "opcion_a": "Prueba de regresión.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de sistema.",
        "opcion_d": "Prueba de aceptación.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba de regresión evalúa el impacto de un cambio en una parte del sistema sobre otras partes ya probadas.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una métrica de prueba común?",
        "opcion_a": "Número de casos de prueba ejecutados.",
        "opcion_b": "Número de defectos encontrados.",
        "opcion_c": "Porcentaje de cobertura de código.",
        "opcion_d": "Número de líneas de código escritas.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Las líneas de código escritas son una métrica de desarrollo, no de progreso o cobertura de pruebas.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de instalación?",
        "opcion_a": "Evaluar la facilidad con la que los usuarios pueden utilizar un sistema.",
        "opcion_b": "Probar el rendimiento del sistema bajo carga.",
        "opcion_c": "Verificar que el sistema se puede instalar y configurar correctamente.",
        "opcion_d": "Probar la seguridad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de instalación verifica que el sistema se puede instalar y configurar correctamente en el entorno de destino.",
        "modelo_examen": "Simulacro 9"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un desafío común en las pruebas de software?",
        "opcion_a": "La falta de tiempo.",
        "opcion_b": "La falta de recursos.",
        "opcion_c": "La falta de comunicación.",
        "opcion_d": "La falta de herramientas de prueba.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La falta de herramientas de prueba no se considera uno de los desafíos fundamentales/universales de las pruebas, a diferencia de la falta de tiempo, recursos y comunicación.",
        "modelo_examen": "Simulacro 9"
    },
]


def main():
    with open(PREGUNTAS_PATH, "r", encoding="utf-8") as f:
        existing = json.load(f)

    print(f"Preguntas existentes antes de agregar: {len(existing)}")

    existing.extend(SIMULACRO_9)

    with open(PREGUNTAS_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"Se agregaron {len(SIMULACRO_9)} preguntas del Simulacro 9.")
    print(f"Total de preguntas ahora: {len(existing)}")


if __name__ == "__main__":
    main()
