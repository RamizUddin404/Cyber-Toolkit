# CREATED BY: RAMIZ UDDIN
import os
import sys
import subprocess
import time
import random

def clear(): os.system('clear')

def animate_text(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def rainbow_banner():
    colors = ["\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[1;35m", "\033[1;36m"]
    banner = [
        "  ██████╗██╗   ██╗██████╗ ███████╗██████╗ ",
        " ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗",
        " ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝",
        " ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗",
        " ╚██████╗   ██║   ██████╔╝███████╗██║  ██║",
        "  ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝"
    ]
    for line in banner:
        print(random.choice(colors) + line)
        time.sleep(0.05)
    print("\033[0m")

def startup_follow():
    clear()
    rainbow_banner()
    print("\033[1;33m" + "!" * 45)
    print("   WELCOME TO RAMIZ UDDIN ULTIMATE TOOLKIT")
    print("   SYSTEM IS REDIRECTING... PLEASE WAIT")
    print("!" * 45 + "\033[0m")
    
    # STEP 1: FORCE GITHUB OPEN
    print("\n\033[1;32m[*] Step 1: Opening GitHub Profile...\033[0m")
    time.sleep(2)
    os.system("termux-open-url https://github.com/RamizUddin404 || am start -a android.intent.action.VIEW -d https://github.com/RamizUddin404 > /dev/null 2>&1")
    
    input("\n\033[1;36m[#] After Following on GitHub, Press ENTER to Open Facebook...\033[0m")
    
    # STEP 2: FORCE FB APP OPEN
    print("\n\033[1;32m[*] Step 2: Opening Facebook App...\033[0m")
    time.sleep(1)
    # Priority 1: Direct FB App Intent | Priority 2: Web Browser Fallback
    os.system('am start -a android.intent.action.VIEW -d "fb://facewebmodal/f?href=https://www.facebook.com/Ramiz.Uddin404" > /dev/null 2>&1 || termux-open-url https://www.facebook.com/Ramiz.Uddin404')
    
    print("\n\033[1;33m[+] Thank You! Launching ULTIMATE MASTER STATION...\033[0m")
    time.sleep(2)

def header(page):
    rainbow_banner()
    print("\033[1;36m" + "─" * 45)
    print(f"  GITHUB: https://github.com/RamizUddin404")
    print(f"  FB: https://www.facebook.com/Ramiz.Uddin404")
    print("─" * 45)
    animate_text(f"  ULTIMATE MASTER STATION v180.0 | PAGE {page}/5", 0.02)
    print("\033[1;33m       CREATED BY: \033[5mRAMIZ UDDIN\033[0m \033[0m") 
    print("\033[1;36m" + "─" * 45 + "\033[0m")

names = {
    1:'Nmap', 2:'Hydra', 3:'SQLMap', 4:'Nikto', 5:'WiFi Scan', 6:'Subdomain', 7:'Crypto', 8:'Whois', 9:'MAC Change', 10:'Sniffer',
    11:'Nethunter', 12:'Metasploit', 13:'ADB Scan', 14:'Social Recon', 15:'System Audit', 16:'Phishing', 17:'XSS Scan', 18:'Admin Finder', 19:'Rev Shell', 20:'Email OSINT',
    21:'ADB Pro', 22:'FRP Bypass', 23:'Flasher', 24:'APK Analyzer', 25:'Recovery', 26:'Exif Scan', 27:'Hash ID', 28:'ZIP Crack', 29:'DNS Recon', 30:'Web Cloner',
    31:'Nuclei', 32:'Payload Gen', 33:'Dir Fuzzer', 34:'Stegano', 35:'Net Discover', 36:'Searchsploit', 37:'ARP Spoof', 38:'CUPP', 39:'Dorker', 40:'JS Analyzer',
    41:'Pass-Gen', 42:'Metadata', 43:'Sherlock', 44:'Optimizer', 45:'QR Hacker', 46:'Universal Crack', 47:'Acc Security', 48:'BT Hack', 49:'SMS Bomber', 50:'Tor/Anonymity',
    51:'IP Rotator', 52:'Dark Search', 53:'Base64', 54:'URL Expand', 55:'HTTP Headers', 56:'Ping Sweep', 57:'Port Listener', 58:'SSH Force', 59:'FTP Force', 60:'WP Scan',
    61:'SSL Scan', 62:'CF Resolve', 63:'Fake ID', 64:'CC Validator', 65:'MAC Vendor', 66:'Pass Strength', 67:'Dict Gen', 68:'Hash Buster', 69:'MD5 Crack', 70:'Img Stego',
    71:'Bin Conv', 72:'Sys Info', 73:'CPU Stress', 74:'Speed Test', 75:'Router Find', 76:'Net Map', 77:'UA Switch', 78:'IBAN Valid', 79:'Rainbow Table', 80:'SHA1 Crack',
    81:'ZIP Lock', 82:'PDF Lock', 83:'Audio Stego', 84:'Hex Conv', 85:'ASCII Art', 86:'Proc Killer', 87:'Mem Clean', 88:'Bat Opt', 89:'Pub IP', 90:'Local Map',
    91:'Email Spoof', 92:'SMS Spoof', 93:'Call Spoof', 94:'Port Scan', 95:'Subnet Calc', 96:'Drupal', 97:'Joomla', 98:'Whois Bulk', 99:'Image Resize', 100:'GOD MODE',
    101:'Cloud Tunnel', 102:'WiFi PassView', 103:'IP Tracker', 104:'Web Crawler', 105:'Cam-Hacker', 106:'Geo-Locator', 107:'DDoS Attack', 108:'AIO Tracker',
    109:'Security Auditor', 110:'Remote Console', 111:'URL Expander', 112:'Hash Cracker', 113:'Web Inspector', 114:'XSS Scanner', 115:'RevShell Gen', 116:'Email Spoof Check',
    117:'BruteForce Sim', 118:'PortScan Light', 119:'Pass Strength', 120:'Proxy Checker', 121:'Domain Info', 122:'ZIP Lock Pro', 123:'PDF Lock Pro', 124:'Base64 Pro', 125:'GOD MODE ULTIMATE'
}

tools_map = {
    '1':'nmap_scanner.py','2':'hydra_tool.py','3':'sql_injector.py','4':'web_vuln.py','5':'wifi_scanner.py',
    '6':'subdomain_finder.py','7':'crypto_tool.py','8':'whois_lookup.py','9':'mac_changer.py','10':'packet_sniffer.py',
    '11':'nethunter_install.py','12':'framework_install.py','13':'adb_scanner.py','14':'social_recon.py','15':'system_audit.py',
    '16':'phishing_sim.py','17':'xss_scanner.py','18':'admin_finder.py','19':'reverse_shell.py','20':'email_osint.py',
    '21':'adb_fastboot_pro.py','22':'frp_bypass_helper.py','23':'firmware_flasher.py','24':'apk_analyzer.py','25':'mobile_recovery.py',
    '26':'exif_scanner.py','27':'hash_id.py','28':'zip_cracker.py','29':'dns_recon.py','30':'web_cloner.py',
    '31':'nuclei_scanner.py','32':'payload_gen.py','33':'dir_fuzzer.py','34':'stegano_tool.py','35':'net_discover.py',
    '36':'searchsploit_tool.py','37':'arp_spoof.py','38':'cupp_pass_gen.py','39':'google_dorker.py','40':'js_analyzer.py',
    '41':'pass_gen.py','42':'metadata_stripper.py','43':'sherlock_osint.py','44':'termux_optimizer.py','45':'qr_toolkit.py',
    '46':'universal_cracker.py','47':'account_security.py','48':'bluetooth_scanner.py','49':'sms_bomber.py','50':'anonymity_tool.py',
    '51':'ip_rotator.py','52':'dark_search.py','53':'base64_tool.py','54':'url_expand.py','55':'http_headers.py',
    '56':'ping_sweep.py','57':'net_listener.py','58':'ssh_force.py','59':'ftp_force.py','60':'wp_scan.py',
    '61':'ssl_scan.py','62':'cf_resolve.py','63':'fake_id.py','64':'cc_validator.py','65':'mac_vendor.py',
    '66':'pass_strength.py','67':'dict_gen.py','68':'hash_buster.py','69':'md5_crack.py','70':'img_stego.py',
    '71':'bin_conv.py','72':'sys_info.py','73':'cpu_stress.py','74':'speed_test.py','75':'router_find.py',
    '76':'net_map.py','77':'ua_switch.py','78':'iban_valid.py','79':'rainbow_gen.py','80':'sha1_crack.py',
    '81':'zip_lock.py','82':'pdf_lock.py','83':'audio_stego.py','84':'hex_conv.py','85':'ascii_art.py',
    '86':'proc_kill.py','87':'mem_clean.py','88':'bat_opt.py','89':'pub_ip.py','90':'local_map.py',
    '91':'email_spoof.py','92':'sms_spoof.py','93':'call_spoof.py','94':'port_scan.py','95':'subnet_calc.py',
    '96':'drupal_scan.py','97':'joomla_scan.py','98':'whois_bulk.py','99':'img_resize.py','100':'god_mode.py',
    '101':'cloud_tunnel.py','102':'wifi_pass_view.py','103':'ip_tracker.py','104':'web_crawler.py',
    '105':'cam_hacker.py','106':'geo_locator.py','107':'dos_attack.py','108':'aio_tracker.py',
    '109':'security_auditor.py','110':'web_shell_pro.py','111':'url_expander.py','112':'hash_cracker.py',
    '113':'web_inspector.py', '114':'xss_scanner.py', '115':'revshell_gen.py', '116':'email_spoof_checker.py',
    '117':'brute_force_sim.py', '118':'scanner.py', '119':'pass_check.py', '120':'proxy_checker.py',
    '121':'domain_info.py', '122':'zip_lock.py', '123':'pdf_lock.py', '124':'base64_pro.py', '125':'god_mode_ultimate.py'
}

def show_page(page_num):
    clear(); header(page_num)
    start = (page_num - 1) * 30 + 1
    end = min(start + 30, 126)
    current_list = list(range(start, end))
    for i in range(0, len(current_list), 2):
        id1 = current_list[i]
        n1 = names.get(id1, f"Tool {id1}")
        col1 = f"[{id1:02}] {n1[:15]}".ljust(22)
        if i+1 < len(current_list):
            id2 = current_list[i+1]
            n2 = names.get(id2, f"Tool {id2}")
            col2 = f"[{id2:02}] {n2[:15]}"
            print(f" {col1} {col2}")
        else:
            print(f" {col1}")
    print("\033[1;36m" + "─" * 45)
    nav = ""
    if page_num < 5: nav += "[N] Next Page  "
    if page_num > 1: nav += "[B] Back Page  "
    print(f" {nav}[0] Exit")
    print("─" * 45 + "\033[0m")

if __name__ == "__main__":
    startup_follow()
    page = 1
    while True:
        show_page(page)
        c = input("\033[1;32m[RAMIZ-UDDIN@Termux]:~\033[0m ").lower()
        if c == '0': sys.exit()
        elif c == 'n' and page < 5: page += 1
        elif c == 'b' and page > 1: page -= 1
        elif c in tools_map:
            try:
                subprocess.run([sys.executable, tools_map[c]])
            except Exception as e:
                print(f"\033[1;31m[!] Error running tool: {e}\033[0m")
                time.sleep(2)
