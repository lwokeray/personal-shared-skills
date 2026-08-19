# Personal Shared Skills

這個 public repository 專門收錄**個人／自建 Agent Skills**，不包含官方 skills、內建 skills、Microsoft／Power Platform collection 或其他系統技能。

目前共有 **15 個個人分類**與 **164 個個人原子 skills**。每個技能的用途與觸發描述均已整理為繁體中文；技能識別名稱維持英文 slug，以保持檔案路徑與 agent routing 的穩定性。

> 目前個人 inventory 保存的是恢復版觸發描述，原始 atomic skill body 並未完整保留。因此每個技能都明確標示為 **metadata-only**，不會捏造缺失的工作流。

## 分類目錄

| 分類 ID | 中文分類 | 個人 skills 數量 |
| --- | --- | ---: |
| `personal-pack-01-agent-mcp-integrations` | AI Agent、MCP 與外部服務整合 | 9 |
| `personal-pack-02-ai-product-ui-design` | AI 產品 UI／UX 設計 | 11 |
| `personal-pack-03-cloud-web-platform` | 雲端與 Web 平台 | 9 |
| `personal-pack-04-software-engineering-security` | 軟體工程與安全 | 13 |
| `personal-pack-05-data-research-analytics` | 資料、研究與分析 | 14 |
| `personal-pack-06-finance-investing` | 財務與投資 | 13 |
| `personal-pack-07-hr-people-operations` | 人資與人員營運 | 30 |
| `personal-pack-08-seo-content-publishing` | SEO、內容與出版 | 13 |
| `personal-pack-09-marketing-commerce-communications` | 行銷、商務與溝通 | 14 |
| `personal-pack-10-documents-academic-workflows` | 文件、學術與知識工作流 | 8 |
| `personal-pack-11-project-product-operations` | 專案、產品與營運 | 11 |
| `personal-pack-12-email-calendar-collaboration` | 電子郵件、行事曆與協作 | 3 |
| `personal-pack-13-visual-design-illustration` | 視覺設計與插畫 | 6 |
| `personal-pack-14-video-audio-motion` | 影片、音訊與動態 | 5 |
| `personal-pack-15-presentations-pitch-decks` | 簡報、提案與演講 | 5 |

## 目錄結構

```text
packs/
  personal-pack-*/SKILL.md       # 16 個中文分類入口
skills/
  <skill-name>/SKILL.md          # 164 個中文個人 skill 入口
catalog/
  skills.json                    # 技能清單、中文用途與來源
  categories.json                # 分類索引
scripts/
  validate_skills.py             # frontmatter 與中文描述驗證
```

## 使用方式

先瀏覽 [`catalog/skills.json`](catalog/skills.json)，再複製需要的 `skills/<skill-name>/` 目錄。每個入口的 `description` 是繁體中文，技能名稱則保留原始 slug。提交前請執行：

```bash
python scripts/validate_skills.py
```

## 授權與安全

本 repository 的整理結構、索引與新增 metadata 包裝採用 MIT License。這個版本沒有複製官方或內建 skills，也沒有提交 API key、cookie、私密金鑰、connector credentials 或本機 registry。請閱讀 [`NOTICE.md`](NOTICE.md) 與 [`SECURITY.md`](SECURITY.md)。

Repository：[github.com/lwokeray/personal-shared-skills](https://github.com/lwokeray/personal-shared-skills)
