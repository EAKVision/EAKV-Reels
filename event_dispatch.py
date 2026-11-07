import time
import json
import os

PAYLOAD_MAP = {
    "CODE": "https://github.com/EAKVision/EAKV-Reels/blob/main/kernel_tracer.c",
    "BUILD": "https://github.com/EAKVision/EAKV-Reels/blob/main/render_pipeline.py",
    "MATRIX": "https://github.com/EAKVision/EAKV-Reels/blob/main/boost_config.py",
    "SYSTEM": "https://github.com/EAKVision/EAKV-Reels"
}

def log_event(user_handle, keyword, payload):
    event = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "user": user_handle,
        "keyword": keyword,
        "payload": payload
    }
    
    events = []
    if os.path.exists("funnel_events.json"):
        with open("funnel_events.json", "r") as f:
            try:
                events = json.load(f)
            except:
                events = []
                
    events.append(event)
    with open("funnel_events.json", "w") as f:
        json.dump(events, f, indent=2)

def handle_comment_event(comment_text, user_handle):
    for kw, payload in PAYLOAD_MAP.items():
        if kw in comment_text.upper():
            print(f"[DM-FUNNEL] Trigger '{kw}' detected from @{user_handle}!")
            print(f"            ↳ Payload Routed: {payload}")
            print(f"            ↳ Dispatching instant DM response...")
            log_event(user_handle, kw, payload)
            print(f"✅ [CONVERSION LOGGED] Event written to funnel_events.json")
            return True
    return False

if __name__ == "__main__":
    print("[EVENT-DISPATCH] Master Webhook & DM Funnel Active.")
    handle_comment_event("Send me the CODE for this system!", "alex_dev")
    handle_comment_event("I want to see the MATRIX config", "sarah_tech")
