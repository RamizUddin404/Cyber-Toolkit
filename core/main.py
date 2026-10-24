#!/usr/bin/env python3
"""Cyber-Toolkit unified launcher for Termux/Linux.

Discovers every top-level Python tool in core/, groups tools into categories,
checks known Python imports, and offers optional installation of allowlisted
Python packages. Legacy high-risk modules remain visible but disabled by default.
"""
from __future__ import annotations

import ast
import importlib.util
import os
import platform
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

CORE_DIR = Path(__file__).resolve().parent
REPO_DIR = CORE_DIR.parent
INTERNAL_FILES = {
    "__init__.py", "main.py", "audit_toolkit.py", "cyber_deps.py",
    "inspect_tools.py",
}
# Explicit blocklist: these legacy modules are inventoried but not launched by default.
BLOCKED_TOOLS = {
    "arp_spoof", "call_spoof", "cam_hacker", "dos_attack", "email_spoof",
    "ftp_force", "frp_bypass_helper", "god_mode", "god_mode_ultimate",
    "hash_cracker", "md5_crack", "sha1_crack", "ssh_force", "sms_bomber",
    "sms_spoof", "sql_injector", "tcp_flooder", "reverse_shell", "revshell_gen",
    "web_shell_pro", "payload_gen", "phishing_sim", "universal_cracker",
    "zip_cracker", "wifi_pass_view", "ip_rotator",
}
# Python import name -> PyPI distribution name. Only these mappings can be installed.
PIP_ALLOWLIST = {
    "requests": "requests",
    "colorama": "colorama",
    "bs4": "beautifulsoup4",
    "mechanize": "mechanize",
    "jwt": "PyJWT",
    "cryptography": "cryptography",
    "PIL": "Pillow",
    "paramiko": "paramiko",
    "dns": "dnspython",
    "whois": "python-whois",
    "nmap": "python-nmap",
    "scapy": "scapy",
    "rich": "rich",
    "qrcode": "qrcode",
    "PIL.Image": "Pillow",
    "Crypto": "pycryptodome",
    "nacl": "PyNaCl",
    "bs4.element": "beautifulsoup4",
}
# Package modules that are part of Python itself and must not be pip-installed.
STDLIB = set(getattr(sys, "stdlib_module_names", ())) | {
    "os", "sys", "time", "json", "re", "math", "random", "socket", "ssl",
    "subprocess", "platform", "pathlib", "typing", "argparse", "hashlib",
    "base64", "binascii", "secrets", "string", "datetime", "collections",
    "itertools", "threading", "multiprocessing", "urllib", "http", "email",
    "html", "csv", "sqlite3", "shutil", "tempfile", "textwrap", "logging",
    "getpass", "hmac", "struct", "zlib", "gzip", "zipfile", "tarfile",
    "xml", "ast", "importlib", "inspect", "unittest", "enum", "dataclasses",
    "contextlib", "functools", "operator", "statistics", "decimal", "fractions",
    "timeit", "traceback", "signal", "select", "selectors", "ctypes",
}

