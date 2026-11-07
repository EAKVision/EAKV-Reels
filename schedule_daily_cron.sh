#!/bin/bash

# EAKV Cron Scheduler Installer

WORKSPACE_DIR=$(pwd)
CRON_JOB="0 9 * * * cd $WORKSPACE_DIR && python3 code_to_reel.py && python3 render_reel_video.py && python3 boost_organic.py && python3 cross_platform_syndicate.py && python3 auto_publish_syndicate.py >> $WORKSPACE_DIR/output/cron_execution.log 2>&1"

(crontab -l 2>/dev/null | grep -F "$WORKSPACE_DIR"; echo "$CRON_JOB") | crontab -

echo "===================================================="
echo "⏰ AUTOMATED DAILY CRON JOB SCHEDULED SUCCESSFULLY"
echo "===================================================="
echo "📅 Schedule: Daily at 9:00 AM sharp"
echo "📁 Execution Log: output/cron_execution.log"
echo "⚡ Pipeline: Code Compile ➔ Render Video ➔ Organic Boost ➔ Syndicate ➔ Auto-Publish"
echo "===================================================="
