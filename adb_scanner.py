# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import cyber_deps
cyber_deps.ensure_deps(system_pkgs=["adb"])
import os

def scan_adb():
    print("\033[1;32m[*] ", end=""); print("\033[1;33m[*] Android Debug Bridge (ADB) Scanner\033[0m")
    print("\033[1;32m[*] ", end=""); print("[!] This checks if a phone has left USB Debugging OPEN over Network.")
    target = input("Enter Target IP: ")
    
    print("\033[1;32m[*] ", end=""); print(f"[*] Connecting to {target}:5555...")
    # Requires adb package
    os.system("pkg install android-tools -y > /dev/null 2>&1")
    os.system(f"adb connect {target}:5555")
    
    print("\033[1;32m[*] ", end=""); print("\n[*] Checking Connection Status...")
    os.system("adb devices")
    
    print("\033[1;32m[*] ", end=""); print("\n[*] If device is listed, you can run 'adb shell' to access it.")

if __name__ == "__main__":
    scan_adb()
