# Personal Shared Skills — Complete Collection

這個 public repository 收錄本機 skills 目錄中盤點到的**全部技能來源**，不再只限於 `personal-pack-*`。目前保留 **508 筆來源記錄**、**475 個不重複技能名稱**，並以命名空間保留同名但不同 runtime、產品或來源的變體。

## Collection 範圍

| 來源類型 | 數量 |
| --- | ---: |
| 完整 `SKILL.md` 來源 | 120 |
| 完整技能內部 reference `SKILL.md` | 19 |
| `.skill` 封裝及其解壓內容 | 183 |
| 個人恢復版 metadata | 186 |
| **來源記錄合計** | **508** |

| 來源根目錄 | 來源記錄 |
| --- | ---: |
| `ai-adoption-case-slide-workflow` | 1 |
| `ai-engineering-toolkit` | 1 |
| `automation-and-scheduling` | 1 |
| `azure-deployment-preflight` | 1 |
| `backlink-analysis` | 1 |
| `builtin-llm-models` | 1 |
| `comparison-article-writer` | 1 |
| `content-gap-analysis` | 1 |
| `data-backup-restoration` | 1 |
| `excel-generator` | 1 |
| `finance-pro-playbooks` | 1 |
| `game-dev` | 1 |
| `github-gem-seeker` | 1 |
| `gws-best-practices` | 1 |
| `html-video-production` | 20 |
| `imagegen` | 1 |
| `internet-skill-finder` | 1 |
| `keyword-research` | 1 |
| `manim-animator` | 1 |
| `manus-api` | 1 |
| `manus-config` | 1 |
| `manus-pptx` | 1 |
| `microsoft-skills-collection` | 184 |
| `persistent-computing` | 1 |
| `personal-pack-01-agent-mcp-integrations` | 11 |
| `personal-pack-02-ai-product-ui-design` | 12 |
| `personal-pack-03-cloud-web-platform` | 27 |
| `personal-pack-04-software-engineering-security` | 15 |
| `personal-pack-05-data-research-analytics` | 15 |
| `personal-pack-06-finance-investing` | 14 |
| `personal-pack-07-hr-people-operations` | 31 |
| `personal-pack-08-seo-content-publishing` | 14 |
| `personal-pack-09-marketing-commerce-communications` | 15 |
| `personal-pack-10-documents-academic-workflows` | 9 |
| `personal-pack-11-project-product-operations` | 12 |
| `personal-pack-12-email-calendar-collaboration` | 4 |
| `personal-pack-13-visual-design-illustration` | 7 |
| `personal-pack-14-video-audio-motion` | 6 |
| `personal-pack-15-presentations-pitch-decks` | 6 |
| `personal-pack-16-automation-operations` | 4 |
| `power-apps-component-collection` | 54 |
| `powerplatform-mcp-toolkit` | 1 |
| `prompt-auto-corrector` | 1 |
| `read-special-images` | 1 |
| `senior-research-architecture-advisor` | 1 |
| `seo-competitor-analysis` | 1 |
| `skill-creator` | 1 |
| `tts-prompter` | 1 |
| `typst-pdf-maker` | 1 |
| `video-generator` | 1 |
| `webdev-custom-dockerfile` | 1 |
| `webdev-data-api` | 1 |
| `webdev-file-storage` | 1 |
| `webdev-image-generation` | 1 |
| `webdev-llm-integration` | 1 |
| `webdev-manus-oauth` | 1 |
| `webdev-maps-integration` | 1 |
| `webdev-owner-notifications` | 1 |
| `webdev-periodic-updates` | 1 |
| `webdev-readme-fullstack` | 1 |
| `webdev-readme-mobile` | 1 |
| `webdev-readme-mobile-backend` | 1 |
| `webdev-readme-static` | 1 |
| `webdev-ssr-conversion` | 1 |
| `webdev-voice-transcription` | 1 |
| `website-traffic-checker` | 1 |
| `youtube-video-research` | 1 |

## 為什麼不直接合併同名技能？

本 collection 中有些技能名稱相同，但實際內容分別針對不同環境，例如 code app、mobile app、不同 Microsoft 元件或不同 package 來源。若只以名稱扁平化，會覆蓋或遺失這些變體。因此檔案保留在以下命名空間：

```text
skills/standard/          # 已存在的完整 SKILL.md 目錄
skills/archives/          # `.skill` 封裝解壓內容，並保留 package.skill
skills/personal-metadata/  # 個人技能恢復版 metadata-only 入口
catalog/skills.json        # 全部來源記錄與重複名稱群組
```

每一筆完整技能都保留自己的 `references/`、`scripts/` 與 `templates/`（若原始來源存在）。對 `.skill` 封裝而言，目錄同時保留解壓後內容與原始 `package.skill`，方便瀏覽及重新分發。

## Metadata-only 狀態

個人技能 inventory 中有 **186** 筆只保留觸發描述的條目。這些條目在 `skills/personal-metadata/` 中被轉成標準 frontmatter，但不會捏造缺失的 atomic skill body。它們可作為觸發索引與後續補全入口，不能誤當成已完成的工作流。

## 使用方式

請先查看 [`catalog/skills.json`](catalog/skills.json)，再複製需要的技能目錄。一般完整技能可直接取用其所在目錄；`.skill` 來源可使用同目錄的 `package.skill`；metadata-only 條目則應先補上可驗證的工作流。

提交前執行：

```bash
python scripts/validate_skills.py
```

## 授權與安全

本 repository 的索引、命名空間與新增 metadata 包裝採用 MIT License。來源技能、Microsoft/Power Platform 內容、第三方套件、品牌與文件可能各自受不同授權條款約束，請閱讀 [`NOTICE.md`](NOTICE.md)，不要把 MIT License 解讀為上游內容的再授權。

本次公開化不包含本機 secrets、cookie、私密金鑰或 connector credentials。公開 repository 仍應在新增 commit 前執行 secrets scan，並遵守 [`SECURITY.md`](SECURITY.md)。

Repository：[github.com/lwokeray/personal-shared-skills](https://github.com/lwokeray/personal-shared-skills)
