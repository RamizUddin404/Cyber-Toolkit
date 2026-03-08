# CREATED BY: RAMIZ UDDIN
import os, sys, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("CLOUD TUNNEL (CLOUDFLARED)")
    print("\033[1;32m[*] Expose your local server to the internet without Port Forwarding!")
    print("[*] Requires: cloudflared binary\033[0m")
    
    # Check if cloudflared is installed
    if subprocess.call(["which", "cloudflared"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        print("\n\033[1;31m[!] Cloudflared not found. Installing...\033[0m")
        # For Termux, usually downloaded from GitHub releases, but let's assume a simplified check or help.
        # Actually, let's try a direct download if possible or just guide the user.
        print("[*] Downloading Cloudflared for Android...")
        os.system("wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O cloudflared")
        os.system("chmod +x cloudflared")
        os.system("mv cloudflared $PREFIX/bin/")
        
    port = input("\n\033[1;33mEnter Local Port to Tunnel (default: 8080): \033[0m") or "8080"
    
    print(f"\n\033[1;32m[+] Starting Tunnel on Port {port}...")
    print("[!] Copy the .trycloudflare.com URL from the logs below:\033[0m\n")
    time.sleep(2)
    
    try:
        os.system(f"cloudflared tunnel --url http://127.0.0.1:{port}")
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Tunnel Stopped.\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
