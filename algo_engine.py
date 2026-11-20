#!/usr/bin/env python3
import argparse
import csv
import datetime
import os
import random

LOG_FILE = os.path.expanduser("~/algo_sprint_log.csv")

IG_NICHES = [
    "systems engineering",
    "C programming linux",
    "software engineer life",
    "dance choreography",
    "creative developer",
]

LI_NICHES = [
    "systems engineering",
    "AI agents production",
    "Linux kernel C",
    "software architecture",
    "developer productivity",
]

IG_COMMENT_ANGLES = [
    "Ask a specific technical or creative question about their setup/timing.",
    "Connect their point to rhythm, precision, or debugging in a 1-sentence insight.",
    "Highlight the exact moment in the clip that stood out and ask how they practiced/built it.",
]

LI_COMMENT_ANGLES = [
    "Add a concrete takeaway from building in C/Unix or shipping production systems.",
    "Agree or respectfully challenge one trade-off they mentioned, then ask a sharp follow-up.",
    "Summarize their core point in one crisp line and share how it applies to your workflow.",
]


def ensure_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "platform", "niche_focus", "actions_done", "notes"])


def generate_sprint():
    today = datetime.date.today().isoformat()
    ig_targets = random.sample(IG_NICHES, 3)
    li_targets = random.sample(LI_NICHES, 3)

    print(f"\n=== ELITE AKV ALGORITHM RESET SPRINT ({today}) ===\n")

    print("[1] INSTAGRAM FEED & SEARCH RESET (10 Mins)")
    print("  • Search & Watch to 100% (3 Reels each) in:")
    for t in ig_targets:
        print(f"      - #{t.replace(' ', '')} / '{t}'")
    print("  • Save 3 high-retention Reels & DM 1 to a peer (signals strong niche interest).")
    print("  • Leave 5 genuine comments (5+ words, zero generic emojis):")
    print(f"      Angle: {random.choice(IG_COMMENT_ANGLES)}")
    print("  • Mute/Not Interested on 5 off-topic feed posts to purge noise.\n")

    print("[2] LINKEDIN REACH & AUTHORITY BOOST (10 Mins)")
    print("  • Search & engage with top recent posts in:")
    for t in li_targets:
        print(f"      - '{t}'")
    print("  • Leave 5 high-signal comments (12+ words) on active threads:")
    print(f"      Angle: {random.choice(LI_COMMENT_ANGLES)}")
    print("  • Post rule: Put native video/text in the post body; place tracked URL in comments.\n")

    print("[3] LOG YOUR SPRINT WHEN DONE:")
    print(f'  python3 ~/algo_engine.py log --platform both --niche "{ig_targets[0]} / {li_targets[0]}" --actions 10 --notes "Completed daily reset"')


def log_sprint(args):
    ensure_log()
    today = datetime.date.today().isoformat()
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, args.platform, args.niche, args.actions, args.notes])
    print(f"Logged algorithm sprint for {today} -> {LOG_FILE}")


def show_stats():
    if not os.path.exists(LOG_FILE):
        print("No sprints logged yet. Run: python3 ~/algo_engine.py sprint")
        return
    with open(LOG_FILE, "r") as f:
        rows = list(csv.DictReader(f))
    total_actions = sum(int(r["actions_done"]) for r in rows)
    print(f"\n=== Algorithm Reset Streak & Stats ===")
    print(f"  Total Sprints Logged : {len(rows)}")
    print(f"  Total High-Signal Ops: {total_actions}")
    for r in rows[-5:]:
        print(f"  - {r['date']} | {r['platform']:<9} | {r['niche_focus']} ({r['actions_done']} actions)")


def main():
    parser = argparse.ArgumentParser(description="Instagram & LinkedIn Algorithm Reset Engine")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("sprint", help="Generate today's 20-minute algorithm reset sprint")

    p_log = sub.add_parser("log", help="Log a completed sprint")
    p_log.add_argument("--platform", default="both", help="ig, li, or both")
    p_log.add_argument("--niche", required=True, help="Niche keywords targeted")
    p_log.add_argument("--actions", type=int, default=10, help="Number of intentional actions completed")
    p_log.add_argument("--notes", default="", help="Observations on feed shift")

    sub.add_parser("stats", help="View sprint streak and logged actions")

    args = parser.parse_args()
    if args.cmd == "sprint":
        generate_sprint()
    elif args.cmd == "log":
        log_sprint(args)
    elif args.cmd == "stats":
        show_stats()


if __name__ == "__main__":
    main()
