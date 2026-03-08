# CREATED BY: RAMIZ UDDIN
import subprocess
import sys
import shutil
import os

PKG_MAP = {
    "termux-api": "termux-bluetooth-scan", "bluez": "hcitool", "wireshark": "tshark",
    "metasploit": "msfconsole", "p7zip": "7z", "nmap": "nmap", "hydra": "hydra",
    "sqlmap": "sqlmap", "nikto": "nikto", "proxychains-ng": "proxychains4",
    "tor": "tor", "jq": "jq", "zbar": "zbarimg", "adb": "adb", "fastboot": "fastboot",
    "sherlock": "sherlock", "dsniff": "arpspoof", "aircrack-ng": "airmon-ng"
}

def is_installed(name):
    cmd = PKG_MAP.get(name, name)
    return shutil.which(cmd) is not None

def remove_deps(tool_name=None):
    """Universal Uninstaller - Cleans based on tool or general mapping."""
    print(f"\n\033[1;31m[*] Starting Deep Uninstall Process...\033[0m")
    
    # Common packages to purge if found in the specific tool requirements
    # For now, let's just purge the main one linked to the tool
    if tool_name in PKG_MAP:
        pkg = tool_name
        print(f"[-] Purging {pkg} from system...")
        os.system(f"apt purge {pkg} -y > /dev/null 2>&1")
        os.system(f"pkg uninstall {pkg} -y > /dev/null 2>&1")
    
    # Generic cleanup
    os.system("pkg clean && apt autoremove -y > /dev/null 2>&1")
    print("\033[1;32m[+] Successfully Uninstalled.\033[0m")

def ensure_deps(system_pkgs=[], python_mods=[]):
    for pkg in system_pkgs:
        if not is_installed(pkg):
            os.system(f"pkg install {pkg} -y > /dev/null 2>&1")
    for mod in python_mods:
        try: __import__(mod)
        except ImportError:
            os.system(f"pip install {mod} > /dev/null 2>&1")

if __name__ == "__main__": pass
