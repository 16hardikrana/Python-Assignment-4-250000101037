from pathlib import Path
import sys

module_path = Path(__file__).with_name("marks_module.py")
module_code = (
    "def calculate(marks):\n"
    "    total = sum(marks)\n"
    "    average = total / len(marks)\n"
    "    return total, average\n"
)
module_path.write_text(module_code, encoding="utf-8")
sys.path.insert(0, str(module_path.parent))
import marks_module

marks = [88, 92, 75, 96, 81]
total, average = marks_module.calculate(marks)
print("Total marks:", total)
print("Average marks:", average)
