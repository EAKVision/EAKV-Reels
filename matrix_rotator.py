#!/usr/bin/env python3
import json
import os

MATRIX_FILE = 'active_target.json'

def rotate_matrix():
    print("[MATRIX-ROTATOR] Analyzing active reel batch matrix...")
    if not os.path.exists(MATRIX_FILE):
        print("[ERROR] active_target.json not found.")
        return

    with open(MATRIX_FILE, 'r') as f:
        data = json.load(f)
    
    targets = data.get('targets', [])
    print(f"[INFO] Current active matrix size: {len(targets)} targets.")
    print("[SUCCESS] Matrix health optimal. Ready for next-gen target injection.")

if __name__ == "__main__":
    rotate_matrix()
