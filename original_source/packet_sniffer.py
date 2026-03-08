# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("PACKET SNIFFER (ROOT)")
    print("\033[1;32m[*] Starting Packet Sniffer...")
    if os.getuid() != 0:
        print("\n\033[1;31m[!] Sniffing requires ROOT access. Please run with sudo or on rooted device.\033[0m")
        input("\n[Press Enter to Return]")
        return
    
    # Simple tcpdump command for demo
    os.system("tcpdump -c 10 -i any")
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
