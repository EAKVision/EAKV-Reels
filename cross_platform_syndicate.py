"""
EAKV Multi-Platform Syndicate Engine
Reformats technical code assets into platform-optimized copy for TikTok, X, LinkedIn, & Threads.
"""

import os
import json

def syndicate_content():
    asset_path = "output/code_reel_asset.txt"
    if not os.path.exists(asset_path):
        print("[ERROR] Code asset not found. Run code_to_reel.py first.")
        return

    with open(asset_path, "r") as f:
        code_snippet = f.read()

    print("🌐 Initializing EAKV Global Syndication Engine...")
    print("--------------------------------------------------")

    syndicate_payload = {
        "x_twitter": {
            "hook": "99% of developers write memory leaks. Here is low-level C memory allocation done right in 10 lines of code: 👇",
            "body": f"```c\n{code_snippet.strip()}\n```",
            "hashtags": "#CProgramming #SystemsEngineering #SoftwareEngineering"
        },
        "linkedin": {
            "hook": "Understanding low-level memory layout isn't optional if you want to build ultra-low latency systems.",
            "body": f"Here is a clean C memory allocation block demonstrating safe pointer checking:\n\n{code_snippet.strip()}\n\nWhat's your go-to pattern for safe allocation?",
            "hashtags": "#SoftwareEngineering #C #SystemsProgramming #ComputerScience"
        },
        "threads": {
            "hook": "Low-level system architecture tip for the day ⚡",
            "body": f"Pointer safety in C:\n{code_snippet.strip()}",
            "hashtags": "#coding #developer #cprogramming"
        },
        "tiktok": {
            "caption": "Low-level C pointers explained in 15s ⚡ #coding #cprogramming #developer #tech #wsl",
            "audio_strategy": "Trending high-tempo beats"
        }
    }

    os.makedirs("output/syndication", exist_ok=True)
    out_file = "output/syndication/syndicate_payload.json"
    with open(out_file, "w") as f:
        json.dump(syndicate_payload, f, indent=4)

    print(f"🎯 Syndication payload compiled across 4 platforms!")
    print(f"📁 Output saved at: {out_file}")
    print("🚀 Platforms Ready: X (Twitter) | LinkedIn | Threads | TikTok")

if __name__ == "__main__":
    syndicate_content()
