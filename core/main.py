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
SUPPORTED_SCRIPT_SUFFIXES = {".py", ".sh"}
# Explicit blocklist: these legacy modules are inventoried but not launched by default.
BLOCKED_TOOLS = {
    "arp_spoof", "call_spoof", "cam_hacker", "dos_attack", "email_spoof",
    "ftp_force", "frp_bypass_helper", "god_mode", "god_mode_ultimate",
    "hash_cracker", "md5_crack", "sha1_crack", "ssh_force", "sms_bomber",
    "sms_spoof", "sql_injector", "tcp_flooder", "reverse_shell", "revshell_gen",
    "web_shell_pro", "payload_gen", "phishing_sim", "universal_cracker",
    "zip_cracker", "wifi_pass_view", "ip_rotator", "email_spoof", "ftp_force",
    "hydra_tool", "brute_force_sim", "web_cloner", "cam_hacker",
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
    "pyfiglet": "pyfiglet",
    "tabulate": "tabulate",
    "tqdm": "tqdm",
    "fake_useragent": "fake-useragent",
    "speedtest": "speedtest-cli",
    "phonenumbers": "phonenumbers",
    "colorama": "colorama",
    "urllib3": "urllib3",
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

def source_needs_manual_review(path: Path) -> bool:
    """Flag obfuscated/dynamic-execution source before it can be launched."""
    try:
        source = path.read_text(encoding="utf-8", errors="strict")
    except (OSError, UnicodeError):
        return True
    suspicious_patterns = (
        r"\bmarshal\.(?:loads|load)\s*\(",
        r"\bexec\s*\(\s*(?:marshal|compile|base64|zlib)",
        r"\beval\s*\(",
        r"\b__import__\s*\(",
        r"base64\.(?:b64decode|decodebytes)\s*\(",
    )
    return any(re.search(pattern, source) for pattern in suspicious_patterns)

def category_for(name: str) -> str:
    if name in BLOCKED_TOOLS:
        return "Lab-only / Disabled"
    for category, hints in CATEGORY_RULES:
        if any(hint in name.lower() for hint in hints):
            return category
    return "General Utilities"

def discover_tools() -> List[dict]:
    """Discover launchable script files for the main menu without listing data/assets."""
    found = []
    paths = [
        path for path in CORE_DIR.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_SCRIPT_SUFFIXES
    ]
    for path in sorted(paths, key=lambda p: p.name.lower()):
        if path.name in INTERNAL_FILES or path.stem.startswith("_"):
            continue
        if path.resolve().parent != CORE_DIR:
            continue
        category = category_for(path.stem)
        # Shell scripts are inventory-only until individually reviewed.
        manual_review = path.suffix.lower() == ".py" and source_needs_manual_review(path)
        blocked = (
            path.stem in BLOCKED_TOOLS
            or category == "Lab-only / Disabled"
            or path.suffix.lower() == ".sh"
            or manual_review
        )
        if manual_review:
            category = "Lab-only / Disabled"
        found.append({
            "name": path.stem,
            "path": path,
            "category": category,
            "blocked": blocked,
            "kind": path.suffix.lower().lstrip("."),
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
    print("\n[+] Automatically installing approved missing Python package(s): " + ", ".join(packages))
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

PAGE_SIZE = 15

def show_tools(tools: List[dict], page: int = 0, page_size: int = PAGE_SIZE) -> None:
    """Show one page of tools; numbering is local to the current page."""
    if not tools:
        print("No tools found in this category.")
        return
    total_pages = max(1, (len(tools) + page_size - 1) // page_size)
    page = max(0, min(page, total_pages - 1))
    start = page * page_size
    visible = tools[start:start + page_size]
    print(f"  Showing {start + 1}-{start + len(visible)} of {len(tools)} | Page {page + 1}/{total_pages}")
    for i, tool in enumerate(visible, 1):
        status = " [DISABLED: review required]" if tool["blocked"] else ""
        print(f"  {i:>2}. {tool['name']}{status}")


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
    if path.suffix.lower() != ".py":
        print("[!] This script type is listed for inventory but is not enabled for launch until it receives a separate safety review.")
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
    """Report each discovered script's static readiness without executing it."""
    counts = {
        "static_ok": 0,
        "missing_dependencies": 0,
        "syntax_error": 0,
        "disabled": 0,
        "review_only": 0,
    }
    print("\nPER-TOOL HEALTH CHECK (no scripts are executed)")
    print("-" * 76)
    for tool in tools:
        name = tool["name"]
        path = tool["path"]
        if tool.get("blocked"):
            status = "DISABLED — safety review required"
            counts["disabled"] += 1
        elif path.suffix.lower() != ".py":
            status = "REVIEW ONLY — script type not enabled"
            counts["review_only"] += 1
        else:
            missing, parsed = missing_packages(path)
            if not parsed:
                status = "SYNTAX/ENCODING ERROR"
                counts["syntax_error"] += 1
            elif missing:
                missing_names = [module for module, _ in missing]
                status = "MISSING IMPORTS — " + ", ".join(missing_names)
                counts["missing_dependencies"] += 1
            else:
                status = "STATIC OK — runtime not verified"
                counts["static_ok"] += 1
        print(f"{name:<27} {status}")
    print("-" * 76)
    print(f"Static OK (not runtime-tested): {counts['static_ok']}")
    print(f"Missing imports/dependencies:  {counts['missing_dependencies']}")
    print(f"Syntax/encoding errors:        {counts['syntax_error']}")
    print(f"Disabled by safe mode:         {counts['disabled']}")
    print(f"Review-only scripts:           {counts['review_only']}")
    print("Static checks do not prove that a tool works. Test each supported tool")
    print("with safe sample inputs and required permissions before marking it working.")

def main() -> int:
    tools = discover_tools()
    selected = tools
    page = 0
    while True:
        clear_screen()
        banner(len(tools))
        print("  MAIN TOOL MENU — all discovered scripts are listed here")
        print(f"  Current view: {len(selected)} script(s)")
        total_pages = max(1, (len(selected) + PAGE_SIZE - 1) // PAGE_SIZE)
        page = max(0, min(page, total_pages - 1))
        show_tools(selected, page=page)
        print("\\n  N. Next page   P. Previous page")
        print("  C. Choose category   A. All scripts   S. Search")
        print("  H. Health / syntax audit   0. Exit")
        choice = input("\\nSelect script number or action: ").strip().lower()

        if choice in {"0", "q", "quit", "exit"}:
            print("Cyber-Toolkit closed.")
            return 0
        if choice in {"n", "next"}:
            if page + 1 < total_pages:
                page += 1
            else:
                print("Already on the last page.")
                input("Press Enter to continue...")
            continue
        if choice in {"p", "prev", "previous"}:
            if page > 0:
                page -= 1
            else:
                print("Already on the first page.")
                input("Press Enter to continue...")
            continue
        if choice == "a":
            selected = tools
            page = 0
            continue
        if choice == "c":
            categories = sorted({t["category"] for t in tools}, key=str.lower)
            print("\\nCategories:")
            for i, category in enumerate(categories, 1):
                count = sum(t["category"] == category for t in tools)
                print(f"  {i}. {category} ({count})")
            print("  B. Back")
            category_choice = input("Choose category: ").strip().lower()
            if category_choice in {"b", "back"}:
                continue
            if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
                category = categories[int(category_choice) - 1]
                selected = [t for t in tools if t["category"] == category]
                page = 0
            else:
                print("Invalid category.")
                input("Press Enter to continue...")
            continue
        if choice == "s":
            query = input("Search script filename: ").strip().lower()
            selected = [t for t in tools if query in t["name"].lower()]
            page = 0
            continue
        if choice == "h":
            health_audit(tools)
            input("\\nPress Enter to return to the main menu...")
            continue

        page_count = min(PAGE_SIZE, len(selected) - page * PAGE_SIZE)
        if not choice.isdigit() or not 1 <= int(choice) <= page_count:
            print("Invalid choice.")
            input("Press Enter to continue...")
            continue
        selected_tool = selected[page * PAGE_SIZE + int(choice) - 1]
        launch_tool(selected_tool)
        input("\\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    raise SystemExit(main())
