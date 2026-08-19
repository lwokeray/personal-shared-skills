---
name: power-apps-component-collection
description: Collect, select, scaffold, and integrate Microsoft Power Apps components, PCF code components, Canvas Apps, model-driven apps, code apps, connectors, and Dataverse-backed UI assets from the bundled official GitHub sources. Use when the user asks for Power Apps components, PCF controls, custom controls, code components, component samples, reusable app UI, or related Microsoft Power Platform skills.
---

# Power Apps Component Collection

Use this skill as a curated index of official Microsoft Power Platform skills and Power Apps Component Framework samples. The bundled `references/catalog.md` maps capabilities to GitHub paths, while `assets/pcf-samples/` contains source snapshots from Microsoft’s official `PowerApps-Samples` repository. The package is a reference and starting point; it does not imply that every external Microsoft plugin or local component has been installed or deployed.

## Select the correct asset family

1. **Need a reusable custom control or PCF sample?** Start with `assets/pcf-samples/`. Read the sample README and `ControlManifest.Input.xml` before copying or modifying it.
2. **Need to create or edit a Canvas App?** Use the `canvas-apps` entries in `references/catalog.md`, especially `canvas-app` and `add-data-source`. Canvas Authoring MCP is a separate surface from the local Dataverse/PowerPlatform MCP connector.
3. **Need a model-driven app or generative page?** Use `model-apps/app-builder` or `model-apps/genpage`; these are app-composition workflows, not PCF compilation workflows.
4. **Need a React/Vite code app or connector?** Use the `code-apps` entries, especially `create-code-app`, `add-dataverse`, `add-connector`, `list-connections`, and `deploy`.
5. **Need a mobile app control or native capability?** Use the `mobile-apps` entries, especially `add-native`, `add-dataverse`, `create-mobile-app`, and `setup-datamodel`.
6. **Need a visual UI for an MCP tool result?** Use `mcp-apps/generate-mcp-app-ui`; this generates an MCP App widget and is not the same as a PCF control.

## PCF sample workflow

1. Pick a sample by behavior, not by name alone. Use dataset samples for grids, React/virtual samples for component rendering patterns, API samples for host APIs, and input samples for field-level controls.
2. Read the sample README and manifest. Record its constructor, control type, properties, data-set declarations, host requirements, and any API keys or external services. Never copy secrets from sample configuration.
3. Copy only source, manifest, package metadata, and documentation. Exclude `node_modules`, `obj`, `bin`, generated bundles, and local caches.
4. Rename the namespace, constructor, display name, and publisher prefix for the target solution. Keep the publisher prefix explicit; do not assume `new` or `sample` is appropriate.
5. Install dependencies and run the repository’s documented build checks. A normal Microsoft sample flow uses `npm install`, `msbuild /t:restore`, `pac solution init`, `pac solution add-reference`, and MSBuild packaging. On Linux or a host without MSBuild/PAC CLI, do not claim the solution was built; provide the exact missing prerequisite.
6. Validate the manifest and host support before deployment. For model-driven and Canvas Apps, follow the official add-component guidance linked from the sample README. Confirm the target environment and solution before any import or publish operation.
7. After deployment, verify the control in the intended host and report the actual outcome. Do not infer Canvas support, model-driven support, API availability, or deployment success solely from the presence of a sample directory.

## Safety and provenance

Treat the bundled repositories as source material. Preserve their original licenses and source links when redistributing or modifying samples. Do not execute install or deployment commands copied from a repository without checking the command and target first. Do not put Client Secrets, tokens, API keys, or tenant credentials into sample source, manifests, reports, or this skill.

The local `PowerPlatform MCP` connector can inspect Dataverse metadata, records, flows, solutions, plugins, security, and configuration, but it is not a PCF compiler and does not replace Canvas Authoring MCP, FlowAgent MCP, PAC CLI, or MSBuild. Use the connector for environment inspection and solution metadata where its live tool list supports the request; use the official component build workflow for PCF packaging.

## Bundled references

- `references/catalog.md` — curated inventory of official Microsoft skills and PCF samples.
- `references/build-and-deploy.md` — source-grounded PCF build, solution packaging, and deployment checklist.
- `assets/pcf-samples/` — source snapshot of the official `component-framework` samples, excluding generated dependencies and caches.
