#!/usr/bin/env bash
set -euo pipefail

failures=0

if command -v node >/dev/null 2>&1; then
  node_version="$(node --version)"
  node_major="${node_version#v}"
  node_major="${node_major%%.*}"
  if [ "${node_major:-0}" -ge 22 ] && [ "${node_major:-0}" -lt 25 ]; then
    printf 'Node.js: %s (supported)\n' "$node_version"
  else
    printf 'Node.js: %s (requires >=22 and <25)\n' "$node_version"
    failures=$((failures + 1))
  fi
else
  printf '%s\n' 'Node.js: not found (requires >=22 and <25)'
  failures=$((failures + 1))
fi

if command -v powerplatform-mcp >/dev/null 2>&1; then
  printf 'powerplatform-mcp: %s\n' "$(command -v powerplatform-mcp)"
else
  printf '%s\n' 'powerplatform-mcp: not found'
  failures=$((failures + 1))
fi

required_names=(
  POWERPLATFORM_ENVIRONMENTS
  POWERPLATFORM_DEFAULT_URL
  POWERPLATFORM_DEFAULT_CLIENT_ID
  POWERPLATFORM_DEFAULT_CLIENT_SECRET
  POWERPLATFORM_DEFAULT_TENANT_ID
)

for name in "${required_names[@]}"; do
  if [ -n "${!name-}" ]; then
    printf '%s: present (value hidden)\n' "$name"
  else
    printf '%s: not present in this shell\n' "$name"
  fi
done

if [ "$failures" -gt 0 ]; then
  exit 1
fi
