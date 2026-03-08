# CREATED BY: RAMIZ UDDIN
import os, sys, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("WIFI PASS-VIEW (ROOT)")
    print("\033[1;31m[!] THIS TOOL REQUIRES ROOT PERMISSION!\033[0m")
    
    # Simple check for root
    if os.getuid() != 0 and subprocess.call(["su", "-c", "whoami"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        print("\n\033[1;31m[!] NO ROOT DETECTED. PLEASE RUN WITH SU OR ON ROOTED DEVICE.\033[0m")
        input("\n[Press Enter to Return]")
        return

    print("\033[1;32m[*] Extracting Saved WiFi Passwords...\033[0m")
    time.sleep(1)
    
    # Most Android versions keep wifi config in /data/misc/wifi/WifiConfigStore.xml
    # Older ones in /data/misc/wifi/wpa_supplicant.conf
    try:
        print("\033[1;33m" + "─" * 45)
        print("SSID                | PASSWORD")
        print("─" * 45 + "\033[0m")
        
        # Method 1: wpa_supplicant
        os.system("su -c 'grep -E \"ssid=|psk=\" /data/misc/wifi/wpa_supplicant.conf' | sed 's/ssid=//g; s/psk=//g'")
        
        # Method 2: WifiConfigStore.xml (Newer Android)
        os.system("su -c 'grep -E \"SSID|PreSharedKey\" /data/misc/wifi/WifiConfigStore.xml' | sed 's/<string name=\"SSID\">//g; s/<string name=\"PreSharedKey\">//g; s/<\\/string>//g; s/&quot;//g'")
        
    except Exception as e:
        print(f"\n[!] Error: {str(e)}")
        
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
