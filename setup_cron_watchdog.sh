#!/bin/bash
echo "===================================================="
echo "⚡ INITIALIZING EAKV AUTONOMOUS CRON WATCHDOG"
echo "===================================================="
# Registering background execution loops for 24/7 sovereign syndication
crontab -l 2>/dev/null | grep -v "master_execution_suite.py" > current_cron.txt
echo "0 * * * * cd /home/AK/EAKV-Reels && python3 master_execution_suite.py >> cron_execution.log 2>&1" >> current_cron.txt
crontab current_cron.txt
rm current_cron.txt
echo "[+] Cron watchdog successfully registered. 24/7 autonomous loop active."
echo "===================================================="
