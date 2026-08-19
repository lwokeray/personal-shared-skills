# AI Adoption Case Slide QA Checklist

## Content fidelity

- [ ] The deck uses the requested case and does not import unrelated example content.
- [ ] Simulated or fictional material is labeled as a case/simulation.
- [ ] Every direct quote is present in the supplied source and is not over-interpreted.
- [ ] Roles, handoffs, tools, rules, dates, thresholds, and exceptions match the source.
- [ ] No unsupported metrics, benefits, compliance claims, or implementation guarantees were invented.

## Process and proposal logic

- [ ] The As-Is workflow is complete enough to explain the current operating model.
- [ ] Pain points are tied to evidence, not only adjectives such as “slow” or “complex.”
- [ ] Exception paths and out-of-scope cases are visible.
- [ ] AI assistance is distinguished from human approval and decision rights.
- [ ] The Agent blueprint names inputs, sources, tasks, outputs, integrations, and handoff points.
- [ ] Guardrails cover no-answer behavior, source/version control, privacy, access, audit, and prompt injection where relevant.
- [ ] Test cases include standard, conditional, edge, out-of-scope, and human-handoff scenarios.
- [ ] POC, pilot, scale, and operating ownership are explicit.

## Slide quality

- [ ] Cover contains only title, subtitle, and optional presenter information.
- [ ] Each content slide has one central idea.
- [ ] Titles are short and conclusion-oriented.
- [ ] Text is readable at presentation size and not clipped or overlapped.
- [ ] Tables and flow diagrams follow a clear reading order.
- [ ] Bright theme is consistent: light background, dark text, teal flow accents, amber warnings/decision gates.
- [ ] Repeated characters, icons, and visual metaphors remain consistent where used.
- [ ] No real logo, personal information, or confidential material appears in generated visuals.

## Chinese and terminology check

- [ ] All Chinese titles are visually checked, not only spell-checked from the prompt.
- [ ] Key terms such as 「規章」「轉真人」「知識庫」「條款」「護欄」「人機分工」 are correct.
- [ ] Similar-looking characters, mixed Chinese/English labels, punctuation, and numbers are checked.
- [ ] Terms such as `AI Agent`, `POC`, `Pilot`, `Scale`, `As-Is`, and `Prompt injection` are consistent.

## Targeted correction workflow

1. Record the user-visible page number, visible error, and exact replacement text.
2. Read the slide mapping from the project state rather than guessing the internal file ID.
3. Regenerate or edit only the affected slide.
4. Put the exact corrected wording in the prompt/content layer and state the character constraint.
5. Re-present the entire deck.
6. Recheck the corrected page and confirm no neighboring page changed unexpectedly.
