with open("master_hub.sh", "r") as f:
    content = f.read()

# Expand range prompt display
content = content.replace("[1-11]", "[1-12]")
content = content.replace("-le 11", "-le 12")

# Add option 12 into the menu text before Option 10 (Exit Hub)
target_menu = " 10. Exit Hub"
new_menu = " 12. Run US & Worldwide Women Reach Optimizer (python3 global_women_reach_optimizer.py)\n 10. Exit Hub"
if target_menu in content and "12." not in content:
    content = content.replace(target_menu, new_menu)

# Add case 12 before option 10
target_case = "10)"
new_case = "12)\n        python3 global_women_reach_optimizer.py\n        ;;\n    10)"
if target_case in content and "12)" not in content:
    content = content.replace(target_case, new_case)

with open("master_hub.sh", "w") as f:
    f.write(content)

print("[+] Master hub updated with Option 12 (Global Women Reach Optimizer).")
