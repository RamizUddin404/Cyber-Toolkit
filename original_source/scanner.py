# CREATED BY: RAMIZ UDDIN
import os, time, socket

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("PORT SCANNER (LIGHT)")
    print("\033[1;32m[*] Simple socket-based port scanner.\033[0m")
    
    target = input("\n\033[1;33mEnter Target IP: \033[0m")
    if target:
        print(f"\n\033[1;32m[*] Scanning common ports on {target}...\033[0m")
        for port in [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"\033[1;32m[+] Port {port:5} : OPEN\033[0m")
            s.close()
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
