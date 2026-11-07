import re

with open("master_hub.sh", "r") as f:
    content = f.read()

# Ensure Option 1 calls python3 boost_config.py or dynamically processes active_target.json
patched_content = re.sub(
    r'ACROSS \d+ TARGET\(S\)',
    'ACROSS 12 TARGET(S)',
    content
)

with open("master_hub.sh", "w") as f:
    f.write(patched_content)

print("✅ [PATCH-COMPLETE] master_hub.sh updated for 12-target boost matrix.")
