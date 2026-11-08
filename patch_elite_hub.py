with open("master_hub.sh", "r") as f:
    content = f.read()

# Expand range display
content = content.replace("[1-18]", "[1-21]")
content = content.replace("-le 18", "-le 21")

# Add options before Option 10 (Exit Hub)
target_menu = " 10. Exit Hub"
new_menu = """ 19. Run Audio Trend Sync (python3 audio_trend_sync.py)
 20. Generate A/B Content Variants (python3 variant_generator.py)
 21. Run Niche Intelligence Radar (python3 niche_radar.py)
 10. Exit Hub"""

if target_menu in content and "19." not in content:
    content = content.replace(target_menu, new_menu)

# Add case statements before option 10
target_case = "10)"
new_case = """19)
        python3 audio_trend_sync.py
        ;;
    20)
        python3 variant_generator.py
        ;;
    21)
        python3 niche_radar.py
        ;;
    10)"""

if target_case in content and "19)" not in content:
    content = content.replace(target_case, new_case)

with open("master_hub.sh", "w") as f:
    f.write(content)

print("[+] Master hub fully updated with Options 19, 20, and 21.")
