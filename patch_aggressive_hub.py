with open("master_hub.sh", "r") as f:
    content = f.read()

# Expand range display to [1-23]
content = content.replace("[1-22]", "[1-23]")
content = content.replace("-le 22", "-le 23")

# Add Option 23 before Option 10 (Exit Hub)
target_menu = " 10. Exit Hub"
new_menu = """ 23. 🎯 AGGRESSIVE 50%+ Female Demographic Shift Engine (python3 aggressive_demographic_shift.py)
 10. Exit Hub"""

if target_menu in content and "23." not in content:
    content = content.replace(target_menu, new_menu)

# Update case statements before option 10
target_case = "10)"
new_case = """23)
        python3 aggressive_demographic_shift.py
        ;;
    10)"""

if target_case in content and "23)" not in content:
    content = content.replace(target_case, new_case)

with open("master_hub.sh", "w") as f:
    f.write(content)

print("[+] Master hub updated with Option 23 (Aggressive Demographic Shift Engine).")
