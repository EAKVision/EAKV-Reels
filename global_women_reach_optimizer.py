#!/usr/bin/env python3
"""
global_women_reach_optimizer.py - Calibrates US & global reach for 50%+ female demographic dominance.
"""

import json

def optimize_reach():
    print("[*] Calibrating US & Worldwide demographic engine for 50%+ female share (18-35)...")
    
    payload = {
        "target_regions": [
            "United States (Primary - NYC, SF, LA tech & design hubs)",
            "Global / Worldwide (Secondary - London, Tokyo, Berlin)"
        ],
        "target_demographic": "Women 18-35 (Tech, Architecture, Minimalist Design, Productivity, Engineering)",
        "demographic_split_goal": "50%+ Female / <50% Male",
        "aesthetic_calibration": "Warm dark mode, clean typography, calm execution, workspace architecture",
        "active_seo_tags": [
            "#aesthetictech",
            "#minimalistdesk",
            "#deepwork",
            "#workspacegoals",
            "#softwareengineer",
            "#productivitysystem",
            "#techlifestyle",
            "#girlsintech",
            "#deskinspiration"
        ],
        "status": "50%+ Female Demographic Lock Active"
    }
    
    with open("active_target.json", "w") as f:
        json.dump(payload, f, indent=2)
        
    print("[+] Demographic distribution successfully updated.")
    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    optimize_reach()
