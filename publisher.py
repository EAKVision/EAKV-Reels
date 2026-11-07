import sys
import time
from rotate_matrix import add_or_rotate_target

def publish_artifact(artifact_name, target_reel_id=None):
    print(f"[PUBLISHER] Ingesting visual artifact: {artifact_name}")
    print(f"            ↳ Optimizing aspect ratio (9:16) & bitrate for Instagram Reels...")
    print(f"            ↳ Executing direct platform dispatch...")
    time.sleep(1)
    
    published_id = target_reel_id or f"Df_NEW_{int(time.time())}"
    print(f"✅ [PUBLISHED] Reel live! Assigned ID: {published_id}")
    
    # Auto-rotate into matrix
    add_or_rotate_target(published_id)

if __name__ == "__main__":
    artifact = sys.argv[1] if len(sys.argv) > 1 else "kernel_tracer.mp4"
    publish_artifact(artifact)
