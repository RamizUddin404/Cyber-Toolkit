#!/bin/bash

# COLORS
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
RESET='\033[0m'

clear
echo -e "$CYAN"
echo "  ██████╗██╗   ██╗██████╗ ███████╗██████╗ "
echo " ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗"
echo " ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝"
echo " ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗"
echo " ╚██████╗   ██║   ██████╔╝███████╗██║  ██║"
echo "  ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝"
echo -e "$RESET"
echo -e "$YELLOW       ULTIMATE CYBER-TOOLKIT v180.0"
echo -e "$YELLOW       CREATED BY: RAMIZ UDDIN$RESET"
echo "============================================="

echo -e "\n$GREEN[*] Step 1: Installing Core Dependencies...$RESET"
pkg update -y && pkg upgrade -y
pkg install python git clang wget curl jq tar zip unzip proot openssl -y
pkg install termux-api -y

echo -e "\n$GREEN[*] Step 2: Installing Python Modules...$RESET"
pip install -r requirements.txt
pip install requests colorama beautifulsoup4 mechanize

echo -e "\n$GREEN[*] Step 3: Setting Permissions...$RESET"
chmod +x *.py
chmod +x *.sh

echo -e "\n$CYAN[+] INSTALLATION COMPLETE!$RESET"
echo -e "$YELLOW[*] Usage: python main.py$RESET"
echo -e "$BLUE[*] Stay Ethical. Stay Powerful.$RESET"
