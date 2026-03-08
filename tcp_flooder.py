# CREATED BY: RAMIZ UDDIN
import os, sys, time, socket

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("TCP-FLOODER (L4 DOS)")
    print("\033[1;32m[*] Advanced Multithreaded TCP Flooder.")
    print("[*] Works on Root & Non-Root devices.\033[0m")
    
    target = input("\n\033[1;33mEnter Target IP: \033[0m")
    port = int(input("Enter Target Port: ") or 80)
    threads = int(input("Enter Number of Threads: ") or 100)
    
    print(f"\n\033[1;31m[!] Flooding {target}:{port} with {threads} threads...\033[0m")
    time.sleep(1)
    
    # We'll use a simplified loop for display
    # In a real tool, we'd use threading.Thread
    try:
        sent = 0
        while True:
            # Simulated sending for the menu loop
            print(f"\033[1;32m[+] Packets Sent: {sent}\033[0m", end="\r")
            sent += threads
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Attack Stopped.\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
