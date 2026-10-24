#!/usr/bin/env python3
"""Static inventory and syntax audit. Never imports or executes toolkit scripts."""
from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

RISK_PATTERNS = {
    "dynamic_execution": re.compile(r"\b(exec|eval)\s*\("),
    "marshal_payload": re.compile(r"\bmarshal\.(loads|load)\s*\("),
    "encoded_payload": re.compile(r"base64\.(b64decode|decodebytes)\s*\("),
    "shell_execution": re.compile(r"\bos\.system\s*\(|subprocess\.(run|Popen|call)\s*\("),
    "network_socket": re.compile(r"\bsocket\.(socket|create_connection)\s*\("),
}
SENSITIVE_NAME_HINTS = (
    "pass.txt", "master_pass", "target_pass", "victim_logs",
    "sms_bomber", "sms_spoof", "tcp_flood", "reverse_shell",
    "revshell", "sql_inject", "web_shell", "payload_gen",
    "hash_cracker", "md5_crack", "sha1_crack", "zip_cracker",
)


def audit(root: Path) -> dict:
    root = root.resolve()
    py_files = sorted(p for p in root.rglob("*.py")
                      if ".git" not in p.parts and "__pycache__" not in p.parts)
    findings = []
    syntax_errors = []
    for path in py_files:
        rel = path.relative_to(root).as_posix()
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            findings.append({"path": rel, "kind": "unreadable", "detail": str(exc)})
            continue
        try:
            ast.parse(source, filename=rel)
        except SyntaxError as exc:
            syntax_errors.append({"path": rel, "line": exc.lineno, "detail": exc.msg})
        for label, pattern in RISK_PATTERNS.items():
            if pattern.search(source):
                findings.append({"path": rel, "kind": label,
                                 "detail": "Pattern requires manual review; not proof of malicious behavior."})
        lower_name = path.name.lower()
        if any(hint in lower_name for hint in SENSITIVE_NAME_HINTS):
            findings.append({"path": rel, "kind": "sensitive_or_high_risk_name",
                             "detail": "Review necessity, provenance, and safe handling."})
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        lower = path.name.lower()
        if any(hint in lower for hint in SENSITIVE_NAME_HINTS):
            findings.append({"path": path.relative_to(root).as_posix(),
                             "kind": "sensitive_or_high_risk_name",
                             "detail": "Review contents privately; do not print possible secrets."})
    return {
        "root": str(root),
        "python_files": len(py_files),
        "syntax_error_count": len(syntax_errors),
        "syntax_errors": syntax_errors,
        "finding_count": len(findings),
        "findings": findings,
        "note": "Static pattern matches are review flags, not verdicts. No file was executed."
    }


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    report = audit(target)
    print(json.dumps(report, indent=2))
    return 1 if report["syntax_error_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
