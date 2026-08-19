from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / "catalog" / "skills.json").read_text(encoding="utf-8"))
errors = []
records = catalog["skills"]
for record in records:
    path = ROOT / record["path"]
    if not path.exists():
        errors.append(f"missing: {path}")
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n") or "\ndescription:" not in text:
        errors.append(f"invalid frontmatter: {path}")
    if not re.search(r"[\u4e00-\u9fff]", record.get("description_zh_tw", "")):
        errors.append(f"description is not Traditional Chinese: {path}")
    if record.get("status") != "recovered-metadata-only":
        errors.append(f"unexpected status: {path}")
if len(records) != 164:
    errors.append(f"expected 164 personal skills, found {len(records)}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"validated {len(records)} personal skills and Traditional Chinese descriptions")
