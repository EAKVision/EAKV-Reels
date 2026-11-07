import json
import sys

def add_or_rotate_target(new_reel_id):
    with open("active_target.json", "r") as f:
        data = json.load(f)
    
    targets = data.get("targets", [])
    
    # Check for placeholder slot to replace
    replaced = False
    for i, t in enumerate(targets):
        if "REEL_TARGET_" in t:
            print(f"[ROTATOR] Replacing placeholder '{t}' at slot {i+1} with real Reel ID: '{new_reel_id}'")
            targets[i] = new_reel_id
            replaced = True
            break
            
    if not replaced:
        print(f"[ROTATOR] Appending new Reel ID: '{new_reel_id}' to active target matrix.")
        targets.append(new_reel_id)
        
    data["targets"] = targets
    data["latest_active"] = new_reel_id
    data["total_count"] = len(targets)
    
    with open("active_target.json", "w") as f:
        json.dump(data, f, indent=2)
        
    print(f"✅ [SUCCESS] Active target matrix updated ({len(targets)} total slots).")

if __name__ == "__main__":
    reel = sys.argv[1] if len(sys.argv) > 1 else "DfccmkhqTqf"
    add_or_rotate_target(reel)
