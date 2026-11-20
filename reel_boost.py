#!/usr/bin/env python3
import argparse
import csv
import datetime
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlencode, urlparse

TARGET_REEL = "https://www.instagram.com/reel/Df2_mtKK8tj/"
LOG_FILE = os.path.expanduser("~/reel_clicks.csv")

CHANNELS = {
    "x": "X / Twitter",
    "li": "LinkedIn",
    "yt": "YouTube Shorts",
    "gh": "GitHub / Bio",
    "wa": "WhatsApp / Direct",
}


def init_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp_utc", "channel", "campaign", "referer", "user_agent"])


def log_click(channel: str, campaign: str, referer: str, user_agent: str):
    init_log()
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([ts, channel, campaign, referer, user_agent[:120]])


class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path != "/r":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")
            return

        params = parse_qs(parsed.query)
        channel = params.get("ch", ["direct"])[0]
        campaign = params.get("camp", ["Df2_mtKK8tj"])[0]
        referer = self.headers.get("Referer", "-")
        ua = self.headers.get("User-Agent", "-")

        log_click(channel, campaign, referer, ua)

        utm = urlencode({
            "utm_source": channel,
            "utm_medium": "social_drop",
            "utm_campaign": campaign,
        })
        dest = f"{TARGET_REEL}?{utm}"

        print(f"[CLICK] {datetime.datetime.now().strftime('%H:%M:%S')} | ch={channel} | ref={referer}")
        self.send_response(302)
        self.send_header("Location", dest)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()

    def log_message(self, format, *args):
        return


def cmd_links(tunnel_url: str, campaign: str):
    base = tunnel_url.rstrip("/")
    print(f"\n=== Tracked Distribution Links ({campaign}) ===\n")
    for code, name in CHANNELS.items():
        url = f"{base}/r?ch={code}&camp={campaign}"
        print(f"  {name:<20} -> {url}")

    print("\n=== Ready-to-Post Copy ===\n")
    print(f"[X / Threads]\nNew drop live. Full breakdown here -> {base}/r?ch=x&camp={campaign}\n")
    print(f"[LinkedIn]\nSharing a quick look at what I've been building lately. Watch the clip -> {base}/r?ch=li&camp={campaign}\n")
    print(f"[YouTube Community / Shorts Pin]\nWatch the full reel here -> {base}/r?ch=yt&camp={campaign}\n")


def cmd_stats():
    if not os.path.exists(LOG_FILE):
        print("No clicks recorded yet.")
        return

    counts = {}
    total = 0
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ch = row["channel"]
            counts[ch] = counts.get(ch, 0) + 1
            total += 1

    print(f"\n=== Reel Click Stats (Total: {total}) ===")
    for ch, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        label = CHANNELS.get(ch, ch)
        print(f"  {label:<20} : {count}")
    print()


def cmd_serve(port: int):
    init_log()
    server = HTTPServer(("127.0.0.1", port), RedirectHandler)
    print(f"Listening on http://127.0.0.1:{port}/r -> forwarding to {TARGET_REEL}")
    print("Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reel UTM Redirector & Distribution CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_serve = sub.add_parser("serve", help="Run local redirect tracker")
    p_serve.add_argument("--port", type=int, default=8085)

    p_links = sub.add_parser("links", help="Generate tracked links & post copy")
    p_links.add_argument("--tunnel", required=True, help="Your Cloudflare Quick Tunnel URL")
    p_links.add_argument("--campaign", default="Df2_mtKK8tj")

    sub.add_parser("stats", help="Show click counts by channel")

    args = parser.parse_args()
    if args.cmd == "serve":
        cmd_serve(args.port)
    elif args.cmd == "links":
        cmd_links(args.tunnel, args.campaign)
    elif args.cmd == "stats":
        cmd_stats()
