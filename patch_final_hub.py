with open("master_hub.sh", "r") as f:
    content = f.read()

# Expand range display
content = content.replace("[1-15]", "[1-18]")
content = content.replace("-le 15", "-le 18")

# Add options before Option 10 (Exit Hub)
target_menu = " 10. Exit Hub"
new_menu = """ 16. Run AI Hook & Caption Optimizer (python3 ai_hook_optimizer.py)
 17. Generate Dashboard Analytics Report (python3 generate_dashboard_report.py)
 18. Execute Cloud Vault Backup Sync (python3 cloud_vault_sync.py)
 10. Exit Hub"""

if target_menu in content and "16." not in content:
    content = content.replace(target_menu, new_menu)

# Add case statements before option 10
target_case = "10)"
new_case = """16)
        python3 ai_hook_optimizer.py
        ;;
    17)
        python3 generate_dashboard_report.py
        ;;
    18)
        python3 cloud_vault_sync.py
        ;;
    10)"""

if target_case in content and "16)" not in content:
    content = content.replace(target_case, new_case)

with open("master_hub.sh", "w") as f:
    f.write(content)

print("[+] Master hub fully updated with Options 16, 17, and 18.")
