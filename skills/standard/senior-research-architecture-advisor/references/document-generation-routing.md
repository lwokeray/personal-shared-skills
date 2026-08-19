# Document Generation Routing

Use the smallest complete document set that matches the engagement mode, audience, and decision. Do not generate every template by default. Ask for the target format and audience only when they change the document.

## Engagement routing

| Situation / trigger | Generate first | Add when evidence or scope requires |
|---|---|---|
| RFP, presales, proposal, “can we do this?” | `solution-brief.md` | `client-solution-proposal.md`, `client-executive-decision-brief.md`, `delivery-plan-estimate.md`, `feasibility-poc.md` |
| Unknown current landscape or conflicting requirements | `discovery-current-state.md` | `requirements-traceability.md`, `client-business-readiness-assessment.md`, `client-stakeholder-engagement-plan.md` |
| Target solution or platform design | `solution-architecture-hld.md` | `architecture-decision-record.md`, `integration-interface-contract.md`, `feasibility-poc.md` |
| Important architecture choice | `architecture-decision-record.md` | `architecture-review-board.md` when cross-team, strategic, standard-setting, high-cost, or high-risk |
| API, event, data, or system integration | `integration-interface-contract.md` | `solution-architecture-hld.md`, `feasibility-poc.md`, `migration-runbook.md` when data movement is involved |
| High-risk, novel, unsupported, or unverified premise | `feasibility-poc.md` | `architecture-decision-record.md` after the test; update the HLD if the result changes the route |
| Implementation mobilization or delivery planning | `delivery-plan-estimate.md` | `client-solution-proposal.md`, `solution-architecture-hld.md`, `operations-readiness.md`, `go-live-readiness.md` |
| Migration programme or migration wave | `migration-runbook.md` | `delivery-plan-estimate.md`, `operations-readiness.md`, `go-live-readiness.md`, `client-acceptance-transition.md` |
| Production support, handover, CloudOps/DevOps choice | `operations-readiness.md` | `client-acceptance-transition.md`, `go-live-readiness.md`, `change-impact-assessment.md` |
| Architecture board or design authority review | `architecture-review-board.md` | Relevant HLD, ADRs, evidence, readiness documents, and client decision brief |
| Scope, platform, interface, requirement, or design change | `change-impact-assessment.md` | New or superseding `architecture-decision-record.md`; update impacted HLD, contract, plan, runbook, or readiness documents |
| Release, cutover, or go/no-go decision | `go-live-readiness.md` | `migration-runbook.md`, `operations-readiness.md`, residual-risk ADR, `client-acceptance-transition.md` |

## Internal audience routing

Identify the internal owner, decision right, and handoff point before generating an internal artifact. Internal documents should expose unresolved assumptions and delivery risk clearly; they are not client-facing summaries.

| Internal audience / situation | Primary need | Generate or translate into |
|---|---|---|
| Account Manager / Sales / Pursuit | Qualification, win strategy, client politics, commercial boundary, no-bid decision | `internal-opportunity-solutioning.md`, `solution-brief.md`, `client-executive-decision-brief.md` |
| Presales / Solution Engineering | Discovery, options, demos, PoC, scope and technical claims | `internal-opportunity-solutioning.md`, `feasibility-poc.md`, `internal-practice-technical-brief.md` |
| Project / Programme Manager | Feasible scope, plan, dependencies, resources, acceptance, risk | `internal-sales-to-delivery-handover.md`, `internal-delivery-mobilization.md`, `delivery-plan-estimate.md` |
| Delivery / Engineering / SME | Buildability, detailed design, work packages, interfaces, test and runbooks | `solution-architecture-hld.md`, `integration-interface-contract.md`, `requirements-traceability.md`, `internal-architecture-sync.md` |
| Security / Compliance | Controls, exceptions, evidence, data boundaries, approval | `architecture-review-board.md`, `operations-readiness.md`, `internal-architecture-sync.md` |
| Finance / Commercial | Margin, estimate assumptions, billing, contract risk, change impact | `internal-opportunity-solutioning.md`, `internal-sales-to-delivery-handover.md`, `change-impact-assessment.md` |
| Procurement / Vendor Management | Product qualification, quotations, licensing, lead time, supplier risk | `internal-vendor-evaluation.md`, `internal-sales-to-delivery-handover.md` |
| Legal / Contract | Obligations, liability, acceptance, exclusions, risk ownership | `internal-sales-to-delivery-handover.md`, `client-solution-proposal.md`, `change-impact-assessment.md` |
| Managed Services / Operations | Support model, service transition, monitoring, runbooks, readiness | `operations-readiness.md`, `internal-delivery-mobilization.md`, `client-acceptance-transition.md` |
| Practice Lead / Leadership | Reusable patterns, quality, capability, margin, portfolio risk | `internal-practice-technical-brief.md`, `internal-vendor-evaluation.md`, `internal-enablement-session.md`, `internal-architecture-sync.md` |
| Cross-functional conflict or blocker | Fast alignment, decision, escalation, ownership | `internal-architecture-sync.md`, then `architecture-decision-record.md` if architecturally significant |
| Awarded opportunity entering delivery | Scope and commercial continuity, resource and vendor readiness, accountability transfer | `internal-sales-to-delivery-handover.md`, `internal-delivery-mobilization.md` |

