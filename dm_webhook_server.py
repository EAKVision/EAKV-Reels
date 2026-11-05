from fastapi import FastAPI, Request, HTTPException
import os

app = FastAPI()

VERIFY_TOKEN = os.getenv("IG_VERIFY_TOKEN", "akv_elite_token_2026")

@app.get("/webhook")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
    
    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("[✓] Webhook verified successfully by Meta Graph API.")
        return int(challenge)
    raise HTTPException(status_code=403, detail="Verification token mismatch")

@app.post("/webhook")
async def handle_comment_webhook(request: Request):
    body = await request.json()
    print(f"[*] Incoming Webhook Payload: {body}")
    
    # Parse Instagram comment event and trigger automated DM funnel
    try:
        entry = body.get("entry", [])
        for item in entry:
            changes = item.get("changes", [])
            for change in changes:
                value = change.get("value", {})
                comment_text = value.get("text", "")
                user_id = value.get("from", {}).get("id", "unknown_user")
                
                if "CODE" in comment_text.upper():
                    print(f"[>] TRIGGER DM TO USER {user_id}: Sending EAKV-Reels GitHub repo link.")
    except Exception as e:
        print(f"[!] Error parsing webhook event: {e}")
        
    return {"status": "received"}

if __name__ == "__main__":
    import uvicorn
    print("=== AKV Elite System: Instagram DM Automation Webhook Active ===")
    uvicorn.run(app, host="0.0.0.0", port=8000)
