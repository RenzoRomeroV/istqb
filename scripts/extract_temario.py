import sys
sys.stdout.reconfigure(encoding="utf-8")

import json
import os
import re

import pypdf

MATERIAL_DIR = r"c:\Users\Admin\Desktop\Proyect-ISTQ\ISTQB\Material de estudio"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "temario_chunks.json")

FUENTES = [
    ("1. Silabo.pdf", "Sílabo"),
    ("3. Capítulo I_ Fundamentos de la Prueba.pdf", "Capítulo I - Fundamentos de la Prueba"),
    ("4. Capítulo II_ Prueba a lo Largo del Ciclo de Vida de Desarrollo de Software.pdf", "Capítulo II - Prueba a lo Largo del Ciclo de Vida de Desarrollo de Software"),
    ("5. Capítulo III_ Pruebas Estáticas.pdf", "Capítulo III - Pruebas Estáticas"),
    ("6. Capítulo IV_ Análisis y Diseño de Pruebas.pdf", "Capítulo IV - Análisis y Diseño de Pruebas"),
    ("7. Capítulo V_ Gestión de las actividades de Prueba.pdf", "Capítulo V - Gestión de las actividades de Prueba"),
    ("8. Capítulo VI_ Herramientas de Prueba.pdf", "Capítulo VI - Herramientas de Prueba"),
]

# Ruido repetido en cada página del PDF (encabezado/pie institucional), sin valor para el contexto
BOILERPLATE_RE = re.compile(
    r"Probador\s*\n?\s*Certificado\.?\s*\n?\s*Nivel\s+básico\s*\n?\s*v4\s*\n?\s*Página\s+\d+\s+de\s*\n?\s*\d+\s*\n?\s*\d{4}-\d{2}-\d{2}\s*\n?\s*Comité\s+Internacional\s+de\s+Cualificación\s+de\s+Pruebas\s+de\s*\n?\s*Software",
    re.IGNORECASE
)

CHUNK_TARGET_SIZE = 1400


def strip_control_chars(text):
    # Postgres no acepta el byte NUL (\x00) en columnas de texto, y otros caracteres
    # de control son artefactos de extracción sin valor semántico. Se conservan \n y \t.
    return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)


def extract_clean_text(path):
    reader = pypdf.PdfReader(path)
    pages_text = []
    for page in reader.pages:
        raw = page.extract_text() or ""
        cleaned = strip_control_chars(raw)
        cleaned = BOILERPLATE_RE.sub("", cleaned)
        cleaned = re.sub(r"\n{2,}", "\n\n", cleaned).strip()
        if cleaned:
            pages_text.append(cleaned)
    return "\n\n".join(pages_text)


def split_into_chunks(text, target_size=CHUNK_TARGET_SIZE):
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    current = ""
    for para in paragraphs:
        if current and len(current) + len(para) + 2 > target_size:
            chunks.append(current.strip())
            current = para
        else:
            current = f"{current}\n\n{para}" if current else para
    if current.strip():
        chunks.append(current.strip())
    return chunks


def main():
    all_chunks = []

    for filename, fuente_label in FUENTES:
        path = os.path.join(MATERIAL_DIR, filename)
        if not os.path.exists(path):
            print(f"ADVERTENCIA: no se encontró {filename}, se omite.")
            continue

        text = extract_clean_text(path)
        if not text.strip():
            print(f"ADVERTENCIA: {filename} no tiene texto extraíble (¿PDF escaneado?), se omite.")
            continue

        chunks = split_into_chunks(text)
        for idx, chunk in enumerate(chunks):
            all_chunks.append({
                "fuente": fuente_label,
                "orden": idx,
                "contenido": chunk
            })

        print(f"{filename}: {len(chunks)} fragmentos extraídos.")

    if not all_chunks:
        print("No se extrajo ningún fragmento. Abortando sin escribir el archivo de salida.")
        sys.exit(1)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    print(f"Se guardaron {len(all_chunks)} fragmentos en {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
