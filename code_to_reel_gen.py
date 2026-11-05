import os
import subprocess
import re

VIRAL_MODULES = [
    {
        "file": "my_malloc.c",
        "output": "malloc_viral_1m.mp4",
        "hook": "WHY 99% OF DEVS CANNOT WRITE MALLOC",
        "subhook": "Bare-Metal Heap Allocator in Pure C",
        "snippet_lines": 14
    },
    {
        "file": "micro_shell.c",
        "output": "shell_viral_1m.mp4",
        "hook": "HOW LINUX EXECUTES COMMANDS UNDER THE HOOD",
        "subhook": "Building a Unix Shell from Scratch",
        "snippet_lines": 14
    },
    {
        "file": "io_bench.c",
        "output": "io_bench_viral_1m.mp4",
        "hook": "POSIX write() VS HIGH-LEVEL I/O",
        "subhook": "Raw Kernel Benchmarking Engine",
        "snippet_lines": 14
    },
    {
        "file": "vm.c",
        "output": "vm_viral_1m.mp4",
        "hook": "BUILDING A BYTECODE VM FROM SCRATCH",
        "subhook": "Stack-Based Virtual Machine Loop",
        "snippet_lines": 14
    },
    {
        "file": "tcp_analyzer.c",
        "output": "tcp_viral_1m.mp4",
        "hook": "RAW SOCKET PACKET CAPTURE IN C",
        "subhook": "Kernel-Level Network Sniffing",
        "snippet_lines": 14
    }
]

def format_snippet(c_file, max_lines):
    if not os.path.exists(c_file):
        return "/* File Missing */"
    with open(c_file, 'r') as f:
        lines = f.readlines()
    snippet = "".join(lines[:max_lines])
    clean_snippet = re.sub(r'["\']', '', snippet)
    clean_snippet = clean_snippet.replace(':', '\\:')
    return clean_snippet.strip()

def build_viral_reels():
    print("=== AKV Elite System: 1M+ Viral Reel Generator Active ===")
    for item in VIRAL_MODULES:
        c_file = item["file"]
        output_mp4 = item["output"]
        hook = item["hook"]
        subhook = item["subhook"]
        
        print(f"[*] Rendering High-Retention Reel: {output_mp4}...")
        snippet = format_snippet(c_file, item["snippet_lines"])
        
        # High-production FFmpeg filtergraph: Terminal card, neon borders, and dynamic text position
        ffmpeg_cmd = [
            "ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=0x0a0a0f:s=1080x1920:r=30:d=12",
            "-vf", (
                # Top Header Banner
                f"drawtext=text='AKV ELITE SYSTEMS':fontcolor=0x00FF66:fontsize=32:x=(w-text_w)/2:y=120,"
                # Viral Hook Line
                f"drawtext=text='{hook}':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=220:"
                f"box=1:boxcolor=0x11111a@0.9:boxborderw=20,"
                # Subhook Description
                f"drawtext=text='{subhook}':fontcolor=0x8888aa:fontsize=32:x=(w-text_w)/2:y=340,"
                # Code Terminal Container Overlay
                f"drawtext=text='{snippet}':fontcolor=0x00FF66:fontsize=26:x=80:y=460:"
                f"box=1:boxcolor=0x05050a@0.95:boxborderw=30,"
                # Bottom CTA Trigger
                f"drawtext=text='COMMENT CODE FOR DIRECT REPO ACCESS':fontcolor=yellow:fontsize=34:x=(w-text_w)/2:y=1650:"
                f"box=1:boxcolor=black@0.8:boxborderw=15"
            ),
            "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", output_mp4
        ]
        
        try:
            subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[✓] Render Complete: {output_mp4}")
        except Exception as e:
            print(f"[!] Render Failed for {output_mp4}: {e}")

if __name__ == "__main__":
    build_viral_reels()
