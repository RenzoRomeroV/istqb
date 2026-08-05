import docx
import pypdf
import re
import json
import sys
import os
from docx.document import Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import Table
from docx.text.paragraph import Paragraph

sys.stdout.reconfigure(encoding='utf-8')

def iter_block_items(parent):
    if isinstance(parent, Document):
        parent_elm = parent.element.body
    elif isinstance(parent, docx.table._Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("Unsupported parent type")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

def format_table_as_text(table):
    lines = []
    for r_idx, row in enumerate(table.rows):
        cells_txt = [cell.text.strip().replace("\n", " ") for cell in row.cells]
        unique_cells = []
        for c in cells_txt:
            if not unique_cells or unique_cells[-1] != c:
                unique_cells.append(c)
        lines.append(" | ".join(unique_cells))
    return "\n".join(lines)

NUMPR_TAG = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}numPr'
SELECTOR_PHRASE_RE = re.compile(r'\s*Seleccione\s+(?:UNA|DOS)\s+opci(?:ó|o)n(?:es)?\.?\s*$', re.IGNORECASE)


def is_option_paragraph(paragraph):
    """Word marca las alternativas a), b), c)... con numeración automática de listas
    (elemento numPr en el XML del párrafo) en vez de escribir la letra como texto
    literal — .text nunca contiene la letra. Esta es la señal confiable para
    distinguir una alternativa del enunciado."""
    return paragraph._p.find('.//' + NUMPR_TAG) is not None


def parse_docx_questions(path):
    doc = docx.Document(path)
    questions = []
    current_q = None
    q_start_re = re.compile(r'^Pregunta\s+(?:nº|no\.|nro\.?)\s*(\d+)', re.IGNORECASE)
    accumulated_items = []

    for item in iter_block_items(doc):
        if isinstance(item, Paragraph):
            text = item.text.strip()
            if not text:
                continue
            match = q_start_re.match(text)
            if match:
                if current_q:
                    process_question(current_q, accumulated_items, questions)
                    accumulated_items = []
                current_q = {
                    "num": match.group(1),
                    "enunciado": "",
                    "opciones": []
                }
            elif current_q:
                clean_text = SELECTOR_PHRASE_RE.sub('', text).strip()
                if clean_text:
                    accumulated_items.append((clean_text, is_option_paragraph(item)))
        elif isinstance(item, Table) and current_q:
            accumulated_items.append(item)

    if current_q:
        process_question(current_q, accumulated_items, questions)

    return questions

MAX_OPTIONS = 5  # ISTQB Foundation nunca ofrece más de 5 alternativas (A-E)


def split_enunciado_and_options(items):
    """Escanea `items` (tuplas (texto, es_opcion), u otros tipos como Table que
    cortan el escaneo igual que es_opcion=False) desde el final hacia el principio,
    tomando como opción cada ítem marcado como es_opcion=True. Se detiene en cuanto
    encuentra un ítem que no lo es, o al alcanzar MAX_OPTIONS — esto evita que listas
    numeradas dentro del propio enunciado (p.ej. los pasos de un escenario) se cuelen
    como si fueran alternativas de respuesta, ya que las alternativas reales son
    siempre las últimas del bloque. Devuelve (enunciado_items, options) con options
    ya como texto plano."""
    remaining = list(items)
    opt_candidates = []
    while remaining and len(opt_candidates) < MAX_OPTIONS:
        curr = remaining[-1]
        if not (isinstance(curr, tuple) and curr[1]):
            break
        opt_candidates.insert(0, curr[0])
        remaining.pop()
    return remaining, opt_candidates

def process_question(q, items, questions_list):
    if not items:
        return

    options = []
    enunciado_parts = []

    if items and isinstance(items[-1], Table):
        opt_table = items.pop()
        for row in opt_table.rows:
            row_text = " ".join([cell.text.strip() for cell in row.cells])
            clean_opt = re.sub(r'^[a-e]\)\s*', '', row_text, flags=re.IGNORECASE).strip()
            options.append(clean_opt)
    else:
        items, options = split_enunciado_and_options(items)

    for item in items:
        if isinstance(item, tuple):
            enunciado_parts.append(item[0])
        elif isinstance(item, Table):
            enunciado_parts.append(format_table_as_text(item))

    q["enunciado"] = "\n".join(enunciado_parts)
    q["opciones"] = options
    questions_list.append(q)

