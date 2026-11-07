import sqlite3
import requests
import time

DB_PATH = "leads.db"

# ⚠️ REPLACE THIS WITH YOUR ACTUAL META GRAPH API PAGE ACCESS TOKEN
META_ACCESS_TOKEN = "YOUR_META_ACCESS_TOKEN_HERE"

def process_retry_queue():
    if META_ACCESS_TOKEN == "YOUR_META_ACCESS_TOKEN_HERE":
        print("[CONFIG ERROR] Please insert your active Meta Access Token inside retry_dms.py")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT rowid, * FROM leads WHERE dm_sent = 0")
        pending_leads = cursor.fetchall()
        print(f"[RETRY QUEUE] Found {len(pending_leads)} pending DMs to process.")
    except Exception as e:
        print(f"[ERROR Reading Database]: {e}")
        conn.close()
        return

    for lead in pending_leads:
        lead_id = lead["rowid"]
        user_id = lead["user_id"]

        url = f"https://graph.facebook.com/v18.0/me/messages?access_token={META_ACCESS_TOKEN}"
        payload = {
            "recipient": {"id": user_id},
            "message": {"text": "Here is your C/Unix low-level source repository: https://github.com/EAKVision/EAKV-Reels"}
        }
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                cursor.execute("UPDATE leads SET dm_sent = 1 WHERE rowid = ?", (lead_id,))
                conn.commit()
                print(f"[DELIVERED] DM successfully sent to User ID: {user_id}")
            else:
                print(f"[FAILED] Meta API Error for User ID {user_id}: {res.text}")
        except Exception as e:
            print(f"[ERROR] Network exception for User ID {user_id}: {e}")
        
        time.sleep(1)
        
    conn.close()

if __name__ == "__main__":
    process_retry_queue()
