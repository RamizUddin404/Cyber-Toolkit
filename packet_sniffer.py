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

def sniff():
    print("\033[1;32m[*] ", end=""); print("[*] Starting Packet Sniffer...")
    if os.geteuid() != 0:
        print("\033[1;32m[*] ", end=""); print("[!] Sniffing requires ROOT access. Use 'tsu' or 'sudo'.")
        return
    # Simple tcpdump command for demo
    os.system("tcpdump -c 5 -i any")

if __name__ == "__main__":
    sniff()
