# Agent Architecture Patterns (2026 Edition)

Design agents the way the AI majors build production agent systems in 2026: three customization primitives (skills / hooks / subagents), the harness-plus-sandbox execution layer, outcome-grading loops, and multi-agent orchestration. Primary sources: Anthropic Claude Code platform docs and Managed Agents, OpenAI "The next evolution of the Agents SDK", Google ADK [1] [2] [3] [4].

## The Three Customization Primitives (Claude Code paradigm, universal in 2026)

| Primitive | What it is | When it fires | Best for |
|-----------|-----------|---------------|----------|
| **Skills** | Folder with SKILL.md + scripts that loads on demand | When the task matches its description | Repeatable expertise, house style, "how we do X here" |
| **Hooks** | Deterministic shell scripts wired to lifecycle events (PreToolUse, PostToolUse, Stop, SubagentStop) | At a fixed event, regardless of agent reasoning | Formatters, linters, security checks, secret scrubbing, build gates |
| **Subagents** | A separate agent instance with its own context window | When the parent decides to delegate | Hard sub-tasks that should not pollute parent context |

Rule of thumb: **Skill** = things you want the agent to know how to do. **Hook** = things that must happen no matter what the agent does. **Subagent** = things you want the agent to delegate.

These remain complementary to AGENTS.md (always-on repo instructions) and MCP (external tool access).

## The Execution Layer: Harness + Compute Separation

OpenAI's 2026 Agents SDK made the production stack explicit, and it is the reference architecture for any agent system [2]:

1. **Harness**: model-native instructions + tools + approvals + tracing + handoffs + resume — the interface between the model and the world.
2. **Compute**: a sandbox with the files, tools, and dependencies the agent needs. Standard providers now supported natively: Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel.
3. **Workspace Manifest**: a declarative description of the agent's workspace (mounted files, output directories, storage mounts from S3/GCS/Azure Blob/R2) so the model always knows where inputs are and where outputs go.

> Design assuming prompt-injection and exfiltration attempts. Separating harness and compute keeps credentials out of environments where model-generated code executes.

Two consequences follow: **durable execution** (state is externalized with snapshotting + rehydration — losing a sandbox container does not lose the run) and **scalability** (route subagents to isolated environments, parallelize across containers).

## Outcomes: Evaluation-Driven Self-Correction

Anthropic's Managed Agents (2026, public beta) productized the evaluator-optimizer pattern as a first-class substrate [4]:

1. Developers define success criteria as a **rubric**.
2. A separate **grader** evaluates outputs against it (decoupled from the producing agent).
3. The agent self-corrects until the grader passes.

Reported results: up to +10 points of task success over a standard prompting loop (+8.4% docx, +10.1% pptx internal benchmarks). Design any long-horizon agent around a rubric + grader — it is the 2026 standard mechanism for reliability on multi-step work.

## Multiagent Orchestration (2026 production patterns)

Anthropic's Managed Agents shipped the coordination model [4]: a **lead agent** decomposes complex work and delegates to specialist agents that work **in parallel on a shared filesystem** and contribute to the lead's context. Each specialist gets its own model, prompt, and toolset. The shared filesystem (not message passing) is the load-bearing coordination surface — plus full tracing of which agent did what, in what order, and why.

Google ADK applies the same shape through `SkillToolset` + MCP tools composed on a root agent, deployable to Agent Engine [3].

Orchestration decision table:

| Pattern | Use when | 2026 example |
|---------|----------|--------------|
| Single agent + skills + AGENTS.md | Most repo work | Codex maintaining OpenAI SDK repos (+45% PR throughput) |
| Hooks-only gates | Deterministic enforcement | CI-style format/lint/secret checks on every edit |
| Parent + subagent delegation | Heavy, context-expensive subtasks | Deep research subtasks returning one summary |
| Lead + specialist swarm | Complex, decomposable, long-horizon | Managed Agents multiagent orchestration; ADK workflows |
| Evaluator loop (Outcomes) | Clear grading criteria exist | Doc/ppt generation, structured data extraction |

Anthropic's guiding principle still holds: find the simplest solution first. Many applications are best served by one well-tuned agent with skills and AGENTS.md — not a swarm.

## Agent Prompt Template (five sections, unchanged in substance)

1. **Frontmatter** — machine-readable metadata: name, description, tool allowlist.
2. **Identity** — who the agent is and what it owns.
3. **Deliverables** — exact artifacts as a concrete checklist. Vague mandates invite scope creep; explicit deliverables define "done."
4. **Workflow** — numbered steps referencing skills by name; skill composition, not prose.
5. **Guardrails** — hard constraints (see `references/guardrails-templates.md`).

## Tiered Isolation for Untrusted Content (deny-by-default)

Keep the established four-tier split, now enforceable at the harness level [1] [2]:

| Tier | Access to untrusted content | Tools |
|------|------------------------------|-------|
| Reader | Yes (quarantine) | Read, grep only. No network, no write, no bash. Output schema-validated with length caps. |
| Orchestrator | No (validated output only) | Read + read-only MCP to trusted internal systems. Cannot write. |
| Resolver | No | Write access only. No MCP, no bash, no external systems. |
| Critic | No | Independently re-checks each finding against trusted sources before the resolver writes. |

Every tier starts with all tools disabled and explicitly enables only what it needs — a config the model cannot override at runtime. The boundary: the tier that reads external data cannot write; the tier that writes cannot read external data, so no compromise chains.

## The Agent Loop (fundamentals, unchanged)

An agent is an LLM using tools in a loop based on environmental feedback: ground truth at every step (tool-call results or code-execution output), explicit stopping conditions (max iterations, completion criteria, blocker detection), human approval gates at defined checkpoints, and sandboxed testing before trusting autonomy.

## References

[1]: https://www.totalum.app/blog/claude-code-skills-totalum "Claude Code Skills in 2026 — the Skills/Hooks/Subagents decision table"
[2]: https://openai.com/index/the-next-evolution-of-the-agents-sdk/ "The next evolution of the Agents SDK — OpenAI (2026-04)"
[3]: https://codelabs.developers.google.com/next26/dev-keynote/building-agents-with-skills "Building ADK Agents with Skills — Google Next '26 (2026-08)"
[4]: https://blakecrosley.com/blog/code-with-claude-sf-2026-recap "Code with Claude SF 2026 — Dreaming, Outcomes, Multiagent Orchestration"
