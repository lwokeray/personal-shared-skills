# Personal Shared Skills

這個 public repository 專門收錄個人／自建 Agent Skills。**本次只更新 README，不修改任何既有 skills 內容、`SKILL.md`、resources 或檔案結構。**

目前 repository 的個人技能目錄包含 **15 個分類與 164 個個人原子 skills**。技能識別名稱維持英文 slug，以保持檔案路徑與 agent routing 的穩定性。

## 個人技能分類目錄

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

## 指定補充 skills

以下 5 個 skills 是使用者指定要在 README 中補充列出的項目。這一節只做文件索引與用途說明，**不代表修改或重建 `skills/` 目錄中的任何內容**。

| Skill | 中文用途 |
| --- | --- |
| `prompt-auto-corrector` | 自動分析、修正、補全與優化使用者提示詞，在保留原始意圖的前提下提升清晰度、可執行性與輸出品質。適用於修正、改善、優化、重寫、結構化或產生提示詞的需求。 |
| `azure-deployment-preflight` | 在執行 Azure 部署前，對 Bicep 部署進行完整預檢驗證，包括模板語法、what-if 變更分析與權限檢查。適用於 Azure 部署、Bicep 驗證、部署權限與 `azd provision` 等需求。 |
| `senior-research-architecture-advisor` | 以系統整合商的資深架構師視角，評估、研究、界定範圍、估算、設計、審查或變更產品、系統、整合、雲端、資料、AI 與營運架構，並建立可追溯的架構與交付建議。 |
| `microsoft-skills-collection` | Microsoft 生態系 Agent Skills 集合，涵蓋 GitHub Copilot、Azure、.NET、PowerShell、Windows、Visual Studio、Microsoft 365 與 Microsoft AI／資料工作流。適用於選擇或安裝 Microsoft 相關技能。 |
| `ai-engineering-toolkit` | 2026 年版 AI 驅動軟體工程生命週期工具包，涵蓋 plan-first 開發、驗證優先、系統化除錯、程式碼審查、第三方 skills／agents 安全稽核，以及 AI agent、MCP、AGENTS.md 與 sandbox 架構設計。 |

## 目錄結構

```text
packs/
  personal-pack-*/SKILL.md       # 個人分類入口
skills/
  <skill-name>/SKILL.md          # 個人 skill 入口
catalog/
  skills.json                    # 個人技能清單、用途與來源
  categories.json                # 分類索引
scripts/
  validate_skills.py             # 驗證工具
```

## 使用方式

請先瀏覽 [`catalog/skills.json`](catalog/skills.json)，再複製需要的 `skills/<skill-name>/` 目錄。README 中的用途說明使用繁體中文；技能名稱則保留原始英文 slug。

```bash
python scripts/validate_skills.py
```

## 授權與安全

本 repository 的整理結構、索引與新增文件採用 MIT License。請勿在技能、範例、issue 或 pull request 中提交 API key、access token、cookie、密碼、私密金鑰、內部 URL 或個人識別資料。請閱讀 [`NOTICE.md`](NOTICE.md) 與 [`SECURITY.md`](SECURITY.md)。

Repository：[github.com/lwokeray/personal-shared-skills](https://github.com/lwokeray/personal-shared-skills)
