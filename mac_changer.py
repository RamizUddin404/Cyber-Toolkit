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
import subprocess

def change_mac(interface, new_mac):
    print("\033[1;32m[*] ", end=""); print(f"[*] Changing MAC address for {interface} to {new_mac}")
    # These commands require ROOT access (tsu)
    commands = [
        f"ip link set {interface} down",
        f"ip link set dev {interface} address {new_mac}",
        f"ip link set {interface} up"
    ]
    
    try:
        if os.geteuid() != 0:
            print("\033[1;32m[*] ", end=""); print("[!] This tool requires ROOT access. Run with 'sudo' or 'tsu'.")
            return

        for cmd in commands:
            subprocess.call(cmd, shell=True)
        print("\033[1;32m[*] ", end=""); print("[+] MAC Address Changed Successfully (if interface exists).")
    except Exception as e:
        print("\033[1;32m[*] ", end=""); print(f"[!] Error: {e}")

if __name__ == "__main__":
    iface = input("Interface (e.g. wlan0): ")
    mac = input("New MAC (e.g. 00:11:22:33:44:55): ")
    change_mac(iface, mac)
