---
name: powerplatform-mcp-toolkit
description: Operate Microsoft Power Platform and Dataverse through the configured PowerPlatform MCP connector, with safe routing for metadata, records, flows, solutions, plugins, security roles, custom APIs, configuration, and dependency checks. Use when the user asks to inspect, query, configure, troubleshoot, or safely change Dataverse, Dynamics 365, Power Automate, or Power Platform resources through MCP.
---

# PowerPlatform MCP Toolkit

Use the configured **PowerPlatform MCP** connector as the primary interface for the user's Dataverse environment. The connector is backed by `michsob/powerplatform-mcp` and currently targets environment `DEFAULT`; always pass `environment: "DEFAULT"` when the tool schema accepts it unless the user explicitly selects another configured environment.

## Operating sequence

1. **Identify the target and intent.** Separate read-only inspection from a state-changing request. Confirm the environment name and organization URL before the first change. The current configured URL is `https://org7308f083.crm.dynamics.com/`; do not disclose credentials or repeat secrets.
2. **Select the narrowest MCP tool.** Prefer a dedicated tool over a broad query. Start with metadata when the entity logical name, plural name, relationship, or attribute type is uncertain.
3. **Bound reads.** Use explicit filters and a conservative `maxRecords`. For large inventories or full definitions, prefer the CLI fallback described in `references/tool-routing.md` when it is installed; do not silently claim that a truncated MCP response is complete.
4. **Explain the proposed change.** Before any create, update, delete, publish, export, cancel, resubmit, role-privilege, or solution operation, state the exact environment, component, scope, and expected impact. Ask for confirmation unless the user has already given unambiguous authorization for that exact operation.
5. **Verify the result.** After a write, query the affected object or inventory again. For metadata changes, verify the entity/attribute or solution component. For flow actions, verify status or run details. Report the actual returned result, not an assumption.

## MCP tool routing

Use the following families exposed by the connector:

| User intent | Preferred tools |
| --- | --- |
| Entity schema | `get-entity-metadata`, `get-entity-attributes`, `get-entity-attribute`, `get-entity-relationships`, `get-entity-keys` |
| Records | `get-record`, `query-records` |
| Plugins and tracing | `get-plugin-assemblies`, `get-plugin-assembly-complete`, `get-entity-plugin-pipeline`, `get-plugin-trace-logs`, `get-all-plugin-steps`, `get-plugin-type`, `get-sdk-message` |
| Power Automate cloud flows | `get-flows`, `search-workflows`, `get-flow-definition`, `get-flow-runs`, `get-flow-run-details`, `scan-flow-health`, `get-flow-inventory` |
| Flow control | `cancel-flow-run`, `resubmit-flow-run` — treat both as state-changing |
| Solutions | `get-publishers`, `get-solutions`, `get-solution`, `get-solution-components`, `export-solution`, `add-solution-component`, `publish-customizations` |
| Classic workflows and business rules | `get-workflows`, `get-workflow-definition`, `get-ootb-workflows`, `get-business-rules`, `get-business-rule` |
| Configuration | `get-connection-references`, `get-environment-variables`, `create-environment-variable`, `set-environment-variable-value` |
| Custom APIs and web resources | `get-custom-apis`, `get-custom-api`, request/response-property tools, `get-web-resources`, `get-web-resource`, `create-web-resource` |
| Security | `get-security-roles`, `get-security-role-privileges`, `list-privileges`, role create/clone/update/delete and privilege tools |
| Dependencies and endpoints | `check-component-dependencies`, `check-delete-eligibility`, `get-service-endpoints` |

For exact schemas, required arguments, and the complete current tool list, inspect the connector at runtime rather than inventing parameters.

## Safety gates

Treat these as potentially irreversible or production-impacting: deleting roles, replacing role privileges, creating or updating metadata, creating or changing environment variables, creating plugin steps, creating web resources, adding solution components, publishing customizations, exporting solutions, cancelling or resubmitting flow runs, and any record create/update/delete. Before executing, confirm the environment URL and the specific object identifiers. For destructive role operations, require the tool's explicit confirmation field where available and explain the impact.

Never put a client secret, access token, or other credential into a prompt, source file, command line, report, or skill attachment. Do not read or parse token caches. If credentials need to be rotated, update the connector through the connector configuration workflow rather than embedding them in a script.

## Choosing related Microsoft plugins

This toolkit complements, rather than silently replaces, the official GitHub sources:

- `microsoft/power-platform-skills` is the broad Power Platform marketplace. Its relevant plugins include `power-automate`, `model-apps`, `mcp-apps`, `power-pages`, `code-apps-preview`, `mobile-app`, and `canvas-apps`.
- `microsoft/Dataverse-skills` is the Dataverse specialist plugin with `dv-connect`, `dv-query`, `dv-data`, `dv-metadata`, `dv-solution`, `dv-admin`, `dv-security`, and `dv-overview`.

Use `references/github-sources.md` when the user asks whether a capability belongs to this connector or to an external coding-agent plugin. Do not claim that the official Microsoft plugins are installed in the current Manus session unless their connectors or skill packages are independently present.

## Power Automate boundary

The installed `powerplatform-mcp` server supports flow inventory, definitions, run history, run details, health scans, cancellation, and resubmission. The Microsoft `power-automate` plugin in `microsoft/power-platform-skills` uses a separate FlowAgent MCP server for broader flow creation, editing, publishing, connections, expressions, and desktop-flow operations. Treat that plugin as a separate optional integration; do not invent FlowAgent tools on the current connector.

## Failure handling

If the host reports an output-schema or structured-content validation error after a read-only call, do not infer that authentication failed or that data was returned. Retry one different read-only tool, inspect the saved error, and report the limitation if it persists. A successful tool listing proves registration, not Dataverse data-plane access.

If a tool is unavailable, inspect the live tool list and use only the names and fields that are actually exposed. If the request exceeds this server's capability, state the gap and recommend the specific Microsoft plugin or CLI surface documented in `references/tool-routing.md`.

## Reusable local checks

Run `scripts/check_powerplatform_mcp.sh` when diagnosing local installation or connector prerequisites. It checks Node.js, the MCP executable, and the presence of required environment-variable names without printing secret values.
