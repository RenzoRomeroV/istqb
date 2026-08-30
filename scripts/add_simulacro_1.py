# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")

import json
import os

PREGUNTAS_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "app", "preguntas.json")

SIMULACRO_1 = [
    {
        "enunciado": "¿Cuál de las siguientes NO es una tarea principal del proceso de prueba?",
        "opcion_a": "Planificación de las pruebas.",
        "opcion_b": "Diseño de las pruebas.",
        "opcion_c": "Implementación del software.",
        "opcion_d": "Evaluación de los criterios de salida y elaboración de informes.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Implementar el software es una actividad de DESARROLLO, no una actividad del proceso de prueba. Las actividades del proceso de prueba son: planificación, monitorización y control, análisis, diseño, implementación de la prueba, ejecución, y compleción (evaluación de criterios de salida e informes).",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de los siguientes es un principio fundamental de las pruebas?",
        "opcion_a": "Las pruebas exhaustivas son posibles si se utilizan las herramientas adecuadas.",
        "opcion_b": "Las pruebas demuestran la ausencia de defectos.",
        "opcion_c": "La detección temprana de defectos reduce el coste de corregirlos.",
        "opcion_d": "Las pruebas deben centrarse únicamente en encontrar defectos.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Es uno de los 7 principios de las pruebas: cuanto antes se detecta un defecto en el ciclo de vida, más barato resulta corregirlo. Las pruebas exhaustivas son imposibles (contradice a) y las pruebas muestran presencia, no ausencia, de defectos (contradice b).",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Qué nivel de pruebas se centra en verificar la interacción entre diferentes módulos o componentes del sistema?",
        "opcion_a": "Prueba de unidad.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de sistema.",
        "opcion_d": "Prueba de aceptación.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de integración verifica específicamente las interfaces y la interacción entre componentes o sistemas ya probados individualmente.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes técnicas es una técnica de prueba estática?",
        "opcion_a": "Prueba de caja negra.",
        "opcion_b": "Prueba de rendimiento.",
        "opcion_c": "Análisis de valores límite.",
        "opcion_d": "Revisión de código.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La revisión de código es una técnica de prueba estática (no requiere ejecutar el software). Las demás opciones son técnicas o tipos de prueba dinámica.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe la técnica de partición de equivalencia?",
        "opcion_a": "Identificar grupos de entradas que se espera que se procesen de la misma manera.",
        "opcion_b": "Probar los valores en los límites de un rango de entrada.",
        "opcion_c": "Utilizar una tabla para definir las combinaciones de entradas y salidas esperadas.",
        "opcion_d": "Analizar el código fuente para identificar posibles defectos.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Es la definición exacta de partición de equivalencia: dividir el dominio de entrada en particiones (clases) donde se espera un comportamiento equivalente del sistema.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un tipo de prueba de mantenimiento?",
        "opcion_a": "Prueba de regresión.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de migración.",
        "opcion_d": "Prueba de mantenimiento correctivo.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de integración es un NIVEL de prueba, no un tipo de prueba de mantenimiento. Los tipos de mantenimiento incluyen correctivo, adaptativo, perfectivo y de emergencia, además de pruebas de regresión y de migración de datos.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la gestión de la configuración en las pruebas?",
        "opcion_a": "Controlar las versiones del software y los artefactos de prueba.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_c": "Planificar y controlar las actividades de prueba.",
        "opcion_d": "Evaluar los riesgos asociados con las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La gestión de la configuración asegura la identificación, control de versiones y trazabilidad de los productos de trabajo, incluyendo el software y los artefactos de prueba.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes métricas NO se utiliza comúnmente para medir el progreso de las pruebas?",
        "opcion_a": "Número de casos de prueba ejecutados.",
        "opcion_b": "Número de defectos encontrados.",
        "opcion_c": "Porcentaje de cobertura de requisitos.",
        "opcion_d": "Número de líneas de código escritas.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "El número de líneas de código escritas es una métrica de DESARROLLO, no de progreso de pruebas.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes herramientas se utiliza para la gestión de defectos?",
        "opcion_a": "Herramienta de gestión de pruebas.",
        "opcion_b": "Herramienta de análisis estático.",
        "opcion_c": "Herramienta de prueba de rendimiento.",
        "opcion_d": "Herramienta de seguimiento de errores.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Una herramienta de seguimiento de errores (bug/defect tracking) es la herramienta específica para gestionar defectos: registrarlos, darles seguimiento y cerrarlos.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el concepto de \"riesgo\" en el contexto de las pruebas?",
        "opcion_a": "La probabilidad de que un defecto cause un fallo.",
        "opcion_b": "La gravedad del impacto de un fallo.",
        "opcion_c": "La combinación de la probabilidad de un fallo y la gravedad de su impacto.",
        "opcion_d": "La dificultad de encontrar un defecto.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "El riesgo se define como la combinación de la probabilidad de que ocurra un evento (fallo) y el impacto (daño) que causaría. Las opciones a y b solo cubren una de las dos dimensiones.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes NO es una característica típica de las pruebas ágiles?",
        "opcion_a": "Las pruebas se realizan en iteraciones cortas (sprints).",
        "opcion_b": "Los testers trabajan en estrecha colaboración con los desarrolladores.",
        "opcion_c": "Se hace un énfasis en la documentación exhaustiva de las pruebas.",
        "opcion_d": "Se fomenta la automatización de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Ágil favorece documentación ligera y justo a tiempo, no documentación exhaustiva — eso es más característico de enfoques secuenciales tradicionales.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de los siguientes es un ejemplo de prueba de caja negra?",
        "opcion_a": "Prueba de caminos básicos.",
        "opcion_b": "Prueba de condición.",
        "opcion_c": "Prueba de partición de equivalencia.",
        "opcion_d": "Prueba de bucle.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La partición de equivalencia es una técnica de caja negra (basada en especificación). Las demás opciones son técnicas de caja blanca (basadas en estructura del código).",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes afirmaciones sobre la prueba de integración es CORRECTA?",
        "opcion_a": "La prueba de integración se realiza después de la prueba de sistema.",
        "opcion_b": "La prueba de integración se centra en probar las interfaces entre los módulos.",
        "opcion_c": "La prueba de integración solo se puede realizar utilizando el enfoque de arriba hacia abajo.",
        "opcion_d": "La prueba de integración no es necesaria si se ha realizado una prueba de unidad exhaustiva.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de integración se enfoca específicamente en las interfaces y la interacción entre módulos ya probados por separado. Existen varios enfoques (arriba-abajo, abajo-arriba, big-bang), no solo uno.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe la técnica de prueba de tabla de decisión?",
        "opcion_a": "Identificar las condiciones y las acciones que se deben tomar en función de las combinaciones de condiciones.",
        "opcion_b": "Probar los valores en los límites de un rango de entrada.",
        "opcion_c": "Utilizar un grafo para representar los estados y las transiciones entre estados.",
        "opcion_d": "Analizar el código fuente para identificar posibles defectos.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Es la definición exacta de tabla de decisión: modela combinaciones lógicas de condiciones y las acciones/resultados correspondientes.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes NO es una actividad típica de la planificación de las pruebas?",
        "opcion_a": "Definir los objetivos de las pruebas.",
        "opcion_b": "Estimar el esfuerzo de las pruebas.",
        "opcion_c": "Ejecutar los casos de prueba.",
        "opcion_d": "Identificar los riesgos de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Ejecutar los casos de prueba es parte de la actividad de EJECUCIÓN de la prueba, no de la planificación.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito del seguimiento de las pruebas?",
        "opcion_a": "Controlar el progreso de las pruebas en relación con el plan.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_c": "Evaluar la calidad del software.",
        "opcion_d": "Automatizar la ejecución de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "El seguimiento (monitorización) de pruebas compara el progreso real contra lo planificado, para poder tomar acciones de control si es necesario.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un tipo de informe de prueba?",
        "opcion_a": "Informe de incidente de prueba.",
        "opcion_b": "Informe de resumen de prueba.",
        "opcion_c": "Informe de progreso de prueba.",
        "opcion_d": "Informe de requisitos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Un \"informe de requisitos\" es un documento de análisis de requisitos, no un tipo de informe de PRUEBA.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de aceptación?",
        "opcion_a": "Verificar que el sistema cumple con los requisitos del usuario.",
        "opcion_b": "Encontrar tantos defectos como sea posible.",
        "opcion_c": "Probar el rendimiento del sistema bajo carga.",
        "opcion_d": "Evaluar la usabilidad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba de aceptación valida que el sistema satisface las necesidades y expectativas del usuario/negocio, generalmente como condición para la aceptación final.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre verificación y validación?",
        "opcion_a": "La verificación se centra en el producto, mientras que la validación se centra en el proceso.",
        "opcion_b": "La verificación se realiza por el equipo de desarrollo, mientras que la validación se realiza por el equipo de pruebas.",
        "opcion_c": "La verificación asegura que el producto se construye correctamente, mientras que la validación asegura que se construye el producto correcto.",
        "opcion_d": "La verificación es una técnica de prueba estática, mientras que la validación es una técnica de prueba dinámica.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Es la definición clásica de ISTQB: verificación = \"¿se está construyendo el producto correctamente?\" (cumple especificaciones); validación = \"¿se está construyendo el producto correcto?\" (cumple necesidades del usuario).",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un factor que influye en la selección de las herramientas de prueba?",
        "opcion_a": "El presupuesto del proyecto.",
        "opcion_b": "La complejidad del sistema.",
        "opcion_c": "Las habilidades del equipo de pruebas.",
        "opcion_d": "La ubicación geográfica del equipo de pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La ubicación geográfica del equipo no es un criterio estándar para elegir una herramienta de prueba; los factores relevantes son presupuesto, complejidad del sistema, habilidades del equipo, compatibilidad, etc.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes es una técnica de diseño de pruebas de caja blanca?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Prueba de casos de uso.",
        "opcion_d": "Prueba de condición.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de condición es una técnica de caja blanca (basada en la estructura del código). Las demás son técnicas de caja negra.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un objetivo típico de las pruebas de rendimiento?",
        "opcion_a": "Medir el tiempo de respuesta del sistema.",
        "opcion_b": "Identificar los cuellos de botella en el sistema.",
        "opcion_c": "Verificar la funcionalidad del sistema.",
        "opcion_d": "Evaluar la escalabilidad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Verificar la funcionalidad es el objetivo de la prueba FUNCIONAL, no de la prueba de rendimiento (que es un tipo de prueba no funcional).",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de regresión?",
        "opcion_a": "Probar nuevas funcionalidades del sistema.",
        "opcion_b": "Verificar que los cambios en el sistema no han introducido nuevos defectos.",
        "opcion_c": "Probar el rendimiento del sistema bajo carga.",
        "opcion_d": "Evaluar la usabilidad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de regresión confirma que las partes ya probadas del software siguen funcionando correctamente después de un cambio.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un tipo de prueba de mantenimiento?",
        "opcion_a": "Prueba de regresión.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de migración.",
        "opcion_d": "Prueba de mantenimiento correctivo.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Igual que en la pregunta 6: la prueba de integración es un nivel de prueba, no un tipo de prueba de mantenimiento.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la gestión de riesgos en las pruebas?",
        "opcion_a": "Identificar y evaluar los riesgos que pueden afectar a las pruebas.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_c": "Planificar y controlar las actividades de prueba.",
        "opcion_d": "Evaluar la calidad del software.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La gestión de riesgos en pruebas consiste en identificar, analizar y evaluar los riesgos de producto y de proyecto que pueden afectar el esfuerzo de prueba.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una técnica de prueba de caja negra?",
        "opcion_a": "Partición de equivalencia.",
        "opcion_b": "Análisis de valores límite.",
        "opcion_c": "Prueba de condición.",
        "opcion_d": "Prueba de tabla de decisión.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de condición es una técnica de caja BLANCA (estructural), no de caja negra.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar la facilidad con la que los usuarios pueden utilizar un sistema?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Prueba de usabilidad.",
        "opcion_c": "Prueba de seguridad.",
        "opcion_d": "Prueba de compatibilidad.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de usabilidad evalúa específicamente la facilidad de uso, aprendizaje y satisfacción del usuario al interactuar con el sistema.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre un error y un fallo?",
        "opcion_a": "Un error es un defecto en el código, mientras que un fallo es el resultado de un error.",
        "opcion_b": "Un error es un problema reportado por el usuario, mientras que un fallo es un problema encontrado por el tester.",
        "opcion_c": "Un error es un problema menor, mientras que un fallo es un problema grave.",
        "opcion_d": "Un error es un problema en el software, mientras que un fallo es un problema en el hardware.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Un fallo (falla en la ejecución) es la manifestación observable causada por un defecto/error subyacente en el producto. Las demás opciones no reflejan la relación causa-efecto real entre ambos conceptos.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una responsabilidad típica del tester?",
        "opcion_a": "Diseñar casos de prueba.",
        "opcion_b": "Ejecutar casos de prueba.",
        "opcion_c": "Reportar defectos.",
        "opcion_d": "Corregir defectos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Corregir defectos es responsabilidad del DESARROLLADOR, no del tester. El tester diseña, ejecuta pruebas y reporta defectos, pero no los corrige.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de integración?",
        "opcion_a": "Probar las unidades individuales de código.",
        "opcion_b": "Probar la interacción entre diferentes módulos del sistema.",
        "opcion_c": "Probar el sistema completo en su entorno de producción.",
        "opcion_d": "Probar la seguridad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El propósito central de la prueba de integración es verificar la interacción y las interfaces entre módulos o componentes.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Qué técnica de prueba se centra en probar las transiciones entre diferentes estados de un sistema?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Prueba de transición de estados.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de transición de estados modela el sistema como estados y las transiciones válidas/inválidas entre ellos, y diseña casos de prueba para cubrirlas.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un beneficio de la automatización de pruebas?",
        "opcion_a": "Mayor eficiencia de las pruebas.",
        "opcion_b": "Mayor cobertura de pruebas.",
        "opcion_c": "Eliminación de la necesidad de pruebas manuales.",
        "opcion_d": "Mayor repetibilidad de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Es un mito común: la automatización NO elimina la necesidad de pruebas manuales (exploratorias, de usabilidad, etc. siguen requiriendo un tester humano). Por eso no es un beneficio real.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de un plan de pruebas?",
        "opcion_a": "Documentar los resultados de las pruebas.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_c": "Guiar las actividades de prueba.",
        "opcion_d": "Evaluar la calidad del software.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "El plan de pruebas documenta el enfoque, alcance, recursos y cronograma, y sirve para guiar las actividades de prueba a lo largo del proyecto.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar si un sistema puede manejar grandes volúmenes de datos o usuarios?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Prueba de carga.",
        "opcion_c": "Prueba de estrés.",
        "opcion_d": "Prueba de volumen.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de volumen evalúa específicamente el manejo de grandes volúmenes de datos por parte del sistema (a diferencia de la prueba de carga, centrada en el número de usuarios/transacciones concurrentes, y la de estrés, centrada en llevar al sistema más allá de su capacidad máxima).",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un atributo de calidad del software según la norma ISO 25010?",
        "opcion_a": "Funcionalidad.",
        "opcion_b": "Fiabilidad.",
        "opcion_c": "Usabilidad.",
        "opcion_d": "Coste.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "El coste es una restricción de proyecto/negocio, no una característica de calidad del producto según ISO 25010 (que incluye funcionalidad, fiabilidad, usabilidad, eficiencia de desempeño, compatibilidad, seguridad, mantenibilidad y portabilidad).",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de seguridad?",
        "opcion_a": "Evaluar la facilidad con la que los usuarios pueden utilizar un sistema.",
        "opcion_b": "Probar el rendimiento del sistema bajo carga.",
        "opcion_c": "Verificar que el sistema está protegido contra accesos no autorizados.",
        "opcion_d": "Probar la compatibilidad del sistema con diferentes plataformas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de seguridad verifica la protección de datos y funcionalidad ante accesos, usos o modificaciones no autorizadas.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Qué tipo de revisión implica una reunión formal con un equipo de revisores?",
        "opcion_a": "Revisión informal.",
        "opcion_b": "Revisión técnica.",
        "opcion_c": "Inspección.",
        "opcion_d": "Recorrido.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La inspección es el tipo de revisión más formal: tiene un proceso definido, un moderador entrenado, checklists, métricas y una reunión formal de revisión.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un tipo de defecto?",
        "opcion_a": "Error de codificación.",
        "opcion_b": "Error de diseño.",
        "opcion_c": "Error de documentación.",
        "opcion_d": "Error de ejecución.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Un \"error de ejecución\" describe una falla que ocurre en tiempo de ejecución (un fallo/failure), no un tipo de defecto estático en un producto de trabajo como el código, el diseño o la documentación.",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de compatibilidad?",
        "opcion_a": "Evaluar la facilidad con la que los usuarios pueden utilizar un sistema.",
        "opcion_b": "Probar el rendimiento del sistema bajo carga.",
        "opcion_c": "Verificar que el sistema funciona correctamente en diferentes entornos.",
        "opcion_d": "Probar la seguridad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de compatibilidad verifica que el sistema funcione correctamente en distintos entornos (navegadores, sistemas operativos, dispositivos, versiones de otro software, etc.).",
        "modelo_examen": "Simulacro 1"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una técnica de gestión de pruebas?",
        "opcion_a": "Planificación de pruebas.",
        "opcion_b": "Seguimiento de pruebas.",
        "opcion_c": "Prueba de integración.",
        "opcion_d": "Gestión de la configuración.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de integración es un NIVEL/TIPO de prueba, no una técnica de gestión de pruebas. Planificación, seguimiento y gestión de la configuración sí son actividades de gestión de pruebas.",
        "modelo_examen": "Simulacro 1"
    },
]


def main():
    with open(PREGUNTAS_PATH, "r", encoding="utf-8") as f:
        existing = json.load(f)

    print(f"Preguntas existentes antes de agregar: {len(existing)}")

    existing.extend(SIMULACRO_1)

    with open(PREGUNTAS_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"Se agregaron {len(SIMULACRO_1)} preguntas del Simulacro 1.")
    print(f"Total de preguntas ahora: {len(existing)}")


if __name__ == "__main__":
    main()
