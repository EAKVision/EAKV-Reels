#!/usr/bin/env python3
import http.server
import socketserver
import json
import os

PORT = 8080

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Load active targets for live telemetry
        try:
            with open("active_target.json", "r") as f:
                data = json.load(f)
                targets = data.get("targets", [])
        except:
            targets = []

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>EAKV Sovereign Live Telemetry Dashboard</title>
            <style>
                body {{ background-color: #0d1117; color: #c9d1d9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 40px; }}
                h1 {{ color: #58a6ff; border-bottom: 1px solid #30363d; padding-bottom: 10px; }}
                .card {{ background-color: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 20px; margin-bottom: 20px; }}
                .status {{ color: #2ea043; font-weight: bold; }}
            </style>
        </head>
        <body>
            <h1>🚀 EAKV SOVEREIGN LIVE WEB TELEMETRY DASHBOARD</h1>
            <div class="card">
                <h3>System Status: <span class="status">ONLINE & MAXIMUM REACH LOCKED</span></h3>
                <p><b>Target Demographic:</b> Women 18-35 / US & Global Tech Ecosystem</p>
                <p><b>Active Syndication Nodes:</b> Instagram (<code>DffK5tmKnyT</code>) & LinkedIn (<code>evufNhDG</code>)</p>
            </div>
            <div class="card">
                <h3>Active Target Matrix</h3>
                <pre>{json.dumps(targets, indent=2)}</pre>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

def run_server():
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        print(f"====================================================")
        print(f"📊 EAKV LIVE WEB TELEMETRY DASHBOARD RUNNING")
        print(f"[*] Access via browser at: http://localhost:{PORT}")
        print(f"====================================================")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
