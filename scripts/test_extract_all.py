import unittest
from extract_all import split_enunciado_and_options


class TestSplitEnunciadoAndOptions(unittest.TestCase):
    def test_four_options_clean_split(self):
        items = [
            "¿Cuál de las siguientes es una técnica de caja negra?",
            "a) Análisis de valor límite",
            "b) Cobertura de sentencias",
            "c) Revisión por pares",
            "d) Análisis estático",
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(enunciado, ["¿Cuál de las siguientes es una técnica de caja negra?"])
        self.assertEqual(options, [
            "Análisis de valor límite",
            "Cobertura de sentencias",
            "Revisión por pares",
            "Análisis estático",
        ])

    def test_five_options_supported(self):
        items = [
            "¿Cuáles de las siguientes son actividades del proceso de pruebas?",
            "a) Planificación",
            "b) Análisis",
            "c) Diseño",
            "d) Implementación",
            "e) Ejecución",
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(len(options), 5)
        self.assertEqual(options[4], "Ejecución")

    def test_enunciado_paragraph_without_marker_is_not_swallowed(self):
        # Caso del bug real: el enunciado no tiene marcador de letra,
        # no debe tratarse como si fuera la opción A.
        items = [
            "¿Cuál de los siguientes es un objetivo típico de una prueba?",
            "a) Validación del cumplimiento de los requisitos documentados",
            "b) Causar fallos e identificar defectos",
            "c) Iniciación a los errores e identificación de las causas profundas",
            "d) Verificar que el objeto de ensayo cumple las expectativas del usuario",
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(len(enunciado), 1)
        self.assertIn("objetivo típico de una prueba", enunciado[0])
        self.assertEqual(len(options), 4)

    def test_stops_at_first_non_matching_line(self):
        items = [
            "Texto de enunciado",
            "más texto de enunciado que no es una opción",
            "a) Primera opción",
            "b) Segunda opción",
        ]
        enunciado, options = split_enunciado_and_options(items)
        self.assertEqual(enunciado, ["Texto de enunciado", "más texto de enunciado que no es una opción"])
        self.assertEqual(options, ["Primera opción", "Segunda opción"])


if __name__ == "__main__":
    unittest.main()
