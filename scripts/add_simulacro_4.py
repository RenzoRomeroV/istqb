# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")

import json
import os

PREGUNTAS_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "app", "preguntas.json")

SIMULACRO_4 = [
    {
        "enunciado": "¿Cuál de las siguientes NO es una actividad principal en el proceso de prueba?",
        "opcion_a": "Planificación de las pruebas.",
        "opcion_b": "Diseño de las pruebas.",
        "opcion_c": "Corrección de defectos.",
        "opcion_d": "Ejecución de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Corregir defectos es una actividad de DESARROLLO, no del proceso de prueba.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de los siguientes es un principio fundamental de las pruebas?",
        "opcion_a": "Las pruebas exhaustivas son siempre posibles si se utilizan las herramientas adecuadas.",
        "opcion_b": "Las pruebas pueden demostrar la ausencia de defectos.",
        "opcion_c": "Las pruebas tempranas ahorran tiempo y dinero.",
        "opcion_d": "Las pruebas no dependen del contexto.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Cuanto antes se detecta un defecto en el ciclo de vida, más barato resulta corregirlo (principio de pruebas tempranas).",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Qué nivel de pruebas se centra en probar la integración de dos o más componentes?",
        "opcion_a": "Prueba de unidad.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de sistema.",
        "opcion_d": "Prueba de aceptación.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de integración verifica las interfaces y la interacción entre dos o más componentes.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes técnicas NO es una técnica de prueba estática?",
        "opcion_a": "Revisión de código.",
        "opcion_b": "Inspección.",
        "opcion_c": "Prueba de caja negra.",
        "opcion_d": "Análisis estático.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de caja negra es una técnica dinámica (requiere ejecutar el software); las demás son estáticas.",
        "modelo_examen": "Simulacro 4"
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
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Qué tipo de prueba se realiza para verificar que el sistema cumple con las necesidades y expectativas del usuario?",
        "opcion_a": "Prueba de regresión.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de aceptación.",
        "opcion_d": "Prueba de sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de aceptación establece confianza en que el sistema cumple con las necesidades y expectativas del usuario/negocio.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la gestión de defectos?",
        "opcion_a": "Controlar las versiones del software y los artefactos de prueba.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas, desde su detección hasta su resolución.",
        "opcion_c": "Planificar y controlar las actividades de prueba.",
        "opcion_d": "Evaluar los riesgos asociados con las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La gestión de defectos abarca todo el ciclo de vida de un defecto, desde que se detecta hasta que se resuelve y cierra.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un tipo de informe de prueba?",
        "opcion_a": "Informe de incidente de prueba.",
        "opcion_b": "Informe de resumen de prueba.",
        "opcion_c": "Informe de progreso de prueba.",
        "opcion_d": "Informe de diseño de la base de datos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Un informe de diseño de base de datos no es un artefacto del proceso de prueba.",
        "modelo_examen": "Simulacro 4"
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
        "modelo_examen": "Simulacro 4"
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
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes NO es una característica de un buen caso de prueba?",
        "opcion_a": "Claro y conciso.",
        "opcion_b": "Repetible.",
        "opcion_c": "Ambiguo.",
        "opcion_d": "Trazable.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Un buen caso de prueba debe ser claro y sin ambigüedad; la ambigüedad es justamente lo opuesto a una buena característica.",
        "modelo_examen": "Simulacro 4"
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
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes afirmaciones sobre la prueba de sistema es CORRECTA?",
        "opcion_a": "La prueba de sistema se realiza antes de la prueba de integración.",
        "opcion_b": "La prueba de sistema se centra en probar las interfaces entre los módulos.",
        "opcion_c": "La prueba de sistema evalúa el sistema completo en su entorno de destino.",
        "opcion_d": "La prueba de sistema no es necesaria si se ha realizado una prueba de integración exhaustiva.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de sistema evalúa el comportamiento del sistema completo e integrado en un entorno similar al de destino.",
        "modelo_examen": "Simulacro 4"
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
        "modelo_examen": "Simulacro 4"
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
        "modelo_examen": "Simulacro 4"
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
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de regresión?",
        "opcion_a": "Verificar que los cambios en el sistema no han afectado la funcionalidad existente.",
        "opcion_b": "Probar la integración de dos o más componentes.",
        "opcion_c": "Probar el rendimiento del sistema bajo carga.",
        "opcion_d": "Evaluar la usabilidad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba de regresión confirma que un cambio no ha afectado negativamente funcionalidad ya existente.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba beta?",
        "opcion_a": "Se realiza por usuarios reales en el entorno de producción.",
        "opcion_b": "Se realiza por testers internos en un entorno simulado.",
        "opcion_c": "Se realiza por testers externos en un entorno controlado.",
        "opcion_d": "Se realiza por desarrolladores en su propio entorno.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba beta es realizada por clientes potenciales/reales en su propio entorno de uso real, a diferencia de la alfa (interna, entorno simulado).",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre verificación y validación?",
        "opcion_a": "La verificación se centra en el producto, mientras que la validación se centra en el proceso.",
        "opcion_b": "La verificación se realiza por el equipo de desarrollo, mientras que la validación se realiza por el equipo de pruebas.",
        "opcion_c": "La verificación asegura que el producto se construye correctamente, mientras que la validación asegura que se construye el producto correcto.",
        "opcion_d": "La verificación es una técnica de prueba estática, mientras que la validación es una técnica de prueba dinámica.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Verificación = \"¿estamos construyendo el producto correctamente?\". Validación = \"¿estamos construyendo el producto correcto?\".",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un factor que influye en la selección de las herramientas de prueba?",
        "opcion_a": "El presupuesto del proyecto.",
        "opcion_b": "La complejidad del sistema.",
        "opcion_c": "Las habilidades del equipo de pruebas.",
        "opcion_d": "La ubicación geográfica del equipo de pruebas",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La ubicación geográfica del equipo no es un factor típico de selección de herramientas.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes es una técnica de diseño de pruebas de caja blanca?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Prueba de casos de uso.",
        "opcion_d": "Prueba de condición.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de condición es una técnica de caja blanca (estructural). Las demás son técnicas de caja negra.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un objetivo típico de las pruebas de rendimiento?",
        "opcion_a": "Medir el tiempo de respuesta del sistema.",
        "opcion_b": "Identificar los cuellos de botella en el sistema.",
        "opcion_c": "Verificar la funcionalidad del sistema.",
        "opcion_d": "Evaluar la escalabilidad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Verificar la funcionalidad es objetivo de la prueba funcional, no de la prueba de rendimiento.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de mantenimiento?",
        "opcion_a": "Probar nuevas funcionalidades del sistema.",
        "opcion_b": "Verificar que los cambios en el sistema no han introducido nuevos defectos.",
        "opcion_c": "Probar el rendimiento del sistema bajo carga.",
        "opcion_d": "Corregir defectos, adaptar el sistema a un nuevo entorno o mejorar el sistema después de su lanzamiento.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de mantenimiento se realiza en un sistema ya operativo, cuando se le corrigen defectos, se migra a un nuevo entorno o se mejora tras su lanzamiento.",
        "modelo_examen": "Simulacro 4"
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
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la gestión de riesgos en las pruebas?",
        "opcion_a": "Identificar y evaluar los riesgos que pueden afectar a las pruebas.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas.",
        "opcion_c": "Planificar y controlar las actividades de prueba.",
        "opcion_d": "Evaluar la calidad del software.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La gestión de riesgos identifica y evalúa los riesgos (de producto y de proyecto) para priorizar y enfocar el esfuerzo de prueba.",
        "modelo_examen": "Simulacro 4"
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
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar la facilidad con la que los usuarios pueden utilizar un sistema?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Prueba de usabilidad.",
        "opcion_c": "Prueba de seguridad.",
        "opcion_d": "Prueba de compatibilidad.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de usabilidad evalúa qué tan fácil e intuitivo es para los usuarios utilizar el sistema.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre un error y un fallo?",
        "opcion_a": "Un error es un defecto en el código, mientras que un fallo es el resultado de un error.",
        "opcion_b": "Un error es un problema reportado por el usuario, mientras que un fallo es un problema encontrado por el tester.",
        "opcion_c": "Un error es un problema menor, mientras que un fallo es un problema grave.",
        "opcion_d": "Un error es un problema en el software, mientras que un fallo es un problema en el hardware.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Un error humano puede introducir un defecto en el código, y ese defecto se manifiesta como un fallo al ejecutarse.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una responsabilidad típica del tester?",
        "opcion_a": "Diseñar casos de prueba.",
        "opcion_b": "Ejecutar casos de prueba.",
        "opcion_c": "Reportar defectos.",
        "opcion_d": "Corregir defectos.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "Corregir defectos es responsabilidad del equipo de desarrollo, no del tester.",
        "modelo_examen": "Simulacro 4"
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
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Qué técnica de prueba se centra en probar las transiciones entre diferentes estados de un sistema?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Prueba de transición de estados.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de transición de estados modela el sistema como estados y transiciones válidas/inválidas entre ellos.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un beneficio de la automatización de pruebas?",
        "opcion_a": "Mayor eficiencia de las pruebas.",
        "opcion_b": "Mayor cobertura de pruebas.",
        "opcion_c": "Eliminación de la necesidad de pruebas manuales.",
        "opcion_d": "Mayor repetibilidad de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La automatización NO elimina la necesidad de pruebas manuales (exploratorias, de usabilidad, etc.).",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de un plan de pruebas?",
        "opcion_a": "Documentar los resultados de las pruebas.",
        "opcion_b": "Gestionar los defectos encontrados durante las pruebas",
        "opcion_c": "Guiar las actividades de prueba.",
        "opcion_d": "Evaluar la calidad del software.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "El plan de pruebas documenta el enfoque, alcance, recursos y cronograma, y sirve para guiar las actividades de prueba.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar si un sistema puede manejar grandes volúmenes de datos o usuarios?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Prueba de carga.",
        "opcion_c": "Prueba de estrés.",
        "opcion_d": "Prueba de volumen.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La prueba de volumen evalúa específicamente el manejo de grandes volúmenes de datos/usuarios por parte del sistema.",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un atributo de calidad del software según la norma ISO 25010?",
        "opcion_a": "Funcionalidad.",
        "opcion_b": "Fiabilidad.",
        "opcion_c": "Usabilidad.",
        "opcion_d": "Coste.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "El coste es una restricción de proyecto/negocio, no una característica de calidad del producto según ISO 25010.",
        "modelo_examen": "Simulacro 4"
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
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Qué tipo de revisión implica una reunión formal con un equipo de revisores?",
        "opcion_a": "Revisión informal.",
        "opcion_b": "Revisión técnica.",
        "opcion_c": "Inspección.",
        "opcion_d": "Recorrido.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La inspección es el tipo de revisión más formal: proceso definido, moderador entrenado, checklists, métricas y una reunión formal de revisión.",
        "modelo_examen": "Simulacro 4"
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
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito de la prueba de compatibilidad?",
        "opcion_a": "Evaluar la facilidad con la que los usuarios pueden utilizar un sistema.",
        "opcion_b": "Probar el rendimiento del sistema bajo carga.",
        "opcion_c": "Verificar que el sistema funciona correctamente en diferentes entornos.",
        "opcion_d": "Probar la seguridad del sistema.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de compatibilidad verifica que el sistema funcione correctamente en distintos entornos (navegadores, sistemas operativos, dispositivos, etc.).",
        "modelo_examen": "Simulacro 4"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es una técnica de gestión de pruebas?",
        "opcion_a": "Planificación de pruebas.",
        "opcion_b": "Seguimiento de pruebas.",
        "opcion_c": "Prueba de integración.",
        "opcion_d": "Gestión de la configuración.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de integración es un nivel/tipo de prueba, no una técnica de gestión de pruebas.",
        "modelo_examen": "Simulacro 4"
    },
]


def main():
    with open(PREGUNTAS_PATH, "r", encoding="utf-8") as f:
        existing = json.load(f)

    print(f"Preguntas existentes antes de agregar: {len(existing)}")

    existing.extend(SIMULACRO_4)

    with open(PREGUNTAS_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"Se agregaron {len(SIMULACRO_4)} preguntas del Simulacro 4.")
    print(f"Total de preguntas ahora: {len(existing)}")


if __name__ == "__main__":
    main()
