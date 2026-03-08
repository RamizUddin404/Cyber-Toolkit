# CREATED BY: RAMIZ UDDIN
import os, sys, time, socketserver, http.server, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

PORT = 8088

class WebShellHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        print(f"\033[1;32m[*] Executing: {post_data}\033[0m")
        try:
            output = subprocess.check_output(post_data, shell=True, stderr=subprocess.STDOUT).decode('utf-8')
        except Exception as e:
            output = str(e)
            
        self.send_response(200)
        self.end_headers()
        self.wfile.write(output.encode('utf-8'))

def run():
    tool_header("REMOTE WEB CONSOLE (ACCESS PRO)")
    print("\033[1;32m[*] Control your Termux from any Browser via Link.")
    print("[*] 100% Working on Root & Non-Root.\033[0m")
    
    # Create the Web Shell Interface
    with open("shell_index.html", "w") as f:
        f.write("""
        <html>
        <head><title>Remote Console</title></head>
        <body style="background: #121212; color: #00FF00; font-family: monospace; padding: 20px;">
            <h3>RAMIZ UDDIN REMOTE CONSOLE</h3>
            <div id="out" style="border: 1px solid #333; height: 300px; overflow-y: scroll; padding: 10px; margin-bottom: 10px;"></div>
            <input id="cmd" type="text" style="width: 80%; background: #000; color: #00FF00; border: 1px solid #333; padding: 5px;">
            <button onclick="exec()" style="padding: 5px;">Send</button>
            <script>
                async function exec() {
                    const cmd = document.getElementById('cmd').value;
                    const res = await fetch('/', {method: 'POST', body: cmd});
                    const text = await res.text();
                    document.getElementById('out').innerHTML += '<br>> ' + cmd + '<br>' + text.replace(/\\n/g, '<br>');
                    document.getElementById('cmd').value = '';
                }
            </script>
        </body>
        </html>
        """)

    print("\n\033[1;33m[+] Console Server Active at: http://127.0.0.1:8088")
    print("[!] Use 'Cloud Tunnel' (Tool 101) to get a public access link.\033[0m")
    
    os.system("mv shell_index.html index.html")
    handler = WebShellHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("\033[1;32m[*] Waiting for remote commands... (Ctrl+C to stop)\033[0m")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\033[1;31m[!] Stopping Server...\033[0m")
            os.system("rm index.html")
            httpd.shutdown()

if __name__ == "__main__": run()
