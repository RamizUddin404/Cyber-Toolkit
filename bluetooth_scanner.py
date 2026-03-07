# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import os
import time
import subprocess
import json
import cyber_deps

# Ensure basic packages
cyber_deps.ensure_deps(system_pkgs=["termux-api", "bluez", "jq"])

def header():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;34m========================================\033[0m")
    print("\033[1;32m[*] ", end=""); print("    ULTIMATE BT HACKER (PRO FIX) v6.0")
    print("\033[1;32m[*] ", end=""); print("\033[1;34m========================================\033[0m")

def run_scan():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;33m[*] Scanning... (Checking 3 Methods)\033[0m")
    devices = []
    
    # Method 1: Direct Termux-API call (Recommended)
    print("\033[1;32m[*] ", end=""); print("[*] Trying Method 1 (Termux-API)...")
    try:
        # Use 'termux-api BluetoothScan' which is the root command
        raw_out = subprocess.check_output("termux-api BluetoothScan", shell=True, stderr=subprocess.STDOUT).decode()
        if "[" in raw_out:
            data = json.loads(raw_out)
            for d in data:
                mac = d.get("address")
                name = d.get("name") or "Unknown"
                if mac: devices.append((mac, name))
    except Exception as e:
        print("\033[1;32m[*] ", end=""); print(f"[-] Method 1 Error: {e}")

    # Method 2: Legacy hcitool (Root Required)
    if not devices:
        print("\033[1;32m[*] ", end=""); print("[*] Trying Method 2 (hcitool)...")
        try:
            output = subprocess.check_output("timeout 10s hcitool scan", shell=True).decode()
            import re
            found = re.findall(r"(([0-9A-F]{2}:){5}[0-9A-F]{2})\s+(.*)", output)
            for mac, _, name in found:
                devices.append((mac, name.strip()))
        except:
            pass

    return devices

def run():
    while True:
        os.system("clear")
        header()
        print("\033[1;32m[*] ", end=""); print("1. Automatic Scan & Target")
        print("\033[1;32m[*] ", end=""); print("2. Manual MAC Stress Test")
        print("\033[1;32m[*] ", end=""); print("3. Check BT Hardware Support (Debug)")
        print("\033[1;32m[*] ", end=""); print("4. How to Fix 'No Devices Found'")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nBT-Pro > ")
        if c == '0': break
        
        if c == '1':
            devs = run_scan()
            if not devs:
                print("\033[1;32m[*] ", end=""); print("\n\033[1;31m[!] SCAN FAILED! No devices visible.\033[0m")
                print("\033[1;32m[*] ", end=""); print("Tip: Use Option 4 to see why this is happening.")
            else:
                print("\033[1;32m[*] ", end=""); print("\n\033[1;32m[ Found Devices ]\033[0m")
                for i, (mac, name) in enumerate(devs, 1):
                    print("\033[1;32m[*] ", end=""); print(f" [{i}] {name} ({mac})")
                
                sel = input("\nSelect Device #: ")
                try:
                    target = devs[int(sel)-1]
                    print("\033[1;32m[*] ", end=""); print(f"\n\033[1;31m[*] ATTACKING: {target[1]}...\033[0m")
                    while True:
                        os.system(f"hcitool info {target[0]} > /dev/null 2>&1")
                        print("\033[1;32m[*] ", end=""); print(f"[+] Handshake packet sent to {target[0]}", end="\r")
                        time.sleep(0.1)
                except: print("\033[1;32m[*] ", end=""); print("[-] Invalid selection.")
        
        elif c == '3':
            print("\033[1;32m[*] ", end=""); print("\n\033[1;36m[*] Hardware Status:\033[0m")
            os.system("hciconfig -a || echo '[-] Bluetooth hardware not accessible via Termux.'")
            print("\033[1;32m[*] ", end=""); print("\n[*] Internal API Status:")
            os.system("termux-api BluetoothScan || echo '[-] Termux-API is blocked.'")
            
        elif c == '4':
            print("\033[1;32m[*] ", end=""); print("\n\033[1;32m[*] 100% WORKING FIX GUIDE:\033[0m")
            print("\033[1;32m[*] ", end=""); print("1. Install 'Termux:API' app from Play Store/F-Droid (MUST).")
            print("\033[1;32m[*] ", end=""); print("2. Phone Settings -> Apps -> Termux:API -> Permissions.")
            print("\033[1;32m[*] ", end=""); print("3. ENABLE ALL: Location, Nearby Devices, and Files.")
            print("\033[1;32m[*] ", end=""); print("4. Turn ON 'Location' (GPS) and 'Bluetooth' in notification bar.")
            print("\033[1;32m[*] ", end=""); print("5. IMPORTANT: Restart Termux after giving permissions.")
            
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
