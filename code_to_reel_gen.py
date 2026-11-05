import os
import subprocess
import re

def extract_snippet(c_file, max_lines=12):
    if not os.path.exists(c_file):
        return "/* File not found */"
    with open(c_file, 'r') as f:
        lines = f.readlines()
    
    # Grab the core implementation function, skipping initial headers if too long
    snippet = "".join(lines[:max_lines])
    # Clean up quotes for ffmpeg drawtext safety
    clean_snippet = re.sub(r'["\']', '', snippet)
    return clean_snippet.strip()

def generate_code_reel(c_file, output_mp4="code_reel_output.mp4"):
    print(f"[*] Parsing {c_file} for elite US tech audience...")
    snippet = extract_snippet(c_file)
    
    hook = f"BUILDING {c_file.upper()} FROM SCRATCH IN C"
    
    # FFmpeg 9:16 vertical conversion with green-screen code terminal styling
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=black:s=1080x1920:r=30:d=10",
        "-vf", (
            f"drawtext=text='{hook}':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=200:"
            f"box=1:boxcolor=black@0.9:boxborderw=20,"
            f"drawtext=text='{snippet}':fontcolor=0x00FF66:fontsize=28:x=80:y=400:"
            f"box=1:boxcolor=black@0.95:boxborderw=30"
        ),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", output_mp4
    ]
    
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"[✓] Successfully generated viral code reel: {output_mp4}")
    except Exception as e:
        print(f"[!] Reel generation failed: {e}")

if __name__ == "__main__":
    generate_code_reel("my_malloc.c", "malloc_reel.mp4")
