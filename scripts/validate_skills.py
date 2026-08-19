from pathlib import Path
import json
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
errors = []
catalog = json.loads((ROOT / "catalog" / "skills.json").read_text(encoding="utf-8"))
skill_files = sorted(ROOT / record["path"] for record in catalog["records"] if record.get("path") and record.get("status") != "internal-reference")

for path in skill_files:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        errors.append(f"{path}: invalid or missing frontmatter")
        continue
    end = text.find("\n---", 4)
    if end == -1:
        errors.append(f"{path}: unterminated frontmatter")
        continue
    frontmatter = text[4:end]
    name_match = re.search(r"^name:\s*(.+)$", frontmatter, flags=re.M)
    description_match = re.search(r"^description:\s*(.+)$", frontmatter, flags=re.M)
    if not name_match or not description_match or not name_match.group(1).strip() or not description_match.group(1).strip():
        errors.append(f"{path}: missing name or description in frontmatter")
    if path.parts[-3:-2] == ("personal-metadata",) and len(text.splitlines()) >= 500:
        errors.append(f"{path}: metadata-only SKILL.md must stay under 500 lines")
for package in sorted((ROOT / "skills").rglob("package.skill")):
    try:
        with zipfile.ZipFile(package) as archive:
            bad = archive.testzip()
            if bad:
                errors.append(f"{package}: corrupt member {bad}")
    except zipfile.BadZipFile:
        errors.append(f"{package}: invalid zip archive")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"validated {len(skill_files)} catalogued SKILL.md files and {len(list((ROOT / 'skills').rglob('package.skill')))} package archives")
