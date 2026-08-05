import unittest
from extract_all import split_enunciado_and_options


class TestSplitEnunciadoAndOptions(unittest.TestCase):
    def test_four_options_clean_split(self):
        items = [
            ("¿Cuál de las siguientes es una técnica de caja negra?", False),
            ("Análisis de valor límite", True),
            ("Cobertura de sentencias", True),
            ("Revisión por pares", True),
            ("Análisis estático", True),
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(enunciado, [("¿Cuál de las siguientes es una técnica de caja negra?", False)])
        self.assertEqual(options, [
            "Análisis de valor límite",
            "Cobertura de sentencias",
            "Revisión por pares",
            "Análisis estático",
        ])

    def test_five_options_supported(self):
        items = [
            ("¿Cuáles de las siguientes son actividades del proceso de pruebas?", False),
            ("Planificación", True),
            ("Análisis", True),
            ("Diseño", True),
            ("Implementación", True),
            ("Ejecución", True),
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(len(options), 5)
        self.assertEqual(options[4], "Ejecución")

    def test_enunciado_paragraph_is_not_swallowed_even_without_marker(self):
        # Caso del bug real: el enunciado no está marcado como opción (es_opcion=False),
        # así que nunca debe tratarse como si fuera la opción A, sin importar su texto.
        items = [
            ("¿Cuál de los siguientes es un objetivo típico de una prueba?", False),
            ("Validación del cumplimiento de los requisitos documentados", True),
            ("Causar fallos e identificar defectos", True),
            ("Iniciación a los errores e identificación de las causas profundas", True),
            ("Verificar que el objeto de ensayo cumple las expectativas del usuario", True),
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(len(enunciado), 1)
        self.assertIn("objetivo típico de una prueba", enunciado[0][0])
        self.assertEqual(len(options), 4)

    def test_stops_at_first_non_option_item(self):
        items = [
            ("Texto de enunciado", False),
            ("más texto de enunciado que no es una opción", False),
            ("Primera opción", True),
            ("Segunda opción", True),
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(enunciado, [("Texto de enunciado", False), ("más texto de enunciado que no es una opción", False)])
        self.assertEqual(options, ["Primera opción", "Segunda opción"])

    def test_caps_at_max_options_when_enunciado_has_embedded_numbered_list(self):
        # Caso real verificado (Examen C, pregunta 5): una lista numerada dentro del
        # propio enunciado (p.ej. pasos de un escenario) también puede llevar la marca
        # de lista. El tope de 5 evita que esos ítems se confundan con las alternativas
        # reales, que son siempre las últimas de la pregunta.
        items = [
            ("Dado el siguiente escenario:", False),
            ("Paso 1", True),
            ("Paso 2", True),
            ("Paso 3", True),
            ("¿Cuál de las siguientes opciones es correcta?", False),
            ("Opción A", True),
            ("Opción B", True),
            ("Opción C", True),
            ("Opción D", True),
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(options, ["Opción A", "Opción B", "Opción C", "Opción D"])
        self.assertEqual(len(enunciado), 5)


if __name__ == "__main__":
    unittest.main()
