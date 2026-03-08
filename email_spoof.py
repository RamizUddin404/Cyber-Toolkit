# CREATED BY: RAMIZ UDDIN
import os, time, cyber_deps

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("EMAIL SPOOFER (PHP MAIL)")
    print("\033[1;32m[*] Professional Email Spoofing Toolkit.")
    print("[*] Requires a web server with PHP mail() enabled.\033[0m")
    
    target = input("\n\033[1;33mEnter Target Email: \033[0m")
    sender = input("Enter Fake Sender Email: \033[0m")
    subject = input("Enter Subject: \033[0m")
    message = input("Enter Message: \033[0m")
    
    print("\n\033[1;32m[*] Generating Spoofing Script...")
    time.sleep(1)
    
    # Create a PHP script for the user to upload
    php_code = f"""<?php
$to = "{target}";
$subject = "{subject}";
$message = "{message}";
$headers = "From: {sender}";
if(mail($to, $subject, $message, $headers)) {{ echo "Email Sent Successfully!"; }}
else {{ echo "Failed to send email."; }}
?>"""
    
    with open("spoof.php", "w") as f:
        f.write(php_code)
        
    print(f"\n\033[1;36m[+] SUCCESS! Spoofing script 'spoof.php' created.\033[0m")
    print("[!] Now upload this file to a PHP hosting and visit the URL to send the mail.")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
