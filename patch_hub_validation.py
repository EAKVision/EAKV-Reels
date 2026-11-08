with open("master_hub.sh", "r") as f:
    code = f.read()

# Replace any strict 1-10 numerical comparison or regex check with 1-11
code = code.replace("-le 10", "-le 11")
code = code.replace("[1-10]", "[1-11]")

# Ensure case 11 is handled if it uses a case statement
if "11)" not in code:
    code = code.replace("10)", "10)\n        ;;\n    11)\n        python3 women_reach_optimizer.py\n        ;;")

with open("master_hub.sh", "w") as f:
    f.write(code)

print("[+] Master hub validation patched successfully.")
