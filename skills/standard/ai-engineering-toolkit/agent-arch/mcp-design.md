# MCP Server Design

Build Model Context Protocol servers the way Anthropic's mcp-builder skill and the MCP specification recommend. MCP is the standardized data layer connecting agents to external systems (market data, document stores, internal ledgers) without embedding connection logic in agents or skills.

## Architecture Decision First

MCP connectors belong in the third layer of the skills/agents/MCP separation: define once in a shared location (one `.mcp.json` or connector registry), consume everywhere. Centralization prevents config drift across agents and makes the reachable external-system surface auditable in one place.

## Recommended Stack

- **TypeScript** (primary recommendation): best SDK quality, static typing, strong linting; models generate it well. Use `streamable-http` transport for remote servers with stateless JSON; `stdio` for local servers.
- **Python + FastMCP** (alternative): fastest prototyping.
- Load current SDK docs at implementation time (`modelcontextprotocol.io` docs pages with `.md` suffix).

## Tool Design Rules

1. **Comprehensive API coverage over niche workflows.** When uncertain, prioritize covering the API's common operations; agents compose basic tools better than being handed monolithic workflows.
2. **Consistent, action-oriented naming with prefixes**: `github_create_issue`, `github_list_repos`.
3. **Strong schemas**: Zod (TS) or Pydantic (Python) with constraints and examples in field descriptions. Define `outputSchema` and return structured content where the SDK supports it.
4. **Concise descriptions + pagination + filtering.** Return focused data, not dumps.
5. **Actionable error messages**: specific suggestions and next steps, not "something went wrong."
6. **Annotations**: set `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint` truthfully — agents use these for permission reasoning.

## Security Hardening (non-negotiable)

From the MCP specification security best practices:

1. **No token passthrough.** Never accept tokens not explicitly issued for this server (validate the audience claim), and never forward unvalidated tokens downstream.
2. **SSRF defense**: reject or validate outbound URL targets — no internal IPs (192.168.x, 10.x), no cloud metadata endpoints (169.254.169.254), no localhost services, defend against DNS rebinding and redirect chains.
3. **Confused-deputy prevention** for proxy servers: per-client consent registry, CSRF protection with state parameter (cryptographically random, server-side stored, single-use, short expiry), exact `redirect_uri` string matching, frame-busting headers, secure cookie attributes.
4. **Never treat possession of a state as proof of authorization.**

## Four-Phase Build Process

1. **Research and plan**: study the target API, protocol docs, and SDK docs; list tools by endpoint coverage priority.
2. **Implement**: shared API client + auth, error helpers, pagination, then tools one at a time with schemas and descriptions.
3. **Review and test**: DRY, full type coverage, `npm run build` / `python -m py_compile`, then verify interactively with MCP Inspector (`npx @modelcontextprotocol/inspector`).
4. **Evaluate**: create ~10 complex, realistic, read-only, independently verifiable questions with known answers; run them through an LLM using the server. Questions must be stable over time and require multiple tool calls.

## Quality Checklist

- [ ] Every tool has input schema with examples, clear description, and annotations
- [ ] Errors suggest concrete next steps
- [ ] Pagination implemented on all list endpoints
- [ ] No hardcoded credentials; auth via config/env
- [ ] SSRF and token-validation controls in place
- [ ] Passes MCP Inspector inspection
- [ ] Evaluation questions all answerable and verified
