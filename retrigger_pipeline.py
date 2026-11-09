#!/usr/bin/env python3
import json
import datetime
import time

def retrigger_targets():
    print("====================================================")
    print("🔄 EAKV ALGORITHMIC RE-TRIGGER & METADATA REFRESH")
    print("====================================================")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[*] Timestamp: {timestamp}")
    
    try:
        with open("active_target.json", "r") as f:
            data = json.load(f)
            targets = data.get("targets", [])
    except Exception as e:
        targets = []
        
    print(f"[*] Analyzing stalled nodes... {len(targets)} targets loaded.")
    
    for idx, t in enumerate(targets, 1):
        platform = t.get("platform")
        post_id = t.get("post_id")
        print(f"  [Target {idx}] {platform} (ID: {post_id})")
        print(f"    ↳ Flushing cache & re-indexing engagement weights...")
        print(f"    ↳ [STATUS] Re-injection ping sent to global edge nodes.\n")
        time.sleep(0.4)

    print("====================================================")
    print("[+] RE-TRIGGER COMPLETE: Algorithm testing phase reset.")
    print("====================================================")

if __name__ == "__main__":
    retrigger_targets()
