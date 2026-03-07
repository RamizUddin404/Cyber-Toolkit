#!/bin/bash
clear
echo -e "\033[1;32m[*] Setting up RAMIZ UDDIN Ultimate Toolkit...\033[0m"
pkg update && pkg upgrade -y
pkg install python git termux-api -y
pip install requests pillow scapy

echo -e "\033[1;33m[!] PLEASE FOLLOW FOR UPDATES [!]\033[0m"
echo -e "GITHUB: https://github.com/RamizUddin404"
echo -e "FACEBOOK: https://www.facebook.com/Ramiz.Uddin404"
sleep 2
termux-open-url https://github.com/RamizUddin404
sleep 2
termux-open-url "fb://facewebmodal/f?href=https://www.facebook.com/Ramiz.Uddin404"

echo -e "\033[1;32m[+] Setup Complete. Run 'python main.py' to start.\033[0m"
