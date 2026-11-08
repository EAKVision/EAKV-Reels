import re

with open("master_hub.sh", "r") as f:
    content = f.read()

# Insert Option 11 right before Option 10 (Exit Hub)
target = " 10. Exit Hub"
replacement = " 11. Run Women Reach & Aesthetic Optimization (python3 women_reach_optimizer.py)\n 10. Exit Hub"

if target in content and "11." not in content:
    content = content.replace(target, replacement)
    with open("master_hub.sh", "w") as f:
        f.write(content)
    print("[+] Successfully added Option 11 to master_hub.sh")
else:
    print("[*] Option 11 already present or target not found.")
