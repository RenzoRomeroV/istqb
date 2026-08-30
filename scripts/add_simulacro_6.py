# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")

import json
import os

PREGUNTAS_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "app", "preguntas.json")

SIMULACRO_6 = [
    {
        "enunciado": "¿Cuál de las siguientes NO es una de las siete pruebas de principios de software?",
        "opcion_a": "Las pruebas exhaustivas son imposibles.",
        "opcion_b": "Las pruebas deben comenzar lo antes posible en el ciclo de vida del software.",
        "opcion_c": "Las pruebas demuestran que el software está libre de defectos.",
        "opcion_d": "Las pruebas dependen del contexto.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Las pruebas muestran la PRESENCIA de defectos, nunca pueden demostrar que el software esté completamente libre de ellos (uno de los 7 principios).",
        "modelo_examen": "Simulacro 6"
    },
    {
        "enunciado": "¿Cuál de las siguientes NO es una tarea principal del proceso de prueba?",
        "opcion_a": "Planificación de las pruebas.",
        "opcion_b": "Diseño de las pruebas.",
        "opcion_c": "Implementación del código.",
        "opcion_d": "Ejecución de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "Implementar el código es una actividad de DESARROLLO, no del proceso de prueba.",
        "modelo_examen": "Simulacro 6"
    },
    {
        "enunciado": "¿Qué nivel de pruebas se centra en probar las unidades individuales de código?",
        "opcion_a": "Prueba de unidad.",
        "opcion_b": "Prueba de integración.",
        "opcion_c": "Prueba de sistema.",
        "opcion_d": "Prueba de aceptación.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La prueba de unidad (componentes) verifica de forma aislada las unidades individuales de código.",
        "modelo_examen": "Simulacro 6"
    },
    {
        "enunciado": "¿Cuál de las siguientes es una técnica de prueba dinámica?",
        "opcion_a": "Revisión de código.",
        "opcion_b": "Inspección.",
        "opcion_c": "Prueba de caja negra.",
        "opcion_d": "Análisis estático.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de caja negra requiere ejecutar el software (dinámica). Las demás son técnicas estáticas.",
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el concepto de \"probabilidad\" de un defecto?",
        "opcion_a": "La frecuencia con la que se espera que ocurra un defecto.",
        "opcion_b": "El impacto del defecto en el funcionamiento del sistema.",
        "opcion_c": "La combinación de la probabilidad de un fallo y la gravedad de su impacto.",
        "opcion_d": "La dificultad de encontrar un defecto.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "La probabilidad indica la frecuencia con la que se espera que ocurra un defecto, a diferencia de la gravedad (impacto) o el riesgo (combinación de ambas).",
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
    },
    {
        "enunciado": "¿Cuál de las siguientes afirmaciones sobre la prueba de sistema es CORRECTA?",
        "opcion_a": "La prueba de sistema se realiza antes de la prueba de integración.",
        "opcion_b": "La prueba de sistema se centra en probar las interfaces entre los módulos.",
        "opcion_c": "La prueba de sistema se realiza en el entorno de producción.",
        "opcion_d": "La prueba de sistema no es necesaria si se ha realizado una prueba de integración exhaustiva.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba de sistema evalúa el sistema completo e integrado en un entorno similar al de producción.",
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor el propósito del control de las pruebas?",
        "opcion_a": "Controlar el progreso de las pruebas en relación con el plan.",
        "opcion_b": "Tomar acciones correctivas cuando las pruebas se desvían del plan.",
        "opcion_c": "Evaluar la calidad del software.",
        "opcion_d": "Automatizar la ejecución de las pruebas.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "El control de pruebas toma acciones correctivas cuando el progreso real se desvía de lo planificado (distinto del seguimiento, que solo monitorea).",
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones describe mejor la diferencia entre pruebas funcionales y no funcionales?",
        "opcion_a": "Las pruebas funcionales se centran en lo que el sistema debe hacer, mientras que las pruebas no funcionales se centran en cómo lo hace.",
        "opcion_b": "Las pruebas funcionales se realizan por el equipo de desarrollo, mientras que las pruebas no funcionales se realizan por el equipo de pruebas.",
        "opcion_c": "Las pruebas funcionales son más importantes que las pruebas no funcionales.",
        "opcion_d": "Las pruebas funcionales se realizan al principio del ciclo de vida del desarrollo, mientras que las pruebas no funcionales se realizan al final.",
        "opcion_e": None,
        "respuesta_correcta": "A",
        "explicacion": "Las pruebas funcionales evalúan QUÉ hace el sistema; las no funcionales evalúan CÓMO lo hace (rendimiento, seguridad, usabilidad, etc.).",
        "modelo_examen": "Simulacro 6"
    },
    {
        "enunciado": "¿Cuál de las siguientes opciones NO es un factor que influye en la priorización de las pruebas?",
        "opcion_a": "El riesgo asociado con la funcionalidad.",
        "opcion_b": "La complejidad de la funcionalidad.",
        "opcion_c": "La disponibilidad de las herramientas de prueba.",
        "opcion_d": "La importancia de la funcionalidad para el usuario.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La disponibilidad de herramientas no es un factor de priorización de pruebas; sí lo son el riesgo, la complejidad y la importancia para el usuario.",
        "modelo_examen": "Simulacro 6"
    },
    {
        "enunciado": "¿Cuál de las siguientes es una técnica de diseño de pruebas de caja negra?",
        "opcion_a": "Prueba de condición.",
        "opcion_b": "Prueba de caminos básicos.",
        "opcion_c": "Prueba de bucle.",
        "opcion_d": "Prueba de tabla de decisión.",
        "opcion_e": None,
        "respuesta_correcta": "D",
        "explicacion": "La tabla de decisión es una técnica de caja negra. Las demás son técnicas de caja blanca.",
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
    },
    {
        "enunciado": "¿Qué tipo de prueba se centra en evaluar si un sistema cumple con los estándares y regulaciones?",
        "opcion_a": "Prueba de rendimiento.",
        "opcion_b": "Prueba de cumplimiento.",
        "opcion_c": "Prueba de seguridad.",
        "opcion_d": "Prueba de compatibilidad.",
        "opcion_e": None,
        "respuesta_correcta": "B",
        "explicacion": "La prueba de cumplimiento (compliance testing) evalúa si el sistema cumple con estándares y regulaciones aplicables.",
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
    },
    {
        "enunciado": "¿Qué técnica de prueba se centra en probar las respuestas del sistema a entradas inválidas o inesperadas?",
        "opcion_a": "Prueba de partición de equivalencia.",
        "opcion_b": "Prueba de tabla de decisión.",
        "opcion_c": "Prueba negativa.",
        "opcion_d": "Prueba de casos de uso.",
        "opcion_e": None,
        "respuesta_correcta": "C",
        "explicacion": "La prueba negativa evalúa cómo responde el sistema ante entradas inválidas o inesperadas.",
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
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
        "modelo_examen": "Simulacro 6"
    },
]


def main():
    with open(PREGUNTAS_PATH, "r", encoding="utf-8") as f:
        existing = json.load(f)

    print(f"Preguntas existentes antes de agregar: {len(existing)}")

    existing.extend(SIMULACRO_6)

    with open(PREGUNTAS_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"Se agregaron {len(SIMULACRO_6)} preguntas del Simulacro 6.")
    print(f"Total de preguntas ahora: {len(existing)}")


if __name__ == "__main__":
    main()
