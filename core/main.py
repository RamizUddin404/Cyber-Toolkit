#!/usr/bin/env python3
"""
🛡️ ULTIMATE CYBER-TOOLKIT v180.0
🔐 Security & Penetration Testing Suite
Created By: RAMIZ UDDIN
Website: https://github.com/RamizUddin404/Cyber-Toolkit
"""

import os
import sys
import time
import platform
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform colors
init(autoreset=True)

def display_banner():
    """Display the toolkit banner"""
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}
  ██████╗██╗   ██╗██████╗ ███████╗██████╗ 
 ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
 ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
 ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
 ╚██████╗   ██║   ██████╔╝███████╗██║  ██║
  ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}
{Fore.YELLOW}{'='*60}
{Fore.GREEN}🛡️  ULTIMATE CYBER-TOOLKIT v180.0{Style.RESET_ALL}
{Fore.CYAN}🔐  100+ Security & Penetration Testing Tools{Style.RESET_ALL}
{Fore.YELLOW}{'='*60}{Style.RESET_ALL}
"""
    print(banner)

def display_main_menu():
    """Display main menu"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.GREEN}📋 MAIN MENU - SELECT A CATEGORY:{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
    
    categories = {
        "1": "🌐 Reconnaissance & Scanning",
        "2": "🔐 Cryptography & Hashing",
        "3": "📱 Mobile & Device Tools",
        "4": "🕵️  OSINT & Tracking",
        "5": "🔗 Web Exploitation",
        "6": "📡 Wireless & Networking",
        "7": "🛠️  System Utilities & Tools",
        "8": "🔥 Advanced & Exploitation",
        "9": "❌ Exit Toolkit"
    }
    
    for key, value in categories.items():
        print(f"   {Fore.YELLOW}[{key}]{Style.RESET_ALL} {value}")
    
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    return input(f"{Fore.GREEN}Enter your choice: {Style.RESET_ALL}")

def run_tool(tool_name):
    """Run a tool safely"""
    try:
        tool_path = f"{tool_name}.py"
        if os.path.exists(tool_path):
            print(f"\n{Fore.GREEN}[+] Launching {tool_name}...{Style.RESET_ALL}\n")
            os.system(f"python3 {tool_path}")
            print(f"\n{Fore.GREEN}[✓] Tool completed{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[!] Tool not found: {tool_name}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")

def reconnaissance_menu():
    """Reconnaissance tools submenu"""
    while True:
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}🌐 RECONNAISSANCE & SCANNING TOOLS:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        tools = {
            "1": ("nmap_scanner", "🔍 Nmap Port Scanner"),
            "2": ("subdomain_finder", "🎯 Subdomain Finder"),
            "3": ("web_crawler", "🕷️  Web Crawler"),
            "4": ("dns_recon", "📡 DNS Reconnaissance"),
            "5": ("ip_lookup", "🌍 IP Lookup"),
            "6": ("admin_finder", "👤 Admin Panel Finder"),
            "0": ("main", "⬅️  Back to Main Menu")
        }
        
        for key, (tool, desc) in tools.items():
            print(f"   {Fore.YELLOW}[{key}]{Style.RESET_ALL} {desc}")
        
        choice = input(f"\n{Fore.GREEN}Select tool: {Style.RESET_ALL}")
        
        if choice == "0":
            break
        elif choice in dict(tools).keys():
            tool_name = dict(tools)[choice][0]
            run_tool(tool_name)
        else:
            print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")

