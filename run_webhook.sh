#!/bin/bash
export IG_VERIFY_TOKEN="akv_elite_token_2026"
echo "[*] Starting AKV Elite IG Lead Funnel on port 8000..."
python3 -m uvicorn dm_webhook_server:app --host 0.0.0.0 --port 8000 --reload
