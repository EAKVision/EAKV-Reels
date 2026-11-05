import os
import datetime

def audit_performance():
    print("==================================================")
    print("     AKV ELITE SYSTEM: PERFORMANCE DASHBOARD      ")
    print("==================================================")
    
    # Check Webhook server status
    webhook_active = os.system("pgrep -f 'dm_webhook_server' > /dev/null 2>&1") == 0
    print(f"[*] Webhook Funnel Status : {'ONLINE (24/7 Active)' if webhook_active else 'OFFLINE'}")
    
    # Audit webhook log conversions if present
    log_file = "webhook.log"
    total_leads = 0
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            for line in f:
                if "TRIGGER DM TO USER" in line or "CODE" in line:
                    total_leads += 1
        print(f"[*] Total Code Leads Captured: {total_leads}")
    else:
        print("[*] Total Code Leads Captured: 0 (No logs yet)")
        
    # Check generated 1M+ viral reels
    reels = [f for f in os.listdir() if f.endswith(".mp4")]
    print(f"[*] Rendered Viral Reels Ready: {len(reels)} assets available.")
    for reel in reels:
        size_mb = os.path.getsize(reel) / (1024 * 1024)
        print(f"    - {reel} ({size_mb:.2f} MB)")
        
    print("==================================================")

if __name__ == "__main__":
    audit_performance()
