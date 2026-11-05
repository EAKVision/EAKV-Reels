import subprocess

def process_reel(input_video, output_video, hook_text, code_overlay_text):
    print(f"[*] Processing viral reel for US market: {output_video}")
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-i", input_video,
        "-vf", (
            f"crop=w='min(iw,ih*9/16)':h='min(ih,iw*16/9)',scale=1080:1920,"
            f"drawtext=text='{hook_text}':fontcolor=white:fontsize=52:x=(w-text_w)/2:y=280:"
            f"box=1:boxcolor=black@0.85:boxborderw=25,"
            f"drawtext=text='{code_overlay_text}':fontcolor=green:fontsize=36:x=(w-text_w)/2:y=1300:"
            f"box=1:boxcolor=black@0.9:boxborderw=20"
        ),
        "-c:v", "libx264", "-crf", "20", "-c:a", "aac", output_video
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"[✓] Successfully generated 1080x1920 Reel: {output_video}")
    except Exception as e:
        print(f"[!] FFmpeg processing failed: {e}")

if __name__ == "__main__":
    process_reel(
        input_video="EAKV_Reel.mp4",
        output_video="final_us_reel.mp4",
        hook_text="WHY 99% CANNOT WRITE MALLOC IN C",
        code_overlay_text="void* my_malloc(size_t size) { ... }"
    )
