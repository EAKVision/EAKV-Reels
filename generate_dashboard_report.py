#!/usr/bin/env python3
"""
generate_dashboard_report.py - Visualizes performance telemetry and demographic growth curves.
"""

import os
import csv

def generate_report():
    print("[*] Compiling executive telemetry analytics report...")
    
    csv_file = "reel_performance.csv"
    if not os.path.exists(csv_file):
        print("[-] No performance data found yet. Run telemetry analytics first.")
        return
        
    print("\n==================================================")
    print("      EAKV SOVEREIGN TELEMETRY DASHBOARD REPORT     ")
    print("==================================================")
    
    with open(csv_file, mode="r") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header:
            print(f" | ".join(header))
            print("-" * 50)
        for row in reader:
            print(f" | ".join(row))
            
    print("==================================================")
    print("[+] Report generated successfully from local data stream.\n")

if __name__ == "__main__":
    generate_report()
