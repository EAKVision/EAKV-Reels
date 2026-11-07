"""
EAKV Comment Velocity Bot
Scans active target reels and queues high-velocity smart responses to trigger algorithm loops.
"""

import json
import os
import time

def process_comments():
    target_file = "active_target.json"
    if not os.path.exists(target_file):
        print("❌ [ERROR] active_target.json not found.")
        return

    with open(target_file, "r") as f:
        config = json.load(f)

    targets = config.get("targets", [])
    if not targets and "target_media_shortcode" in config:
        targets = [config["target_media_shortcode"]]

    print("====================================================")
    print(f"🤖 INITIALIZING COMMENT VELOCITY BOT ({len(targets)} TARGETS)")
    print("====================================================")

    sample_incoming = [
        {"user": "@dev_hustle", "text": "Is malloc returning NULL guaranteed on failure?", "type": "technical"},
        {"user": "@gym_coder", "text": "The energy in this reel is insane 🔥💪", "type": "hype"},
        {"user": "@c_architect", "text": "Why not use calloc here?", "type": "technical"}
    ]

    for shortcode in targets:
        print(f"\n📩 Monitoring incoming comments on Reel: {shortcode}")
        time.sleep(0.3)

        for item in sample_incoming:
            user = item["user"]
            comment = item["text"]
            c_type = item["type"]

            if c_type == "technical":
                reply = f"⚡ @{user} Yes! Always check for NULL pointer return before dereferencing."
            else:
                reply = f"🔥 @{user} Low-level code + high-energy execution! Appreciate the hype!"

            print(f"   👤 {user}: '{comment}'")
            print(f"   🤖 Response Dispatched: '{reply}'")
            time.sleep(0.3)

    print("\n✅ Comment velocity queue cleared! Engagement rate boosted.")
    print("====================================================")

if __name__ == "__main__":
    process_comments()
