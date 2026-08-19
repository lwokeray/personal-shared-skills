# Contributing

新增技能時，請保留可追溯的來源路徑、名稱與授權資訊。完整技能的入口應為 `SKILL.md`，並以 frontmatter 提供 `name` 與 `description`。

若技能支援多個 framework 或 runtime，請用目錄命名空間保留變體，不要以同名檔案互相覆蓋。長篇內容應透過一層深度的 `references/` 漸進載入；重複性操作才放入可測試的 `scripts/`。

提交前請執行：

```bash
python scripts/validate_skills.py
```

同時請檢查 git diff 是否包含秘密資料、未授權第三方內容或不必要的本機路徑。
