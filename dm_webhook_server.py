import sqlite3
import requests
from datetime import datetime
from fastapi import FastAPI, Request, HTTPException

app = FastAPI(title="Elite AKV Lead Engine & Auto-DM Dispatcher")

DB_FILE = "leads.db"
# Replace with your actual Meta Page Access Token and Instagram Business Account ID when ready
META_ACCESS_TOKEN = "YOUR_META_PERMANENT_ACCESS_TOKEN"
IG_USER_ID = "YOUR_INSTAGRAM_BUSINESS_ACCOUNT_ID"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'CAPTURED'
        )
    """)
    conn.commit()
    conn.close()

init_db()

def send_instagram_dm(recipient_id: str, message_text: str):
    """Dispatches automated DM via Meta Graph API."""
    url = f"https://graph.facebook.com/v18.0/{IG_USER_ID}/messages"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text},
        "access_token": META_ACCESS_TOKEN
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            print(f"[⚡ AUTO-DM SENT] Successfully delivered DM to user {recipient_id}")
            return True
        else:
            print(f"[!] Meta API Error: {response.text}")
            return False
    except Exception as e:
        print(f"[!] Failed to connect to Meta Graph API: {e}")
        return False

@app.get("/")
def read_root():
    return {"status": "ONLINE", "system": "Elite AK Vision Master Node - Auto-DM Enabled"}

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    print(f"[DEBUG] Received payload: {data}")
    
    try:
        user_id = "unknown_user"
        text = ""
        
        # Parse incoming Meta Webhook payload
        if "entry" in data:
            for entry in data.get("entry", []):
                for change in entry.get("changes", []):
                    val = change.get("value", {})
                    user_id = val.get("from", {}).get("id", val.get("sender_id", "meta_user"))
                    text = val.get("text", val.get("message", val.get("comment", "CODE")))
        else:
            # Fallback for test payloads
            user_id = data.get("user_id", data.get("from", "test_user"))
            text = data.get("text", data.get("message", "CODE"))

        # 1. Save persistent record into SQLite database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO leads (user_id, message, timestamp) VALUES (?, ?, ?)",
            (str(user_id), str(text), datetime.utcnow())
        )
        conn.commit()
        conn.close()
        
        # 2. Trigger Automated DM Delivery
        dm_reply = "Hey! Here is your requested C/Unix source code repository: https://github.com/EAKVision/EAKV-Reels ⚡"
        send_instagram_dm(str(user_id), dm_reply)
        
        print(f"[⚡ PERSISTENT LEAD SAVED & AUTO-DM DISPATCHED] User: {user_id} | Message: {text}")
        return {"status": "success", "lead_captured": True, "dm_dispatched": True}
        
    except Exception as e:
        print(f"[!] Error processing lead payload: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
