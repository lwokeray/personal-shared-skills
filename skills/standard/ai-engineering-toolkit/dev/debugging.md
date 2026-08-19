# Systematic Debugging

Diagnose failures methodically instead of guessing fixes. Adapted from obra/superpowers systematic-debugging and Anthropic's agent-loop ground-truth principle.

## The Loop

1. **Reproduce reliably.** Isolate the smallest input that triggers the failure every time. If it is not reproducible, instrument logging before proceeding.
2. **Form one hypothesis at a time.** Write it down. Guessing multiple fixes at once corrupts the evidence.
3. **Design a decisive test.** The test must distinguish this hypothesis from the alternatives. Run it and observe — actual output, not belief.
4. **Narrow the blast radius.** Bisect: cut the problem space in half (git bisect, half the code path, half the input). Never inspect every line.
5. **Fix the root cause, not the symptom.** If the fix only suppresses output or adds a special case, the hypothesis was wrong — return to step 2.
6. **Encode the regression.** Add a failing test for the bug before fixing it, so it never returns.
7. **Verify nothing else broke.** Run the full suite, not just the failing test.

## Instrumentation Rules

- Log at the boundaries: inputs in, outputs out, exceptions caught.
- When a tool, MCP server, or agent misbehaves, log the full request/response payloads before "fixing" anything.
- Prefer observing over theorizing: strace, print actual state, dump the schema.

## Common Traps

- **The Heisenbug**: a failure that vanishes under observation is usually a timing/ordering issue. Freeze the order (disable parallelism) before debugging the logic.
- **The cascade**: one failure produces many symptoms. Find the first failing check in the log, not the last.
- **The environment lie**: "it works on my machine" means the environment is part of the hypothesis. Pin and diff dependencies, env vars, and paths.
- **The patch spiral**: three or more attempted fixes without a passing test means the hypothesis strategy has failed. Stop, read `references/gotchas.md`, and re-formulate.

## When to Escalate

Stop and ask the human partner when: the failure cannot be reproduced, the root cause contradicts the design, or fixing it requires a decision only the owner can make (data loss tradeoffs, breaking API changes, security-impacting workarounds).
