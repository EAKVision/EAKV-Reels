#!/bin/bash
cd /home/AK/EAKV-Reels
while true; do
    echo "[$(date)] 🚀 Launching global_247_daemon.py..." >> daemon_runtime.log
    python3 global_247_daemon.py >> daemon_runtime.log 2>&1
    echo "[$(date)] ⚠️ Daemon exited. Restarting in 5 seconds..." >> daemon_runtime.log
    sleep 5
done
