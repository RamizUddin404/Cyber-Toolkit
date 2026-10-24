#!/usr/bin/env python3
"""Root entry point for Cyber-Toolkit.

Uses the current Python interpreter and an argument-list subprocess call.
The legacy menu and its tool scripts still require individual safety/functionality review.
"""
from pathlib import Path
import subprocess
import sys


def main() -> int:
    repo_root = Path(__file__).resolve().parent
    core_main = repo_root / "core" / "main.py"
    if not core_main.is_file():
        print("[!] Error: core/main.py not found. Please check the repository checkout.")
        return 1
    try:
        completed = subprocess.run([sys.executable, str(core_main)], cwd=str(core_main.parent), check=False)
        return completed.returncode
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
        return 130
    except OSError as exc:
        print(f"[!] Unable to launch core/main.py: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
