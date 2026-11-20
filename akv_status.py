#!/usr/bin/env python3
import csv
import os
import subprocess

REPO_DIR = os.path.expanduser("~/projects/EAKV-Reels")
SPRINT_LOG = os.path.expanduser("~/algo_sprint_log.csv")


def check_procs():
    out = subprocess.run(
        ["pgrep", "-af", "reel_boost.py|cloudflared"],
        capture_output=True,
        text=True,
    )
    lines = [ln for ln in out.stdout.strip().splitlines() if ln]
    print("[Processes]")
    if lines:
        for ln in lines:
            print(f"  OK  {ln}")
    else:
        print("  WARN No active reel_boost.py or cloudflared process detected")


def check_sprints():
    print("\n[Algorithm Reset Streak]")
    if not os.path.exists(SPRINT_LOG):
        print("  No sprint log found yet.")
        return
    with open(SPRINT_LOG, "r", newline="") as f:
        rows = list(csv.DictReader(f))
    total_actions = sum(int(r.get("actions_done") or 0) for r in rows)
    last_date = rows[-1]["date"] if rows else "N/A"
    print(f"  Sprints logged : {len(rows)} (last: {last_date})")
    print(f"  Total actions  : {total_actions}")


def check_git():
    print("\n[Git Repo: EAKV-Reels]")
    if not os.path.isdir(os.path.join(REPO_DIR, ".git")):
        print(f"  Missing git repo at {REPO_DIR}")
        return
    st = subprocess.run(
        ["git", "-C", REPO_DIR, "status", "--short"],
        capture_output=True,
        text=True,
    )
    dirty = [ln for ln in st.stdout.strip().splitlines() if ln]
    if dirty:
        print(f"  Uncommitted changes ({len(dirty)}):")
        for ln in dirty:
            print(f"    {ln}")
    else:
        print("  Clean working tree")


def main():
    print("\n=== ELITE AKV SYSTEM HEALTH ===")
    check_procs()
    check_sprints()
    check_git()


if __name__ == "__main__":
    main()
