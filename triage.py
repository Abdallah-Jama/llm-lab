from pathlib import Path

COMPLAINTS_FOLDER = Path("complaints")

for file in sorted(COMPLAINTS_FOLDER.glob("*.txt"), key=lambda f: f.name.lower()):
    content = file.read_text(encoding="utf-8")
    print("File:", file.name)
    print(content)
    print("-" * 40)