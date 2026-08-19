# PowerPlatform MCP routing reference

## Local connector tool groups

The local `PowerPlatform MCP` connector is backed by `michsob/powerplatform-mcp`. Inspect its live tool list before calling any operation because names and schemas can change between versions.

| Domain | Read / inspect | State-changing or potentially impactful |
| --- | --- | --- |
| Entity metadata | `get-entity-metadata`, `get-entity-attributes`, `get-entity-attribute`, `get-entity-relationships`, `get-entity-keys` | `create-entity-string-attribute`, `create-entity-alternate-key` |
| Records | `get-record`, `query-records` | record creation/update/deletion tools if exposed by the installed version |
| Plugins | `get-plugin-assemblies`, `get-plugin-assembly-complete`, `get-entity-plugin-pipeline`, `get-plugin-trace-logs`, `get-all-plugin-steps`, `get-plugin-type`, `get-sdk-message` | `create-plugin-step` |
| Flows | `get-flows`, `search-workflows`, `get-flow-definition`, `get-flow-runs`, `get-flow-run-details`, `scan-flow-health`, `get-flow-inventory` | `cancel-flow-run`, `resubmit-flow-run` |
| Solutions | `get-publishers`, `get-solutions`, `get-solution`, `get-solution-components` | `export-solution`, `add-solution-component`, `publish-customizations` |
| Classic workflows / rules | `get-workflows`, `get-workflow-definition`, `get-ootb-workflows`, `get-business-rules`, `get-business-rule` | Treat any activation/deactivation or update operation as a change and confirm scope. |
| Configuration | `get-connection-references`, `get-environment-variables` | `create-environment-variable`, `set-environment-variable-value` |
| Custom APIs / resources | `get-custom-apis`, `get-custom-api`, request/response property reads, `get-web-resources`, `get-web-resource` | Custom API creation, request/response property creation, and `create-web-resource` |
| Security | `get-security-roles`, `get-security-role-privileges`, `list-privileges` | security role create/clone/update/delete and add/remove/replace privilege operations |
| Dependencies / endpoints | `check-component-dependencies`, `check-delete-eligibility`, `get-service-endpoints` | The dependency checks are read-only; deletion or publish must still be confirmed separately. |

## CLI fallback

The repository also publishes `powerplatform-cli`. Use it when a result is too large for MCP context or when a CLI-only operation is required. Typical read commands include `solutions`, `solution <uniqueName>`, `solution-components <uniqueName>`, `flows`, `flow-definition <flowId>`, `flow-runs <flowId>`, `flow-health`, `entity-metadata <entityName>`, `entity-attributes <entityName>`, `query-records <entityNamePlural> <filter>`, and `plugin-trace-logs`. The CLI writes full results to a `.pp-cache/<environment>/` directory. Do not assume a CLI command exists; check `powerplatform-cli --help` or the repository README first.

## External Microsoft plugin fallback

Use `microsoft/power-platform-skills` when the request concerns Power Automate authoring through FlowAgent, model-driven app generation, Power Pages, code apps, mobile apps, canvas apps, or MCP App widgets. Use `microsoft/Dataverse-skills` when the request needs its documented Dataverse CLI/Python SDK/PAC CLI workflows, larger-volume data operations, advanced schema operations, or solution ALM patterns beyond the local MCP server.

## Verification rule

A successful connector tool listing confirms MCP registration. It does not prove that a Dataverse call returned valid structured data. If a read-only call fails with `Output validation error` because structured content is missing, retry one different read-only tool once, inspect the saved error, and report the host/server response-format limitation if it persists. Do not convert that error into an authentication success or failure claim.
