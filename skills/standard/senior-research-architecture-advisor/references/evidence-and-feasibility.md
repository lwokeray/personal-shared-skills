# Evidence and Feasibility Rules

## What Requires Current Verification

Retrieve current authoritative evidence before making a recommendation when the claim concerns any of the following:

| Claim category | Minimum evidence |
|---|---|
| Product feature, API, integration, quota, region, plan, pricing, support status, deprecation | Official documentation, release notes, or status page |
| Standard, regulation, policy, compliance obligation | Competent official authority or standards body, with effective date and jurisdiction |
| Performance, capacity, reliability, security posture | Official specification plus independently stated conditions; do not generalize benchmark results beyond their test conditions |
| Market availability, ownership, acquisition, funding, roadmap | Primary company statement or current filing; label roadmaps as non-binding unless contractual |
| Compatibility | Vendor compatibility matrix or documentation for every named component, version, edition, and operating environment |

Do not use memory, a search snippet, an undated blog post, a secondary comparison page, or a generic marketing statement as final proof for a design-sensitive claim.

## Freshness Protocol

Record both the source update date, if available, and the access date. Treat a source as potentially stale when it predates a relevant product release, policy effective date, pricing change, or announced lifecycle change. For software, check the source's stated product version and the current release or lifecycle documentation. For policies, confirm jurisdiction and effective date.

If a fact cannot be confirmed from primary sources, state the exact unknown, why it matters, and the smallest way to validate it. Do not replace the uncertainty with a confident recommendation.

## Evidence Ledger

Maintain a compact internal ledger for only decision-changing claims.

| Claim | Status | Evidence | Scope and date | Why it matters |
|---|---|---|---|---|
| [claim] | Verified / Inferred / Assumption / Unknown | URL or test | version, region, date | decision consequence |

When delivering, surface only ledger rows that affect the chosen route or could reverse the recommendation.

## Compatibility Protocol

Never say two systems integrate merely because each has an API. Verify the actual path:

1. Required data objects and permissions can be read or written.
2. Required authentication and identity model work in the target environment.
3. The necessary trigger, event, batch, or polling mechanism is supported.
4. Rate, payload, regional, plan, and retention limits satisfy the use case.
5. Failure handling, retries, idempotency, and audit needs can be met.
6. The integration is supported in the relevant product version and plan.

If any element is unverified, label the integration `Plausible—needs validation`, not `Supported`.

## Feasibility Test Design

When one unknown could reverse the decision, recommend the smallest reversible validation rather than a full implementation. State:

| Item | Required definition |
|---|---|
| Hypothesis | The exact premise being tested |
| Method | Documentation check, proof of concept, sample-data test, load test, or specialist review |
| Pass condition | Observable condition required to proceed |
| Fail condition | Observable condition that invalidates the route |
| Cost and duration | Smallest reasonable effort to learn the result |
| Next decision | What is chosen if the test passes or fails |

A proof of concept confirms a narrow condition only. Do not claim that a successful prototype proves security, scale, maintainability, or commercial viability unless those conditions were separately tested.
