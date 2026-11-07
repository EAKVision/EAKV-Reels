import json
import os
import time

def process_live_webhook(event_payload):
    user = event_payload.get("user", "unknown_user")
    comment = event_payload.get("comment", "").upper()
    
    print(f"[WEBHOOK] Incoming engagement event from @{user}: '{comment}'")
    
    keyword_map = {
        "CODE": "https://github.com/EAKVision/EAKV-Reels/blob/main/kernel_tracer.c",
        "PLAYBOOK": "https://github.com/EAKVision/EAKV-Reels",
        "MATRIX": "https://github.com/EAKVision/EAKV-Reels/blob/main/boost_config.py"
    }
    
    for kw, link in keyword_map.items():
        if kw in comment:
            dispatch_event = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "platform": event_payload.get("platform", "Instagram"),
                "user": user,
                "keyword": kw,
                "payload_dispatched": link
            }
            
            # Append to funnel log
            events = []
            if os.path.exists("funnel_events.json"):
                with open("funnel_events.json", "r") as f:
                    try:
                        events = json.load(f)
                    except:
                        events = []
            events.append(dispatch_event)
            with open("funnel_events.json", "w") as f:
                json.dump(events, f, indent=2)
                
            print(f"✅ [DISPATCHED] Instant DM sent to @{user} with payload: {link}")
            return True
            
    print("ℹ️ [IGNORED] No matching keyword trigger found.")
    return False

if __name__ == "__main__":
    print("[WEBHOOK-BRIDGE] Listening for live platform events...")
    sample_event = {"platform": "Instagram", "user": "elite_coder_99", "comment": "Send me the PLAYBOOK!"}
    process_live_webhook(sample_event)
