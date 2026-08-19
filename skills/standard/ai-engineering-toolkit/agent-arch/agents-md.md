# AGENTS.md — Repository-Level Agent Instructions (2026 Standard)

**Read this guide** when configuring or writing repository instructions that agents must follow (AGENTS.md for Anthropic/OpenAI, or per-repo customization files for Google ADK).

## Why AGENTS.md Exists

AGENTS.md is the 2026 cross-vendor standard for repository instructions. It travels with the codebase in version control, applies before the agent starts work, and is consulted on every session. Anthropic (Claude Code), OpenAI (Codex and the Agents SDK harness), and Google (ADK) all consume it — a single file now shapes agent behavior across all major platforms [1] [2] [3].

> Key rule: keep it small. AGENTS.md is always-read context. Put only the instructions that matter on every session in it; push detailed workflows into skills (see `agent-arch/skill-design.md`) and trigger them with if/then rules.

## Structure (the agents.md spec shape)

Follow the community-agreed sections and order:

1. **Project overview** — where the core code lives, what the project does.
2. **Build and test commands** — the exact commands for format/lint/typecheck/test. These are the highest-value lines; put them near the top.
3. **Code style and conventions** — naming, structure, patterns used in this repo.
4. **Mandatory skill usage** — if/then triggers that make specific skills required (the pattern that made OpenAI's own SDK repos measurably faster).
5. **Compatibility and release rules** — e.g., preserve positional compatibility of public constructors; how to bump versions.
6. **Security considerations** — what must never be committed, how secrets are handled.

## The Pattern That Works: If/Then Skill Triggers

OpenAI maintains its Agents SDK repos with a compact if/then section. Real examples from their production files [1]:

```markdown
## Mandatory skill usage
- Use `$implementation-strategy` before editing runtime or API changes that may affect compatibility boundaries.
- Run `$code-change-verification` when runtime code, tests, examples, or build/test behavior changes.
- Use `$openai-knowledge` for OpenAI API or platform work.
- Use `$pr-draft-summary` when substantial code work is ready for review.
```

The power is in conditionality: the verification rule is NOT "always run the long validation stack" but "run it when runtime code changed, and do not mark the work complete until it passes." The conditional part keeps docs-only work lightweight; the mandatory part guarantees SDK changes pass the standard gate.

## Feedback Loop — How AGENTS.md Stays Accurate

The single most important operational habit, per OpenAI's Codex documentation [2]:

1. When the agent makes the same mistake repeatedly, add a rule.
2. When the agent reads too many files, add routing guidance (which directories to prioritize).
3. When PR review feedback repeats, codify it.
4. **When a human corrects the agent, tell the agent to update AGENTS.md so the fix persists.** This is the memory mechanism for stateless agent sessions.
5. Automate drift checks with scheduled tasks that look for guidance gaps and suggest additions.

Pair AGENTS.md with infrastructure that enforces it: pre-commit hooks, linters, and type checkers catch violations before humans see them. AGENTS.md describes the rules; tooling enforces them.

## Layering Rules

| Layer | File | Scope |
|-------|------|-------|
| Global instructions | `~/.claude/CLAUDE.md` / `~/.codex/AGENTS.md` | Your personal defaults across all repos |
| Repo instructions | `AGENTS.md` in repo root | Team rules, always applied |
| Directory-specific | `AGENTS.md` in subdirectories | Nested scope; closer to working directory takes precedence |
| Repo skills | `.claude/skills/` / `.agents/skills/` | Workflows that apply to this project |

## Common Mistakes

1. **Writing a 500-line AGENTS.md.** It is always-read context; every line costs tokens on every turn. Move long procedures into skills.
2. **Duplicating what tooling already enforces.** If a linter catches it, do not write prose about it — configure the linter and point at it.
3. **Never updating it after corrections.** Every manual fix that is not codified will recur in the next session.
4. **Vague rules.** "Write good tests" does nothing. "Run `make tests` and do not mark complete until green" is enforceable.

## References

[1]: https://developers.openai.com/blog/skills-agents-sdk "Using skills to accelerate OSS maintenance — OpenAI Developers (2026-03)"
[2]: https://developers.openai.com/codex/customization/overview "Codex Customization — AGENTS guidance and skills"
[3]: https://agents.md/ "AGENTS.md community specification"
