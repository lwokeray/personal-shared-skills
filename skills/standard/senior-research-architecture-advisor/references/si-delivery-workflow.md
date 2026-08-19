# SI Senior Architecture Delivery Workflow

## Purpose

Use this workflow for architecture work performed in a systems-integration context. The architecture function spans presales, discovery, delivery, governance, and operational evolution. Scale each phase to the engagement; do not omit a phase merely because the client has already proposed a solution.

## Phase map

| Phase | Senior architect objective | Core artifacts | Exit condition |
|---|---|---|---|
| Opportunity / qualification | Decide whether the request is technically and commercially credible enough to pursue. | Solution brief, scope/in-scope/out-of-scope, initial assumptions/dependencies, option outline, estimate basis. | Client outcome, critical constraints, and high-level delivery path are understood; deal-breaking unknowns are visible. |
| Discovery / current state | Replace proposal assumptions with facts about the business, landscape, integration boundaries, data, NFRs, and operations. | Workshop findings, current-state views, requirement traceability, interface/data inventory, RAID log. | Critical systems, owners, quality targets, and constraints are known or explicitly carried as risk. |
| Solutioning / target state | Create an architecture that meets client outcomes and can be delivered and supported. | Architecture principles, target-state views, ADRs, option comparison, roadmap, solution estimate assumptions. | Preferred route is traceable to requirements; major tradeoffs, dependencies, and operating model are accepted. |
| Prove / de-risk | Test the assumptions capable of causing material rework, non-delivery, breach, or cost overrun. | Evidence ledger, PoC/spike/test results, updated risk log and ADRs. | Critical feasibility gates pass, or a pivot/exception is approved. |
| Delivery design / mobilization | Convert intent into work that teams can implement and verify. | Detailed design, interface contracts, backlog/work packages, environment plan, NFR acceptance, test/migration/release plans. | Work can be sequenced, owned, estimated, tested, and governed; dependency owners have committed. |
| Implementation governance | Protect architectural integrity while resolving delivery discoveries and scope changes. | Design-review record, ADR/change log, issue escalation, quality dashboard, architecture baseline. | Changes have impact analysis and approval; test evidence supports each material decision. |
| Go-live / hypercare | Decide whether the solution is safe and supportable to release, then stabilize it with evidence. | Operational readiness, go/no-go, rollback, runbooks, monitoring/alerting, hypercare review. | Functional and NFR acceptance pass; support ownership and recovery procedures are in place. |
| Evolution | Reassess the architecture from observed usage, cost, incidents, new requirements, and product lifecycle change. | Metrics review, technical-debt/optimization backlog, roadmap and decision updates. | Next investment or change decisions are evidence-based. |

## Discovery workshop discipline

Use workshops to expose decisions and constraints, not to collect endless requirements. Ask only questions that affect solution choice, estimate, architecture, or acceptance. Prioritize:

1. What outcome is valuable enough to justify this work, and how will success be measured?
2. Which systems, people, data, and vendors are in scope? Who owns each boundary?
3. What must work under normal, peak, failed, and recovery conditions?
4. What quality attributes are contractually, operationally, or regulatorily required?
5. Which current facts are assumptions? Which assumption would make the proposed route impossible or uneconomic?
6. What decisions, access, procurement, data, environment, or test dependencies are outside the delivery team’s control?

Document an answer only once and link it to subsequent requirements, decisions, risks, and tests.

## Architecture decision record discipline

Create an ADR for a decision that is hard to reverse, affects multiple teams, changes cost/risk materially, or establishes a reusable pattern. Use the following fields:

| Field | Record |
|---|---|
| Decision ID and status | Proposed, accepted, superseded, rejected, or deferred |
| Context | Outcome, scope, constraints, and triggering issue |
| Options | Viable alternatives—including the option not to change |
| Decision and rationale | Chosen route and evidence / tradeoffs |
| Consequences | Delivery, operational, security, cost, and lifecycle implications |
| Assumptions / dependencies | Facts that must remain true |
| Validation | Required PoC, test, review, or specialist approval |
| Revisit trigger | Condition that invalidates or reopens the decision |
| Owners / approvals | Accountable owner, consulted parties, and decision authority |

## Design authority and change control

Operate as technical authority rather than as a bottleneck. Review only changes with material impact on interfaces, data, quality attributes, security/compliance, deployment topology, dependencies, delivery commitment, or operational ownership.

For every material change, state the architecture impact, delivery impact, operational impact, risk, cost/time effect, decision owner, and whether a prior ADR/feasibility gate must be reopened. Escalate when a request trades away accepted NFRs, violates a supported configuration, creates unowned operational work, or changes contracted scope.

## Go-live readiness

A feature-complete solution is not necessarily releasable. Confirm the following when applicable:

| Readiness area | Evidence required |
|---|---|
| Functional and integration | Acceptance, contract, error-path, reconciliation, and dependency test results |
| Quality attributes | Performance/capacity, availability/recovery, security, accessibility, and resiliency evidence against targets |
| Data and migration | Data quality, migration/reconciliation, retention, and rollback readiness |
| Operations | Monitoring, dashboards, alerts, runbooks, on-call/support model, patching, backup/restore |
| Release | Environment parity, approvals, cutover plan, go/no-go decision, rollback, communications, hypercare owners |
| Governance | Decision log, residual-risk acceptance, documentation, handover, and escalation contacts |

When evidence is missing, classify the status as `Not ready`, `Ready with accepted risk`, or `Ready`, and state the decision authority.
