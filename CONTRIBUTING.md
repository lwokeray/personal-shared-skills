# Contributing

新增或補全技能時，請保持 `SKILL.md` 的 frontmatter 僅包含 `name` 與 `description`，並讓 description 同時說明技能用途與觸發時機。

完整技能應把核心流程放在 `SKILL.md`，把變體、schema、範例與長篇資料放在一層深度的 `references/`；重複性或脆弱操作才應放入可測試的 `scripts/`。不要複製未授權的系統提示、私有工作區內容或第三方原文。

提交前請執行 `python scripts/validate_skills.py`，並在 `catalog/skills.json` 更新條目的 `status`、`source` 與 `description`。
