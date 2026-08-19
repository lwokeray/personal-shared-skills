# Skill Design (2026 Edition — Open Standard)

Design skills the way all three AI majors design them in 2026: composable units of domain expertise loaded via progressive disclosure. **Agent Skills is now an open standard (agentskills.io)**, jointly adopted by Anthropic (Claude Code, Claude.ai, Managed Agents), OpenAI (Agents SDK harness, Codex), and Google (ADK `SkillToolset`) — one SKILL.md format runs everywhere [1] [2] [3] [4].

## What a Skill Is

A skill is a directory containing `SKILL.md` (frontmatter + instructions) plus optional `scripts/`, `references/`, and `assets/` (OpenAI/Codex terminology; Anthropic also uses `templates/`). It packages procedural knowledge that turns a general-purpose agent into a specialist. Skills are **passive**: they describe how to do X well; they never contain workflow sequencing logic ("first do A, then do B" belongs to the agent, not the skill). This passivity is what makes skills composable across workflows, hooks, and subagents.

Skills complement — not replace — other primitives: **AGENTS.md** shapes always-on behavior, **hooks** enforce deterministic events, **subagents** isolate heavy work. A skill defines the workflow and names the MCP tools to use.

## Three-Level Progressive Disclosure

| Level | Loaded | Budget | Content |
|-------|--------|--------|---------|
| 1. Metadata | Always (discovery) | ~100–200 tokens | YAML frontmatter `name` + `description` |
| 2. Instructions | When triggered | <5,000 tokens, <500 lines | `SKILL.md` body |
| 3. Resources | On demand | None until accessed | `references/`, `scripts/`, `assets/` |

## 2026 Frontmatter: Trigger AND Skip Rules

The format evolved in 2026. The best official skills now state explicit trigger conditions *and* explicit skip conditions, preventing false-positive loading when the task concerns a different provider or stack [1]:

```yaml
---
name: my-skill
description: >-
  What it does AND when to use it.
  TRIGGER — use when: [tasks, file types, phrases, project patterns].
  SKIP only when: [e.g., a different provider is named; grep shows no match].
---
```

Rules: `name` ≤64 chars, lowercase + numbers + hyphens. `description` ≤1024 chars and is the whole trigger mechanism — name both capability and activation scenarios. In 2026 tooling also supports **invocation control** (name-only or user-invocable-only) for skills that must not auto-load [3].

## Design Principles

1. **Add what the agent lacks, omit what it knows.** No explanations of HTTP, PDFs, or migrations. Only project conventions, non-obvious edge cases, and the specific APIs/tools to use.
2. **Design coherent units.** Scope like a function: one composable unit of work with a narrow contract, a clear trigger, and a concrete output. Too narrow → multiple skills load per task; too broad → imprecise activation.
3. **Moderate detail beats exhaustiveness.** Concise stepwise guidance + a working example outperforms exhaustive documentation. Leave judgment calls to the agent.
4. **Match specificity to fragility.** Fragile sequences (fixed install order, API quirks) → scripts with low freedom. Flexible judgment → high-freedom prose that explains why.
5. **Gotchas are the highest-value content.** Concrete, counterintuitive facts that defy reasonable assumptions — not generic advice like "handle errors appropriately."
6. **Templates for formats; scripts for reinvented logic.** Concrete templates beat prose descriptions. When the agent rebuilds the same parsing/validation logic every run, write it once as a tested script in `scripts/` (scripts run via shell; only output enters context).
7. **Conditional references.** Move mutually-exclusive contexts to `references/` and tell the agent *when* to load each file ("read references/api-errors.md if the API returns non-200").
8. **MCP dependencies are declared.** If a skill depends on MCP tools, declare the dependency so the platform can wire it (Codex: `agents/openai.yaml`; Claude Code: MCP config); point at a quickstart when the server is not present locally.

## Development Workflow (measure, then iterate)

1. **Extract from real work.** Complete real tasks with the agent, capture corrections and preferences, then extract the reusable pattern. Start from real expertise, never generic LLM knowledge.
2. **Structure for scale.** Split `SKILL.md` when unwieldy; move context into `references/`; wire conditional loading.
3. **Iterate with real execution.** Run the skill on real tasks; false-positive and missed triggers drive description edits (adjust triggers/skip rules, not just content).
4. **Evaluate with evals.** Define test cases with expected outputs and run graded evals; iterate until quality is consistent. Anthropic's official skill-creator now includes benchmarking and variance analysis; measure trigger accuracy separately from output quality [1].

## Directory Layout

```
my-skill/
├── SKILL.md              # frontmatter (trigger + skip) + core instructions (<500 lines)
├── scripts/              # deterministic, tested code (only output enters context)
├── references/           # conditional docs: "load X when Y happens"
└── assets/               # output assets/templates, not loaded into context
```

Avoid duplication: content lives in `SKILL.md` OR `references/`, never both. No README/CHANGELOG — skills are for agents, not humans.

## Distribution (2026 landscape)

| Channel | Audience | Trust level |
|---------|----------|-------------|
| Repo-local (`.claude/skills/`, `.agents/skills/`) | Your team | High — fully auditable |
| Official repos (anthropics/skills, 169k+ stars) | Everyone | High — vetted |
| Codex plugins / Claude plugins | Teams, marketplace | Medium — audit before install |
| Skills Directory (partner skills) | Claude users | Medium-high — Anthropic curated |
| skills.sh (600k+ indexed skills, Vercel OIDC) | Open market | Low-medium — audit every import |

## Security Checklist (before sharing or installing)

Run `python3 ../../scripts/skill_audit.py .` and review findings. Then confirm: no instructions that override agent guardrails, no unexpected network calls, no file-access patterns that do not match the stated purpose, no data exfiltration to external URLs. Skills that fetch external content are the highest-risk category — fetched content may contain prompt injection.

## References

[1]: https://code.claude.com/docs/en/skills "Claude Code Skills — Anthropic"
[2]: https://developers.openai.com/codex/customization/overview "Codex Customization — Skills (OpenAI)"
[3]: https://support.claude.com/en/articles/12512176-what-are-skills "What are skills? — Claude Help Center (2026-08)"
[4]: https://codelabs.developers.google.com/next26/dev-keynote/building-agents-with-skills "Building ADK Agents with Skills — Google Next '26 (2026-08)"
