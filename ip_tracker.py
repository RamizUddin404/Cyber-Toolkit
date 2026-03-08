# CREATED BY: RAMIZ UDDIN
import os, sys, time, json, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("IP TRACKER (GEO-IP)")
    print("\033[1;32m[*] Track any IP Address for Location and ISP details.\033[0m")
    
    ip = input("\n\033[1;33mEnter Target IP (Leave blank for your IP): \033[0m").strip()
    
    print("\n\033[1;32m[*] Fetching details from API...\033[0m")
    time.sleep(1)
    
    try:
        # Using curl to fetch data from ip-api.com
        url = f"http://ip-api.com/json/{ip}"
        cmd = f"curl -s {url}"
        output = subprocess.check_output(cmd, shell=True).decode('utf-8')
        data = json.loads(output)
        
        if data['status'] == 'success':
            print("\033[1;36m" + "─" * 45)
            print(f"  IP         : {data.get('query')}")
            print(f"  Country    : {data.get('country')} ({data.get('countryCode')})")
            print(f"  Region     : {data.get('regionName')}")
            print(f"  City       : {data.get('city')}")
            print(f"  ZIP        : {data.get('zip')}")
            print(f"  ISP        : {data.get('isp')}")
            print(f"  Org        : {data.get('org')}")
            print(f"  Timezone   : {data.get('timezone')}")
            print(f"  Lat/Lon    : {data.get('lat')}, {data.get('lon')}")
            print("─" * 45 + "\033[0m")
        else:
            print(f"\033[1;31m[!] Error: {data.get('message', 'Invalid IP')}\033[0m")
            
    except Exception as e:
        print(f"\033[1;31m[!] Failed to connect: {str(e)}\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
