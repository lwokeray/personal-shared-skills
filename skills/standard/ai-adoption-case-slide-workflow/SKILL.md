---
name: ai-adoption-case-slide-workflow
description: "Case-based AI adoption consulting and bright visual slide production. Use when the user provides a case-study PDF, interview transcript, policy document, SOP, or workflow evidence and asks to analyze AI adoption opportunities, design an AI Agent proposal, create a case-based presentation, or turn the findings into a bright image-based slide deck with QA and targeted slide corrections."
---

# AI Adoption Case-to-Slide Workflow

## Overview

Use this skill to turn case evidence into a defensible AI adoption proposal and, when requested, a bright image-based presentation. Preserve the distinction between source evidence, interpretation, candidate requirements, AI assistance, human decisions, risks, validation tests, and presentation copy.

This skill is for case-based work, not generic slide decoration. It is especially useful for PDF/DOCX case studies, interview transcripts, policy excerpts, SOPs, customer-service workflows, HR processes, internal FAQ assistants, and AI Agent implementation proposals.

## Workflow decision tree

1. **Determine the source material.**
   - If the user provides PDF, DOCX, images, transcripts, or policy files, inspect the files first.
   - If the source is sensitive or fictional, anonymize names and label simulated material as a case, not as real research.
   - If no source evidence exists, ask for the missing context before presenting detailed claims.

2. **Determine the deliverable.**
   - If the user wants analysis only, produce the evidence and proposal artifacts without creating slides.
   - If the user wants a presentation, write the slide outline before generating pages.
   - If the user explicitly requests image-generated slides or an image-based deck, use `slide_initialize` with `generate_mode: image`, then generate each page with `image_slide_generate` and finish with `slide_present`.
   - If exact editable text, dense tables, or pixel-precise diagrams are essential, prefer `html` or `pptx` mode and keep AI-generated imagery decorative rather than using it for the exact text layer.

3. **Handle revisions locally.**
   - When the user reports a bad word, wrong page, or visual defect, map the user-visible page number to the internal slide ID before editing.
   - Regenerate or edit only the affected page unless the user requests a global redesign.
   - Re-present the full deck after a targeted correction.

## Core workflow

### Step 1 — Inspect and preserve source evidence

Read every supplied source that materially affects the proposal. For PDFs, inspect the rendered pages and save key findings to a text note before continuing. For DOCX files, extract the full text and preserve direct quotes, section names, tables, thresholds, dates, and exceptions.

Create an evidence ledger with these fields:

- source file and page/section
- role or stakeholder
- direct quote or exact rule
- observed action or workflow step
- tool/system/document used
- pain point, delay, error, or risk
- exception or boundary condition
- candidate requirement
- confidence and unresolved question

Never convert a direct quote into a factual claim beyond what the source supports. If the material is a simulation, state that clearly in the proposal and slides.

### Step 2 — Extract the operating model

Build these artifacts before writing slide copy:

1. **Stakeholder map:** requester, operator, approver, recipient, support owner, risk owner, data owner, and affected user.
2. **As-Is workflow:** trigger → actions → handoffs → systems/documents → waiting → decision → outcome.
3. **Pain-point map:** repeated work, delay, missing information, inconsistent answers, poor traceability, user experience, and compliance risk.
4. **Exception map:** urgent cases, VIP cases, paper/manual paths, internal referrals, missing data, special terms, and out-of-scope topics.
5. **Decision-boundary map:** what AI may draft, summarize, classify, recommend, or route; what a human must approve, decide, or own.

Use the supplied `templates/case_analysis_notes_template.md` when starting a new case.

### Step 3 — Separate rule retrieval from case judgment

For policy or FAQ agents, classify questions into three categories:

| Category | Agent behavior |
|---|---|
| General rule | Answer from approved sources and cite the rule/section. |
| Conditional question | Ask for required conditions, show the calculation or rule, and avoid pretending to know missing personal facts. |
| Case-specific or out of scope | Explain the limit and hand off to the named human owner. |

Never let an FAQ Agent invent policies, decide personal eligibility, approve compensation, determine hiring outcomes, or resolve an exception unless the source explicitly authorizes that behavior and a human owner is still accountable.

For every AI proposal, define at least:

- approved knowledge sources and version owner
- retrieval/search method
- answer format
- uncertainty and no-answer behavior
- human handoff route
- logging and audit fields
- privacy and access controls
- prompt-injection and instruction-conflict handling
- test questions, including edge cases and out-of-scope cases

