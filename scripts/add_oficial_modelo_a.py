# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")

import json
import os

PREGUNTAS_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "app", "preguntas.json")

# Examen de muestra OFICIAL de ISTQB (SSTQB/HASTQB), Modelo A, Version 1.0,
# para el programa de estudio Foundation Level v4.0. Respuestas y justificaciones
# tomadas literalmente de la guia de respuestas oficial (no generadas por IA).
OFICIAL_MODELO_A = [
    {
        "enunciado": "¿Cuál de los siguientes enunciados describe un objetivo de prueba válido?",
        "opcion_a": "Demostrar que no hay defectos no corregidos en el sistema sujeto a prueba.",
        "opcion_b": "Demostrar que no se producirán fallos tras la implementación del sistema en producción.",
        "opcion_c": "Reducir el nivel de riesgo del objeto de prueba y generar confianza en el nivel de calidad.",
        "opcion_d": "Comprobar que no existen combinaciones de entradas no probadas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las pruebas encuentran defectos y fallos, lo que reduce el nivel de riesgo y, al mismo tiempo, da más confianza respecto al nivel de calidad del objeto de prueba. Las demás opciones son imposibles (principios 1 y 2 de las pruebas).",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones es un ejemplo de actividades de prueba que contribuyen al éxito?",
        "opcion_a": "La participación de probadores durante varias actividades del ciclo de vida de desarrollo del software (CVDS) ayudará a detectar defectos en los productos software.",
        "opcion_b": "Los probadores intentan no molestar a los desarrolladores mientras codifican, para que éstos escriban un código de mejor calidad.",
        "opcion_c": "Los probadores que colaboran con los usuarios finales ayudan a mejorar la calidad de los informes de defectos durante la integración de componentes y las pruebas de sistemas.",
        "opcion_d": "Los probadores certificados diseñan casos de prueba mucho mejores que los probadores no certificados.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Es importante que los probadores participen desde el principio del CVDS. Esta participación permitirá mejorar la comprensión de las decisiones de diseño y detectar los defectos en una fase temprana.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Usted ha sido asignado como probador a un equipo que está desarrollando un nuevo sistema de forma incremental. Ha notificado que no se han realizado cambios en los casos de prueba de regresión existentes durante varias iteraciones y que no se han identificado nuevos defectos de regresión. Su jefe está contento, pero usted no. ¿Qué principio de prueba explica su escepticismo?",
        "opcion_a": "Las pruebas se desgastan.",
        "opcion_b": "Falacia de la ausencia de errores.",
        "opcion_c": "Los defectos se agrupan.",
        "opcion_d": "Es imposible realizar pruebas exhaustivas.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Este principio significa que si se repiten las mismas pruebas una y otra vez, con el tiempo estas pruebas dejan de detectar nuevos defectos. Esta es probablemente la razón por la que todas las pruebas han pasado también en esta entrega.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Usted trabaja en un equipo que desarrolla una aplicación móvil para hacer pedidos de comida. En la iteración actual el equipo decidió implementar la funcionalidad de pago. ¿Cuál de las siguientes actividades forma parte del análisis de prueba?",
        "opcion_a": "Estimar que probar la integración con el servicio de pago llevará 8 días-persona.",
        "opcion_b": "Decidir que el equipo debe probar si es posible compartir correctamente el pago entre muchos usuarios.",
        "opcion_c": "Utilizar el análisis del valor frontera (AVF) para obtener los datos de prueba para los casos de prueba que comprueban el procesamiento correcto del pago para el importe mínimo permitido a pagar.",
        "opcion_d": "Analizar la discrepancia entre el resultado real y el resultado esperado tras ejecutar un caso de prueba que comprueba el proceso de pago con tarjeta de crédito e informar de un defecto.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Se trata de un ejemplo de definición de condiciones de prueba que forma parte del análisis de prueba. Estimar el esfuerzo es planificación; usar AVF para obtener datos es diseño; informar defectos es ejecución.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuáles de los siguientes factores (del I al V) tienen una influencia SIGNIFICATIVA en el proceso de prueba? I. El ciclo de vida de desarrollo de software (CVDS). II. El número de defectos detectados en proyectos anteriores. III. Los riesgos de producto identificados. IV. Los nuevos requisitos normativos obligatorios. V. El número de probadores certificados en la organización.",
        "opcion_a": "I, II tienen una influencia significativa; III, IV, V no la tienen.",
        "opcion_b": "I, III, IV tienen una influencia significativa; II, V no la tienen.",
        "opcion_c": "II, IV, V tienen una influencia significativa; I, III no la tienen.",
        "opcion_d": "III, V tienen una influencia significativa; I, II, IV no la tienen.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El CVDS, los riesgos de producto identificados y los requisitos normativos tienen influencia significativa en el proceso de prueba. El número de defectos en proyectos anteriores y el número de probadores certificados no la tienen de forma significativa.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuáles DOS de las siguientes tareas pertenecen PRINCIPALMENTE a un rol de prueba?",
        "opcion_a": "Configurar entornos de prueba.",
        "opcion_b": "Mantener la lista de trabajo acumulado del producto (\"backlog\").",
        "opcion_c": "Diseñar soluciones para nuevos requisitos.",
        "opcion_d": "Crear el plan de prueba.",
        "opcion_e": "Informar sobre la cobertura alcanzada",
        "respuesta_correcta": "A,E",
        "explicacion": "Configurar entornos de prueba e informar sobre la cobertura alcanzada son tareas de los probadores. El backlog lo mantiene el propietario de producto, diseñar soluciones es del equipo de desarrollo, y crear el plan de prueba es un rol directivo.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuáles de las siguientes competencias (I-V) son las MÁS importantes en un probador? I. Tener conocimiento del dominio. II. Crear una visión del producto. III. Ser un buen jugador de equipo. IV. Planificar y organizar el trabajo del equipo. V. Pensamiento crítico.",
        "opcion_a": "II y IV son importantes; I, III y V no lo son.",
        "opcion_b": "I, III y V son importantes; II y IV no lo son.",
        "opcion_c": "I, II y V son importantes; III y IV no lo son.",
        "opcion_d": "III y IV son importantes; I, II y V no lo son.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Tener conocimiento del dominio, ser buen jugador de equipo y tener pensamiento crítico son competencias importantes de un probador. Crear visión de producto y planificar el trabajo del equipo son tareas de otros roles.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cómo queda reflejado el enfoque de equipo completo en las interacciones entre probadores y representantes de negocio?",
        "opcion_a": "Los representantes de negocio deciden los enfoques de automatización de la prueba.",
        "opcion_b": "Los probadores ayudan a los representantes de negocio a definir la estrategia de prueba.",
        "opcion_c": "Los representantes de negocio no forman parte del enfoque de equipo completo.",
        "opcion_d": "Los probadores ayudan a los representantes de negocio a crear pruebas de aceptación adecuadas.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Los probadores colaborarán estrechamente con los representantes de negocio para asegurar que se alcanzan los niveles de calidad deseados, apoyándolos en crear pruebas de aceptación adecuadas.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Tenga en cuenta la siguiente regla: \"para cada actividad del ciclo de vida de desarrollo de software (CVDS) existe una actividad de prueba correspondiente\". ¿En qué modelos de CVDS se cumple esta regla?",
        "opcion_a": "Sólo en modelos CVDS secuenciales.",
        "opcion_b": "Sólo en modelos CVDS iterativos.",
        "opcion_c": "Sólo en modelos CVDS iterativos e incrementales.",
        "opcion_d": "En modelos CVDS secuenciales, incrementales e iterativos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Esta regla es válida para todos los modelos de CVDS.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de los siguientes enunciados describe MEJOR el enfoque de desarrollo guiado por prueba de aceptación (DGPA)?",
        "opcion_a": "En DGPA, los criterios de aceptación suelen crearse basándose en el formato dado/cuando/entonces (\"given/when/then\").",
        "opcion_b": "En DGPA, los casos de prueba se crean principalmente en la prueba de componente y están orientados al código.",
        "opcion_c": "En DGPA, se crean pruebas basadas en criterios de aceptación para impulsar el desarrollo del software correspondiente.",
        "opcion_d": "En DGPA, las pruebas se basan en el comportamiento deseado del software, lo que facilita su comprensión por parte de los miembros del equipo.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "En el desarrollo guiado por pruebas de aceptación (DGPA) las pruebas se escriben a partir de criterios de aceptación como parte del proceso de diseño, para impulsar el desarrollo. El formato dado/cuando/entonces se usa más en DGC; b) describe DGP; d) describe BDD.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un ejemplo del enfoque de desplazamiento a la izquierda?",
        "opcion_a": "Revisar los requisitos de usuario antes de que sean aceptados formalmente por los implicados.",
        "opcion_b": "Escribir una prueba de componente antes de escribir el código correspondiente.",
        "opcion_c": "Ejecutar una prueba de eficiencia de desempeño de un componente durante la prueba de componente.",
        "opcion_d": "Redactar un guion de prueba antes de establecer el proceso de gestión de la configuración.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Los guiones de prueba deben estar sujetos a la gestión de la configuración, por lo que no tiene sentido crear los guiones de prueba antes de que se establezca este proceso.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de los siguientes argumentos utilizaría para convencer a su jefe de que organice retrospectivas al final de cada ciclo de entrega?",
        "opcion_a": "Las retrospectivas son muy populares hoy en día y los clientes agradecerían que las añadiéramos a nuestros procesos.",
        "opcion_b": "Organizar retrospectivas ahorrará dinero a la organización porque los representantes de los usuarios finales no proporcionan retroalimentación inmediata sobre el producto.",
        "opcion_c": "Los puntos débiles del proceso identificados durante la retrospectiva pueden analizarse y servir como lista de tareas para el programa de mejora continua del proceso de la organización.",
        "opcion_d": "Los puntos débiles del proceso identificados durante la retrospectiva pueden analizarse y servir como lista de tareas para el programa de mejora continua del proceso de la organización.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las retrospectivas realizadas con regularidad, cuando se llevan a cabo las actividades de seguimiento adecuadas, son fundamentales para la mejora continua del desarrollo y las pruebas.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Qué tipos de fallos (1-4) se ajustan MEJOR a qué niveles de prueba (A-D)? 1. Fallos en el comportamiento del sistema cuando se desvía de las necesidades de negocio del usuario. 2. Fallos en la comunicación entre componentes. 3. Fallos en la lógica de un módulo. 4. Fallos en la implementación incorrecta de las reglas de negocio. A. Prueba de componente. B. Prueba de integración de componentes. C. Prueba de sistema. D. Prueba de aceptación.",
        "opcion_a": "1D, 2B, 3A, 4C.",
        "opcion_b": "1D, 2B, 3C, 4A.",
        "opcion_c": "1B, 2A, 3D, 4C.",
        "opcion_d": "1C, 2B, 3A, 4D.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La base de prueba para las pruebas de aceptación son las necesidades de negocio del usuario (1D). La comunicación entre componentes se prueba durante las pruebas de integración de componentes (2B). Los fallos en la lógica se encuentran durante las pruebas de componentes (3A). Las reglas de negocio son la base de prueba para las pruebas de sistema (4C).",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Usted está probando una historia de usuario con tres criterios de aceptación: CA1, CA2 y CA3. CA1 está cubierto por el caso de prueba CP1, CA2 por CP2, y CA3 por CP3. La historia de ejecución de prueba tuvo tres ejecuciones de prueba en tres versiones consecutivas del software: Ejecución 01: CP1 Falló, CP2 Pasó, CP3 Falló. Ejecución 02: CP1 Pasó, CP2 Falló, CP3 Falló. Ejecución 03: CP1 Pasó, CP2 Pasó, CP3 Pasó. Las pruebas se repiten una vez que se informa de que se han corregido todos los defectos encontrados y de que está disponible una nueva versión del software. ¿Cuáles de las pruebas anteriores se ejecutan como prueba de regresión?",
        "opcion_a": "Sólo 4, 7, 8, 9 (numerando las 9 ejecuciones en orden: CP1E1=1, CP2E1=2, CP3E1=3, CP1E2=4, CP2E2=5, CP3E2=6, CP1E3=7, CP2E3=8, CP3E3=9).",
        "opcion_b": "Sólo 5, 7.",
        "opcion_c": "Sólo 4, 6, 8, 9.",
        "opcion_d": "Sólo 5, 6.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "CP1 y CP3 fallaron en la Ejecución 1, así que su repetición (pruebas 4 y 6) son de confirmación. CP2 y CP3 fallaron en la Ejecución 2, así que su repetición (pruebas 8 y 9) también son de confirmación. CP2 pasó en la Ejecución 1, así que su repetición (prueba 5) es de regresión. CP1 pasó en la Ejecución 2, así que su repetición (prueba 7) también es de regresión.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las opciones siguientes NO es una ventaja de la prueba estática?",
        "opcion_a": "Tener una gestión de defectos menos costosa debido a la facilidad de detectar defectos más tarde en el CVDS.",
        "opcion_b": "Corregir los defectos encontrados durante la prueba estática es generalmente mucho menos costoso que corregir los defectos encontrados durante la prueba dinámica.",
        "opcion_c": "Encontrar defectos de código que no se habrían encontrado con pruebas dinámicas.",
        "opcion_d": "Detectar carencias e incoherencias en los requisitos.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La gestión de defectos no es menos costosa por detectar defectos MÁS TARDE en el CVDS; al contrario, encontrar y corregir defectos más tarde en el CVDS es más costoso. Las demás opciones sí son ventajas reales de la prueba estática.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones es una ventaja de la retroalimentación temprana y frecuente?",
        "opcion_a": "Mejora el proceso de prueba para futuros proyectos.",
        "opcion_b": "Obliga a los clientes a priorizar sus requisitos en función de los riesgos acordados.",
        "opcion_c": "Es la única forma de medir la calidad de los cambios.",
        "opcion_d": "Ayuda a evitar malentendidos sobre los requisitos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La retroalimentación temprana y frecuente permite la comunicación precoz de posibles problemas de calidad, ayudando a evitar malentendidos sobre los requisitos.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Las revisiones que se utilizan en su organización presentan las siguientes características: cuentan con el rol de escriba; el objetivo principal es evaluar la calidad; la reunión está liderada por el autor del producto de trabajo; hay una preparación individual; se elabora un informe de revisión. ¿Cuál de los siguientes tipos de revisión es MÁS probable que se utilice?",
        "opcion_a": "Revisión informal.",
        "opcion_b": "Revisión guiada.",
        "opcion_c": "Revisión técnica.",
        "opcion_d": "Inspección.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El rol de escriba descarta la revisión informal. Que la reunión esté dirigida por el autor del producto de trabajo apunta a una revisión guiada (esto no está permitido en inspecciones y no suele hacerse en revisiones técnicas).",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de estos enunciados NO es un factor que contribuye al éxito de las revisiones?",
        "opcion_a": "Los participantes deben dedicar un tiempo adecuado a la revisión.",
        "opcion_b": "Dividir los productos de trabajo grandes en partes pequeñas para que el esfuerzo requerido sea menos intenso.",
        "opcion_c": "Los participantes deben evitar comportamientos que puedan indicar aburrimiento, exasperación u hostilidad hacia otros participantes.",
        "opcion_d": "Los fallos encontrados deben reconocerse, valorarse y tratarse objetivamente.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Durante las revisiones se pueden encontrar defectos, no fallos (las revisiones son estáticas, no ejecutan el software). Las demás opciones sí son factores de éxito reales.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones es una característica de las técnicas de prueba basadas en la experiencia?",
        "opcion_a": "Los casos de prueba se crean a partir de información de diseño detallada.",
        "opcion_b": "Los elementos probados en la sección de código de la interfaz se utilizan para medir la cobertura.",
        "opcion_c": "Las técnicas se basan en gran medida en los conocimientos del probador sobre el software y el dominio del negocio.",
        "opcion_d": "Los casos de prueba se utilizan para identificar desviaciones con respecto a los requisitos.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "El conocimiento y experiencia del probador (uso previsto del software, entorno, defectos probables) se utiliza para definir las pruebas basadas en la experiencia. a) y b) son caja blanca; d) es caja negra.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Estás probando un formulario de búsqueda de pisos simplificado que sólo tiene dos criterios de búsqueda: Piso (con tres opciones: planta baja; primer piso; segundo piso o superior) y Tipo de jardín (con tres opciones: sin jardín; jardín pequeño; jardín grande). Sólo los pisos de la planta baja pueden tener jardín; el formulario valida esto. Cada prueba tiene dos valores de entrada: planta y tipo de jardín. Desea aplicar la partición de equivalencia (PE) para cubrir cada planta y cada tipo de jardín en sus pruebas. ¿Cuál es el número mínimo de casos de prueba para alcanzar el 100% de cobertura PE?",
        "opcion_a": "3",
        "opcion_b": "4",
        "opcion_c": "5",
        "opcion_d": "6",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "\"Jardín pequeño\" y \"jardín grande\" sólo pueden ir con \"planta baja\": CP1 (planta baja, jardín pequeño), CP2 (planta baja, jardín grande). Faltan cubrir primera planta y segunda planta o superior con \"sin jardín\": CP3 (primera planta, sin jardín), CP4 (segunda planta o superior, sin jardín). Total: 4 casos de prueba.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Está probando un sistema que calcula la nota final del curso para un alumno determinado. La nota final se asigna según: 0-50 suspenso, 51-60 regular, 61-70 satisfactorio, 71-80 bien, 81-90 muy bien, 91-100 excelente. Ha preparado los casos de prueba: CP1(91,excelente), CP2(50,suspenso), CP3(81,muy bien), CP4(60,regular), CP5(70,satisfactorio), CP6(80,bien). ¿Cuál es la cobertura del análisis del valor frontera (AVF) de 2 valores para el resultado final que se consigue con los casos de prueba existentes?",
        "opcion_a": "50%",
        "opcion_b": "60%",
        "opcion_c": "33,3%",
        "opcion_d": "100%",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Hay 12 valores frontera: 0, 50, 51, 60, 61, 70, 71, 80, 81, 90, 91 y 100. Los casos de prueba cubren seis de ellos (91, 50, 81, 60, 70 y 51 -este último implícito por rango-). Por lo tanto, cubren 6/12 = 50%.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Su tienda favorita de alquiler diario de bicicletas tiene un sistema con estas reglas: cualquiera puede alquilar una bicicleta, pero los socios obtienen un descuento del 20%; si no se cumple el plazo de devolución, el descuento deja de estar disponible; después de 15 alquileres, los socios reciben una camiseta de regalo. La tabla de decisión tiene 8 reglas (R1-R8) combinando ser miembro (V/F), incumplimiento de plazo (V/F) y alquiler número 15 (V/F), con acciones de 20% descuento y camiseta de regalo marcadas según cada combinación. Basándose ÚNICAMENTE en la descripción de las prestaciones, ¿cuál de las reglas describe una situación imposible?",
        "opcion_a": "R4",
        "opcion_b": "R2",
        "opcion_c": "R6",
        "opcion_d": "R8",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "No hay descuento porque es socio con plazo incumplido en R4, pero sí tiene marcada la camiseta de regalo cuando también incumplió el plazo. Solo los socios pueden recibir camiseta de regalo tras 15 alquileres, y en R4 (socio con plazo incumplido en el alquiler 15) la acción no es coherente con la descripción de las prestaciones.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Usted prueba un sistema cuyo ciclo de vida está modelado por un diagrama de transición de estado con los estados INICIO, MODO DEPURACIÓN, APAGADO, EN OPERACIÓN y EN ESPERA, con transiciones PROBAR (Inicio→Modo depuración), COMPLETADO (Modo depuración→Apagado), ERROR (En operación→Modo depuración), EJECUTAR (Inicio→En operación), PAUSAR (En operación→En espera), REANUDAR (En espera→En operación), COMPLETADO (En espera→Apagado). El sistema comienza en INICIO y termina en APAGADO. ¿Cuál es el número MÍNIMO de casos de prueba para lograr una cobertura de transiciones válidas?",
        "opcion_a": "4",
        "opcion_b": "2",
        "opcion_c": "7",
        "opcion_d": "3",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Las transiciones PROBAR y ERROR no pueden darse en un mismo caso de prueba, ni las dos transiciones COMPLETADO juntas. Se necesitan al menos tres casos: CP1: PROBAR,COMPLETADO. CP2: EJECUTAR,ERROR,COMPLETADO. CP3: EJECUTAR,PAUSAR,REANUDAR,PAUSAR,COMPLETADO.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Su juego de prueba logró una cobertura de sentencia del 100%. ¿Cuál es la consecuencia de este hecho?",
        "opcion_a": "Cada instrucción del código que contiene un defecto se ha ejecutado al menos una vez.",
        "opcion_b": "Cualquier juego de prueba que contenga más casos de prueba que su juego de prueba también alcanzará una cobertura de sentencia del 100%.",
        "opcion_c": "Cada camino del código se ha ejecutado al menos una vez.",
        "opcion_d": "Cada combinación de valores de entrada se ha probado al menos una vez.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Dado que se consigue un 100% de cobertura de sentencia, todas las sentencias, incluidas las que tienen defectos, deben haberse ejecutado y evaluado al menos una vez.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es correcta con respecto a la prueba de caja blanca?",
        "opcion_a": "Durante la prueba de caja blanca se tiene en cuenta toda la implementación del software.",
        "opcion_b": "Las métricas de cobertura de caja blanca pueden ayudar a identificar pruebas adicionales para aumentar la cobertura de código.",
        "opcion_c": "Las técnicas de prueba de caja blanca pueden utilizarse en pruebas estáticas.",
        "opcion_d": "La prueba de caja blanca puede ayudar a identificar lagunas en la implementación de requisitos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Este es el punto débil de las técnicas de caja blanca: no son capaces de identificar la implementación que falta, porque se basan únicamente en la estructura del objeto de prueba, no en la especificación de requisitos.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe MEJOR el concepto de predicción de errores?",
        "opcion_a": "La predicción de errores implica utilizar sus conocimientos y experiencia sobre los defectos encontrados en el pasado y los errores típicos cometidos por los desarrolladores.",
        "opcion_b": "La predicción de errores implica utilizar su experiencia personal en el desarrollo y los errores que cometió como desarrollador.",
        "opcion_c": "La predicción de errores requiere que imagine que es el usuario del objeto de prueba y que adivine los errores que podría cometer al interactuar con él.",
        "opcion_d": "La predicción de errores requiere replicar rápidamente la tarea de desarrollo para identificar el tipo de equivocación que podría cometer un desarrollador.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "El concepto básico de la predicción de errores es que el probador intenta conjeturar qué errores puede haber cometido el desarrollador y qué defectos puede haber en el objeto de prueba basándose en la experiencia pasada.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "En su proyecto se ha producido un retraso en la entrega de una nueva aplicación y la ejecución de la prueba ha comenzado con retraso, pero usted tiene un conocimiento muy detallado del dominio y buenas competencias analíticas. La lista completa de requisitos aún no se ha compartido con el equipo, pero la dirección pide que se presenten algunos resultados de la prueba. ¿Qué técnica de prueba encaja MEJOR en esta situación?",
        "opcion_a": "Prueba basada en lista de comprobación.",
        "opcion_b": "Predicción de errores.",
        "opcion_c": "Prueba exploratoria.",
        "opcion_d": "Prueba de rama.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las pruebas exploratorias son más útiles cuando hay pocas especificaciones conocidas y/o hay un plazo apremiante para realizar las pruebas.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe MEJOR la forma en que se pueden documentar los criterios de aceptación?",
        "opcion_a": "Realizar retrospectivas para determinar las necesidades reales de los implicados con respecto a una historia de usuario dada.",
        "opcion_b": "Utilizar el formato dado/cuando/entonces (\"given/when/then\") para describir un ejemplo de condición de prueba relacionada con una historia de usuario determinada.",
        "opcion_c": "Utilizar la comunicación verbal para reducir el riesgo de que los demás malinterpreten los criterios de aceptación.",
        "opcion_d": "Documentar los riesgos relacionados con una historia de usuario dada en un plan de prueba para facilitar la prueba basada en el riesgo de una historia de usuario dada.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Es la forma estándar de documentar los criterios de aceptación (formato dado/cuando/entonces).",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Historia de usuario: Como Editor, quiero revisar el contenido antes de que se publique, para asegurarme de que la gramática es correcta. Criterios de aceptación: el usuario puede iniciar sesión como Editor; el editor puede ver páginas existentes; el editor puede editar el contenido; el editor puede añadir comentarios; el editor puede guardar cambios; el editor puede reasignar el rol de \"propietario del contenido\" para realizar actualizaciones. ¿Cuál de las siguientes opciones es el MEJOR ejemplo de prueba DGPA para esta historia de usuario?",
        "opcion_a": "Probar si el editor puede guardar el documento después de borrar el contenido de la página.",
        "opcion_b": "Probar si el propietario del contenido puede iniciar sesión y realizar actualizaciones del contenido.",
        "opcion_c": "Probar si el editor puede programar el contenido editado para su publicación.",
        "opcion_d": "Probar si el editor puede reasignar a otro editor para realizar actualizaciones.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Los criterios de aceptación se refieren a la reasignación de un editor al propietario del contenido, no a otro editor; y cubren que el propietario del contenido pueda iniciar sesión y actualizar.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿De qué forma los probadores aportan valor a la planificación de la iteración y entrega?",
        "opcion_a": "Los probadores determinan la prioridad de las historias de usuario que hay que desarrollar.",
        "opcion_b": "Los probadores se concentran sólo en los aspectos funcionales del sistema que se va a probar.",
        "opcion_c": "Los probadores participan en la identificación detallada del riesgo y en la evaluación del riesgo de las historias de usuario.",
        "opcion_d": "Los probadores garantizan la entrega de software de alta calidad mediante un diseño de prueba temprano durante la planificación de la entrega.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Según el programa de estudio, participar en la identificación y evaluación detallada del riesgo de las historias de usuario es una de las formas en que los probadores añaden valor a la planificación de la iteración y la entrega.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuáles DOS de las siguientes opciones son criterios de salida para probar un sistema?",
        "opcion_a": "La preparación del entorno de prueba.",
        "opcion_b": "La capacidad de iniciar sesión en el objeto de prueba por parte del probador.",
        "opcion_c": "Haber alcanzado la densidad de defectos estimada.",
        "opcion_d": "Los requisitos se traducen al formato dado/cuando/entonces (\"given/when/then\").",
        "opcion_e": "Las pruebas de regresión se encuentran automatizadas",
        "respuesta_correcta": "C,E",
        "explicacion": "La densidad de defectos estimada es una medida de diligencia (criterio de salida). La automatización de las pruebas de regresión es un criterio de compleción (criterio de salida). Las demás opciones son criterios de entrada (disponibilidad de recursos).",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Su equipo utiliza la técnica de estimación de tres puntos para estimar el esfuerzo de prueba de una nueva prestación de alto riesgo. Estimaciones: más optimista 2 horas-persona; más probable 11 horas-persona; más pesimista 14 horas-persona. ¿Cuál es la estimación final?",
        "opcion_a": "9 horas-persona.",
        "opcion_b": "14 horas-persona.",
        "opcion_c": "11 horas-persona.",
        "opcion_d": "10 horas-persona.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Fórmula de estimación de tres puntos: E = (optimista + 4*más probable + pesimista)/6 = (2+(4*11)+14)/6 = 10.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Usted está probando una aplicación móvil que permite encontrar un restaurante cercano según el tipo de comida. Casos de prueba con prioridad (menor número = mayor prioridad) y dependencias: CP001 Seleccionar tipo de alimento (prioridad 3, sin dependencia), CP002 Seleccionar restaurante (prioridad 2, depende de CP001), CP003 Obtener dirección (prioridad 1, depende de CP002), CP004 Llamar restaurante (prioridad 2, depende de CP002), CP005 Hacer reserva (prioridad 3, depende de CP002). ¿Cuál de los siguientes casos de prueba debe ejecutarse en tercer lugar?",
        "opcion_a": "TC 003",
        "opcion_b": "TC 005",
        "opcion_c": "TC 002",
        "opcion_d": "TC 001",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "CP001 debe ser la primera (satisface dependencias), seguida de CP002. Después, CP003 para satisfacer la prioridad más alta restante (prioridad 1), y luego CP004 y CP005.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Tenga en cuenta las siguientes categorías de prueba (1-4) y los cuadrantes de prueba ágil (A-D): 1. Prueba de usabilidad. 2. Prueba de componente. 3. Prueba funcional. 4. Prueba de fiabilidad. A. Cuadrante Q1: de cara a la tecnología, apoya al equipo de desarrollo. B. Cuadrante Q2: de cara al negocio, apoya al equipo de desarrollo. C. Cuadrante Q3: de cara al negocio, critica el producto. D. Cuadrante Q4: de cara a la tecnología, critica el producto. ¿Cómo se corresponden las categorías de prueba con los cuadrantes de prueba ágil?",
        "opcion_a": "1C, 2A, 3B, 4D",
        "opcion_b": "1D, 2A, 3C, 4B",
        "opcion_c": "1C, 2B, 3D, 4A",
        "opcion_d": "1D, 2B, 3C, 4A",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Usabilidad está en Q3 (de cara al negocio, critica el producto). Prueba de componente está en Q1 (de cara a la tecnología, apoya al desarrollo). Prueba funcional está en Q2 (de cara al negocio, apoya al desarrollo). Fiabilidad está en Q4 (de cara a la tecnología, critica el producto).",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Durante un análisis del riesgo se identificó: Riesgo: el tiempo de respuesta es muy prolongado para generar un informe. Probabilidad: media; impacto: alto. Respuesta al riesgo: un equipo de prueba independiente realiza pruebas de rendimiento durante la prueba de sistema; una muestra de usuarios finales realiza pruebas de aceptación alfa y beta antes de la entrega. ¿Qué medida se propone tomar en respuesta a este riesgo analizado?",
        "opcion_a": "Aceptación del riesgo.",
        "opcion_b": "Plan de contingencia.",
        "opcion_c": "Mitigación del riesgo.",
        "opcion_d": "Transferencia del riesgo.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las acciones propuestas (pruebas de rendimiento, pruebas de aceptación) están relacionadas con la prueba, lo cual es una forma de mitigación del riesgo, no aceptación, contingencia ni transferencia.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Qué herramienta puede utilizar un equipo ágil para mostrar la cantidad de trabajo que se ha completado y la cantidad de trabajo total restante para una iteración determinada?",
        "opcion_a": "Criterios de aceptación.",
        "opcion_b": "Informe de defecto.",
        "opcion_c": "Informe de compleción de la prueba.",
        "opcion_d": "Gráfico de quemado.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Los gráficos de quemado son una representación gráfica del trabajo que queda por hacer frente al tiempo restante, actualizados diariamente para mostrar el avance de forma continua.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Usted necesita actualizar uno de los guiones de prueba automatizados para que se ajuste a un nuevo requisito. ¿Qué proceso indica que debe crear una nueva versión del guion de prueba en el repositorio de pruebas?",
        "opcion_a": "Gestión de la trazabilidad.",
        "opcion_b": "Prueba de mantenimiento.",
        "opcion_c": "Gestión de la configuración.",
        "opcion_d": "Ingeniería de requisitos.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Para apoyar la prueba, la gestión de la configuración puede implicar el control de versión de todos los elementos de prueba, incluidos los guiones de prueba.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Ha recibido el siguiente informe de defecto de los desarrolladores, indicando que la anomalía descrita no es reproducible: \"La aplicación se bloquea tras introducir 'Entrada de prueba: $ä' en el campo Nombre de la pantalla de creación de un nuevo usuario. Intenté cerrar sesión, iniciar sesión con test_admin01, mismo problema. Probado con otras cuentas de administrador, mismo problema. No se ha recibido ningún mensaje de error; el registro contiene una notificación de error crítico. Basándose en el caso de prueba TC-1305, la aplicación debería aceptar la entrada proporcionada y crear el usuario. Por favor, corrija con alta prioridad, esta prestación está relacionada con REQ-0012.\" ¿Qué información crítica falta en este informe que hubiera sido útil para los desarrolladores?",
        "opcion_a": "Resultado esperado y resultado real.",
        "opcion_b": "Referencias y estado de los defectos.",
        "opcion_c": "Entorno de prueba y elemento de prueba.",
        "opcion_d": "Prioridad y severidad.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "No sabemos en qué entorno de prueba se detectó la anomalía, ni qué aplicación (y versión) está afectada; eso es lo que impide a los desarrolladores reproducirla.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿A qué actividad de prueba da soporte una herramienta de preparación de datos de prueba?",
        "opcion_a": "Monitorización y control de prueba.",
        "opcion_b": "Análisis y diseño de la prueba.",
        "opcion_c": "Implementación y ejecución de la prueba.",
        "opcion_d": "Compleción de la prueba.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La implementación de prueba incluye la creación o adquisición del software de prueba necesario para la ejecución de prueba, incluidos los datos de prueba.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Qué elemento identifica correctamente un riesgo potencial de realizar la automatización de la prueba?",
        "opcion_a": "Puede introducir regresiones desconocidas en producción.",
        "opcion_b": "Es posible que no se dediquen suficientes esfuerzos al mantenimiento del producto de prueba.",
        "opcion_c": "Puede que no se confíe lo suficiente en las herramientas de prueba y los productos de prueba asociados.",
        "opcion_d": "Puede reducir el tiempo asignado a la prueba manual.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La asignación incorrecta o insuficiente del esfuerzo para mantener el producto de prueba automatizado es un riesgo real de la automatización.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Se le ha encomendado la tarea de analizar y solucionar las causas de los fallos de un nuevo sistema que se va a entregar. ¿Qué actividad está realizando?",
        "opcion_a": "Depuración.",
        "opcion_b": "Prueba de software.",
        "opcion_c": "Educción de requisitos.",
        "opcion_d": "Gestión de defectos.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La depuración es el proceso de encontrar, analizar y eliminar las causas de los fallos en un componente o sistema.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "En muchas organizaciones de software, el departamento de prueba se denomina departamento de Aseguramiento de la Calidad (QA). ¿Es esta frase correcta o no y por qué?",
        "opcion_a": "Es correcta. Probar y Aseguramiento de la Calidad significan exactamente lo mismo.",
        "opcion_b": "Es correcta. Estas denominaciones pueden utilizarse indistintamente porque tanto la prueba como el aseguramiento de la calidad centran sus actividades en los mismos problemas de calidad.",
        "opcion_c": "No es correcto. Las pruebas son algo más; las pruebas incluyen todas las actividades relacionadas con la calidad. El aseguramiento de la calidad se centra en los procesos relacionados con la calidad.",
        "opcion_d": "No es correcto. El aseguramiento de la calidad se concentra en los procesos relacionados con la calidad, mientras que las pruebas se centran en demostrar que un componente o sistema es adecuado para su finalidad y en detectar defectos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba y el aseguramiento de la calidad no son lo mismo: la prueba consiste en actividades del CVDS relacionadas con determinar que un componente cumple requisitos y detectar defectos; el aseguramiento de la calidad se concentra en establecer, introducir, monitorizar, mejorar y adherirse a los procesos relacionados con la calidad.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Un teléfono que suena en un cubículo vecino distrae a un programador y le hace programar incorrectamente la lógica que comprueba la frontera superior de una variable de entrada. Más tarde, durante la prueba de sistema, un probador notifica que este campo de entrada acepta valores de entrada no válidos. ¿Cuál de las siguientes opciones describe correctamente una frontera superior codificada incorrectamente?",
        "opcion_a": "La causa raíz.",
        "opcion_b": "Un fallo.",
        "opcion_c": "Un error.",
        "opcion_d": "Un defecto.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "El problema en el código (la frontera superior codificada incorrectamente) es un defecto. La causa raíz es la distracción; el fallo es aceptar entradas no válidas; el error es la equivocación del programador.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Tener en cuenta el siguiente producto de prueba: Contrato de Prueba #04.081, Duración de la sesión: 1 hora, Explorar: Página de registro, Con: Diferentes conjuntos de datos de entrada incorrectos, Para descubrir: Defectos relacionados con la aceptación del proceso de registro con la entrada incorrecta. ¿Qué actividad de prueba produce este producto de prueba como salida?",
        "opcion_a": "Planificación de la prueba.",
        "opcion_b": "Monitorización y control de prueba.",
        "opcion_c": "Análisis de prueba.",
        "opcion_d": "Diseño de prueba.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "El software de prueba que se está describiendo es un contrato de prueba (\"test charter\"), producto de salida del diseño de prueba (típico en pruebas exploratorias basadas en sesión).",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones es el MEJOR ejemplo de cómo la trazabilidad apoya la prueba?",
        "opcion_a": "Realizar el análisis de impacto de un cambio dará información sobre la compleción de las pruebas.",
        "opcion_b": "El análisis de la trazabilidad entre los casos de prueba y los resultados de prueba proporcionará información sobre el nivel de riesgo residual estimado.",
        "opcion_c": "Realizar el análisis de impacto de un cambio ayudará a seleccionar los casos de prueba adecuados para la prueba de regresión.",
        "opcion_d": "El análisis de la trazabilidad entre la base de prueba, los objetos de prueba y los casos de prueba ayudará a seleccionar los datos de prueba para lograr la cobertura que se asume del objeto de prueba.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Realizar el análisis de impacto de los cambios ayuda a seleccionar los casos de prueba adecuados para la prueba de regresión; ésta es la aplicación práctica más clara de la trazabilidad.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones explica MEJOR una ventaja de la independencia de la prueba?",
        "opcion_a": "El uso de un equipo de prueba independiente permite a la gestión de proyecto asignar la responsabilidad de la calidad del entregable final al equipo de prueba.",
        "opcion_b": "Si se puede permitir un equipo de prueba externo a la organización, entonces hay claras ventajas en cuanto a que este equipo externo no se deja influir tan fácilmente por los asuntos de entrega de la gestión de proyectos y la necesidad de cumplir plazos de entrega estrictos.",
        "opcion_c": "Un equipo de prueba independiente puede trabajar separado de los desarrolladores, no necesita distraerse con los cambios de requisitos del proyecto y puede limitar la comunicación con los desarrolladores a los informes de defectos a través del sistema de gestión de defectos.",
        "opcion_d": "Cuando las especificaciones contienen ambigüedades e incoherencias, se hacen suposiciones sobre su interpretación, y un probador independiente puede ser útil para cuestionar esas suposiciones y la interpretación hecha por el desarrollador.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Las especificaciones nunca son perfectas, lo que significa que el desarrollador tendrá que hacer suposiciones. Un probador independiente es útil en la medida en que puede cuestionar y verificar esas suposiciones y la interpretación realizada por el desarrollador.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Usted trabaja como probador en un equipo que sigue el modelo V. ¿Cómo afecta la elección de este modelo de ciclo de vida de desarrollo del software (CVDS) a la cronología de las pruebas?",
        "opcion_a": "La prueba dinámica no puede realizarse al principio del CVDS.",
        "opcion_b": "La prueba estática no puede realizarse al principio del CVDS.",
        "opcion_c": "La planificación de la prueba no puede realizarse al principio del CVDS.",
        "opcion_d": "La prueba de aceptación puede realizarse al principio del CVDS.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "En los modelos de desarrollo secuencial como el modelo V, en las fases iniciales los probadores participan en revisión de requisitos, análisis y diseño de prueba (estática); el código ejecutable suele crearse en fases posteriores, así que la prueba dinámica no puede realizarse al principio.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuáles de las siguientes son ventajas de DevOps? I. Entrega del producto más rápida y plazo de comercialización más rápido. II. Aumenta la necesidad de la prueba manual repetitiva. III. Disponibilidad permanente de software ejecutable. IV. Reducción del número de pruebas de regresión asociadas a la refactorización de código. V. La configuración del marco de trabajo de automatización de la prueba es poco costosa, ya que todo está automatizado.",
        "opcion_a": "I, II, IV son ventajas; III, V no lo son.",
        "opcion_b": "III, V son ventajas; I, II, IV no lo son.",
        "opcion_c": "I, III son ventajas; II, IV, V no lo son.",
        "opcion_d": "II, IV, V son ventajas; I, III no lo son.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Entrega más rápida (I) y disponibilidad permanente de software ejecutable (III) son ventajas reales de DevOps. Con DevOps se necesita MENOS prueba manual (no más, II es falso), se necesitan MÁS pruebas de regresión por la refactorización frecuente (IV es falso), y configurar la automatización sigue siendo costoso (V es falso).",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Usted trabaja como probador en un proyecto sobre una aplicación móvil para pedidos de comida. El cliente envió un requisito de alta prioridad: \"El pedido debe procesarse en menos de 10 segundos en el 95% de los casos\". Usted creó un conjunto de casos de prueba en los que se realizaron pedidos aleatoriamente, se midió el tiempo de procesamiento y se comprobaron los resultados con los requisitos. ¿Qué tipo de prueba llevó a cabo?",
        "opcion_a": "Funcional, porque los casos de prueba cubren el requisito de negocio del usuario para el sistema.",
        "opcion_b": "No funcional, porque mide el rendimiento del sistema.",
        "opcion_c": "Funcional, porque los casos de prueba interactúan con la interfaz de usuario.",
        "opcion_d": "Estructural, porque necesitamos conocer la estructura interna del programa para medir el tiempo de procesamiento del pedido.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Es un ejemplo de prueba de rendimiento, un tipo de prueba no funcional (evalúa CÓMO se comporta el sistema, no QUÉ hace, aunque el requisito provenga directamente del cliente y sea de alta prioridad).",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "La estrategia de pruebas de su organización sugiere que, una vez que se vaya a retirar un sistema, se pruebe la migración de datos. ¿En el marco de qué tipo de prueba es MÁS probable que se realice esta prueba?",
        "opcion_a": "Prueba de mantenimiento.",
        "opcion_b": "Prueba de regresión.",
        "opcion_c": "Prueba de componente.",
        "opcion_d": "Prueba de integración.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Cuando se retira un sistema puede ser necesario probar la migración de datos, lo cual es una forma de prueba de mantenimiento.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "La siguiente es una lista de productos de trabajo producidos en el CVDS: I. Requisitos de negocio. II. Cronograma. III. Presupuesto de la prueba. IV. Código ejecutable de terceros. V. Historias de usuario y sus criterios de aceptación. ¿Cuáles de ellos pueden ser revisados?",
        "opcion_a": "I y IV pueden ser revisados; II, III y V no.",
        "opcion_b": "I, II, III y IV pueden ser revisados; V no.",
        "opcion_c": "I, II, III y V pueden ser revisados; IV no.",
        "opcion_d": "III, IV y V pueden ser revisados; I y II no.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Solo el código ejecutable de terceros no puede ser revisado (las revisiones son técnicas estáticas sobre documentos/productos de trabajo, no sobre código de terceros ya compilado).",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Decida cuáles de los siguientes enunciados (I-V) son correctos para la prueba dinámica y cuáles para la prueba estática. I. Los comportamientos anómalos externos son más fáciles de identificar con esta prueba. II. Las discrepancias respecto a un estándar de codificación son más fáciles de encontrar con esta prueba. III. Identifica fallos causados por defectos cuando se ejecuta el software. IV. Su objetivo de prueba es identificar los defectos tan pronto como sea posible. V. La falta de cobertura de requisitos de seguridad críticos es más fácil de encontrar y solucionar.",
        "opcion_a": "I, IV, V son correctas para la prueba estática; II, III son correctas para la prueba dinámica.",
        "opcion_b": "I, III, IV son correctas para la prueba estática; II, V son correctas para la prueba dinámica.",
        "opcion_c": "II, III son correctas para la prueba estática; I, IV, V son correctas para la prueba dinámica.",
        "opcion_d": "II, IV, V son correctas para la prueba estática; I, III, IV son correctas para la prueba dinámica.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "II (discrepancias de estándar) y V (falta de cobertura de requisitos de seguridad) son más fáciles de encontrar con prueba estática. IV (identificar defectos lo antes posible) también aplica a estática. I (comportamientos anómalos externos) y III (fallos al ejecutar) son propios de la prueba dinámica.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de los siguientes enunciados sobre las revisiones formales es VERDADERO?",
        "opcion_a": "Algunas revisiones no requieren más de un rol.",
        "opcion_b": "El proceso de revisión tiene varias actividades.",
        "opcion_c": "La documentación que se va a revisar no se distribuye antes de la reunión de revisión, a excepción del producto de trabajo para tipos de revisión específicos.",
        "opcion_d": "Los defectos encontrados durante la revisión no se informan ya que no se encuentran mediante pruebas dinámicas.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Hay varias actividades durante el proceso de revisión formal (planificación, inicio, preparación individual, reunión de revisión, corrección, seguimiento). En todos los tipos de revisión hay más de un rol (incluso las informales); la documentación debe distribuirse lo antes posible; los defectos sí deben informarse.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Qué tarea puede asumir la dirección durante una revisión formal?",
        "opcion_a": "Asumir la responsabilidad general de la revisión.",
        "opcion_b": "Decidir qué se va a revisar.",
        "opcion_c": "Asegurar que las reuniones de revisión se lleven a cabo de forma efectiva y mediar, si es necesario.",
        "opcion_d": "Registrar la información de la revisión, tales como las decisiones de la revisión.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Decidir qué se va a revisar es tarea de la dirección en una revisión formal. Asumir la responsabilidad general es del revisor/moderador; asegurar reuniones efectivas es del moderador; registrar información es del escriba.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Un sistema de almacenamiento de vino usa un dispositivo que mide la temperatura T de la bodega (°C, redondeada al grado más próximo) y avisa si se desvía del valor óptimo de 12: si T=12 dice \"temperatura óptima\"; si T<12 dice \"la temperatura es demasiado baja\"; si T>12 dice \"¡la temperatura es demasiado alta!\". Desea usar el análisis del valor frontera (AVF) de 3 puntos. ¿Cuál es el conjunto MÍNIMO de entradas de prueba que consigue el 100% de la cobertura deseada?",
        "opcion_a": "11, 12, 13",
        "opcion_b": "10, 12, 14",
        "opcion_c": "10, 11, 12, 13, 14",
        "opcion_d": "10, 11, 13, 14",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Hay tres particiones con fronteras en 11, 12 y 13. Para AVF de 3 puntos, cada frontera necesita probarse junto a sus dos vecinos: para 11 (10,11,12), para 12 (11,12,13), para 13 (12,13,14). En total se necesitan 10, 11, 12, 13 y 14.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de los siguientes enunciados sobre la prueba de rama es CORRECTO?",
        "opcion_a": "Si un programa sólo incluye ramas incondicionales, entonces se puede conseguir un 100% de cobertura de rama sin ejecutar ningún caso de prueba.",
        "opcion_b": "Si los casos de prueba practican todas las ramas incondicionales del código, se consigue un 100% de cobertura de rama.",
        "opcion_c": "Si se consigue un 100% de cobertura de sentencia, entonces también se consigue un 100% de cobertura de rama.",
        "opcion_d": "Si se consigue un 100% de cobertura de rama, entonces se habrán practicado todos los resultados de decisión de cada sentencia de decisión del código.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Cada resultado de la decisión corresponde a una rama condicional, así que una cobertura de rama del 100% implica una cobertura de decisión del 100%. Sigue siendo necesario un caso de prueba aunque solo haya ramas incondicionales (a). Cubrir sólo las ramas incondicionales no basta (b). Una cobertura de sentencia del 100% NO implica cobertura de rama del 100% (c).",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Usted está probando una aplicación móvil que permite a los clientes acceder y gestionar sus cuentas bancarias. Está ejecutando un juego de prueba que implica la evaluación de cada pantalla, y de cada campo de cada pantalla, con respecto a una lista general de buenas prácticas de interfaz de usuario derivadas de un libro popular sobre el tema que maximiza el atractivo, la facilidad de uso y la accesibilidad para este tipo de aplicaciones. ¿Cuál de las siguientes opciones clasifica MEJOR la técnica de prueba que está utilizando?",
        "opcion_a": "Caja negra.",
        "opcion_b": "Exploratoria.",
        "opcion_c": "Basada en lista de comprobación.",
        "opcion_d": "Predicción de errores.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La lista de buenas prácticas de la interfaz de usuario es la lista de condiciones de prueba que deben comprobarse sistemáticamente, característico de la prueba basada en lista de comprobación.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe MEJOR el enfoque colaborativo en la redacción de historias de usuario?",
        "opcion_a": "Las historias de usuario son creadas por probadores y desarrolladores y luego aceptadas por los representantes de negocio.",
        "opcion_b": "Las historias de usuario son creadas conjuntamente por representantes de negocio, desarrolladores y probadores.",
        "opcion_c": "Las historias de usuario son creadas por representantes de negocio y verificadas por desarrolladores y probadores.",
        "opcion_d": "Las historias de usuario se crean de forma que sean independientes, negociables, valiosas, estimables, pequeñas y puedan ser objeto de prueba.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La redacción colaborativa de historias de usuario significa que todos los implicados (representantes de negocio, desarrolladores y probadores) crean las historias de usuario en colaboración, para obtener la visión compartida.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Tener en cuenta la siguiente parte de un plan de prueba: \"La prueba se realizará mediante la prueba de componente y la prueba de integración de componentes. El reglamento exige demostrar que se ha alcanzado un 100% de cobertura de rama para cada componente clasificado como crítico.\" ¿A qué parte del plan de pruebas pertenece esta parte?",
        "opcion_a": "Comunicación.",
        "opcion_b": "Registro de riesgos.",
        "opcion_c": "Contexto de la prueba.",
        "opcion_d": "Enfoque de prueba.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "El párrafo contiene información sobre los niveles de prueba y los criterios de salida, que forman parte del enfoque de prueba.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Su equipo utiliza el póker de planificación para estimar el esfuerzo de prueba de una nueva prestación solicitada. Existe la norma de que si no hay tiempo para llegar a un acuerdo total y la variación en los resultados es pequeña, se pueden aplicar reglas como \"aceptar el número con más votos\". Tras dos rondas sin consenso, se inició la tercera ronda. Resultados: Ronda 1: 21,2,5,34,13,8,2. Ronda 2: 13,8,8,34,13,8,5. Ronda 3: 13,8,13,13,13,13,8. ¿Cuál de las siguientes opciones es el MEJOR ejemplo del siguiente paso?",
        "opcion_a": "El propietario de producto tiene que intervenir y tomar una decisión final.",
        "opcion_b": "Aceptar 13 como estimación final de la prueba, ya que cuenta con la mayoría de los votos.",
        "opcion_c": "No se necesitan más acciones. Se ha alcanzado el consenso.",
        "opcion_d": "Eliminar la nueva prestación de la entrega actual porque no se ha alcanzado el consenso.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Si las estimaciones no son iguales, pero la variación de los resultados es pequeña, se pueden aplicar reglas como \"aceptar el número con más votos\": 13 aparece 5 veces en la Ronda 3, así que se acepta como estimación final.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es verdadera en relación con la pirámide de prueba?",
        "opcion_a": "La pirámide de prueba hace hincapié en tener un mayor número de pruebas en los niveles de prueba inferiores.",
        "opcion_b": "Cuanto más cerca de la cúspide de la pirámide, más formal debería ser su automatización de la prueba.",
        "opcion_c": "Normalmente, la prueba de componente y la prueba de integración de componentes se automatizan utilizando herramientas basadas en API (\"Application Programming Interface - API\").",
        "opcion_d": "Para la prueba de sistema y la prueba de aceptación, las pruebas automatizadas suelen crearse utilizando herramientas basadas en IGU (\"Interfaz Gráfica de Usuario - GUI\").",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "No es cierto que cerca de la cúspide de la pirámide la automatización de la prueba deba ser más formal. Las demás opciones sí son verdaderas.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "Durante el análisis del riesgo, el equipo consideró el riesgo: \"El sistema permite un descuento demasiado alto a un cliente\". El equipo estimó que el impacto del riesgo era muy alto. ¿Qué se puede decir de la probabilidad del riesgo?",
        "opcion_a": "También es muy alta. Un impacto del riesgo alto siempre implica una probabilidad del riesgo alta.",
        "opcion_b": "Es muy baja. Un impacto del riesgo alto siempre implica una probabilidad del riesgo baja.",
        "opcion_c": "No se puede decir nada sobre la probabilidad del riesgo. El impacto del riesgo y la probabilidad del riesgo son independientes.",
        "opcion_d": "La probabilidad del riesgo no es importante con un impacto del riesgo tan alto. No se necesita definirla.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "El impacto del riesgo y la probabilidad del riesgo son independientes; conocer uno no permite deducir el otro. Se necesitan ambos factores para calcular el nivel de riesgo.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "La siguiente lista contiene riesgos identificados para un nuevo producto software: I. La dirección traslada a dos probadores experimentados a otro proyecto. II. El sistema no cumple los estándares de seguridad física funcional. III. El tiempo de respuesta del sistema supera los requisitos de usuario. IV. Los implicados tienen expectativas imprecisas. V. Las personas discapacitadas tienen problemas al utilizar el sistema. ¿Cuáles de ellos son riesgos de proyecto?",
        "opcion_a": "I, IV son riesgos de proyecto; II, III, V no son riesgos de proyecto.",
        "opcion_b": "IV, V son riesgos de proyecto; I, II, III no son riesgos de proyecto.",
        "opcion_c": "I, III son riesgos de proyecto; II, IV, V no son riesgos de proyecto.",
        "opcion_d": "II, V son riesgos de proyecto; I, III, IV no son riesgos de proyecto.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "I (trasladar probadores) y IV (expectativas imprecisas de los implicados) son riesgos de PROYECTO. II (estándares de seguridad), III (tiempo de respuesta) y V (accesibilidad) son riesgos de PRODUCTO.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de los siguientes es un ejemplo de cómo el análisis del riesgo de producto influye en la minuciosidad y el alcance de la prueba?",
        "opcion_a": "El jefe de prueba monitoriza e informa diariamente del nivel de todos los riesgos conocidos para que los implicados puedan tomar una decisión informada sobre la fecha de entrega.",
        "opcion_b": "Uno de los riesgos identificados fue la \"Falta de soporte de bases de datos de código abierto\", por lo que el equipo decidió integrar el sistema con una base de datos de código abierto.",
        "opcion_c": "Durante el análisis cuantitativo del riesgo, el equipo estimó el nivel total de todos los riesgos identificados y lo comunicó como riesgo residual total antes de la prueba.",
        "opcion_d": "La evaluación del riesgo puso de manifiesto un nivel muy alto de riesgos de rendimiento, por lo que se decidió realizar pruebas detalladas de eficiencia del rendimiento en una fase temprana del ciclo de vida de desarrollo de software.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Esto muestra cómo el análisis del riesgo influye directamente en la minuciosidad de la prueba (nivel de detalle): un riesgo de rendimiento alto llevó a decidir pruebas detalladas y tempranas de eficiencia del rendimiento.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuáles DOS de las siguientes opciones son métricas comunes utilizadas para informar sobre el nivel de calidad del objeto de prueba?",
        "opcion_a": "Número de defectos encontrados durante la prueba de sistema.",
        "opcion_b": "Esfuerzo total en el diseño de pruebas dividido por el número de casos de prueba diseñados.",
        "opcion_c": "Número de procedimientos de prueba ejecutados.",
        "opcion_d": "Número de defectos encontrados dividido por el tamaño de un producto de trabajo.",
        "opcion_e": "Tiempo necesario para reparar un defecto.",
        "respuesta_correcta": "A,D",
        "explicacion": "El número de defectos encontrados y la densidad de defectos (defectos/tamaño) están relacionados con la calidad del objeto de prueba. Las demás son métricas de eficiencia o de proceso, no de calidad del producto.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
    {
        "enunciado": "¿Cuál de las siguientes informaciones contenidas en un informe del avance de la prueba es la MENOS útil para los representantes de negocio?",
        "opcion_a": "Impedimentos para la prueba.",
        "opcion_b": "Cobertura de rama alcanzada.",
        "opcion_c": "Avances de la prueba.",
        "opcion_d": "Nuevos riesgos dentro del ciclo de prueba.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La cobertura de rama es una métrica técnica utilizada por desarrolladores y probadores técnicos; no suele interesar a los representantes de negocio, a diferencia de impedimentos, avances y nuevos riesgos.",
        "modelo_examen": "Oficial ISTQB Modelo A"
    },
]


def main():
    with open(PREGUNTAS_PATH, "r", encoding="utf-8") as f:
        existing = json.load(f)

    print(f"Preguntas existentes antes de agregar: {len(existing)}")

    existing.extend(OFICIAL_MODELO_A)

    with open(PREGUNTAS_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"Se agregaron {len(OFICIAL_MODELO_A)} preguntas OFICIALES (Modelo A).")
    print(f"Total de preguntas ahora: {len(existing)}")


if __name__ == "__main__":
    main()