CATEGORY_RULES = [
    ("Recon & Scanning", ("scan", "recon", "nmap", "port", "subdomain", "dns", "whois", "domain", "dir_fuzz", "web_vuln", "headers", "crawler", "inspector", "ping_sweep", "net_discover", "net_map", "router_find", "ssl_scan", "admin_finder", "nuclei", "drupal", "joomla", "wp_scan")),
    ("OSINT & Privacy", ("osint", "tracker", "track", "geo", "social", "email_osint", "google_dork", "dark_search", "sherlock", "url_expand", "cf_resolve", "local_map", "mac_vendor", "pub_ip", "proxy_checker", "aio_tracker")),
    ("Cryptography & Password Hygiene", ("crypto", "base64", "hash", "pass_", "dict_gen", "rainbow", "hex_conv", "bin_conv", "cc_validator", "iban_valid", "pdf_lock", "zip_lock")),
    ("Mobile & Android", ("adb", "apk", "firmware", "mobile", "phone", "frp", "nethunter", "god_mode")),
    ("Wi-Fi & Networking", ("wifi", "bluetooth", "packet", "listener", "speed", "subnet", "mac_changer", "network", "net_", "ip_lookup", "ip_rotator", "anonymity", "cloud_tunnel", "ua_switch")),
    ("Files & Media", ("stego", "steg", "metadata", "exif", "img_", "audio", "qr_", "url_expander", "web_cloner")),
    ("System & Diagnostics", ("sys_", "system_", "security_auditor", "audit", "termux", "mem_clean", "proc_kill", "cpu_stress", "bat_opt", "inspect", "framework_install", "cyber_deps")),
    ("Lab-only / Disabled", ("spoof", "bomber", "flood", "dos", "shell", "injector", "payload", "cracker", "force", "phishing", "cam_hacker")),
]

def category_for(name: str) -> str:
    if name in BLOCKED_TOOLS:
        return "Lab-only / Disabled"
    for category, hints in CATEGORY_RULES:
        if any(hint in name.lower() for hint in hints):
            return category
    return "General Utilities"

def discover_tools() -> List[dict]:
    found = []
    for path in sorted(CORE_DIR.glob("*.py"), key=lambda p: p.name.lower()):
        if path.name in INTERNAL_FILES or path.stem.startswith("_"):
            continue
        if path.resolve().parent != CORE_DIR:
            continue
        found.append({
            "name": path.stem,
            "path": path,
            "category": category_for(path.stem),
            "blocked": path.stem in BLOCKED_TOOLS,
        })
    return found