## Client-facing audience routing

Identify the audience and decision context before generating an external document. Do not send internal technical artifacts directly to every client audience.

| Client audience | Primary need | Generate or translate into |
|---|---|---|
| Executive sponsor / steering committee | Outcome, investment, risk, decision, consequence of delay | `client-executive-decision-brief.md`, `client-steering-status-report.md` |
| Business owner / product owner | Current-to-target gap, process impact, acceptance, benefits | `client-business-readiness-assessment.md`, `client-acceptance-transition.md` |
| Client PMO / programme lead | Scope, milestones, dependencies, RACI, risks, governance | `client-solution-proposal.md`, `client-steering-status-report.md`, `delivery-plan-estimate.md` |
| Client enterprise / solution architect | Architecture, options, standards, evidence, integration, ADR | `solution-architecture-hld.md`, `architecture-decision-record.md`, `architecture-review-board.md` |
| Client security / compliance | Data, trust boundaries, controls, evidence, exceptions, approvals | HLD security view, `architecture-review-board.md`, `operations-readiness.md` |
| Client operations / service owner | Support model, handover, monitoring, runbooks, SLOs, recovery | `operations-readiness.md`, `client-acceptance-transition.md`, `go-live-readiness.md` |
| Procurement / commercial / vendor management | Scope, assumptions, estimate basis, contractual boundaries, supplier responsibilities | `client-solution-proposal.md`, `solution-brief.md`, `delivery-plan-estimate.md` |
| End users / affected teams | What changes, when, why, how to prepare, support path | `client-discovery-workshop.md`, `client-acceptance-transition.md`, plain-language release brief |

## Client-facing communication rules

1. Start with the client outcome, not the supplier’s technology or internal workstream.
2. Separate `client decision required`, `client action required`, `supplier recommendation`, and `information only`.
3. State what changes for the client, what does not change, and what the client must provide or approve.
4. Translate technical risk into client impact: service, time, investment, compliance, adoption, operations, or reversibility.
5. Keep implementation detail and unresolved technical debate in linked appendices or internal artifacts, but never hide material risk from the client.
6. Use plain language for executive and business audiences without removing caveats, evidence status, ownership, or decision consequences.
7. Before issuing an external document, check that claims, scope, estimates, commitments, service levels, responsibilities, and approval status agree with the internal source documents.

## Generation rules

1. Start with a one-paragraph architect position and the decision requested.
2. Populate the template with known facts and mark every unverified item as `Assumption`, `Open question`, `Risk`, `Not assessed`, or `Pending approval`.
3. Do not invent values for volumes, targets, costs, versions, owners, dates, approvals, or test evidence. Put them in the validation backlog.
4. Link documents through IDs: requirements, ADRs, interfaces, risks, changes, tests, approvals, benefits, and handovers.
5. Keep ADRs atomic and append-only; when the context changes, generate a new superseding ADR rather than editing history.
6. For material SI work, generate in this order: solution brief → discovery/current state → requirements traceability → HLD/options → feasibility/ADR → delivery plan → integration/runbooks/operations → review board/go-live → client acceptance/transition.
7. If the requested artifact is only a summary, provide the summary and state which full document would be generated next; do not replace a needed governance artifact with prose.
