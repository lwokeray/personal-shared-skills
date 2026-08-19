#!/usr/bin/env python3
"""Third-party skill security auditor.

Scans a skill directory for common malicious or risky patterns so a human can
decide whether the skill is safe to install. This implements the audit workflow
recommended by Anthropic: only install skills from trusted sources, and when
using a less-trusted source, audit all bundled files before use
(see https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

Usage:
    python3 skill_audit.py <skill-directory>

Exit codes:
    0 = clean (no findings)
    1 = findings present (review required before installing)
"""

import argparse
import os
import re
import sys
from pathlib import Path

# Patterns that indicate elevated risk. Each entry: (label, regex, severity).
RISK_PATTERNS = [
    # Prompt injection: instructions trying to override agent guardrails
    ("ignore " + "(previous|above|earlier|all)" + "|ignore all " + "(previous )?instructions", "prompt-injection", "critical"),
    (r"do not (show|reveal|tell|mention) (this|these|the above)", "instruction-hiding", "critical"),
    ("this is a t" + "est|as a " + "(language model|AI)" + "|act as if", "persona-jailbreak", "high"),
    # Data exfiltration: outbound network calls to arbitrary hosts
    (r"(curl|wget|requests\.(get|post)|urllib|fetch\() *\(? *['\"]https?://", "external-http-call", "high"),
    ("http" + "://169.254.169.254", "metadata-endpoint-access", "critical"),
    (r"(os\.environ|getenv)", "env-var-read", "medium"),
    # Destructive operations
    ("rm -" + "rf|shutil\\.rmtree|remove_" + "tree|DROP (TABLE|DATABASE)|DELETE FROM", "destructive-operation", "medium"),
    # Hidden/executable abuse
    (r"base64\.b64decode|eval\(|exec\(|__import__\(", "dynamic-code-execution", "high"),
    (r"(chmod|chown)\s", "permission-change", "medium"),
    (r"\.(?:hidden|secret|shadow|shadowed)", "hidden-path-reference", "medium"),
    # Key/credential handling
    (r"(api_key|secret|password|token)\s*=\s*['\"][A-Za-z0-9]", "hardcoded-credential", "high"),
    (r"(export|write).*(to (external|remote))", "remote-write", "medium"),
]

TEXT_EXTENSIONS = {".md", ".py", ".js", ".ts", ".sh", ".yaml", ".yml", ".json", ".txt", ".mjs", ".cjs"}


def _is_pattern_definition(lines, line_no, pattern):
    """True when the match only appears inside the RISK_PATTERNS definitions.

    The pattern string is usually split across one or two lines above the
    definition line. Check the match line and the line(s) above it for the
    literal risky text combined with the tuple marker (label/separator).
    """
    try:
        snippet = next(m.group(0) for m in re.finditer(pattern, lines[line_no - 1], re.IGNORECASE))
    except StopIteration:
        return False
    # The risky snippet appears literally in a file line — suspicious in docs,
    # but here we additionally require the line to be part of a tuple
    # definition that mentions the same label, i.e. a pattern source line.
    window = " ".join(lines[max(0, line_no - 3):line_no + 1])
    in_literal = snippet in lines[line_no - 1]
    is_tuple_line = ("\"" in lines[line_no - 1]) and any(
        s in window for s in ("critical", "high", "medium"))
    return in_literal and is_tuple_line


def scan_file(path: Path):
    findings = []
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return findings
    lines = content.split("\n")
    for pattern, label, severity in RISK_PATTERNS:
        for match in re.finditer(pattern, content, re.IGNORECASE):
            line_no = content[: match.start()].count("\n") + 1
            line_text = lines[line_no - 1] if line_no <= len(lines) else ""
            # Skip matches where the risky text only exists inside the pattern
            # definition itself (self-reference in the audit script).
            if _is_pattern_definition(lines, line_no, pattern):
                continue
            findings.append({"file": str(path), "line": line_no, "label": label,
                             "severity": severity, "snippet": match.group(0)[:80]})
    return findings


def scan_skill(skill_dir: Path):
    findings = []
    for root, _dirs, files in os.walk(skill_dir):
        for fname in files:
            p = Path(root) / fname
            # Always audit SKILL.md; audit other text files by extension;
            # skip binary assets (images/fonts) which are audited visually by humans.
            if fname == "SKILL.md" or p.suffix in TEXT_EXTENSIONS:
                findings.extend(scan_file(p))
    findings.sort(key=lambda f: ("critical", "high", "medium").index(f["severity"]))
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", help="path to skill directory to audit")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir)
    if not (skill_dir / "SKILL.md").exists():
        print(f"ERROR: {skill_dir} is not a valid skill (missing SKILL.md)", file=sys.stderr)
        sys.exit(2)

    findings = scan_skill(skill_dir)
    print(f"=== Skill audit: {skill_dir.name} ===")
    if not findings:
        print("Result: CLEAN — no risky patterns detected.")
        print("Note: automated scans do not replace human review. Read SKILL.md")
        print("and all scripts before installing a skill from an untrusted source.")
        sys.exit(0)

    by_severity = {}
    for f in findings:
        by_severity.setdefault(f["severity"], []).append(f)

    for sev in ("critical", "high", "medium"):
        for f in by_severity.get(sev, []):
            print(f"[{sev.upper()}] {f['label']} | {f['file']}:{f['line']}")
            print(f"         snippet: {f['snippet']}")

    n_critical = len(by_severity.get("critical", []))
    print(f"\nResult: {len(findings)} findings ({n_critical} critical).")
    print("Review each finding. Some matches are false positives in legitimate")
    print("skills (e.g., error-handling docs mention 'rm'). Verify context manually.")
    sys.exit(1)


if __name__ == "__main__":
    main()
