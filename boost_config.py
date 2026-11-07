import json

with open("active_target.json", "r") as f:
    config = json.load(f)

targets = config["targets"]
print(f"[CONFIG] Active organic boost matrix scaled to {len(targets)} targets.")
