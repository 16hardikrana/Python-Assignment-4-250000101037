from pathlib import Path
import sys

module_path = Path(__file__).with_name("square_module.py")
module_path.write_text("def square(number):\n    return number * number\n", encoding="utf-8")
sys.path.insert(0, str(module_path.parent))
import square_module

number = float(input("Enter a number: "))
print("Square using imported module:", square_module.square(number))
