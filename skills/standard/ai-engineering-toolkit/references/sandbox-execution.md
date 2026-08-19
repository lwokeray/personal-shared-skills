# Sandbox Execution & Durable Runs (2026 Standard)

**Read this guide** when an agent must execute code, run commands, write files, install dependencies, or operate across long-horizon tasks.

## The Core Principle: Harness/Compute Separation

Design every agent system assuming **prompt-injection and exfiltration attempts**. The 2026 production architecture separates the harness (model instructions, tools, approvals, tracing, handoffs) from the compute (the sandbox where model-generated code executes), so that credentials and platform access never live in the same environment as generated code. This is now OpenAI's explicit design doctrine and the operating model of Anthropic's Managed Agents (customer-controlled sandboxes with private MCP) [1] [2].

## What a Proper Agent Workspace Provides

The agent needs a predictable environment, declaratively described (OpenAI Manifest abstraction; equivalent concepts in Claude Code worktrees and Google ADK projects) [1] [3]:

| Capability | Why it matters |
|------------|----------------|
| Read/write files | Persistent artifacts between steps |
| Shell execution | Install dependencies, run build/test commands |
| Mountable volumes | Mount local files, define output directories |
| Storage mounts | Pull inputs from S3 / GCS / Azure Blob / R2 |
| Snapshotting | Save state at checkpoints |
| Rehydration | Restore into a fresh container from the last checkpoint |
| Network policy | Deny-by-default egress; allowlist only needed hosts |

Built-in sandbox providers now standardized across the ecosystem: **Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel** (OpenAI Agents SDK native support) [1].

## The Three Properties That Make Sandboxes Production-Grade

1. **Isolation** — each run, and each subagent, gets its own environment. One compromised container cannot reach siblings or the host. Route subagents to isolated environments by default.
2. **Durability** — externalize agent state with snapshot + rehydration. When a container fails or expires, the run continues from the last checkpoint instead of restarting from zero. Long-horizon work is only viable with this property.
3. **Scalability** — agent runs can use one sandbox or many; invoke sandboxes only when needed; parallelize work across containers.

## Deny-by-Default Security Model (apply inside the sandbox too)

The tiered subagent isolation from `agent-arch/agent-patterns.md` applies inside any sandbox: Reader (read + grep only, schema-validated output), Orchestrator (read-only access to trusted systems), Resolver (write-only, no MCP), Critic (independent verification). Mechanical enforcement: every tier starts with all tools disabled; only what is needed is explicitly enabled; the model cannot override this config at runtime.

## Lifecycle Hooks

Deterministic hooks fire regardless of agent reasoning and are the enforcement layer the sandbox alone cannot provide (Claude Code hooks; equivalent in Codex pre-commit + CI) [2] [4]:

| Hook | Typical gate |
|------|--------------|
| PreToolUse | Block writes outside the repo; block network when disallowed |
| PostToolUse | Run formatter/linter after every file edit |
| Stop | Run full test suite at completion |
| SubagentStop | Quarantine and validate subagent output before merging into parent context |
| Redact-secrets | Scan every shell command for leaked credentials |

## Checklist (before running untrusted or long-horizon work)

Run the matching checklist in `references/checklists.md` (Agent Sandbox Gate). In brief: sandbox enabled with deny-by-default network; credentials absent from the compute environment; state checkpointing configured for long runs; subagent outputs validated through quarantine tiers; hooks active for file-write and secret-scrubbing; container image and dependencies pinned.

## References

[1]: https://openai.com/index/the-next-evolution-of-the-agents-sdk/ "The next evolution of the Agents SDK — OpenAI (2026-04)"
[2]: https://blakecrosley.com/blog/code-with-claude-sf-2026-recap "Code with Claude SF 2026 recap"
[3]: https://codelabs.developers.google.com/next26/dev-keynote/building-agents-with-skills "Building ADK Agents with Skills — Google Next '26"
[4]: https://developers.openai.com/codex/customization/overview "Codex Customization — hooks and guardrails"
