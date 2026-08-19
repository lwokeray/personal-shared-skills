# Personal Shared Skills

這個 repository 將本機個人技能索引整理成可公開瀏覽、複製與逐項擴充的共享技能集合。它目前包含 **16 個分類**與 **186 個技能入口**。

## 重要狀態說明

目前保留的個人技能檔案是從本機 inventory 恢復出的觸發描述；原始 atomic skill body 並未完整存在。因此，本次公開版本採取誠實的 **metadata-only reconstruction**：每個條目都具備標準 YAML frontmatter 與可觸發的 description，但不會捏造缺失的實作步驟。後續可以逐個補上經驗證的 `references/`、`scripts/` 或 `templates/`。

> 公開 repository 不等於自動授予第三方服務、品牌、API 或上游套件的商標與內容權利。請先檢查 `NOTICE.md`，並在新增上游內容時保留適當 attribution。

## 分類目錄

| 分類 ID | 分類 | 技能數量 |
| --- | --- | ---: |
| `personal-pack-01-agent-mcp-integrations` | Agent Mcp Integrations | 10 |
| `personal-pack-02-ai-product-ui-design` | Ai Product Ui Design | 11 |
| `personal-pack-03-cloud-web-platform` | Cloud Web Platform | 26 |
| `personal-pack-04-software-engineering-security` | Software Engineering Security | 14 |
| `personal-pack-05-data-research-analytics` | Data Research Analytics | 14 |
| `personal-pack-06-finance-investing` | Finance Investing | 13 |
| `personal-pack-07-hr-people-operations` | Hr People Operations | 30 |
| `personal-pack-08-seo-content-publishing` | Seo Content Publishing | 13 |
| `personal-pack-09-marketing-commerce-communications` | Marketing Commerce Communications | 14 |
| `personal-pack-10-documents-academic-workflows` | Documents Academic Workflows | 8 |
| `personal-pack-11-project-product-operations` | Project Product Operations | 11 |
| `personal-pack-12-email-calendar-collaboration` | Email Calendar Collaboration | 3 |
| `personal-pack-13-visual-design-illustration` | Visual Design Illustration | 6 |
| `personal-pack-14-video-audio-motion` | Video Audio Motion | 5 |
| `personal-pack-15-presentations-pitch-decks` | Presentations Pitch Decks | 5 |
| `personal-pack-16-automation-operations` | Automation Operations | 3 |

## 目錄結構

```text
skills/
  <skill-name>/
    SKILL.md
catalog/
  skills.json
  categories.json
scripts/
  validate_skills.py
```

每個 `skills/<skill-name>/` 都是獨立技能目錄，入口固定為 `SKILL.md`。這種結構便於使用者只複製需要的技能，也便於後續將完整 workflow 逐項加入。

## 使用方式

請先瀏覽 [`catalog/skills.json`](catalog/skills.json)，再將需要的 `skills/<skill-name>/` 目錄複製到你的 agent skills 目錄。若你的執行環境要求額外的安裝封裝格式，請以該環境的技能安裝器將同一個目錄封裝；不要把 metadata-only 條目當成完整工具實作。

提交前可執行：

```bash
python scripts/validate_skills.py
```

## 貢獻方式

若要把某個 metadata-only 條目提升為完整技能，請補上可重現的工作流、必要的 references、可測試的 scripts 或 templates，並更新 `catalog/skills.json` 的 `status`。請遵守 [`CONTRIBUTING.md`](CONTRIBUTING.md) 與 [`SECURITY.md`](SECURITY.md)。

## 授權

本 repository 的整理結構、索引與由本專案新增的 metadata 包裝採用 MIT License；上游或第三方內容仍可能受其各自授權條款約束，詳見 [`NOTICE.md`](NOTICE.md)。

## Repository

公開入口：[github.com/lwokeray/personal-shared-skills](https://github.com/lwokeray/personal-shared-skills)
