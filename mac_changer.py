# CREATED BY: RAMIZ UDDIN
import os, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("MAC CHANGER (ROOT)")
    print("\033[1;32m[*] Change your device MAC address to stay anonymous.")
    print("[!] THIS TOOL REQUIRES ROOT ACCESS!\033[0m")
    
    if os.getuid() != 0:
        print("\n\033[1;31m[!] ROOT access not detected. Run with 'tsu' or 'sudo'.\033[0m")
        input("\n[Press Enter to Return]")
        return
        
    iface = input("\n\033[1;33mEnter Interface (e.g. wlan0): \033[0m")
    new_mac = input("Enter New MAC (e.g. 00:11:22:33:44:55): \033[0m")
    
    if iface and new_mac:
        print(f"\n\033[1;32m[*] Changing MAC address for {iface}...\033[0m")
        try:
            os.system(f"ip link set {iface} down")
            os.system(f"ip link set dev {iface} address {new_mac}")
            os.system(f"ip link set {iface} up")
            print("\n\033[1;32m[+] MAC Address Changed Successfully.\033[0m")
        except Exception as e:
            print(f"\n\033[1;31m[!] Error: {str(e)}\033[0m")
            
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
