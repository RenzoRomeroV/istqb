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
                accumulated_items.append(text)
        elif isinstance(item, Table) and current_q:
            accumulated_items.append(item)
            
    if current_q:
        process_question(current_q, accumulated_items, questions)

    return questions

OPTION_MARKER_RE = re.compile(r'^([a-e])\)\s*', re.IGNORECASE)


def split_enunciado_and_options(items):
    """Escanea `items` desde el final hacia el principio, tomando como opción cada
    línea de texto que empieza con un marcador de letra (a) a e)). Se detiene en
    cuanto encuentra un ítem que no matchea (o que no es texto) — ese ítem y todos
    los anteriores quedan como parte del enunciado. Devuelve (enunciado_items, options)."""
    remaining = list(items)
    opt_candidates = []
    while remaining:
        curr = remaining[-1]
        if not isinstance(curr, str):
            break
        match = OPTION_MARKER_RE.match(curr.strip())
        if not match:
            break
        clean_opt = OPTION_MARKER_RE.sub('', curr.strip(), count=1).strip()
        opt_candidates.insert(0, clean_opt)
        remaining.pop()
    return remaining, opt_candidates

def process_question(q, items, questions_list):
    if not items:
        return
    last_item = items[-1]
    has_selector_last = isinstance(last_item, str) and ("seleccione" in last_item.lower() and "opci" in last_item.lower())
    if has_selector_last:
        items.pop()
        
    options = []
    enunciado_parts = []
    
    if items and isinstance(items[-1], Table):
        opt_table = items.pop()
        for row in opt_table.rows:
            row_text = " ".join([cell.text.strip() for cell in row.cells])
            clean_opt = re.sub(r'^[a-d]\)\s*', '', row_text, flags=re.IGNORECASE).strip()
            options.append(clean_opt)
    else:
        if items and isinstance(items[-1], str):
            last_p = items[-1]
            clean_last = re.sub(r'\s*Seleccione\s+(?:UNA|DOS)\s+opci(?:ó|o)nes?\.?$', '', last_p, flags=re.IGNORECASE).strip()
            items[-1] = clean_last
            
        text_count = 0
        opt_candidates = []
        idx = len(items) - 1
        while idx >= 0 and text_count < 4:
            curr = items[idx]
            if isinstance(curr, str):
                clean_opt = re.sub(r'^[a-d]\)\s*', '', curr, flags=re.IGNORECASE).strip()
                opt_candidates.insert(0, clean_opt)
                text_count += 1
                items.pop(idx)
            idx -= 1
        options = opt_candidates

    for item in items:
        if isinstance(item, str):
            enunciado_parts.append(item)
        elif isinstance(item, Table):
            enunciado_parts.append(format_table_as_text(item))
            
    q["enunciado"] = "\n".join(enunciado_parts)
    q["opciones"] = options
    questions_list.append(q)

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
        if len(q["opciones"]) == 4:
            compiled_questions.append({
                "enunciado": q["enunciado"],
                "opcion_a": q["opciones"][0],
                "opcion_b": q["opciones"][1],
                "opcion_c": q["opciones"][2],
                "opcion_d": q["opciones"][3],
                "respuesta_correcta": answers_c.get(num, ""),
                "explicacion": explanations_c.get(num, ""),
                "modelo_examen": "C"
            })
            
    # 2. Parse Exam D
    questions_d = parse_docx_questions(os.path.join(simulacros_dir, "3. Preguntas - D.docx"))
    answers_d, explanations_d = parse_pdf_answers(os.path.join(simulacros_dir, "3.1 Respuestas - D.pdf"))
    
    print(f"Exam D: Parsed {len(questions_d)} questions, {len(answers_d)} answers, {len(explanations_d)} explanations")
    for q in questions_d:
        num = q["num"]
        if len(q["opciones"]) == 4:
            compiled_questions.append({
                "enunciado": q["enunciado"],
                "opcion_a": q["opciones"][0],
                "opcion_b": q["opciones"][1],
                "opcion_c": q["opciones"][2],
                "opcion_d": q["opciones"][3],
                "respuesta_correcta": answers_d.get(num, ""),
                "explicacion": explanations_d.get(num, ""),
                "modelo_examen": "D"
            })
            
    # Output to preguntas.json
    output_path = r"c:\Users\Admin\Desktop\Proyect-ISTQ\simulador-istq\src\app\preguntas.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(compiled_questions, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully compiled and saved {len(compiled_questions)} questions to {output_path}")

if __name__ == "__main__":
    main()
