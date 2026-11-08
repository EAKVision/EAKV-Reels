with open("master_hub.sh", "r") as f:
    content = f.read()

# Expand range display to [1-22]
content = content.replace("[1-21]", "[1-22]")
content = content.replace("-le 21", "-le 22")

# Add Option 22 before Option 10 (Exit Hub)
target_menu = " 10. Exit Hub"
new_menu = """ 22. ⚡ MASTER KEY: Run All 21 Protocols Simultaneously (python3 master_execution_suite.py)
 10. Exit Hub"""

if target_menu in content and "22." not in content:
    content = content.replace(target_menu, new_menu)

# Update case 9 or add case 22 before option 10
target_case = "10)"
new_case = """22)
        python3 master_execution_suite.py
        ;;
    10)"""

if target_case in content and "22)" not in content:
    content = content.replace(target_case, new_case)

with open("master_hub.sh", "w") as f:
    f.write(content)

print("[+] Master hub updated with Option 22 (Master Execution Suite).")
