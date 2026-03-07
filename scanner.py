# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import socket

def scan_ports(ip):
    print("\033[1;32m[*] ", end=""); print(f"[*] Scanning IP: {ip}")
    for port in range(1, 1025):  # Common ports 1-1024
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        if result == 0:
            print("\033[1;32m[*] ", end=""); print(f"[+] Port {port} is OPEN")
        s.close()

if __name__ == "__main__":
    target = input("Enter Target IP (e.g. 127.0.0.1): ")
    scan_ports(target)
