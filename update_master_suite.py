with open("master_execution_suite.py", "r") as f:
    content = f.read()

# Check if aggressive script is already in the suite
if "aggressive_demographic_shift.py" not in content:
    target_str = '("global_women_reach_optimizer.py", "US & Global Women Reach Optimizer"),'
    replacement = target_str + '\n        ("aggressive_demographic_shift.py", "Aggressive 50%+ Female Demographic Shift Engine"),'
    content = content.replace(target_str, replacement)
    
    with open("master_execution_suite.py", "w") as f:
        f.write(content)
    print("[+] Master execution suite updated to include Option 23.")
else:
    print("[+] Aggressive demographic shift already integrated into master execution suite.")
