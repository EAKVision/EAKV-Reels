# Read the current cron watchdog script
with open("setup_cron_watchdog.sh", "r") as f:
    content = f.read()

# Update the cron job string to include the aggressive shift script
old_cron = 'python3 global_women_reach_optimizer.py && python3 matrix_analytics.py'
new_cron = 'python3 aggressive_demographic_shift.py && python3 global_women_reach_optimizer.py && python3 matrix_analytics.py'

if old_cron in content:
    content = content.replace(old_cron, new_cron)
    with open("setup_cron_watchdog.sh", "w") as f:
        f.write(content)
    print("[+] Cron watchdog updated to execute Option 23 automatically.")
else:
    print("[+] Cron watchdog already synchronized or structure differs.")
