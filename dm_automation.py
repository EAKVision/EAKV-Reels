def handle_incoming_comment(user_handle, comment_text):
    keyword = "CODE"
    if keyword.lower() in comment_text.lower():
        dm_payload = (
            f"Hey {user_handle}! Here is the direct link to the low-level C codebase "
            f"and systems architecture repo: https://github.com/EAKVision/EAKV-Reels"
        )
        send_instagram_dm(user_handle, dm_payload)

def send_instagram_dm(user_handle, message):
    print(f"[DM SENT -> @{user_handle}]: {message}")

if __name__ == "__main__":
    print("[*] Elite System DM Funnel Active. Listening for incoming comments...")
    handle_incoming_comment("us_tech_lead", "Send me the CODE for this vm!")
