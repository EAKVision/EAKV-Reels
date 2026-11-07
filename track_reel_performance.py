import csv
import os
import sys
import time

CSV_FILE = "reel_performance.csv"

def log_reel(reel_id, title, niche, views=0, likes=0, shares=0):
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "reel_id", "title", "niche", "views", "likes", "shares", "status"])
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), reel_id, title, niche, views, likes, shares, "LOGGED_&_TRACKED ⚡"])
    print(f"✅ [SUCCESS] Reel payload '{reel_id}' ({title}) logged to {CSV_FILE}")

if __name__ == "__main__":
    reel_id = sys.argv[1] if len(sys.argv) > 1 else "DfccmkhqTqf"
    title = sys.argv[2] if len(sys.argv) > 2 else "World Record Breaker"
    niche = sys.argv[3] if len(sys.argv) > 3 else "hybrid_athletics"
    log_reel(reel_id, title, niche)