def validate_questions(compiled_questions):
    errors = []
    opt_fields = {"A": "opcion_a", "B": "opcion_b", "C": "opcion_c", "D": "opcion_d", "E": "opcion_e"}

    for q in compiled_questions:
        label = f"Examen {q.get('modelo_examen', '?')} - {q.get('enunciado', '')[:50]!r}"

        if not q.get("enunciado") or len(q["enunciado"].strip()) < 10:
            errors.append(f"{label}: enunciado vacío o demasiado corto")

        if not q.get("respuesta_correcta", "").strip():
            errors.append(f"{label}: respuesta_correcta está vacío")

        respuestas = [r.strip().upper() for r in q.get("respuesta_correcta", "").split(",") if r.strip()]
        for letra in respuestas:
            field = opt_fields.get(letra)
            if field is None or not q.get(field):
                errors.append(f"{label}: respuesta_correcta incluye '{letra}' pero {field or 'esa letra'} está vacío")

        num_opciones = sum(1 for f in ("opcion_a", "opcion_b", "opcion_c", "opcion_d", "opcion_e") if q.get(f))
        if num_opciones < 4:
            errors.append(f"{label}: solo se capturaron {num_opciones} opciones (se esperaban al menos 4)")

    return errors

def parse_pdf_answers(path):
    reader = pypdf.PdfReader(path)
    grid_page_idx = -1
    for idx, page in enumerate(reader.pages):
        text = page.extract_text()
        if "LO" in text and "Nivel" in text and "Puntos" in text:
            grid_page_idx = idx
            break
            
    if grid_page_idx == -1:
        return {}, {}
        
    grid_text = reader.pages[grid_page_idx].extract_text()
    answers = {}
    
    grid_re = re.compile(
        r'(\d+)\s+([a-e](?:,\s*[a-e])*)\s+FL-\S+\s+K\d\s+\d+\s+(\d+)\s+([a-e](?:,\s*[a-e])*)\s+FL-\S+\s+K\d\s+\d+'
    )
    for line in grid_text.split('\n'):
        match = grid_re.search(line)
        if match:
            q1, ans1, q2, ans2 = match.groups()
            answers[q1] = ans1.upper().replace(" ", "")
            answers[q2] = ans2.upper().replace(" ", "")
            
    full_text = ""
    for i in range(grid_page_idx + 1, len(reader.pages)):
        full_text += "\n" + reader.pages[i].extract_text()
        
    explanations = {}
    
    for q_num in range(1, 41):
        num_str = str(q_num)
        ans_str = answers.get(num_str, "").lower()
        
        ans_list = [char for char in ans_str if char.isalpha()]
        ans_pattern = r"[\s,]*".join(ans_list)
        
        start_pattern = rf"\n{num_str}\s+{ans_pattern}\s+"
        
        next_num_str = str(q_num + 1)
        next_ans_str = answers.get(next_num_str, "").lower()
        if next_ans_str:
            next_ans_list = [char for char in next_ans_str if char.isalpha()]
            next_ans_pattern = r"[\s,]*".join(next_ans_list)
            end_pattern = rf"\n{next_num_str}\s+{next_ans_pattern}\s+"
        else:
            end_pattern = r"$"
            
        start_match = re.search(start_pattern, full_text)
        if start_match:
            start_idx = start_match.end()
            end_match = re.search(end_pattern, full_text[start_idx:])
            if end_match:
                end_idx = start_idx + end_match.start()
            else:
                end_idx = len(full_text)
                
            explanation = full_text[start_idx:end_idx].strip()
            lines = explanation.split('\n')
            cleaned_lines = []
            for line in lines:
                l_lower = line.lower()
                if "certified tester" in l_lower or "modelo de examen" in l_lower or "ejemplo de examen" in l_lower or "consejo internacional" in l_lower or "software" in l_lower or "página" in l_lower:
                    continue
                if line.strip().isdigit() and (line.strip() == "2024" or line.strip() == "2023"):
                    continue
                cleaned_lines.append(line.strip())
                
            explanations[num_str] = " ".join(cleaned_lines).strip()
            
    return answers, explanations

