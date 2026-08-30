# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")

import json
import os

PREGUNTAS_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "app", "preguntas.json")

SIMULACRO_5 = [
    {
        "enunciado": "¿Cuál de las siguientes NO es una razón común para realizar pruebas?",
        "opcion_a": "Encontrar defectos.",
        "opcion_b": "Reducir el riesgo.",
        "opcion_c": "Aumentar la confianza en el software.",
        "opcion_d": "Demostrar que el software está 100% libre de defectos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Las pruebas nunca pueden demostrar que el software está completamente libre de defectos (uno de los 7 principios de las pruebas).",
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Qué nivel de pruebas se centra en probar el sistema completo en su entorno de destino?",
        "opcion_a": "Prueba de unidad.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de sistema.",
        "opcion_d": "Prueba de aceptación.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de sistema evalúa el comportamiento del sistema completo e integrado en un entorno similar al de destino.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes técnicas es una técnica de prueba estática?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Análisis de valores límite.",
        "opcion_c": "Prueba de tabla de decisión.",
        "opcion_d": "Revisión de pares.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La revisión de pares es una técnica de prueba estática. Las demás son técnicas dinámicas de caja negra.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe la técnica de prueba de casos de uso?",
        "opcion_a": "Identificar grupos de entradas que se espera que se procesen de la misma manera.",
        "opcion_b": "Probar los valores en los límites de un rango de entrada.",
        "opcion_c": "Utilizar una tabla para definir las combinaciones de entradas y salidas esperadas.",
        "opcion_d": "Diseñar casos de prueba basados en las interacciones típicas de los usuarios con el sistema.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de casos de uso deriva casos de prueba a partir de las interacciones típicas entre el usuario (actor) y el sistema.",
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de un plan de pruebas?",
        "opcion_a": "Controlar las versiones del software y los artefactos de prueba.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_c": "Describir el alcance, el enfoque, los recursos y el cronograma de las actividades de prueba.",
        "opcion_d": "Evaluar los riesgos asociados con las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Un plan de pruebas describe el alcance, enfoque, recursos y cronograma de las actividades de prueba previstas.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una métrica de prueba común?",
        "opcion_a": "Número de casos de prueba ejecutados.",
        "opcion_b": "Número de defectos encontrados.",
        "opcion_c": "Tasa de defectos por hora.",
        "opcion_d": "Número de líneas de código escritas.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Las líneas de código escritas son una métrica de desarrollo, no de progreso o cobertura de pruebas.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes herramientas se utiliza para la gestión de la configuración?",
        "opcion_a": "Herramienta de gestión de pruebas.",
        "opcion_b": "Herramienta de control de versiones.",
        "opcion_c": "Herramienta de prueba de rendimiento.",
        "opcion_d": "Herramienta de seguimiento de errores.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "Una herramienta de control de versiones es la usada para la gestión de la configuración de software y artefactos.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el concepto de \"prioridad\" de un defecto?",
        "opcion_a": "La probabilidad de que un defecto cause un fallo.",
        "opcion_b": "El impacto del defecto en el funcionamiento del sistema.",
        "opcion_c": "La urgencia con la que se debe corregir el defecto.",
        "opcion_d": "La dificultad de encontrar un defecto.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prioridad indica la urgencia con la que debe resolverse un defecto, a diferencia de la gravedad (impacto en el sistema).",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes NO es una ventaja de las pruebas tempranas?",
        "opcion_a": "Reducción de los costes de corrección de defectos.",
        "opcion_b": "Mejora de la calidad del software.",
        "opcion_c": "Aumento del tiempo de desarrollo.",
        "opcion_d": "Reducción del riesgo.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "El aumento del tiempo de desarrollo no es una ventaja, sino un posible coste percibido; las pruebas tempranas reducen costes, mejoran calidad y reducen riesgo.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de los siguientes es un ejemplo de prueba no funcional?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Prueba de rendimiento.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de rendimiento evalúa un atributo de calidad no funcional. Las demás son técnicas de diseño de pruebas funcionales.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes afirmaciones sobre la prueba de integración es CORRECTA?",
        "opcion_a": "La prueba de integración se realiza después de la prueba de sistema.",
        "opcion_b": "La prueba de integración se centra en probar las interfaces entre los módulos.",
        "opcion_c": "La prueba de integración solo se puede realizar utilizando el enfoque de arriba hacia abajo.",
        "opcion_d": "La prueba de integración no es necesaria si se ha realizado una prueba de unidad exhaustiva.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de integración se enfoca en las interfaces y la interacción entre componentes o sistemas.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe la técnica de prueba de transición de estados?",
        "opcion_a": "Identificar las condiciones y las acciones que se deben tomar en función de las combinaciones de condiciones.",
        "opcion_b": "Probar los valores en los límites de un rango de entrada.",
        "opcion_c": "Utilizar un grafo para representar los estados y las transiciones entre estados.",
        "opcion_d": "Analizar el código fuente para identificar posibles defectos.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de transición de estados modela el sistema como estados y las transiciones válidas/inválidas entre ellos.",
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito del seguimiento de las pruebas?",
        "opcion_a": "Controlar el progreso de las pruebas en relación con el plan.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_c": "Evaluar la calidad del software.",
        "opcion_d": "Automatizar la ejecución de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "El seguimiento (monitorización) de pruebas compara el progreso real contra lo planificado.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un objetivo de las pruebas de mantenimiento?",
        "opcion_a": "Adaptar el sistema a un nuevo entorno.",
        "opcion_b": "Corregir defectos en el sistema existente.",
        "opcion_c": "Añadir nuevas funcionalidades al sistema.",
        "opcion_d": "Encontrar defectos en el código fuente original.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de mantenimiento se centra en el impacto de un cambio, no en encontrar defectos en el código original ya en producción desde cero.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba beta?",
        "opcion_a": "Se realiza por usuarios reales en el entorno de producción.",
        "opcion_b": "Se realiza por testers internos en un entorno simulado.",
        "opcion_c": "Se realiza por testers externos en un entorno controlado.",
        "opcion_d": "Se realiza por desarrolladores en su propio entorno.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba beta es realizada por clientes/usuarios reales en su propio entorno de uso real, a diferencia de la alfa (interna, simulada).",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre pruebas estáticas y dinámicas?",
        "opcion_a": "Las pruebas estáticas se realizan al principio del ciclo de vida del desarrollo, mientras que las pruebas dinámicas se realizan al final.",
        "opcion_b": "Las pruebas estáticas se basan en el código fuente, mientras que las pruebas dinámicas se basan en las especificaciones de los requisitos.",
        "opcion_c": "Las pruebas estáticas se realizan sin ejecutar el código, mientras que las pruebas dinámicas implican la ejecución del código.",
        "opcion_d": "Las pruebas estáticas son más importantes que las pruebas dinámicas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las pruebas estáticas (revisiones, análisis estático) no ejecutan el código; las dinámicas sí requieren su ejecución.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un factor que influye en la selección de las técnicas de prueba?",
        "opcion_a": "El tipo de sistema que se está probando.",
        "opcion_b": "Los riesgos asociados con el sistema.",
        "opcion_c": "La disponibilidad de las herramientas de prueba.",
        "opcion_d": "Las habilidades del equipo de pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La disponibilidad de herramientas influye en la selección de herramientas, no en la elección fundamental de técnicas de prueba.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes es una técnica de diseño de pruebas de caja blanca?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Prueba de condición.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de condición es una técnica de caja blanca (estructural). Las demás son técnicas de caja negra.",
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un objetivo típico de las pruebas de seguridad?",
        "opcion_a": "Evaluar la confidencialidad de los datos.",
        "opcion_b": "Evaluar la integridad de los datos.",
        "opcion_c": "Evaluar la disponibilidad del sistema.",
        "opcion_d": "Evaluar la facilidad de uso del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La facilidad de uso es objetivo de la prueba de usabilidad, no de seguridad (que evalúa confidencialidad, integridad y disponibilidad).",
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un beneficio de las pruebas independientes?",
        "opcion_a": "Mayor objetividad en las pruebas.",
        "opcion_b": "Mayor probabilidad de encontrar defectos.",
        "opcion_c": "Reducción del coste de las pruebas.",
        "opcion_d": "Mayor confianza en la calidad del software.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La independencia no reduce el coste de las pruebas; sus beneficios reales son objetividad, mayor detección de defectos y confianza en la calidad.",
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
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
        "modelo_examen": "Simulacro 5"
    },
]


def main():
    with open(PREGUNTAS_PATH, "r", encoding="utf-8") as f:
        existing = json.load(f)

    print(f"Preguntas existentes antes de agregar: {len(existing)}")

    existing.extend(SIMULACRO_5)

    with open(PREGUNTAS_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"Se agregaron {len(SIMULACRO_5)} preguntas del Simulacro 5.")
    print(f"Total de preguntas ahora: {len(existing)}")


if __name__ == "__main__":
    main()
