import os
import subprocess
import re

MODULES = [
    ("my_malloc.c", "malloc_reel.mp4", "WHY 99% CANNOT WRITE MALLOC IN C"),
    ("micro_shell.c", "shell_reel.mp4", "BUILDING A UNIX SHELL FROM SCRATCH IN C"),
    ("io_bench.c", "io_bench_reel.mp4", "RAW POSIX SYS-CALLS VS HIGH-LEVEL I/O"),
    ("vm.c", "vm_reel.mp4", "WRITING A STACK BYTECODE VM IN C"),
    ("tcp_analyzer.c", "tcp_reel.mp4", "RAW SOCKET PACKET SNIFFING AT KERNEL LEVEL")
]

def extract_snippet(c_file, max_lines=12):
    if not os.path.exists(c_file):
        return "/* File not found */"
    with open(c_file, 'r') as f:
        lines = f.readlines()
    snippet = "".join(lines[:max_lines])
    clean_snippet = re.sub(r'["\']', '', snippet)
    return clean_snippet.strip()

def generate_all_reels():
    print("=== AKV Elite System: Batch Reel Generator Active ===")
    for c_file, output_mp4, hook in MODULES:
        print(f"[*] Processing reel: {output_mp4} ({c_file})...")
        snippet = extract_snippet(c_file)
        
        ffmpeg_cmd = [
            "ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=black:s=1080x1920:r=30:d=10",
            "-vf", (
                f"drawtext=text='{hook}':fontcolor=white:fontsize=44:x=(w-text_w)/2:y=200:"
                f"box=1:boxcolor=black@0.9:boxborderw=20,"
                f"drawtext=text='{snippet}':fontcolor=0x00FF66:fontsize=26:x=70:y=380:"
                f"box=1:boxcolor=black@0.95:boxborderw=25"
            ),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", output_mp4
        ]
        
        try:
            subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[✓] Generated: {output_mp4}")
        except Exception as e:
            print(f"[!] Failed to generate {output_mp4}: {e}")

if __name__ == "__main__":
    generate_all_reels()
