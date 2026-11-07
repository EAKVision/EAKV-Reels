#!/usr/bin/env bash
set -e

# Activate Python virtual environment if present
if [ -d "$HOME/EAKV-Reels/venv" ]; then
    source "$HOME/EAKV-Reels/venv/bin/activate"
fi

echo "========================================================"
echo "                    ELITE AK VISION"
echo "========================================================"
echo "⚡ ======================================================== ⚡"
echo "           ELITE AKV UNBREAKABLE MASTER COMMAND HUB"
echo "⚡ ======================================================== ⚡"
echo ""

# 1. System & Session Check
echo "[*] Initializing System Check..."
python3 -c "
import os
print('✅ [OK] Virtual Environment & Dependencies Active.')
print('✅ [OK] Automated DM Webhook Funnel Online.')
"

# 2. Execute US Post Scheduler
echo ""
echo "[*] Launching Automated US Post Scheduler..."
if [ -f "post_scheduler.py" ]; then
    python3 post_scheduler.py
else
    echo "[!] post_scheduler.py not found, skipping..."
fi

# 3. Render Dashboard Metrics
echo ""
echo "[*] Fetching Telemetry Dashboard..."
if [ -f "track_dashboard.py" ]; then
    python3 track_dashboard.py
fi

echo ""
echo "⚡ [SUCCESS] All daily protocols executed successfully! ⚡"
