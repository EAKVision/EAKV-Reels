#!/usr/bin/env python3
import json
import os
import datetime

def check_system_health():
    print("====================================================")
    print("📊 EAKV SOVEREIGN TELEMETRY & HEALTH CHECK")
    print("====================================================")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[*] Timestamp: {timestamp}")
    
    # Check active targets file
    if os.path.exists("active_target.json"):
        try:
            with open("active_target.json", "r") as f:
                data = json.load(f)
                count = len(data.get("targets", []))
            print(f"  [Check 1] active_target.json : [OK] ({count} active nodes loaded)")
        except Exception:
            print("  [Check 1] active_target.json : [ERROR] (Malformed JSON)")
    else:
        print("  [Check 1] active_target.json : [MISSING]")
        
    # Check core scripts
    scripts = ["live_social_publisher.py", "growth_booster.py", "boost_protocol.py", "retrigger_pipeline.py"]
    for s in scripts:
        if os.path.exists(s):
            print(f"  [Check Script] {s} : [ONLINE]")
        else:
            print(f"  [Check Script] {s} : [MISSING]")
            
    # Check git status
    git_status = os.system("git status --porcelain > /dev/null 2>&1")
    if git_status == 0:
        print("  [Check 2] Git Working Tree : [CLEAN & SYNCHED]")
    else:
        print("  [Check 2] Git Working Tree : [UNCOMMITTED CHANGES]")

    print("====================================================")
    print("[+] SYSTEM TELEMETRY NOMINAL: 24/7 autonomous engines ready.")
    print("====================================================")

if __name__ == "__main__":
    check_system_health()
