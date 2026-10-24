#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

CYAN='\033[1;36m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
RED='\033[1;31m'
RESET='\033[0m'

say() { printf "%b%s%b\n" "$1" "$2" "$RESET"; }
fail() { say "$RED" "[!] $1"; exit 1; }

say "$CYAN" "Cyber-Toolkit setup • safe dependency mode"

if [[ -d "/data/data/com.termux/files/usr" ]]; then
  command -v pkg >/dev/null 2>&1 || fail "Termux package manager not found."
  say "$GREEN" "[+] Termux detected"
  pkg update -y
  pkg install -y python git curl wget jq openssl
  PYTHON_BIN="$(command -v python)"
elif [[ -f /etc/os-release ]]; then
  command -v apt-get >/dev/null 2>&1 || fail "This installer currently supports Termux or apt-based Linux."
  if [[ "$(id -u)" -eq 0 ]]; then SUDO=(); else command -v sudo >/dev/null 2>&1 || fail "Install sudo or run as root."; SUDO=(sudo); fi
  "${SUDO[@]}" apt-get update
  "${SUDO[@]}" apt-get install -y python3 python3-venv python3-pip git curl wget jq openssl
  PYTHON_BIN="$(command -v python3)"
else
  fail "Unsupported OS. Install Python 3.10+ and pip, then run: python -m venv .venv"
fi

[[ -n "${PYTHON_BIN:-}" ]] || fail "Python executable not found."
"$PYTHON_BIN" -c 'import sys; print("Python", sys.version)' || fail "Python is not working."

if [[ ! -f core/requirements.txt ]]; then
  fail "core/requirements.txt is missing."
fi

if [[ ! -d .venv ]]; then
  "$PYTHON_BIN" -m venv .venv || fail "Could not create .venv. On Debian/Ubuntu install python3-venv."
fi

VENV_PY="$ROOT/.venv/bin/python"
[[ -x "$VENV_PY" ]] || VENV_PY="$ROOT/.venv/bin/python3"
[[ -x "$VENV_PY" ]] || fail "Virtual-environment Python not found."

"$VENV_PY" -m pip install --upgrade pip
"$VENV_PY" -m pip install -r core/requirements.txt || fail "Dependency installation failed; see pip output above."
"$VENV_PY" -m compileall -q core DroidCheck_FilePilot_NetPulse || fail "Python syntax check failed."

say "$GREEN" "[+] Dependencies installed in .venv"
say "$GREEN" "[+] Python syntax check passed"
printf "\nNext steps:\n  source .venv/bin/activate\n  python main.py\n"
printf "Optional static audit (does not execute tools):\n  .venv/bin/python core/audit_toolkit.py .\n"
say "$YELLOW" "Review SECURITY.md and AUDIT_REPORT.md before running legacy modules."
