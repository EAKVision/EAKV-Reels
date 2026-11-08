with open("master_hub.sh", "r") as f:
    lines = f.readlines()

new_lines = []
menu_added = False
case_added = False

for line in lines:
    # Update range display
    if "[1-10]" in line:
        line = line.replace("[1-10]", "[1-11]")
    if "-le 10" in line:
        line = line.replace("-le 10", "-le 11")
        
    # Insert menu item before Exit Hub
    if "10. Exit Hub" in line and not menu_added:
        new_lines.append(" 11. Run Women Reach & Aesthetic Optimization (python3 women_reach_optimizer.py)\n")
        menu_added = True
        
    # Insert case logic before option 10
    if "10)" in line and not case_added:
        new_lines.append("    11)\n")
        new_lines.append("        python3 women_reach_optimizer.py\n")
        new_lines.append("        ;;\n")
        case_added = True
        
    new_lines.append(line)

with open("master_hub.sh", "w") as f:
    f.writelines(new_lines)

print("[+] Clean master hub patch applied successfully.")
