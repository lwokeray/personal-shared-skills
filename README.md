# Personal Shared Skills

這個 public repository 收錄原本的完整 skills collection，並保留各技能的原始 `SKILL.md`、`references/`、`scripts/`、`templates/`、assets 與 `.skill` 封裝內容。**本次恢復只還原原始 skills 內容，不翻譯、不改寫、不重建任何 skill 檔案。**

## Collection 範圍

| 內容 | 數量 | 說明 |
| --- | ---: | --- |
| 來源記錄 | **508** | 原始 collection 的全部來源記錄 |
| 不重複技能名稱 | **475** | 同名但不同 runtime／產品／來源的變體均保留 |
| 完整標準技能來源 | **120** | 保留完整技能目錄與 resources |
| `.skill` 封裝 | **183** | 保留原始 package 與解壓後內容 |
| 個人恢復版 metadata | **186** | 原始備份本身只有觸發 metadata，沒有可恢復的 atomic body |
| 內部 reference `SKILL.md` | **19** | 完整技能內部使用的參考檔，原樣保留 |

## 目錄結構

```text
skills/
  standard/                  # 完整標準技能與原始 resources
  archives/                  # 原始 .skill 封裝與解壓後內容
  personal-metadata/         # 原始個人 metadata-only 條目
catalog/
  skills.json                # 全部來源記錄與索引
  sources.json               # 來源統計
scripts/
  validate_skills.py         # collection 驗證工具
```

## 指定 skills 用途

以下 5 個 skills 已完整保留在 `skills/standard/` 中；本節只提供繁體中文用途索引，沒有修改它們的原始內容。

| Skill | 中文用途 |
| --- | --- |
| `prompt-auto-corrector` | 自動分析、修正、補全與優化使用者提示詞，在保留原始意圖的前提下提升清晰度、可執行性與輸出品質。 |
| `azure-deployment-preflight` | 在 Azure 部署前，對 Bicep 模板進行語法驗證、what-if 變更分析與權限預檢查。 |
| `senior-research-architecture-advisor` | 以系統整合商的資深架構師視角，評估、研究、界定範圍、估算、設計與審查產品、系統、雲端、資料、AI 及營運架構。 |
| `microsoft-skills-collection` | Microsoft 生態系 Agent Skills collection 入口，涵蓋 GitHub Copilot、Azure、.NET、PowerShell、Windows、Visual Studio、Microsoft 365 與 Microsoft AI／資料工作流。 |
| `ai-engineering-toolkit` | AI 驅動軟體工程生命週期工具包，涵蓋 plan-first 開發、驗證優先、系統化除錯、程式碼審查、skills／agents 安全稽核與 AI agent 架構設計。 |

## 使用方式

請先瀏覽 [`catalog/skills.json`](catalog/skills.json)，再依來源命名空間複製需要的技能目錄。完整標準技能可直接使用 `skills/standard/<skill-name>/`；`.skill` 來源可使用 `skills/archives/` 下相應的 `package.skill`；個人 metadata-only 條目只能作為觸發索引，不能當作原始完整 workflow。

```bash
python scripts/validate_skills.py
```

## 重要說明

本 repository 的 `skills/` 內容已恢復至完整 collection commit 的原始狀態。個人 `personal-metadata` 條目之所以仍標示 metadata-only，是因為原始本機備份本來就只保存觸發描述；這不是本次恢復過程刪除或改寫造成的。若要補回那些缺失的 atomic skill body，需要另外提供原始來源或備份。

## 授權與安全

本 repository 的整理結構、索引與新增 README 採用 MIT License。來源技能、Microsoft／Power Platform 內容、第三方套件、品牌與文件可能各自受不同授權條款約束，請閱讀 [`NOTICE.md`](NOTICE.md)。請勿提交 API key、access token、cookie、密碼、私密金鑰、內部 URL 或個人識別資料。

Repository：[github.com/lwokeray/personal-shared-skills](https://github.com/lwokeray/personal-shared-skills)
