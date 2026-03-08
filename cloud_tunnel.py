# CREATED BY: RAMIZ UDDIN
import os, sys, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    while True:
        tool_header("CLOUD TUNNEL (PRO-V1)")
        print("\033[1;32m[1] CLOUDFLARE (Free & Fast)")
        print("[2] LOCALXPOSE (High Success Rate)")
        print("[0] Back\033[0m")
        
        choice = input("\nTunnel > ")
        if choice == '0': break
        
        port = input("\n\033[1;33mEnter Local Port to Tunnel (default: 8080): \033[0m") or "8080"
        
        if choice == '1':
            print(f"\n\033[1;32m[+] Starting Cloudflare Tunnel on Port {port}...")
            print("[!] Copy the .trycloudflare.com URL from the logs below:\033[0m\n")
            time.sleep(2)
            try:
                # Using 0.0.0.0 for better local server binding
                os.system(f"cloudflared tunnel --url http://127.0.0.1:{port}")
            except KeyboardInterrupt:
                print("\n\033[1;31m[!] Tunnel Stopped.\033[0m")
                
        elif choice == '2':
            # Check LocalXpose
            if not os.path.exists(f"{os.environ['PREFIX']}/bin/loclx"):
                print("\n\033[1;31m[!] LocalXpose not found. Installing...\033[0m")
                os.system("wget -q https://api.localxpose.io/api/v2/client-builds/loclx-linux-arm64.zip -O loclx.zip")
                os.system("unzip -q loclx.zip && chmod +x loclx-linux-arm64")
                os.system("mv loclx-linux-arm64 $PREFIX/bin/loclx && rm loclx.zip")
            
            print(f"\n\033[1;32m[+] Starting LocalXpose Tunnel on Port {port}...")
            time.sleep(1)
            try:
                os.system(f"loclx tunnel http --to 127.0.0.1:{port}")
            except KeyboardInterrupt:
                print("\n\033[1;31m[!] Tunnel Stopped.\033[0m")
        
        input("\n[Press Enter to Continue]")

if __name__ == "__main__":
    run()
