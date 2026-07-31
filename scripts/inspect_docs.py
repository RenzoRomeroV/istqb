import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"c:\Users\Admin\Desktop\Proyect-ISTQ\simulador-istq\src\app\preguntas.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Total questions: {len(questions)}")
count = 0
for q in questions:
    if "exhaustiv" in q["enunciado"].lower() or "exhaustiv" in q["opcion_a"].lower() or "exhaustiv" in q["opcion_b"].lower() or "exhaustiv" in q["opcion_c"].lower() or "exhaustiv" in q["opcion_d"].lower():
        print(f"[{q['modelo_examen']}] {q['enunciado']}")
        count += 1
print(f"Found {count} questions about exhaustivas.")