def imports_for(path: Path) -> Tuple[Set[str], bool]:
    """Return top-level imports and parse status without importing/executing the tool."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, UnicodeError, SyntaxError):
        return set(), False
    names: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".")[0])
    return names, True

def missing_packages(path: Path) -> Tuple[List[Tuple[str, str]], bool]:
    imports, parsed = imports_for(path)
    missing = []
    for module in sorted(imports):
        if module in STDLIB or module.startswith("_"):
            continue
        try:
            present = importlib.util.find_spec(module) is not None
        except (ImportError, ValueError, ModuleNotFoundError):
            present = False
        if not present:
            package = PIP_ALLOWLIST.get(module)
            if package:
                missing.append((module, package))
            else:
                missing.append((module, ""))
    return missing, parsed

def install_allowlisted(packages: Iterable[str]) -> bool:
    packages = sorted(set(packages))
    if not packages:
        return True
    print("\n[+] Missing approved Python package(s): " + ", ".join(packages))
    answer = input("Install these packages into the current Python environment? [y/N]: ").strip().lower()
    if answer not in {"y", "yes"}:
        return False
    command = [sys.executable, "-m", "pip", "install", *packages]
    try:
        return subprocess.run(command, check=False, timeout=240).returncode == 0
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f"[!] Package installation failed: {exc}")
        return False

def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("clear" if os.name != "nt" else "cls")

def banner(total: int) -> None:
    print("\033[1;36m")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                 CYBER-TOOLKIT • UNIFIED MENU                ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("\033[0m")
    print(f"  Platform: {platform.system()} {platform.release()} | Python {platform.python_version()}")
    print(f"  Discovered tools: {total} | Root: {REPO_DIR}")
    print("  Use only on devices, networks, and accounts you are authorized to test.")
    print("-" * 64)

def show_categories(tools: List[dict]) -> List[str]:
    categories = sorted({t["category"] for t in tools}, key=str.lower)
    for i, category in enumerate(categories, 1):
        count = sum(t["category"] == category for t in tools)
        print(f"  {i:>2}. {category} ({count})")
    print("   A. All tools")
    print("   S. Search tools")
    print("   H. Health / syntax audit")
    print("   0. Exit")
    return categories

def show_tools(tools: List[dict]) -> None:
    if not tools:
        print("No tools found in this category.")
        return
    for i, tool in enumerate(tools, 1):
        status = " [DISABLED: review required]" if tool["blocked"] else ""
        print(f"  {i:>3}. {tool['name']}{status}")

def launch_tool(tool: dict) -> None:
    name = tool["name"]
    path = tool["path"]
    if tool["blocked"]:
        print(f"\n[!] '{name}' is inventoried but disabled by safe mode.")
        print("    This legacy module needs a manual safety review and a controlled lab test.")
        return
    if not path.is_file() or path.resolve().parent != CORE_DIR:
        print("[!] Tool path is missing or outside core/.")
        return
    missing, parsed = missing_packages(path)
    if not parsed:
        print("[!] Cannot parse this tool's Python source. It will not be launched.")
        return
    unknown = [module for module, package in missing if not package]
    approved = [package for module, package in missing if package]
    if approved:
        if not install_allowlisted(approved):
            print("[!] Required package installation was declined or failed; tool not started.")
            return
    if unknown:
        print("[!] Could not map these missing imports to an approved package: " + ", ".join(unknown))
        print("    No guessed package was installed. Check that tool's own documentation.")
        return
    # Re-check imports after optional dependency installation.
    remaining, _ = missing_packages(path)
    if remaining:
        print("[!] Dependencies remain missing: " + ", ".join(m or p for m, p in remaining))
        return
    print(f"\n[+] Launching {name} with {sys.executable}")
    try:
        result = subprocess.run([sys.executable, str(path)], cwd=str(CORE_DIR), check=False)
        if result.returncode:
            print(f"[!] Tool exited with status {result.returncode}.")
        else:
            print("[+] Tool finished.")
    except KeyboardInterrupt:
        print("\n[!] Tool interrupted.")
    except (OSError, subprocess.SubprocessError) as exc:
        print(f"[!] Could not start tool: {exc}")

def health_audit(tools: List[dict]) -> None:
    errors = []
    for tool in tools:
        _, parsed = imports_for(tool["path"])
        if not parsed:
            errors.append(tool["name"])
    print(f"\nPython files discovered: {len(tools)}")
    print(f"Syntax/encoding issues found by static parse: {len(errors)}")
    if errors:
        print("Needs review: " + ", ".join(errors))
    print("Note: this does not execute tools or prove their runtime behavior.")

def main() -> int:
    tools = discover_tools()
    while True:
        clear_screen()
        banner(len(tools))
        categories = show_categories(tools)
        choice = input("\nSelect category/action: ").strip().lower()
        if choice in {"0", "q", "quit", "exit"}:
            print("Cyber-Toolkit closed.")
            return 0
        if choice == "h":
            health_audit(tools)
            input("\nPress Enter to return...")
            continue
        if choice == "a":
            selected = tools
        elif choice == "s":
            query = input("Search tool name: ").strip().lower()
            selected = [t for t in tools if query in t["name"].lower()]
        elif choice.isdigit() and 1 <= int(choice) <= len(categories):
            category = categories[int(choice) - 1]
            selected = [t for t in tools if t["category"] == category]
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")
            continue
        while True:
            clear_screen()
            banner(len(tools))
            print(f"Category/search results: {len(selected)} tool(s)")
            show_tools(selected)
            print("\n  B. Back to categories   S. Search   0. Exit")
            tool_choice = input("\nSelect tool: ").strip().lower()
            if tool_choice in {"b", "back"}:
                break
            if tool_choice in {"0", "q", "quit", "exit"}:
                return 0
            if tool_choice == "s":
                query = input("Search tool name: ").strip().lower()
                selected = [t for t in tools if query in t["name"].lower()]
                continue
            if not tool_choice.isdigit() or not 1 <= int(tool_choice) <= len(selected):
                print("Invalid choice.")
                input("Press Enter to continue...")
                continue
            launch_tool(selected[int(tool_choice) - 1])
            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    raise SystemExit(main())
