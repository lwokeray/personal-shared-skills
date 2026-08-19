# Official GitHub sources and integration boundaries

## 1. `microsoft/power-platform-skills`

Repository: https://github.com/microsoft/power-platform-skills

This is Microsoft's broader Power Platform plugin marketplace for Claude Code and GitHub Copilot. Its root `marketplace.json` lists these plugins:

| Plugin | Scope | Relation to this toolkit |
| --- | --- | --- |
| `power-automate` | Build, edit, run, debug, publish, and manage cloud flows through the separate FlowAgent MCP server; also includes desktop-flow and connection operations. | Complementary. The installed `powerplatform-mcp` exposes flow inventory, definitions, run history, health, cancellation, and resubmission, but not the FlowAgent tool surface. |
| `model-apps` | Build model-driven Power Apps and generative pages. | Complementary for app composition; use this toolkit for Dataverse metadata and records when the local connector is the available surface. |
| `mcp-apps` | Generate self-contained HTML MCP App widgets for visualizing MCP tool results. | Optional presentation layer; not required for Dataverse operations. |
| `power-pages` | Create and deploy Power Pages sites and related ALM workflows. | Separate Power Pages workflow; use only when the user explicitly asks for Power Pages. |
| `code-apps-preview` | Build and deploy Power Apps code apps using React, Vite, connectors, and PAC CLI. | Separate application-development workflow. |
| `mobile-app` | Build Power Apps mobile code apps with Expo/React Native and connectors. | Separate mobile workflow. |
| `canvas-apps` | Build and deploy canvas apps. | Separate canvas-app workflow. |

Installation documented by the repository includes `/plugin marketplace add microsoft/power-platform-skills` followed by selecting a plugin in compatible Claude Code/Copilot environments. Do not execute that command automatically in a Manus session; it is an external agent installation path.

## 2. `microsoft/Dataverse-skills`

Repository: https://github.com/microsoft/Dataverse-skills

This is Microsoft's Dataverse specialist plugin. It contains `dv-overview`, `dv-connect`, `dv-query`, `dv-data`, `dv-metadata`, `dv-solution`, `dv-admin`, and `dv-security`. It drives the Dataverse MCP server, Dataverse CLI, Python SDK, and PAC CLI. Use it as a routing and safety reference, not as proof that those external skills are installed in the current session.

## 3. `michsob/powerplatform-mcp`

Repository: https://github.com/michsob/powerplatform-mcp

This is the installed local stdio MCP server. It exposes tools for Dataverse entity metadata, records, plugins, Power Automate flows, solutions, classic workflows, business rules, configuration, custom APIs, web resources, security roles, dependencies, service endpoints, and MCP prompts. It requires Node.js 22+ and per-environment variables for the organization URL, client ID, client secret, and tenant ID.

## Selection rule

Use the local `PowerPlatform MCP` connector when the needed tool is present. Use an external Microsoft plugin only when the requested capability is outside the local tool surface, such as FlowAgent-based flow authoring, model-driven app composition, Power Pages, canvas apps, mobile apps, or MCP App widget generation. State the boundary explicitly and never invent one server's tools under another server's name.
