#!/usr/bin/env python3
"""
variant_generator.py - Generates A/B content variants for multi-platform algorithmic testing.
"""

import json
import os

def generate_variants():
    print("[*] Initializing A/B variant generation pipeline...")
    
    variants = [
        {"variant_id": "A", "hook_style": "Direct Statement", "aesthetic": "Warm Dark Mode", "target": "Instagram Reels"},
        {"variant_id": "B", "hook_style": "Open-Ended Question", "aesthetic": "High-Contrast Terminal", "target": "TikTok"},
        {"variant_id": "C", "hook_style": "Silent Execution / Code-First", "aesthetic": "Minimalist Slate", "target": "YouTube Shorts"}
    ]
    
    os.makedirs("content_variants", exist_ok=True)
    for v in variants:
        filename = f"content_variants/variant_{v['variant_id']}.json"
        with open(filename, "w") as f:
            json.dump(v, f, indent=2)
        print(f"[+] Generated variant spec: {filename}")
        
    print("[+] Successfully generated all A/B testing variants.")

if __name__ == "__main__":
    generate_variants()
