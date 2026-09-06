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
echo -e "$YELLOW       ULTIMATE CYBER-TOOLKIT v180.0 SETUP"
echo -e "$YELLOW       CREATED BY: RAMIZ UDDIN$RESET"
echo "============================================="

echo -e "\n$GREEN[*] Step 1: Detecting System...$RESET"
if [ -d "/data/data/com.termux/files/usr" ]; then
    echo -e "$BLUE[+] Termux Environment Detected$RESET"
    PKG_MGR="pkg"
    INSTALL_CMD="pkg install -y"
    UPDATE_CMD="pkg update -y && pkg upgrade -y"
    SYS_PACKAGES="python git clang wget curl jq tar zip unzip proot openssl python-pip"
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
    SYS_PACKAGES="python3 python3-pip git curl wget jq tar zip unzip openssl build-essential"
else
    echo -e "$RED[!] Unknown System. Proceeding with caution...$RESET"
    PKG_MGR="unknown"
fi

echo -e "\n$GREEN[*] Step 2: Installing Core System Dependencies...$RESET"
if [ "$PKG_MGR" != "unknown" ]; then
    echo -e "$YELLOW[*] Running: $UPDATE_CMD$RESET"
    eval $UPDATE_CMD
    echo -e "$YELLOW[*] Running: $INSTALL_CMD $SYS_PACKAGES$RESET"
    eval $INSTALL_CMD $SYS_PACKAGES
    echo -e "$GREEN[+] System dependencies installed successfully$RESET"
else
    echo -e "$YELLOW[!] Please install dependencies manually: python, git, wget, curl, build-essential...$RESET"
fi

echo -e "\n$GREEN[*] Step 3: Installing Python Modules...$RESET"
if [ "$PKG_MGR" == "apt" ]; then
    echo -e "$YELLOW[*] Installing from core/requirements.txt...$RESET"
    pip3 install -r core/requirements.txt --break-system-packages 2>/dev/null || pip3 install -r core/requirements.txt
    echo -e "$GREEN[+] Python modules installed successfully$RESET"
else
    echo -e "$YELLOW[*] Installing from core/requirements.txt...$RESET"
    pip install -r core/requirements.txt
    echo -e "$GREEN[+] Python modules installed successfully$RESET"
fi

echo -e "\n$GREEN[*] Step 4: Setting Permissions...$RESET"
chmod +x main.py
chmod +x setup.sh
chmod +x core/*.py 2>/dev/null
chmod +x core/*.sh 2>/dev/null
echo -e "$GREEN[+] Permissions set successfully$RESET"

echo -e "\n$CYAN╔════════════════════════════════════════════════════╗"
echo -e "$CYAN║$GREEN     ✓ INSTALLATION COMPLETE SUCCESSFULLY!    $CYAN║"
echo -e "$CYAN╚════════════════════════════════════════════════════╝$RESET"

echo -e "\n$YELLOW📋 NEXT STEPS:$RESET"
echo -e "$GREEN[1]$RESET Run: ${CYAN}python3 main.py$RESET"
echo -e "$GREEN[2]$RESET Select a tool category (1-8)"
echo -e "$GREEN[3]$RESET Choose a specific tool"
echo -e "$GREEN[4]$RESET Follow tool instructions"

echo -e "\n$YELLOW📚 DOCUMENTATION:$RESET"
echo -e "$GREEN[*]$RESET README.md - Full documentation & features"
echo -e "$GREEN[*]$RESET Check GitHub: https://github.com/RamizUddin404/Cyber-Toolkit"

echo -e "\n$BLUE[*] Stay Ethical. Stay Powerful.$RESET"
echo -e "$CYAN[*] © 2026 RAMIZ UDDIN | All Rights Reserved$RESET\n"