### Step 4 — Form the AI adoption thesis

Write one sentence that connects evidence to intervention:

> Because [role] currently performs [repeated or risky work] through [fragmented process], an AI Agent can [assist with bounded task] while [human owner] retains [high-risk decision], validated through [POC/pilot test].

Then define the Agent blueprint:

- inputs and source systems
- retrieval or transformation step
- Agent task and tool calls
- output and user interface
- human approval or takeover point
- failure and escalation path
- measurable validation criteria

Avoid claims such as “AI will automate the whole process” unless the source and governance model explicitly support them.

### Step 5 — Design the presentation story

For a standard case-based deck, use 8–12 slides and one central idea per page:

1. Cover: case title and promise.
2. Why this is a workflow problem, not a tool purchase.
3. Case context and stakeholder roles.
4. Source evidence and direct pain points.
5. As-Is workflow and exception paths.
6. AI-suitable work versus human-only decisions.
7. Agent blueprint: inputs, retrieval, tasks, outputs, integrations.
8. Guardrails and human-in-the-loop design.
9. Test cases and validation criteria.
10. POC → pilot → scale and operating ownership.
11. Success standard or decision summary.

Use `templates/slide_outline_template.md` to draft the content. Keep titles insight-driven, content concise, and tables/flows limited to what the audience needs to decide.

### Step 6 — Establish visual direction

For a bright image-based deck, use a warm-white or light-grey background, dark-grey text, teal for flow/collaboration, and amber orange for pain points, warnings, and decision gates. Use a consistent editorial documentary or clean business-illustration style.

Define before generation:

- palette and contrast
- recurring roles or characters
- diagram language
- whitespace and text-safe areas
- slide aspect ratio
- whether exact text is essential or can be treated as illustrative

Do not use real company logos, personal data, or confidential information in generated visuals. Use role names or anonymized labels.

### Step 7 — Generate the deck

When using image mode:

1. Initialize the complete slide outline once.
2. Generate the cover first to establish the visual baseline.
3. Generate content slides one at a time.
4. Include exact required titles and critical labels in each prompt.
5. Reference the previous generated slide for continuity whenever possible.
6. Vary composition while preserving the palette and visual language.
7. Avoid overly dense pages; use a separate slide for tables, workflow diagrams, guardrails, or test cases when needed.

For a policy FAQ case, favor visuals such as approved knowledge libraries, retrieval pipelines, decision boundaries, human handoff, shield/guardrail metaphors, test matrices, and POC roadmaps.

### Step 8 — QA before delivery

Present the complete deck and inspect it page by page. Check:

- source fidelity and case naming
- role and workflow consistency
- quote and rule accuracy
- correct page order
- readable text and no clipping
- Chinese character accuracy, especially in titles and key terms
- diagrams and arrows that follow the intended reading order
- AI/human boundary and escalation path
- POC/pilot/scale logic
- no unsupported certainty or fabricated metrics

Use `references/qa_checklist.md` for the full checklist.

AI-generated Chinese text can contain malformed characters even when the prompt is correct. If a user reports a bad character, identify the user-visible page and internal slide ID, then regenerate only that page with the exact corrected text and an explicit character constraint. Re-present the deck after the correction.

## Reusable output requirements

For a complete case-based AI adoption deck, aim to produce:

- evidence ledger or case analysis notes
- stakeholder and As-Is workflow summary
- AI boundary and guardrail model
- slide content outline
- generated slide project
- QA record or correction note when defects occur
- final presentation link through `slide_present`

Do not present a polished visual as if it were validated implementation. Label simulations, assumptions, candidate requirements, and untested benefits clearly.

## Resources

Read these only when needed:

- [Case analysis template](templates/case_analysis_notes_template.md): start here when source files are provided.
- [Slide outline template](templates/slide_outline_template.md): use before initializing a deck.
- [QA checklist](references/qa_checklist.md): use before presenting or after a targeted correction.
- [Agent guardrails](references/agent_guardrails.md): use for FAQ, policy, HR, finance, or other high-impact assistants.

## Final delivery

Use `slide_present` for finished presentations. In the final user message, attach the returned `manus-slides://...` URI and briefly state what the deck is based on. For a skill-creation task, attach this skill's `SKILL.md` path so the system can package the directory as an installable skill.
