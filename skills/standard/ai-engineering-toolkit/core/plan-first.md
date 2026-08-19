# Plan-First Development

Plan before implementing. This prevents scope creep, wrong decomposition, and wasted rework. Adapted from Anthropic's three-layer agent system and obra/superpowers writing-plans.

## Announce

Announce at start: "I'm using the ai-engineering-toolkit plan-first guide to create the implementation plan."

## Process

### 1. Scope the ask

Confirm the target, constraints, and acceptance criteria before decomposing. If the request spans multiple independent subsystems, propose breaking it into separate plans — one per subsystem — each producing working, testable software on its own.

### 2. Map the file structure first

Before defining tasks, decide which files will be created or modified and each one's responsibility. This locks in decomposition decisions:

- One clear responsibility per file. Smaller, focused files outperform large ones.
- Split by responsibility, not by technical layer. Files that change together live together.
- In existing codebases, follow established patterns; do not unilaterally restructure.

### 3. Right-size tasks

A task is the smallest unit that carries its own test cycle and is worth a fresh reviewer gate. Fold setup, configuration, scaffolding, and documentation into the task whose deliverable needs them. Split only where a reviewer could reject one task while approving its neighbor. Each task ends with an independently testable deliverable.

### 4. Write bite-sized steps

Each step is one action (2–5 minutes):

- Write the failing test
- Run it to confirm it fails
- Implement the minimal code that makes it pass
- Run the tests to confirm they pass
- Commit

### 5. Write the plan document

Start with this header:

```markdown
# [Feature Name] Implementation Plan

## Overview
[Goal, constraints, acceptance criteria]

## File Structure
[File → responsibility mapping]

## Tasks
### Task 1: [name]
- [ ] Step: ...
- [ ] Step: ...
- [ ] Verification: how this task is independently testable
- [ ] Commit point
```

Save to `docs/plans/YYYY-MM-DD-<feature-name>.md`.

## Rules

- The plan is a contract: execute its steps exactly. Do not skip verifications.
- If the plan has critical gaps, raise them before starting — ask, do not guess.
- If a fundamentally better approach emerges mid-execution, stop, propose a revised plan, and wait for approval.
- Never start implementation on the main/master branch without explicit consent. Use an isolated branch or worktree.
