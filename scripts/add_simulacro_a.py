# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")

import json
import os

PREGUNTAS_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "app", "preguntas.json")

SIMULACRO_A = [
    {
        "enunciado": "¿Cuál de los siguientes enunciados describe un objetivo de prueba válido?",
        "opcion_a": "Demostrar que no hay defectos no corregidos en el sistema sujeto a prueba.",
        "opcion_b": "Demostrar que no se producirán fallos tras la implementación del sistema en producción.",
        "opcion_c": "Reducir el nivel de riesgo del objeto de prueba y generar confianza en el nivel de calidad.",
        "opcion_d": "Comprobar que no existen combinaciones de entradas no probadas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las pruebas exhaustivas son imposibles, así que no se puede 'demostrar' ausencia de defectos ni de fallos futuros (a y b), ni probar todas las combinaciones (d). El objetivo válido es reducir el riesgo del objeto de prueba y dar confianza sobre el nivel de calidad.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones es un ejemplo de actividades de prueba que contribuyen al éxito?",
        "opcion_a": "La participación de probadores durante varias actividades del ciclo de vida de desarrollo del software (CVDS) ayudará a detectar defectos en los productos software.",
        "opcion_b": "Los probadores intentan no molestar a los desarrolladores mientras codifican, para que éstos escriban un código de mejor calidad.",
        "opcion_c": "Los probadores que colaboran con los usuarios finales ayudan a mejorar la calidad de los informes de defectos durante la integración de componentes y las pruebas de sistemas.",
        "opcion_d": "Los probadores certificados diseñan casos de prueba mucho mejores que los probadores no certificados.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La participación temprana de probadores en las actividades del CVDS (no solo en la ejecución) ayuda a detectar defectos en los propios productos de trabajo (requisitos, diseño, etc.), no solo en el código.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Usted ha sido asignado como probador a un equipo que está desarrollando un nuevo sistema de forma incremental. Ha notificado que no se han realizado cambios en los casos de prueba de regresión existentes durante varias iteraciones y que no se han identificado nuevos defectos de regresión. Su jefe está contento, pero usted no. ¿Qué principio de prueba explica su escepticismo?",
        "opcion_a": "Las pruebas se desgastan.",
        "opcion_b": "Falacia de la ausencia de errores.",
        "opcion_c": "Los defectos se agrupan.",
        "opcion_d": "Es imposible realizar pruebas exhaustivas.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Es el principio de la paradoja del pesticida ('las pruebas se desgastan'): repetir las mismas pruebas sin modificarlas hace que dejen de encontrar defectos nuevos, no porque el software esté libre de ellos.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Usted trabaja en un equipo que desarrolla una aplicación móvil para hacer pedidos de comida. En la iteración actual el equipo decidió implementar la funcionalidad de pago. ¿Cuál de las siguientes actividades forma parte del análisis de prueba?",
        "opcion_a": "Estimar que probar la integración con el servicio de pago llevará 8 días-persona.",
        "opcion_b": "Decidir que el equipo debe probar si es posible compartir correctamente el pago entre muchos usuarios.",
        "opcion_c": "Utilizar el análisis del valor frontera (AVF) para obtener los datos de prueba para los casos de prueba que comprueban el procesamiento correcto del pago para el importe mínimo permitido a pagar.",
        "opcion_d": "Analizar la discrepancia entre el resultado real y el resultado esperado tras ejecutar un caso de prueba que comprueba el proceso de pago con tarjeta de crédito e informar de un defecto.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El análisis de prueba identifica QUÉ probar (condiciones de prueba), como decidir que hay que probar el pago compartido entre usuarios. Estimar esfuerzo es planificación (a), usar AVF para generar datos es diseño de prueba (c), y analizar un fallo tras ejecutar es parte de la ejecución/informe de defectos (d).",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuáles de los siguientes factores (del I al V) tienen una influencia SIGNIFICATIVA en el proceso de prueba?\n\nI. El ciclo de vida de desarrollo de software (CVDS).\nII. El número de defectos detectados en proyectos anteriores.\nIII. Los riesgos de producto identificados.\nIV. Los nuevos requisitos normativos obligatorios.\nV. El número de probadores certificados en la organización.",
        "opcion_a": "I, II tienen una influencia significativa; III, IV, V no la tienen.",
        "opcion_b": "I, III, IV tienen una influencia significativa; II, V no la tienen.",
        "opcion_c": "II, IV, V tienen una influencia significativa; I, III no la tienen.",
        "opcion_d": "III, V tienen una influencia significativa; I, II, IV no la tienen.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El CVDS, los riesgos de producto y los requisitos normativos obligatorios son factores de contexto reconocidos que moldean el enfoque de prueba. La cantidad de defectos de proyectos pasados y la cantidad de probadores certificados no determinan el enfoque de prueba en sí.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuáles DOS de las siguientes tareas pertenecen PRINCIPALMENTE a un rol de prueba? Seleccionar DOS opciones.",
        "opcion_a": "Configurar entornos de prueba.",
        "opcion_b": "Mantener la lista de trabajo acumulado del producto (\"backlog\").",
        "opcion_c": "Diseñar soluciones para nuevos requisitos.",
        "opcion_d": "Crear el plan de prueba.",
        "opcion_e": "Informar sobre la cobertura alcanzada.",
        "respuesta_correcta": "A,E",
        "explicacion": "Configurar entornos de prueba e informar sobre la cobertura alcanzada son tareas propias del rol de probador. Mantener el backlog es del Product Owner, diseñar soluciones es del desarrollador, y crear el plan de prueba corresponde típicamente al rol de gestor de pruebas.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuáles de las siguientes competencias (I-V) son las MÁS importantes en un probador?\n\nI. Tener conocimiento del dominio.\nII. Crear una visión del producto.\nIII. Ser un buen jugador de equipo.\nIV. Planificar y organizar el trabajo del equipo.\nV. Pensamiento crítico.",
        "opcion_a": "II y IV son importantes; I, III y V no lo son.",
        "opcion_b": "I, III y V son importantes; II y IV no lo son.",
        "opcion_c": "I, II y V son importantes; III y IV no lo son.",
        "opcion_d": "III y IV son importantes; I, II y V no lo son.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Conocimiento del dominio, buen jugador de equipo y pensamiento crítico son competencias genéricas de un probador. Crear la visión del producto es del Product Owner, y planificar/organizar el trabajo del equipo es del Scrum Master o gestor.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cómo queda reflejado el enfoque de equipo completo en las interacciones entre probadores y representantes de negocio?",
        "opcion_a": "Los representantes de negocio deciden los enfoques de automatización de la prueba.",
        "opcion_b": "Los probadores ayudan a los representantes de negocio a definir la estrategia de prueba.",
        "opcion_c": "Los representantes de negocio no forman parte del enfoque de equipo completo.",
        "opcion_d": "Los probadores ayudan a los representantes de negocio a crear pruebas de aceptación adecuadas.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "El enfoque de equipo completo se refleja en que los probadores colaboran con los representantes de negocio para redactar buenas pruebas de aceptación, aprovechando cada rol según su fortaleza.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Tenga en cuenta la siguiente regla: \"para cada actividad del ciclo de vida de desarrollo de software (CVDS) existe una actividad de prueba correspondiente\". ¿En qué modelos de CVDS se cumple esta regla?",
        "opcion_a": "Sólo en modelos CVDS secuenciales.",
        "opcion_b": "Sólo en modelos CVDS iterativos.",
        "opcion_c": "Sólo en modelos CVDS iterativos e incrementales.",
        "opcion_d": "En modelos CVDS secuenciales, incrementales e iterativos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Esta regla es un principio general del temario que se cumple sin importar el modelo de CVDS utilizado: secuencial, incremental o iterativo.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuál de los siguientes enunciados describe MEJOR el enfoque de desarrollo guiado por prueba de aceptación (DGPA)?",
        "opcion_a": "En DGPA, los criterios de aceptación suelen crearse basándose en el formato dado/cuando/entonces (\"given/when/then\").",
        "opcion_b": "En DGPA, los casos de prueba se crean principalmente en la prueba de componente y están orientados al código.",
        "opcion_c": "En DGPA, se crean pruebas basadas en criterios de aceptación para impulsar el desarrollo del software correspondiente.",
        "opcion_d": "En DGPA, las pruebas se basan en el comportamiento deseado del software, lo que facilita su comprensión por parte de los miembros del equipo.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La definición central de ATDD/DGPA es que las pruebas se crean a partir de los criterios de aceptación y esas pruebas son las que impulsan (guían) el desarrollo del software correspondiente.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un ejemplo del enfoque de desplazamiento a la izquierda?",
        "opcion_a": "Revisar los requisitos de usuario antes de que sean aceptados formalmente por los implicados.",
        "opcion_b": "Escribir una prueba de componente antes de escribir el código correspondiente.",
        "opcion_c": "Ejecutar una prueba de eficiencia de desempeño de un componente durante la prueba de componente.",
        "opcion_d": "Redactar un guion de prueba antes de establecer el proceso de gestión de la configuración.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Redactar un guion de prueba antes de tener un proceso de gestión de la configuración es simplemente un problema de orden de actividades, no un ejemplo de mover una prueba más temprano en el ciclo de vida (shift-left).",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuál de los siguientes argumentos utilizaría para convencer a su jefe de que organice retrospectivas al final de cada ciclo de entrega?",
        "opcion_a": "Las retrospectivas son muy populares hoy en día y los clientes agradecerían que las añadiéramos a nuestros procesos.",
        "opcion_b": "Organizar retrospectivas ahorrará dinero a la organización porque los representantes de los usuarios finales no proporcionan retroalimentación inmediata sobre el producto.",
        "opcion_c": "Los puntos débiles del proceso identificados durante la retrospectiva pueden analizarse y servir como lista de tareas para el programa de mejora continua del proceso de la organización.",
        "opcion_d": "Los puntos débiles del proceso identificados durante la retrospectiva pueden analizarse y servir como lista de tareas para el programa de mejora continua del proceso de la organización.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las retrospectivas identifican puntos débiles del proceso que alimentan el programa de mejora continua de la organización. (Nota: en el formulario original, las opciones c y d tienen el mismo texto — es así en la fuente original, no un error de captura.)",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Qué tipos de fallos (1-4) se ajustan MEJOR a qué niveles de prueba (A-D)?\n\n1. Fallos en el comportamiento del sistema cuando se desvía de las necesidades de negocio del usuario.\n2. Fallos en la comunicación entre componentes.\n3. Fallos en la lógica de un módulo.\n4. Fallos en la implementación incorrecta de las reglas de negocio.\n\nA. Prueba de componente.\nB. Prueba de integración de componentes.\nC. Prueba de sistema.\nD. Prueba de aceptación.",
        "opcion_a": "1D, 2B, 3A, 4C.",
        "opcion_b": "1D, 2B, 3C, 4A.",
        "opcion_c": "1B, 2A, 3D, 4C.",
        "opcion_d": "1C, 2B, 3A, 4D.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Desviarse de las necesidades de negocio se detecta en aceptación (1D); fallos de comunicación entre componentes en integración de componentes (2B); fallos de lógica de un módulo en prueba de componente (3A); reglas de negocio mal implementadas a nivel de todo el sistema, en prueba de sistema (4C).",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Usted está probando una historia de usuario con tres criterios de aceptación: CA1, CA2 y CA3. CA1 está cubierto por el caso de prueba CP1, CA2 por CP2, y CA3 por CP3. La historia de ejecución de prueba tuvo tres ejecuciones de prueba en tres versiones consecutivas del software, como se indica a continuación:\n\n| | Ejecución 01 | Ejecución 02 | Ejecución 03 |\n|---|---|---|---|\n| CP1 | (1) Falló | (4) Pasó | (7) Pasó |\n| CP2 | (2) Pasó | (5) Falló | (8) Pasó |\n| CP3 | (3) Falló | (6) Falló | (9) Pasó |\n\nLas pruebas se repiten una vez que se informa de que se han corregido todos los defectos encontrados en la ejecución anterior.\n\n¿Cuáles de las pruebas anteriores se ejecutan como prueba de regresión?",
        "opcion_a": "Sólo 4, 7, 8, 9.",
        "opcion_b": "Sólo 5, 7.",
        "opcion_c": "Sólo 4, 6, 8, 9.",
        "opcion_d": "Sólo 5, 6.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "(4), (6), (8) y (9) son pruebas de CONFIRMACIÓN (re-prueban un caso que había fallado antes, para verificar la corrección). (5) y (7) son pruebas de REGRESIÓN (re-prueban un caso que ya había pasado, para confirmar que las correcciones hechas para otros defectos no rompieron nada).",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuál de las opciones siguientes NO es una ventaja de la prueba estática?",
        "opcion_a": "Tener una gestión de defectos menos costosa debido a la facilidad de detectar defectos más tarde en el CVDS.",
        "opcion_b": "Corregir los defectos encontrados durante la prueba estática es generalmente mucho menos costoso que corregir los defectos encontrados durante la prueba dinámica.",
        "opcion_c": "Encontrar defectos de código que no se habrían encontrado con pruebas dinámicas.",
        "opcion_d": "Detectar carencias e incoherencias en los requisitos.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La ventaja real de la prueba estática es detectar defectos MÁS TEMPRANO en el CVDS, no más tarde — la opción a es contradictoria y por eso NO es una ventaja real.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones es una ventaja de la retroalimentación temprana y frecuente?",
        "opcion_a": "Mejora el proceso de prueba para futuros proyectos.",
        "opcion_b": "Obliga a los clientes a priorizar sus requisitos en función de los riesgos acordados.",
        "opcion_c": "Es la única forma de medir la calidad de los cambios.",
        "opcion_d": "Ayuda a evitar malentendidos sobre los requisitos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La retroalimentación temprana y frecuente ayuda a detectar y corregir malentendidos sobre los requisitos antes de que se propaguen más en el desarrollo.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Las revisiones que se utilizan en su organización presentan las siguientes características:\n- Cuentan con el rol de escriba.\n- El objetivo principal es evaluar la calidad.\n- La reunión está liderada por el autor del producto de trabajo.\n- Hay una preparación individual.\n- Se elabora un informe de revisión.\n\n¿Cuál de los siguientes tipos de revisión es MÁS probable que se utilice?",
        "opcion_a": "Revisión informal.",
        "opcion_b": "Revisión guiada.",
        "opcion_c": "Revisión técnica.",
        "opcion_d": "Inspección.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El dato clave es que la reunión está liderada por el AUTOR del producto de trabajo — eso es específico de la revisión guiada (walkthrough); en revisión técnica e inspección la lidera un moderador entrenado, no el autor.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuál de estos enunciados NO es un factor que contribuye al éxito de las revisiones?",
        "opcion_a": "Los participantes deben dedicar un tiempo adecuado a la revisión.",
        "opcion_b": "Dividir los productos de trabajo grandes en partes pequeñas para que el esfuerzo requerido sea menos intenso.",
        "opcion_c": "Los participantes deben evitar comportamientos que puedan indicar aburrimiento, exasperación u hostilidad hacia otros participantes.",
        "opcion_d": "Los fallos encontrados deben reconocerse, valorarse y tratarse objetivamente.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Las revisiones (prueba estática) encuentran DEFECTOS, no fallos (los fallos ocurren durante la ejecución/prueba dinámica) — el enunciado usa el término incorrecto, por lo que no describe correctamente un factor de éxito de las revisiones.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones es una característica de las técnicas de prueba basadas en la experiencia?",
        "opcion_a": "Los casos de prueba se crean a partir de información de diseño detallada.",
        "opcion_b": "Los elementos probados en la sección de código de la interfaz se utilizan para medir la cobertura.",
        "opcion_c": "Las técnicas se basan en gran medida en los conocimientos del probador sobre el software y el dominio del negocio.",
        "opcion_d": "Los casos de prueba se utilizan para identificar desviaciones con respecto a los requisitos.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Es la definición de las técnicas basadas en la experiencia: se apoyan en el conocimiento y experiencia del probador sobre el software y el dominio de negocio, a diferencia de las técnicas de caja negra o caja blanca.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Estás probando un formulario de búsqueda de pisos simplificado que sólo tiene dos criterios de búsqueda:\n- Piso (con tres opciones posibles: planta baja; primer piso; segundo piso o superior).\n- Tipo de jardín (con tres opciones posibles: sin jardín; jardín pequeño; jardín grande).\nSólo los pisos de la planta baja pueden tener jardín. El formulario tiene incorporado un mecanismo de validación que no le permitirá utilizar los criterios de búsqueda que infrinjan esta regla.\n\nCada prueba tiene dos valores de entrada: planta y tipo de jardín. Desea aplicar la partición de equivalencia (PE) para cubrir cada planta y cada tipo de jardín en sus pruebas.\n\n¿Cuál es el número mínimo de casos de prueba para alcanzar el 100% de cobertura PE?",
        "opcion_a": "3",
        "opcion_b": "4",
        "opcion_c": "5",
        "opcion_d": "6",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Jardín pequeño y jardín grande solo son válidos junto con planta baja (2 casos), y primer piso/segundo piso+ solo son válidos con 'sin jardín' (2 casos más) — 4 casos mínimos cubren las 3 particiones de piso y las 3 de jardín sin usar combinaciones inválidas.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Está probando un sistema que calcula la nota final del curso para un alumno determinado. La nota final se asigna en función del resultado final, de acuerdo con las siguientes reglas:\n- 0 - 50 puntos: suspenso\n- 51 - 60 puntos: regular\n- 61 - 70 puntos: satisfactorio\n- 71 - 80 puntos: bien\n- 81 - 90 puntos: muy bien\n- 91 - 100 puntos: excelente\n\nUsted ha preparado el siguiente conjunto de casos de prueba:\n\n| Caso | Resultado Final | Nota Final |\n|---|---|---|\n| CP1 | 91 | excelente |\n| CP2 | 50 | suspenso |\n| CP3 | 81 | muy bien |\n| CP4 | 60 | regular |\n| CP5 | 70 | satisfactorio |\n| CP6 | 80 | bien |\n\n¿Cuál es la cobertura del análisis del valor frontera (AVF) de 2 valores para el resultado final que se consigue con los casos de prueba existentes?",
        "opcion_a": "50%",
        "opcion_b": "60%",
        "opcion_c": "33,3%",
        "opcion_d": "100%",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Con 6 particiones hay 12 valores frontera relevantes (2 por partición, incluyendo los extremos 0 y 100). Los casos existentes (91,50,81,60,70,80) cubren 6 de esos 12 valores → 50%.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Su tienda favorita de alquiler diario de bicicletas acaba de introducir un nuevo sistema de gestión de las relaciones con los clientes y le ha pedido a usted, uno de sus socios más fieles, que lo pruebe.\n\nLas prestaciones implementadas son las siguientes:\n- Cualquiera puede alquilar una bicicleta, pero los socios obtienen un descuento del 20%.\n- Sin embargo, si no se cumple el plazo de devolución, el descuento deja de estar disponible.\n- Después de 15 alquileres, los socios reciben un regalo: una camiseta.\n\nLa tabla de decisión que describe las prestaciones implementadas tiene columnas de reglas R1 a R8, combinando las condiciones 'Ser miembro', 'Incumplimiento de plazo' y 'Alquiler número 15', con las acciones '20% de descuento' y 'Camiseta de regalo'.\n\nBasándose ÚNICAMENTE en la descripción de las prestaciones del sistema de gestión de relaciones con los clientes, ¿cuál de las reglas anteriores describe una situación imposible?",
        "opcion_a": "R4",
        "opcion_b": "R2",
        "opcion_c": "R6",
        "opcion_d": "R8",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La regla de negocio establece que si no se cumple el plazo de devolución, el descuento deja de estar disponible (sin excepción, aunque se sea socio). R2 corresponde a un socio que incumplió el plazo pero la tabla igual le otorga el 20% de descuento — eso contradice directamente la regla, por lo que es la situación imposible.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Usted prueba un sistema cuyo ciclo de vida está modelado por el diagrama de transición de estado que se muestra a continuación. El sistema comienza en el estado INICIO y termina su operación en el estado APAGADO.\n\nTransiciones:\n- INICIO --PROBAR--> MODO DEPURACIÓN\n- INICIO --EJECUTAR--> EN OPERACIÓN\n- MODO DEPURACIÓN --COMPLETADO--> APAGADO\n- EN OPERACIÓN --ERROR--> MODO DEPURACIÓN\n- EN OPERACIÓN --PAUSAR--> EN ESPERA\n- EN ESPERA --REANUDAR--> EN OPERACIÓN\n- EN ESPERA --COMPLETADO--> APAGADO\n\n¿Cuál es el número MÍNIMO de casos de prueba para lograr una cobertura de transiciones válidas?",
        "opcion_a": "4",
        "opcion_b": "2",
        "opcion_c": "7",
        "opcion_d": "3",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Cada caso de prueba es un camino INICIO→APAGADO. Se necesita 1 camino vía PROBAR, 1 camino EJECUTAR→ERROR (no se puede combinar con el de PROBAR porque INICIO solo permite una salida por camino), y 1 camino EJECUTAR→PAUSAR→REANUDAR→PAUSAR→COMPLETADO para cubrir la salida por ESPERA. Mínimo: 3 caminos cubren las 7 transiciones.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Su juego de prueba logró una cobertura de sentencia del 100%. ¿Cuál es la consecuencia de este hecho?",
        "opcion_a": "Cada instrucción del código que contiene un defecto se ha ejecutado al menos una vez.",
        "opcion_b": "Cualquier juego de prueba que contenga más casos de prueba que su juego de prueba también alcanzará una cobertura de sentencia del 100%.",
        "opcion_c": "Cada camino del código se ha ejecutado al menos una vez.",
        "opcion_d": "Cada combinación de valores de entrada se ha probado al menos una vez.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "100% de cobertura de sentencia significa que cada instrucción del código se ejecutó al menos una vez, incluida cualquier instrucción defectuosa. No implica cobertura de caminos (c) ni de combinaciones de entrada (d), y añadir más casos de prueba no garantiza mantener la cobertura (b).",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es correcta con respecto a la prueba de caja blanca?",
        "opcion_a": "Durante la prueba de caja blanca se tiene en cuenta toda la implementación del software.",
        "opcion_b": "Las métricas de cobertura de caja blanca pueden ayudar a identificar pruebas adicionales para aumentar la cobertura de código.",
        "opcion_c": "Las técnicas de prueba de caja blanca pueden utilizarse en pruebas estáticas.",
        "opcion_d": "La prueba de caja blanca puede ayudar a identificar lagunas en la implementación de requisitos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La caja blanca se basa en la estructura interna del código, no en los requisitos — no puede identificar funcionalidad FALTANTE respecto a los requisitos (eso es tarea de las técnicas basadas en especificación/caja negra).",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe MEJOR el concepto de predicción de errores?",
        "opcion_a": "La predicción de errores implica utilizar sus conocimientos y experiencia sobre los defectos encontrados en el pasado y los errores típicos cometidos por los desarrolladores.",
        "opcion_b": "La predicción de errores implica utilizar su experiencia personal en el desarrollo y los errores que cometió como desarrollador.",
        "opcion_c": "La predicción de errores requiere que imagine que es el usuario del objeto de prueba y que adivine los errores que podría cometer al interactuar con él.",
        "opcion_d": "La predicción de errores requiere replicar rápidamente la tarea de desarrollo para identificar el tipo de equivocación que podría cometer un desarrollador.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Es la definición estándar de predicción de errores (error guessing): usar conocimiento y experiencia sobre defectos pasados y errores típicos de desarrolladores para anticipar dónde pueden estar los próximos defectos.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "En su proyecto se ha producido un retraso en la entrega de una nueva aplicación y la ejecución de la prueba ha comenzado con retraso, pero usted tiene un conocimiento muy detallado del dominio y buenas competencias analíticas. La lista completa de requisitos aún no se ha compartido con el equipo, pero la dirección pide que se presenten algunos resultados de la prueba. ¿Qué técnica de prueba encaja MEJOR en esta situación?",
        "opcion_a": "Prueba basada en lista de comprobación.",
        "opcion_b": "Predicción de errores.",
        "opcion_c": "Prueba exploratoria.",
        "opcion_d": "Prueba de rama.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Sin requisitos completos y con necesidad de resultados rápidos, la prueba exploratoria encaja mejor: no depende de especificaciones detalladas de antemano y aprovecha el conocimiento de dominio y las competencias analíticas del probador.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe MEJOR la forma en que se pueden documentar los criterios de aceptación?",
        "opcion_a": "Realizar retrospectivas para determinar las necesidades reales de los implicados con respecto a una historia de usuario dada.",
        "opcion_b": "Utilizar el formato dado/cuando/entonces (\"given/when/then\") para describir un ejemplo de condición de prueba relacionada con una historia de usuario determinada.",
        "opcion_c": "Utilizar la comunicación verbal para reducir el riesgo de que los demás malinterpreten los criterios de aceptación.",
        "opcion_d": "Documentar los riesgos relacionados con una historia de usuario dada en un plan de prueba para facilitar la prueba basada en el riesgo de una historia de usuario dada.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El formato dado/cuando/entonces es la forma estándar de documentar criterios de aceptación de una historia de usuario de manera clara y verificable.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Tenga en cuenta la siguiente historia de usuario:\nComo Editor,\nquiero revisar el contenido antes de que se publique,\npara asegurarme de que la gramática es correcta.\n\ny sus criterios de aceptación:\n- El usuario puede iniciar sesión en el sistema de gestión de contenido existente con el rol de \"Editor\".\n- El editor puede ver las páginas de contenido existentes.\n- El editor puede editar el contenido de la página.\n- El editor puede añadir comentarios.\n- El editor puede guardar cambios.\n- El editor puede reasignar al rol de \"propietario del contenido\" para realizar actualizaciones.\n\n¿Cuál de las siguientes opciones es el MEJOR ejemplo de prueba desarrollo guiado por prueba de aceptación (DGPA) para esta historia de usuario?",
        "opcion_a": "Probar si el editor puede guardar el documento después de borrar el contenido de la página.",
        "opcion_b": "Probar si el propietario del contenido puede iniciar sesión y realizar actualizaciones del contenido.",
        "opcion_c": "Probar si el editor puede programar el contenido editado para su publicación.",
        "opcion_d": "Probar si el editor puede reasignar a otro editor para realizar actualizaciones.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El criterio de aceptación habla de reasignar al rol de 'propietario del contenido' para que realice actualizaciones — la prueba DGPA correcta verifica exactamente eso: que el propietario del contenido pueda iniciar sesión y actualizar, no que se reasigne a 'otro editor'.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿De qué forma los probadores aportan valor a la planificación de la iteración y entrega?",
        "opcion_a": "Los probadores determinan la prioridad de las historias de usuario que hay que desarrollar.",
        "opcion_b": "Los probadores se concentran sólo en los aspectos funcionales del sistema que se va a probar.",
        "opcion_c": "Los probadores participan en la identificación detallada del riesgo y en la evaluación del riesgo de las historias de usuario.",
        "opcion_d": "Los probadores garantizan la entrega de software de alta calidad mediante un diseño de prueba temprano durante la planificación de la entrega.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Los probadores aportan valor participando en la identificación y evaluación detallada del riesgo de las historias de usuario, no decidiendo prioridades (eso es del Product Owner) ni 'garantizando' calidad de forma absoluta.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Cuáles DOS de las siguientes opciones son criterios de salida para probar un sistema?",
        "opcion_a": "La preparación del entorno de prueba.",
        "opcion_b": "La capacidad de iniciar sesión en el objeto de prueba por parte del probador.",
        "opcion_c": "Haber alcanzado la densidad de defectos estimada.",
        "opcion_d": "Los requisitos se traducen al formato dado/cuando/entonces (\"given/when/then\").",
        "opcion_e": "Las pruebas de regresión se encuentran automatizadas.",
        "respuesta_correcta": "C,E",
        "explicacion": "Haber alcanzado la densidad de defectos estimada y tener las pruebas de regresión automatizadas son criterios de salida. La preparación del entorno y la capacidad de iniciar sesión son criterios de ENTRADA, no de salida, y traducir requisitos a given/when/then es una actividad previa a la prueba.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Su equipo utiliza la técnica de estimación de tres puntos para estimar el esfuerzo de prueba de una nueva prestación de alto riesgo. Se realizaron las siguientes estimaciones:\n\n• estimación más optimista: 2 horas-persona.\n• estimación más probable: 11 horas-persona.\n• estimación más pesimista: 14 horas-persona.\n\n¿Cuál es la estimación final?",
        "opcion_a": "9 horas-persona.",
        "opcion_b": "14 horas-persona.",
        "opcion_c": "11 horas-persona.",
        "opcion_d": "10 horas-persona.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Estimación de tres puntos: (optimista + 4×probable + pesimista) / 6 = (2 + 4×11 + 14) / 6 = 60 / 6 = 10 horas-persona.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Usted está probando una aplicación móvil que permite a los usuarios encontrar un restaurante cercano en función del tipo de comida que desean comer. Tenga en cuenta la siguiente lista de casos de prueba, prioridades (es decir, un número menor significa una mayor prioridad) y dependencias:\n\n| Caso de Prueba | Condición de prueba cubierta | Prioridad | Dependencia lógica |\n|---|---|---|---|\n| CP 001 | Seleccionar tipo de alimento | 3 | ninguna |\n| CP 002 | Seleccionar restaurante | 2 | CP 001 |\n| CP 003 | Obtener dirección | 1 | CP 002 |\n| CP 004 | Llamar restaurante | 2 | CP 002 |\n| CP 005 | Hacer reserva | 3 | CP 002 |\n\n¿Cuál de los siguientes casos de prueba debe ejecutarse en tercer lugar?",
        "opcion_a": "TC 003",
        "opcion_b": "TC 005",
        "opcion_c": "TC 002",
        "opcion_d": "TC 001",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "CP001 no tiene dependencia y va primero; CP002 depende de CP001 y va segundo; CP003, CP004 y CP005 dependen todos de CP002 y se ordenan por prioridad (menor número = mayor prioridad): CP003 (prioridad 1) va tercero.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Tenga en cuenta las siguientes categorías de prueba (1-4) y los cuadrantes de prueba ágil (A-D):\n1. Prueba de usabilidad\n2. Prueba de componente\n3. Prueba funcional\n4. Prueba de fiabilidad\n\nA. Cuadrante de prueba ágil Q1: de cara a la tecnología, apoya al equipo de desarrollo.\nB. Cuadrante de prueba ágil Q2: de cara al negocio, apoya al equipo de desarrollo.\nC. Cuadrante de prueba ágil Q3: de cara al negocio, critica el producto.\nD. Cuadrante de prueba ágil Q4: de cara a la tecnología, critica el producto.\n\n¿Cómo se corresponden las categorías de prueba con los cuadrantes de prueba ágil?",
        "opcion_a": "1C, 2A, 3B, 4D",
        "opcion_b": "1D, 2A, 3C, 4B",
        "opcion_c": "1C, 2B, 3D, 4A",
        "opcion_d": "1D, 2B, 3C, 4A",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Usabilidad es de cara al negocio y critica el producto → Q3 (1C). Componente es de cara a la tecnología y apoya al equipo → Q1 (2A). Funcional es de cara al negocio y apoya al equipo → Q2 (3B). Fiabilidad es de cara a la tecnología y critica el producto → Q4 (4D).",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Durante un análisis del riesgo se identificó y evaluó el siguiente riesgo:\n• Riesgo: El tiempo de respuesta es muy prolongado para generar un informe.\n• Probabilidad del riesgo: media; impacto del riesgo: alto.\n• Respuesta al riesgo:\n   o un equipo de prueba independiente realiza pruebas de rendimiento durante la prueba de sistema.\n   o una muestra seleccionada de usuarios finales realiza pruebas de aceptación alfa y beta antes de la entrega.\n\n¿Qué medida se propone tomar en respuesta a este riesgo analizado?",
        "opcion_a": "Aceptación del riesgo.",
        "opcion_b": "Plan de contingencia.",
        "opcion_c": "Mitigación del riesgo.",
        "opcion_d": "Transferencia del riesgo.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Tomar medidas de prueba activas (rendimiento, alfa/beta) para reducir y verificar el riesgo antes de que ocurra es mitigación del riesgo, no simple aceptación, plan de contingencia ni transferencia a terceros.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Qué herramienta puede utilizar un equipo ágil para mostrar la cantidad de trabajo que se ha completado y la cantidad de trabajo total restante para una iteración determinada?",
        "opcion_a": "Criterios de aceptación.",
        "opcion_b": "Informe de defecto.",
        "opcion_c": "Informe de compleción de la prueba.",
        "opcion_d": "Gráfico de quemado.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "El gráfico de quemado (burndown chart) es la herramienta estándar en ágil para visualizar trabajo completado vs. restante en una iteración.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Usted necesita actualizar uno de los guiones de prueba automatizados para que se ajuste a un nuevo requisito. ¿Qué proceso indica que debe crear una nueva versión del guion de prueba en el repositorio de pruebas?",
        "opcion_a": "Gestión de la trazabilidad.",
        "opcion_b": "Prueba de mantenimiento.",
        "opcion_c": "Gestión de la configuración.",
        "opcion_d": "Ingeniería de requisitos.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La gestión de la configuración es el proceso que rige el versionado de los productos de trabajo de prueba, incluidos los guiones de prueba automatizados.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "Usted ha recibido el siguiente informe de defecto de los desarrolladores en el que se indica que la anomalía descrita en este informe de prueba no es reproducible.\n\nLa aplicación se bloquea\n03-Mayo-2022 – Juan Piedra Seca - Rechazado\nLa aplicación se bloquea tras introducir \"Entrada de prueba: $ä\" en el campo Nombre de la pantalla de creación de un nuevo usuario. Intenté cerrar la sesión, iniciar sesión con la cuenta test_admin01, mismo problema. Probado con otras cuentas de administrador de prueba, mismo problema. No se ha recibido ningún mensaje de error; el registro (véase adjunto) contiene una notificación de error crítico. Basándose en el caso de prueba TC-1305, la aplicación debería aceptar la entrada proporcionada y crear el usuario. Por favor, corrija con alta prioridad, esta prestación está relacionada con REQ-0012, que es un nuevo requisito de negocio crítico.\n\n¿Qué información crítica falta en este informe de prueba que hubiera sido útil para los desarrolladores?",
        "opcion_a": "Resultado esperado y resultado real.",
        "opcion_b": "Referencias y estado de los defectos.",
        "opcion_c": "Entorno de prueba y elemento de prueba.",
        "opcion_d": "Prioridad y severidad.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "El informe no especifica en qué entorno de prueba (navegador, SO, versión de la build) ni sobre qué elemento/versión exacta del sistema se probó — precisamente la información que suele faltar cuando un defecto se reporta como 'no reproducible'.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿A qué actividad de prueba da soporte una herramienta de preparación de datos de prueba?",
        "opcion_a": "Monitorización y control de prueba.",
        "opcion_b": "Análisis y diseño de la prueba.",
        "opcion_c": "Implementación y ejecución de la prueba.",
        "opcion_d": "Compleción de la prueba.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las herramientas de preparación de datos de prueba dan soporte a la implementación y ejecución de la prueba, según el temario oficial.",
        "modelo_examen": "Simulacro A"
    },
    {
        "enunciado": "¿Qué elemento identifica correctamente un riesgo potencial de realizar la automatización de la prueba?",
        "opcion_a": "Puede introducir regresiones desconocidas en producción.",
        "opcion_b": "Es posible que no se dediquen suficientes esfuerzos al mantenimiento del producto de prueba.",
        "opcion_c": "Puede que no se confíe lo suficiente en las herramientas de prueba y los productos de prueba asociados.",
        "opcion_d": "Puede reducir el tiempo asignado a la prueba manual.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Un riesgo real y documentado de la automatización es subestimar el esfuerzo necesario para mantener los guiones y productos de prueba automatizados a lo largo del tiempo.",
        "modelo_examen": "Simulacro A"
    },
]


def main():
    with open(PREGUNTAS_PATH, "r", encoding="utf-8") as f:
        existing = json.load(f)

    print(f"Preguntas existentes antes de agregar: {len(existing)}")

    existing.extend(SIMULACRO_A)

    with open(PREGUNTAS_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"Se agregaron {len(SIMULACRO_A)} preguntas del Simulacro A.")
    print(f"Total de preguntas ahora: {len(existing)}")


if __name__ == "__main__":
    main()
