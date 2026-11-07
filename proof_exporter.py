#!/usr/bin/env python3
import subprocess
import json
import os

def export_proof():
    print("[PROOF-EXPORTER] Gathering git metrics and build velocity...")
    try:
        git_log = subprocess.check_output(
            ["git", "log", "-n", "5", "--pretty=format:%h - %an, %ar : %s"],
            universal_newlines=True
        )
    except Exception:
        git_log = "No git history found or not a git repository."

    target_count = 0
    if os.path.exists('active_target.json'):
        with open('active_target.json', 'r') as f:
            data = json.load(f)
            target_count = len(data.get('targets', []))

    report = f"""# EAKV Proof-of-Work & Activity Report
Generated automatically for interview reference & self-audit.

## Active System Metrics
- **Active Reel Batch Matrix:** {target_count} targets loaded
- **Environment:** WSL / Linux Low-Level Systems Dev

## Recent Code & Git Velocity
{git_log}
"""
    with open("PROOF_OF_WORK.md", "w") as f:
        f.write(report)
    print("[SUCCESS] Proof-of-work report generated: PROOF_OF_WORK.md")

if __name__ == "__main__":
    export_proof()
