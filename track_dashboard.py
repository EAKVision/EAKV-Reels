import os
import sqlite3

def print_dashboard():
    print("==================================================")
    print("     AKV ELITE SYSTEM: UNBREAKABLE TELEMETRY")
    print("==================================================")
    
    # Query database leads
    db_file = "leads.db"
    total_leads = 0
    recent_leads = []
    
    if os.path.exists(db_file):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM leads")
        total_leads = cursor.fetchone()[0]
        
        cursor.execute("SELECT user_id, message, timestamp FROM leads ORDER BY id DESC LIMIT 3")
        recent_leads = cursor.fetchall()
        conn.close()
        print(f"[*] Webhook Funnel Status : ONLINE (Database Backed)")
    else:
        print(f"[*] Webhook Funnel Status : INITIALIZING")
        
    print(f"[*] Total Code Leads Captured: {total_leads}")
    
    if recent_leads:
        print("\n--- Recent Lead Feed ---")
        for u_id, msg, ts in recent_leads:
            print(f"  • [{ts}] User: {u_id} -> '{msg}'")
            
    print("\n--- Rendered Assets ---")
    video_files = [f for f in os.listdir('.') if f.endswith('.mp4')]
    print(f"[*] Rendered Viral Reels Ready: {len(video_files)} assets available.")
    for vf in video_files[:5]:
        size = os.path.getsize(vf) / (1024 * 1024)
        print(f"    - {vf} ({size:.2f} MB)")
    print("==================================================")

if __name__ == "__main__":
    print_dashboard()
