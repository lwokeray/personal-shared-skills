# Contributing

新增技能時，請確認它是個人／自建內容，不要把官方、內建或第三方系統技能複製進來。`SKILL.md` 必須提供 `name` 與繁體中文 `description`，並說明用途與觸發時機。

完整 skill 可在 `SKILL.md` 放入核心流程，將變體、schema、範例與長篇資料放到一層深度的 `references/`；需要時再加入可測試的 `scripts/` 或 `templates/`。

提交前執行 `python scripts/validate_skills.py`，並檢查 diff 是否含有秘密資料或非個人來源。
