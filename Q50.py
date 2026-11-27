from pathlib import Path
import sys

base = Path(__file__).parent
package_dir = base / "simplepackage"
package_dir.mkdir(exist_ok=True)
(package_dir / "__init__.py").write_text("", encoding="utf-8")
(package_dir / "operations.py").write_text(
    "def add(a, b):\n    return a + b\n\ndef multiply(a, b):\n    return a * b\n",
    encoding="utf-8"
)
(package_dir / "messages.py").write_text(
    "def welcome(name):\n    return 'Welcome, ' + name + '!'\n",
    encoding="utf-8"
)
sys.path.insert(0, str(base))
from simplepackage.operations import add, multiply
from simplepackage.messages import welcome

print("Addition from package:", add(12, 8))
print("Multiplication from package:", multiply(6, 7))
print("Message from package:", welcome("Hardik"))
