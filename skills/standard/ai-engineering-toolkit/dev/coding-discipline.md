# Coding Discipline

TDD, file structure, and commit hygiene for AI-assisted development. Adapted from obra/superpowers test-driven-development and Anthropic's Building Effective Agents.

## Workflow

Follow the red-green-refactor loop for every unit of work:

1. **Red**: write a failing test that encodes the desired behavior. A task's test comes before its code — the test defines done.
2. **Green**: implement the minimal code that makes the test pass. No gold-plating.
3. **Refactor**: clean up with the full suite green. Never refactor while tests are red.
4. **Verify and commit**: run the whole suite, then commit with a message stating what changed and why.

## Test Design Rules

- Tests describe behavior, not implementation. A reader should understand the feature from the test name alone.
- One behavior per test; tests fail for exactly one reason.
- Cover the happy path, the boundary case, and the failure mode — especially the edge cases known to bite (see `references/gotchas.md`).
- Tests run fast and deterministically. No flaky sleeps; mock external systems.
- When the human corrects an approach ("use library X instead of Y", "check edge case Z"), encode the correction as a test so it never regresses.

## File Structure Rules

- Small, focused files with one responsibility. Code you can hold in context at once is code you reason about reliably.
- Split by responsibility, not technical layer. Files that change together live together.
- Respect existing codebase conventions. Do not unilaterally restructure; propose restructuring as its own task.

## Commit Hygiene

- Frequent, small commits. Each commit is one testable change.
- Commit messages: imperative mood, one line of what, one line of why when non-obvious.
- Never commit on main/master without explicit consent; work on a branch or isolated worktree.

## Code Quality Defaults

- Prefer the standard library and well-known dependencies over clever solutions. DRY and YAGNI.
- Fail loudly and early with actionable error messages that suggest the next step (this doubles as good tool/MCP output design).
- Handle errors at boundaries; let internal code raise and propagate.
