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

echo -e "\n$GREEN[*] Step 1: Detecting System...$RESET"
if [ -d "/data/data/com.termux/files/usr" ]; then
    echo -e "$BLUE[+] Termux Environment Detected$RESET"
    PKG_MGR="pkg"
    INSTALL_CMD="pkg install -y"
    UPDATE_CMD="pkg update -y && pkg upgrade -y"
    SYS_PACKAGES="python git clang wget curl jq tar zip unzip proot openssl termux-api"
elif [ -f "/etc/os-release" ]; then
    echo -e "$BLUE[+] Linux Environment Detected$RESET"
    PKG_MGR="apt"
    if [ "$EUID" -ne 0 ]; then
        SUDO="sudo"
    else
        SUDO=""
    fi
    UPDATE_CMD="$SUDO apt update -y"
    INSTALL_CMD="$SUDO apt install -y"
    SYS_PACKAGES="python3 python3-pip git clang wget curl jq tar zip unzip openssl"
else
    echo -e "$RED[!] Unknown System. Proceeding with caution...$RESET"
    PKG_MGR="unknown"
fi

echo -e "\n$GREEN[*] Step 2: Installing Core Dependencies...$RESET"
if [ "$PKG_MGR" != "unknown" ]; then
    eval $UPDATE_CMD
    eval $INSTALL_CMD $SYS_PACKAGES
else
    echo -e "$YELLOW[!] Please install dependencies manually: python, git, wget, curl...$RESET"
fi

echo -e "\n$GREEN[*] Step 3: Installing Python Modules...$RESET"
if [ "$PKG_MGR" == "apt" ]; then
    pip3 install -r requirements.txt --break-system-packages 2>/dev/null || pip3 install -r requirements.txt
    pip3 install requests colorama beautifulsoup4 mechanize --break-system-packages 2>/dev/null || pip3 install requests colorama beautifulsoup4 mechanize
else
    pip install -r requirements.txt
    pip install requests colorama beautifulsoup4 mechanize
fi

echo -e "\n$GREEN[*] Step 4: Setting Permissions...$RESET"
chmod +x *.py
chmod +x *.sh

echo -e "\n$CYAN[+] INSTALLATION COMPLETE!$RESET"
echo -e "$YELLOW[*] Usage: python3 main.py$RESET"
echo -e "$BLUE[*] Stay Ethical. Stay Powerful.$RESET"
