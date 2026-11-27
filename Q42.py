from pathlib import Path
import sys

module_path = Path(__file__).with_name("calc_module.py")
module_code = (
    "def add(a, b):\n"
    "    return a + b\n"
    "\n"
    "def subtract(a, b):\n"
    "    return a - b\n"
    "\n"
    "def multiply(a, b):\n"
    "    return a * b\n"
    "\n"
    "def divide(a, b):\n"
    "    return a / b\n"
)
module_path.write_text(module_code, encoding="utf-8")
sys.path.insert(0, str(module_path.parent))
import calc_module

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", calc_module.add(a, b))
print("Subtraction:", calc_module.subtract(a, b))
print("Multiplication:", calc_module.multiply(a, b))
print("Division:", calc_module.divide(a, b))
