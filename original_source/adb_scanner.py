# CREATED BY: RAMIZ UDDIN
import os, time, cyber_deps

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("ADB SCANNER (NETWORK DEBUG)")
    print("\033[1;32m[*] Android Debug Bridge (ADB) Scanner")
    print("[!] This checks if a phone has left USB Debugging OPEN over Network.\033[0m")
    
    cyber_deps.ensure_deps(system_pkgs=["android-tools"])
    
    target = input("\n\033[1;33mEnter Target IP: \033[0m")
    if target:
        print(f"\n\033[1;32m[*] Connecting to {target}:5555...\033[0m")
        os.system(f"adb connect {target}:5555")
        print("\n\033[1;36m[*] Checking Connection Status...\033[0m")
        os.system("adb devices")
        print("\n\033[1;32m[*] If device is listed, you can run 'adb shell' to access it.\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