def cryptography_menu():
    """Cryptography & hashing tools submenu"""
    while True:
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}🔐 CRYPTOGRAPHY & HASHING TOOLS:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        tools = {
            "1": ("hash_cracker", "🔓 Hash Cracker Pro"),
            "2": ("base64_pro", "📊 Base64 Encoder/Decoder"),
            "3": ("crypto_tool", "🔑 Encryption Tool"),
            "4": ("pass_gen", "🎲 Password Generator"),
            "5": ("md5_crack", "🎯 MD5 Cracker"),
            "6": ("pass_strength", "💪 Password Strength Checker"),
            "0": ("main", "⬅️  Back to Main Menu")
        }
        
        for key, (tool, desc) in tools.items():
            print(f"   {Fore.YELLOW}[{key}]{Style.RESET_ALL} {desc}")
        
        choice = input(f"\n{Fore.GREEN}Select tool: {Style.RESET_ALL}")
        
        if choice == "0":
            break
        elif choice in dict(tools).keys():
            tool_name = dict(tools)[choice][0]
            run_tool(tool_name)
        else:
            print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")

def mobile_menu():
    """Mobile & device tools submenu"""
    while True:
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}📱 MOBILE & DEVICE TOOLS:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        tools = {
            "1": ("adb_scanner", "📱 ADB Scanner"),
            "2": ("apk_analyzer", "📦 APK Analyzer"),
            "3": ("firmware_flasher", "⚡ Firmware Flasher"),
            "4": ("mac_changer", "🔄 MAC Changer"),
            "5": ("mobile_recovery", "🔧 Mobile Recovery Tool"),
            "0": ("main", "⬅️  Back to Main Menu")
        }
        
        for key, (tool, desc) in tools.items():
            print(f"   {Fore.YELLOW}[{key}]{Style.RESET_ALL} {desc}")
        
        choice = input(f"\n{Fore.GREEN}Select tool: {Style.RESET_ALL}")
        
        if choice == "0":
            break
        elif choice in dict(tools).keys():
            tool_name = dict(tools)[choice][0]
            run_tool(tool_name)
        else:
            print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")

def osint_menu():
    """OSINT & tracking tools submenu"""
    while True:
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}🕵️  OSINT & TRACKING TOOLS:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        tools = {
            "1": ("ip_tracker", "🌍 IP Tracker"),
            "2": ("geo_locator", "📍 Geo Locator"),
            "3": ("sherlock_osint", "🔍 Sherlock OSINT"),
            "4": ("aio_tracker", "📊 AIO Ultimate Tracker"),
            "5": ("social_recon", "👥 Social Media Recon"),
            "0": ("main", "⬅️  Back to Main Menu")
        }
        
        for key, (tool, desc) in tools.items():
            print(f"   {Fore.YELLOW}[{key}]{Style.RESET_ALL} {desc}")
        
        choice = input(f"\n{Fore.GREEN}Select tool: {Style.RESET_ALL}")
        
        if choice == "0":
            break
        elif choice in dict(tools).keys():
            tool_name = dict(tools)[choice][0]
            run_tool(tool_name)
        else:
            print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")

def web_exploitation_menu():
    """Web exploitation tools submenu"""
    while True:
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}🔗 WEB EXPLOITATION TOOLS:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        tools = {
            "1": ("xss_scanner", "⚠️  XSS Scanner"),
            "2": ("sql_injector", "💉 SQL Injector"),
            "3": ("web_crawler", "🕷️  Web Crawler"),
            "4": ("web_shell_pro", "🐚 Web Shell Pro"),
            "5": ("phishing_sim", "🎣 Phishing Simulator"),
            "0": ("main", "⬅️  Back to Main Menu")
        }
        
        for key, (tool, desc) in tools.items():
            print(f"   {Fore.YELLOW}[{key}]{Style.RESET_ALL} {desc}")
        
        choice = input(f"\n{Fore.GREEN}Select tool: {Style.RESET_ALL}")
        
        if choice == "0":
            break
        elif choice in dict(tools).keys():
            tool_name = dict(tools)[choice][0]
            run_tool(tool_name)
        else:
            print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")

