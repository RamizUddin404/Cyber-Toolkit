# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import os, ssl, socket
def run():
    print("\033[1;32m[*] ", end=""); print("\n[*] SSL Scanner")
    h = input("Host: ")
    if h=="99": import cyber_deps; cyber_deps.remove_deps(); return
    ctx = ssl.create_default_context()
    with socket.create_connection((h, 443)) as sock:
        with ctx.wrap_socket(sock, server_hostname=h) as ssock:
            print("\033[1;32m[*] ", end=""); print(ssock.version())
    input("[Enter]")
if __name__=="__main__": run()