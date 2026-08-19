from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
errors = []
for path in sorted(SKILLS.glob("*/SKILL.md")):
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing frontmatter start")
        continue
    match = re.match(r"^---\nname: ([^\n]+)\ndescription: (.+)\n---\n", text)
    if not match:
        errors.append(f"{path}: invalid frontmatter")
        continue
    if not match.group(1).strip() or not match.group(2).strip():
        errors.append(f"{path}: empty name or description")
    if len(text.splitlines()) >= 500:
        errors.append(f"{path}: SKILL.md must stay under 500 lines")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"validated {len(list(SKILLS.glob('*/SKILL.md')))} skills")