def wireless_menu():
    """Wireless & networking tools submenu"""
    while True:
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}📡 WIRELESS & NETWORKING TOOLS:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        tools = {
            "1": ("wifi_scanner", "📶 WiFi Scanner"),
            "2": ("bluetooth_scanner", "🔵 Bluetooth Scanner"),
            "3": ("arp_spoof", "🔀 ARP Spoofer"),
            "4": ("packet_sniffer", "📦 Packet Sniffer"),
            "5": ("net_discover", "🔎 Network Discovery"),
            "0": ("main", "⬅️  Back to Main Menu")
        }
        
        for key, (tool, desc) in tools.items():
            print(f"   {Fore.YELLOW}[{key}]{Style.RESET_ALL} {desc}")
        
        choice = input(f"\n{Fore.GREEN}Select tool: {Style.RESET_ALL}")
        
        if choice == "0":
            break
        elif choice in dict(tools).keys():
            tool_name = dict(tools)[choice][0]
            run_tool(tool_name)
        else:
            print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")

def system_utilities_menu():
    """System utilities submenu"""
    while True:
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}🛠️  SYSTEM UTILITIES & TOOLS:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        tools = {
            "1": ("sys_info", "💻 System Information"),
            "2": ("security_auditor", "🔍 Security Auditor"),
            "3": ("metadata_stripper", "🧹 Metadata Stripper"),
            "4": ("file_encryption", "🔒 File Encryption"),
            "5": ("termux_optimizer", "⚡ Termux Optimizer"),
            "0": ("main", "⬅️  Back to Main Menu")
        }
        
        for key, (tool, desc) in tools.items():
            print(f"   {Fore.YELLOW}[{key}]{Style.RESET_ALL} {desc}")
        
        choice = input(f"\n{Fore.GREEN}Select tool: {Style.RESET_ALL}")
        
        if choice == "0":
            break
        elif choice in dict(tools).keys():
            tool_name = dict(tools)[choice][0]
            run_tool(tool_name)
        else:
            print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")

def advanced_menu():
    """Advanced & exploitation tools submenu"""
    while True:
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}🔥 ADVANCED & EXPLOITATION TOOLS:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        tools = {
            "1": ("reverse_shell", "🐚 Reverse Shell Generator"),
            "2": ("payload_gen", "🎯 Payload Generator"),
            "3": ("dos_attack", "💥 DOS Attack Simulator"),
            "4": ("tcp_flooder", "🌊 TCP Flooder"),
            "5": ("proxy_checker", "🔍 Proxy Checker"),
            "0": ("main", "⬅️  Back to Main Menu")
        }
        
        for key, (tool, desc) in tools.items():
            print(f"   {Fore.YELLOW}[{key}]{Style.RESET_ALL} {desc}")
        
        choice = input(f"\n{Fore.GREEN}Select tool: {Style.RESET_ALL}")
        
        if choice == "0":
            break
        elif choice in dict(tools).keys():
            tool_name = dict(tools)[choice][0]
            run_tool(tool_name)
        else:
            print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")

def main():
    """Main function - Start the toolkit"""
    display_banner()
    
    while True:
        choice = display_main_menu()
        
        if choice == "1":
            reconnaissance_menu()
        elif choice == "2":
            cryptography_menu()
        elif choice == "3":
            mobile_menu()
        elif choice == "4":
            osint_menu()
        elif choice == "5":
            web_exploitation_menu()
        elif choice == "6":
            wireless_menu()
        elif choice == "7":
            system_utilities_menu()
        elif choice == "8":
            advanced_menu()
        elif choice == "9":
            print(f"\n{Fore.GREEN}[✓] Thank you for using Cyber-Toolkit!")
            print(f"{Fore.CYAN}[✓] Stay Ethical & Stay Powerful{Style.RESET_ALL}\n")
            break
        else:
            print(f"{Fore.RED}[!] Invalid choice. Please try again.{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Program interrupted by user{Style.RESET_ALL}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[!] Fatal error: {e}{Style.RESET_ALL}\n")
        sys.exit(1)
