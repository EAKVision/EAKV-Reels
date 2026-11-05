import json

CROSS_PLATFORM_DATA = [
    {
        "video": "malloc_viral_1m.mp4",
        "platforms": {
            "instagram_reels": {
                "title": "Why 99% of Developers Can't Write Malloc in C",
                "caption": "Most software engineers use malloc() daily without understanding dynamic memory metadata headers and sbrk() syscalls.\n\nComment 'CODE' to get repo link automatically.\n\nFollow @amrkhedrrr for systems engineering & elite physical routines.\n\n#cprogramming #systemssoftware #baremetal #faang #linuxkernel",
                "target_audience": "US / Global Tech Leaders & Systems Devs"
            },
            "youtube_shorts": {
                "title": "Writing Dynamic Memory Allocator (Malloc) in C #shorts #programming #coder",
                "description": "Learn low-level dynamic memory allocation in pure C using POSIX system call sbrk(). Full repo: https://github.com/EAKVision/EAKV-Reels",
                "tags": ["c programming", "malloc", "memory allocation", "systems programming", "linux"]
            },
            "tiktok": {
                "title": "Why 99% of devs can't write malloc from scratch in C 💻 #coding #tech #programmer #cprogramming #softwareengineer",
                "sound": "Trending Cyberpunk / Dark Synthwave (US Region)"
            }
        }
    },
    {
        "video": "shell_viral_1m.mp4",
        "platforms": {
            "instagram_reels": {
                "title": "How Linux Executes Commands Under The Hood",
                "caption": "Building a minimalist Unix shell in C using POSIX fork() and execvp().\n\nComment 'CODE' for direct access to source repo.\n\nFollow @amrkhedrrr for low-level systems & high-performance discipline.\n\n#linux #unix #cprogramming #softwareengineer #operating-systems",
                "target_audience": "US Backend Engineers & Kernel Enthusiasts"
            },
            "youtube_shorts": {
                "title": "Building a Unix Shell from Scratch in C #shorts #linux #coding",
                "description": "Step-by-step Unix shell process execution using fork() and execvp(). Full repo: https://github.com/EAKVision/EAKV-Reels",
                "tags": ["unix shell", "linux terminal", "c programming", "posix"]
            },
            "tiktok": {
                "title": "Building a custom Unix shell in C 🐧 #linux #terminal #programmer #softwareengineer #coding",
                "sound": "High-Energy Tech / Dark Electro (US Region)"
            }
        }
    }
]

def generate_manifest():
    with open("cross_platform_manifest.json", "w") as f:
        json.dump(CROSS_PLATFORM_DATA, f, indent=2)
    print("=== AKV Elite System: Multi-Platform Manifest Generated ===")
    print("[✓] Saved cross_platform_manifest.json for IG, YouTube Shorts, and TikTok distribution.")

if __name__ == "__main__":
    generate_manifest()
