with open("master_hub.sh", "r") as f:
    content = f.read()

# Expand range prompt display
content = content.replace("[1-10]", "[1-11]")
content = content.replace("-le 10", "-le 11")

# Add option 11 into the menu text before Option 10
target_menu = " 10. Exit Hub"
new_menu = " 11. Run Women Reach & Aesthetic Optimization (python3 women_reach_optimizer.py)\n 10. Exit Hub"
if target_menu in content and "11." not in content:
    content = content.replace(target_menu, new_menu)

# Add case 11 cleanly before case 10
target_case = "10)"
new_case = "11)\n        python3 women_reach_optimizer.py\n        ;;\n    10)"
if target_case in content and "11)" not in content:
    content = content.replace(target_case, new_case)

with open("master_hub.sh", "w") as f:
    f.write(content)

print("[+] master_hub.sh cleanly repaired and patched.")
