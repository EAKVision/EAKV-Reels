# 1. Update Master Execution Suite
with open("master_execution_suite.py", "r") as f:
    suite_content = f.read()

new_suites = [
    '("live_web_dashboard.py", "Live Web Telemetry Dashboard"),',
    '("advanced_niche_radar.py", "Advanced Competitor & Niche Intelligence Radar"),',
    '("video_splicing_pipeline.py", "Automated Video-Splicing Pipeline"),'
]

for ns in new_suites:
    if ns.split(',')[0] not in suite_content:
        target = '("telegram_command_bot.py", "Remote Command Bot Interface"),'
        suite_content = suite_content.replace(target, target + '\n        ' + ns)

with open("master_execution_suite.py", "w") as f:
    f.write(suite_content)

# 2. Update Master Hub
with open("master_hub.sh", "r") as f:
    hub_content = f.read()

hub_content = hub_content.replace("[1-27]", "[1-30]")
hub_content = hub_content.replace("-le 27", "-le 30")

menu_target = " 27. 🤖 Remote Command Bot Interface (python3 telegram_command_bot.py)"
new_menu_items = """ 27. 🤖 Remote Command Bot Interface (python3 telegram_command_bot.py)
 28. 📊 Live Web Telemetry Dashboard (python3 live_web_dashboard.py)
 29. 📡 Advanced Competitor & Niche Intelligence Radar (python3 advanced_niche_radar.py)
 30. 🎬 Automated Video-Splicing Pipeline (python3 video_splicing_pipeline.py)"""

if menu_target in hub_content and "28." not in hub_content:
    hub_content = hub_content.replace(menu_target, new_menu_items)

case_target = """27)
        python3 telegram_command_bot.py
        ;;"""
new_cases = """27)
        python3 telegram_command_bot.py
        ;;
    28)
        python3 live_web_dashboard.py
        ;;
    29)
        python3 advanced_niche_radar.py
        ;;
    30)
        python3 video_splicing_pipeline.py
        ;;"""

if case_target in hub_content and "28)" not in hub_content:
    hub_content = hub_content.replace(case_target, new_cases)

with open("master_hub.sh", "w") as f:
    f.write(hub_content)

print("[+] Master Hub and Master Execution Suite successfully expanded to 30 Protocols.")
