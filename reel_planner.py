#!/usr/bin/env python3
import argparse
import csv
import datetime
import os
import random

PLAN_FILE = os.path.expanduser("~/reel_experiments.csv")

HOOKS = [
    "Most engineers miss this subtle bug until production breaks:",
    "Here is the exact reason this failed under real load:",
    "Stop doing this in your pipeline—do this instead:",
    "60 seconds on how this actually works under the hood:",
    "One small change that made a massive difference:",
]

CTAS = [
    "Save this for later and tell me what you'd test next.",
    "Drop a comment if you've hit this exact issue.",
    "Share this with someone building systems right now.",
]


def init_plan():
    if not os.path.exists(PLAN_FILE):
        with open(PLAN_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "date_utc",
                "reel_id",
                "topic",
                "hook",
                "cta",
                "views",
                "shares",
                "notes",
            ])


def cmd_pitch(reel_id: str, topic: str):
    hook = random.choice(HOOKS)
    cta = random.choice(CTAS)
    print("\n=== Reel Hook & Caption Draft ===")
    print(f"Reel ID : {reel_id}")
    print(f"Topic   : {topic}")
    print(f"\nFirst 3s Hook:\n  {hook}")
    print(f"\nCaption Draft:\n  {hook} {topic}\n\n  {cta}\n")


def cmd_log(reel_id: str, topic: str, hook: str, views: int, shares: int, notes: str):
    init_plan()
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    with open(PLAN_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([today, reel_id, topic, hook, "", views, shares, notes])
    print(f"Logged experiment for {reel_id} -> {PLAN_FILE}")


def cmd_report():
    if not os.path.exists(PLAN_FILE):
        print("No Reel experiments logged yet.")
        return
    with open(PLAN_FILE, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print(f"\n=== Logged Reel Experiments ({len(rows)}) ===")
    for r in rows[-10:]:
        print(f"  {r['date_utc']} | {r['reel_id']} | views={r['views']} | shares={r['shares']} | {r['topic']}")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reel Hook & Experiment CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_pitch = sub.add_parser("pitch", help="Generate a hook and caption draft")
    p_pitch.add_argument("--reel", default="Df2_mtKK8tj")
    p_pitch.add_argument("--topic", required=True)

    p_log = sub.add_parser("log", help="Log Reel results after posting")
    p_log.add_argument("--reel", required=True)
    p_log.add_argument("--topic", required=True)
    p_log.add_argument("--hook", default="")
    p_log.add_argument("--views", type=int, default=0)
    p_log.add_argument("--shares", type=int, default=0)
    p_log.add_argument("--notes", default="")

    sub.add_parser("report", help="Show recent logged Reel experiments")

    args = parser.parse_args()
    if args.cmd == "pitch":
        cmd_pitch(args.reel, args.topic)
    elif args.cmd == "log":
        cmd_log(args.reel, args.topic, args.hook, args.views, args.shares, args.notes)
    elif args.cmd == "report":
        cmd_report()
