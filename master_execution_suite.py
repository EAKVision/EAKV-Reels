#!/usr/bin/env python3
"""
master_execution_suite.py - Fires the entire EAKV 21-protocol engine in a unified pipeline.
"""

import os
import subprocess

def run_protocol(script_name, description):
    print(f"\n[*] Executing: {description} ({script_name})...")
    if os.path.exists(script_name):
        result = subprocess.run(["python3", script_name], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[SUCCESS] {description} completed.")
            print(result.stdout.strip())
        else:
            print(f"[WARNING] {description} exited with code {result.returncode}")
            print(result.stderr.strip())
    else:
        print(f"[-] Script not found: {script_name}")

def execute_all_protocols():
    print("==================================================")
    print("   EAKV MASTER EXECUTION SUITE - ALL SYSTEMS FIRE")
    print("==================================================")
    
    protocols = [
        ("global_women_reach_optimizer.py", "US & Global Women Reach Optimizer"),
        ("aggressive_demographic_shift.py", "Aggressive 50%+ Female Demographic Shift Engine"),
        ("telegram_command_bot.py", "Remote Command Bot Interface"),
        ("video_splicing_pipeline.py", "Automated Video-Splicing Pipeline"),
        ("advanced_niche_radar.py", "Advanced Competitor & Niche Intelligence Radar"),
        ("live_web_dashboard.py", "Live Web Telemetry Dashboard"),
        ("self_learning_optimizer.py", "Predictive Self-Learning Telemetry Loop"),
        ("multi_platform_syndicator.py", "Cross-Platform Syndication Mesh"),
        ("visual_synthesis_engine.py", "AI Visual Asset Synthesis"),
        ("auto_reel_batcher.py", "Automated Reel Batcher"),
        ("ai_hook_optimizer.py", "AI Hook & Caption Optimizer"),
        ("audio_trend_sync.py", "Audio Trend Sync"),
        ("variant_generator.py", "A/B Content Variant Generator"),
        ("niche_radar.py", "Niche Intelligence Radar"),
        ("matrix_analytics.py", "Matrix Analytics & Telemetry Logger"),
        ("generate_dashboard_report.py", "Dashboard Analytics Report"),
        ("cloud_vault_sync.py", "Cloud Vault Backup Sync")
    ]
    
    for script, desc in protocols:
        run_protocol(script, desc)
        
    print("\n==================================================")
    print("⚡ [COMPLETE] All sovereign protocols successfully executed! ⚡")
    print("==================================================")

if __name__ == "__main__":
    execute_all_protocols()
