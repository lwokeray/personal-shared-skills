# Verification-Before-Completion

Never report a task done until verification actually passes. Adapted from obra/superpowers verification-before-completion and Anthropic's evaluator-optimizer loop.

## The Rule

Completion ≠ last commit. Completion = all verification gates passed and evidence recorded. Before reporting completion, run the matching checklist in `references/checklists.md` (development, debugging, review, or skill-creation checklist).

## Verification Loop

For each deliverable:

1. **Define success criteria** from the plan's acceptance criteria before verifying — never verify against a moving target.
2. **Run automated checks first**: tests, linters, type checkers, build. Actual command output, not belief.
3. **Run functional checks**: exercise the real user-facing behavior end to end (start the app, call the API, render the document).
4. **Check for regressions**: verify things that worked before still work.
5. **Record evidence**: paste the passing output or describe the concrete test performed. A claim without evidence is not verification.

## Self-Review Gate

Before completion, answer honestly:

- Did any verification get skipped because it was "probably fine"? If yes, run it now.
- Does the deliverable still match the original ask, or did scope drift?
- Are there uncommitted changes, leftover debug prints, TODO hacks, or temporary credentials?
- Would a reviewer with zero context understand what changed and why?

## Validation Loop for Iterative Work

When the deliverable can be graded objectively: do the work → run a validator (script, checklist, or self-check) → fix issues → repeat until it passes. Stop after a fixed number of failed iterations (default 3) and ask for help instead of looping indefinitely.

## Destructive or Batch Operations

For operations that modify or delete real data, use plan-validate-execute:

1. Produce the change plan in a structured format (list of actions with targets).
2. Validate the plan against the source of truth (dry-run, preview, or comparison diff).
3. Only then execute, and verify the result matches the plan.

## When to Stop and Ask

Stop and ask the human partner when: verification fails repeatedly, the success criteria are ambiguous, or completing would require violating a stated constraint (e.g., breaking an existing test to ship a feature).
