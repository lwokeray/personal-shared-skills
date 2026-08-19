# Code Review

A rigorous, checklist-driven review process. Adapted from obra/superpowers receiving-code-review and requesting-code-review, plus Anthropic's guardrail philosophy.

## Requesting a Review

Before asking for review:

1. Branch is rebased on the current main and contains only the changes for this task.
2. All tests pass, including the regression test added for this change.
3. The diff is small enough to review in one sitting — split before requesting if not.
4. Include a summary: what changed, why, and what the reviewer should focus on. Name known risks explicitly.

## Conducting a Review

Review in passes, not line-by-line from the top:

1. **Understand the intent.** Read the PR summary and the changed files' purpose before judging individual lines.
2. **Check correctness.** Does it do what the spec says? Are edge cases covered (see `references/gotchas.md`)?
3. **Check the tests.** Do tests verify behavior or merely exercise the new code? Would the test fail if the fix were reverted?
4. **Check security.** Secrets, input validation at boundaries, permission scope, external calls (apply `core/security-by-default.md` rules).
5. **Check maintainability.** Naming, file boundaries, no duplicated logic, actionable error messages.

## Verdict Format

Give an explicit verdict — `APPROVE`, `REQUEST_CHANGES`, or `QUESTION` — with findings ranked: must-fix (correctness, security), should-fix (maintainability), nitpick (style). Do not mix severities.

## Receiving a Review

- Treat every comment as data. Do not argue about severity; fix or respond with evidence.
- Corrections from the reviewer are encoding opportunities: add the correction as a test or a checklist item so the same review never happens twice.
- After addressing comments, re-run the full suite before re-requesting review.
