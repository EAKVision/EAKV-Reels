import json

POSTS = [
    {
        "file": "malloc_viral_1m.mp4",
        "title": "Why 99% of Developers Can't Write Malloc in C",
        "hook": "Most engineers rely on high-level memory management without understanding how sbrk() and memory metadata headers actually work at the kernel layer.",
        "cta": "Comment 'CODE' to get the full zero-warning C codebase sent directly to your DMs."
    },
    {
        "file": "shell_viral_1m.mp4",
        "title": "Building a Unix Shell from Scratch in Pure C",
        "hook": "Ever wondered how your terminal creates processes? Here is the exact POSIX fork() and execvp() implementation.",
        "cta": "Comment 'CODE' for GitHub repository access."
    },
    {
        "file": "io_bench_viral_1m.mp4",
        "title": "Raw POSIX write() vs High-Level I/O Benchmarking",
        "hook": "We benchmarked raw kernel system calls against standard library buffer wrappers over 100MB of stream output.",
        "cta": "Comment 'CODE' to review the benchmark source file."
    }
]

HASHTAGS = "#systemsengineering #cprogramming #baremetal #linuxkernel #faang #softwareengineering #coding #computerarchitecture #tech"

def build_manifest():
    print("=== AKV Elite System: Multi-Platform Manifest Builder ===")
    manifest = []
    for post in POSTS:
        full_caption = (
            f"{post['title']}\n\n"
            f"{post['hook']}\n\n"
            f"{post['cta']}\n\n"
            f"Follow @amrkhedrrr for bare-metal engineering & high-performance routines.\n\n"
            f"{HASHTAGS}"
        )
        manifest.append({
            "video_file": post["file"],
            "caption": full_caption
        })
    
    with open("publishing_manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
        
    print("[✓] Created publishing_manifest.json with pre-formatted captions & US tags.")

if __name__ == "__main__":
    build_manifest()