def main():
    simulacros_dir = r"c:\Users\Admin\Desktop\Proyect-ISTQ\ISTQB\Simulacros\Simulacros\1. Simuladores tipo examen de certificación"
    
    compiled_questions = []
    
    # 1. Parse Exam C
    questions_c = parse_docx_questions(os.path.join(simulacros_dir, "2. Preguntas - C.docx"))
    answers_c, explanations_c = parse_pdf_answers(os.path.join(simulacros_dir, "2.1 Respuestas - C.pdf"))
    
    print(f"Exam C: Parsed {len(questions_c)} questions, {len(answers_c)} answers, {len(explanations_c)} explanations")
    for q in questions_c:
        num = q["num"]
        if len(q["opciones"]) >= 4:
            compiled_questions.append({
                "enunciado": q["enunciado"],
                "opcion_a": q["opciones"][0],
                "opcion_b": q["opciones"][1],
                "opcion_c": q["opciones"][2],
                "opcion_d": q["opciones"][3],
                "opcion_e": q["opciones"][4] if len(q["opciones"]) >= 5 else None,
                "respuesta_correcta": answers_c.get(num, ""),
                "explicacion": explanations_c.get(num, ""),
                "modelo_examen": "C"
            })
        else:
            print(f"ADVERTENCIA: Examen C Pregunta {num} descartada, solo se detectaron {len(q['opciones'])} opciones")

    # 2. Parse Exam D
    questions_d = parse_docx_questions(os.path.join(simulacros_dir, "3. Preguntas - D.docx"))
    answers_d, explanations_d = parse_pdf_answers(os.path.join(simulacros_dir, "3.1 Respuestas - D.pdf"))
    
    print(f"Exam D: Parsed {len(questions_d)} questions, {len(answers_d)} answers, {len(explanations_d)} explanations")
    for q in questions_d:
        num = q["num"]
        if len(q["opciones"]) >= 4:
            compiled_questions.append({
                "enunciado": q["enunciado"],
                "opcion_a": q["opciones"][0],
                "opcion_b": q["opciones"][1],
                "opcion_c": q["opciones"][2],
                "opcion_d": q["opciones"][3],
                "opcion_e": q["opciones"][4] if len(q["opciones"]) >= 5 else None,
                "respuesta_correcta": answers_d.get(num, ""),
                "explicacion": explanations_d.get(num, ""),
                "modelo_examen": "D"
            })
        else:
            print(f"ADVERTENCIA: Examen D Pregunta {num} descartada, solo se detectaron {len(q['opciones'])} opciones")

    # Guarda agregada de seguridad: hoy se pierde 1 pregunta conocida (Examen D,
    # pregunta 29, advertencia intencional). Si un cambio en la detección de
    # opciones (p.ej. is_option_paragraph dejara de matchear) hiciera que se
    # descarten muchas más preguntas de las esperadas, abortamos ruidosamente en
    # vez de escribir un preguntas.json vacío o casi vacío con exit code 0 (que
    # db-upload.js subiría igual, vaciando la producción).
    total_parsed = len(questions_c) + len(questions_d)
    min_expected_compiled = total_parsed - 2
    if len(compiled_questions) < min_expected_compiled:
        print(
            f"\nERROR: se compilaron solo {len(compiled_questions)} preguntas de "
            f"{total_parsed} parseadas (se esperaba perder a lo sumo 2, hoy se "
            f"pierde 1 conocida). Esto indica un fallo catastrófico en la "
            f"detección de opciones. No se escribirá preguntas.json."
        )
        sys.exit(1)

    validation_errors = validate_questions(compiled_questions)
    if validation_errors:
        print(f"\nSe encontraron {len(validation_errors)} problema(s) de validación. No se escribirá preguntas.json:")
        for err in validation_errors:
            print(f"  - {err}")
        sys.exit(1)

    # Output to preguntas.json
    output_path = r"c:\Users\Admin\Desktop\Proyect-ISTQ\simulador-istq\src\app\preguntas.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(compiled_questions, f, ensure_ascii=False, indent=2)

    print(f"Successfully compiled and saved {len(compiled_questions)} questions to {output_path}")

if __name__ == "__main__":
    main()
