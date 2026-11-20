#!/usr/bin/env python3
import csv
import os
from collections import Counter, defaultdict

CLICKS_FILE = os.path.expanduser("~/reel_clicks.csv")
EXP_FILE = os.path.expanduser("~/reel_experiments.csv")


def load_rows(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", newline="") as f:
        return list(csv.DictReader(f))


def main():
    clicks = load_rows(CLICKS_FILE)
    exps = load_rows(EXP_FILE)

    print("\n=== ELITE AKV FUNNEL & EXPERIMENT REPORT ===\n")

    if not clicks:
        print(f"No click logs found at {CLICKS_FILE}")
    else:
        by_channel = Counter(r.get("ch", "unknown") for r in clicks)
        by_camp = Counter(r.get("camp", "unknown") for r in clicks)
        print(f"Total Tracked Clicks: {len(clicks)}")
        print("\nBy Channel:")
        for ch, cnt in by_channel.most_common():
            pct = (cnt / len(clicks)) * 100
            print(f"  - {ch:<10}: {cnt} ({pct:.1f}%)")
        print("\nBy Campaign:")
        for camp, cnt in by_camp.most_common():
            print(f"  - {camp:<18}: {cnt}")

    if not exps:
        print(f"\nNo experiment logs found at {EXP_FILE}")
    else:
        grouped = defaultdict(list)
        for r in exps:
            grouped[r.get("reel", "unknown")].append(r)
        print(f"\nLogged Reel Experiments: {len(exps)} across {len(grouped)} reel(s)")
        for reel, rows in grouped.items():
            latest = rows[-1]
            views = int(latest.get("views") or 0)
            shares = int(latest.get("shares") or 0)
            rate = (shares / views * 100) if views > 0 else 0.0
            print(
                f"  - {reel}: latest views={views}, shares={shares} "
                f"({rate:.2f}% share rate) | hook: {latest.get('hook', '')[:60]}"
            )


if __name__ == "__main__":
    main()
