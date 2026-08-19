# Checklists

Run the matching checklist at each gate. Copy the relevant block into the task and check items off with evidence.

## Development Gate (run before requesting review)

```markdown
- [ ] Tests exist for happy path, boundary case, and failure mode
- [ ] All tests pass, including regression test for this change
- [ ] Linter and type checker pass
- [ ] Build succeeds
- [ ] No debug prints, TODO hacks, or commented-out code
- [ ] No hardcoded credentials or secrets
- [ ] Error messages are actionable
- [ ] Commit history: small commits, clear messages
- [ ] Branch up to date with main; diff contains only this task's changes
```

## Debugging Gate (run before claiming a fix)

```markdown
- [ ] Failure reproduces reliably from a minimal input
- [ ] Root cause identified, not just symptom suppressed
- [ ] Fix is minimal and does not special-case around the failure
- [ ] Regression test added (test fails without the fix, passes with it)
- [ ] Full suite passes; related behaviors verified
```

## Review Gate (run during reviews)

```markdown
- [ ] Understands intent before judging lines
- [ ] Correctness: behavior matches spec; edge cases covered
- [ ] Tests verify behavior, not just coverage; would fail if fix reverted
- [ ] Security: secrets, input validation at boundaries, permission scope, external calls
- [ ] Maintainability: naming, file boundaries, no duplication
- [ ] Verdict explicit (APPROVE / REQUEST_CHANGES / QUESTION) with ranked findings
```

## Skill Creation Gate (run before sharing a skill)

```markdown
- [ ] name ≤64 chars, lowercase + hyphens; description ≤1024 chars with capability AND triggers AND explicit skip conditions (2026 trigger/skip format)
- [ ] SKILL.md <500 lines, <5000 tokens; core workflow only
- [ ] Conditional content moved to references/, with explicit "load X when Y" guidance
- [ ] Deterministic logic extracted to scripts/, tested
- [ ] No duplication between SKILL.md and references/
- [ ] Gotchas section covers counterintuitive facts
- [ ] `python3 scripts/skill_audit.py .` reviewed; no unexplained findings
- [ ] External-URL fetching reviewed for prompt-injection risk
- [ ] No README/CHANGELOG; no content Manus already knows
- [ ] Tested on real tasks; false-positive and missed triggers fixed
- [ ] Trigger accuracy and output quality evaluated with graded evals; description tuned separately from content
```

## Agent Design Gate (run before deploying an agent)

```markdown
- [ ] Five-section prompt: frontmatter, identity, deliverables, workflow, guardrails
- [ ] Deliverables are concrete artifacts with a checklist, not vague goals
- [ ] Each workflow step references a named skill or MCP connector
- [ ] Guardrails include: no system-of-record writes, no external comms, [UNSOURCED] policy, approval gates
- [ ] Tool allowlist deny-by-default; only needed tools enabled mechanically
- [ ] Stopping conditions defined (max iterations, completion criteria, blocker policy)
- [ ] Untrusted-content handling: reader/orchestrator/resolver tiering or equivalent
- [ ] Tested in a sandbox with guardrails before autonomous use
- [ ] Sandbox: deny-by-default network, credentials outside compute, durable state (snapshot + rehydration) for long runs
- [ ] Hooks active where deterministic enforcement is needed (file-write, secret-scrub, test-on-stop)
- [ ] Success criteria defined as a rubric with a separate grader (outcomes loop) where grading criteria exist
```

## MCP Server Gate (run before publishing a server)

```markdown
- [ ] Tool schemas: constraints, examples, annotations set truthfully
- [ ] Actionable error messages; pagination on list endpoints
- [ ] Token audience validation; no token passthrough
- [ ] SSRF controls (internal IPs, metadata endpoints, localhost blocked/validated)
- [ ] Auth via config/env, not hardcoded
- [ ] Passes MCP Inspector
- [ ] ~10 evaluation questions created, read-only, verified, stable

## Agent Sandbox Gate (run before executing untrusted or long-horizon agent work)

```markdown
- [ ] Sandbox enabled; harness and compute separated; credentials absent from compute env
- [ ] Network deny-by-default; egress allowlist only covers needed hosts
- [ ] Workspace manifest defined: input mounts, output directories, storage mounts
- [ ] Snapshotting + rehydration configured for long-horizon runs
- [ ] Subagents routed to isolated environments; output validated through reader/orchestrator tiers
- [ ] PreToolUse/Stop hooks enforcing file-scope and test gates
- [ ] Container image and dependencies pinned; no host privilege escalation
```
