with open("master_hub.sh", "r") as f:
    content = f.read()

# Expand range display
content = content.replace("[1-12]", "[1-15]")
content = content.replace("-le 12", "-le 15")

# Add options before Option 10 (Exit Hub)
target_menu = " 10. Exit Hub"
new_menu = """ 13. Run Automated Reel Batcher (python3 auto_reel_batcher.py)
 14. Run Matrix Analytics & Telemetry (python3 matrix_analytics.py)
 15. Setup Autonomous Cron Watchdog (python3 setup_cron_watchdog.sh)
 10. Exit Hub"""

if target_menu in content and "13." not in content:
    content = content.replace(target_menu, new_menu)

# Add case statements before option 10
target_case = "10)"
new_case = """13)
        python3 auto_reel_batcher.py
        ;;
    14)
        python3 matrix_analytics.py
        ;;
    15)
        python3 setup_cron_watchdog.sh
        ;;
    10)"""

if target_case in content and "13)" not in content:
    content = content.replace(target_case, new_case)

with open("master_hub.sh", "w") as f:
    f.write(content)

print("[+] Master hub fully updated with Options 13, 14, and 15.")
