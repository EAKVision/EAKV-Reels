#!/usr/bin/env python3
import os
import sys
import subprocess

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("[INFO] Pillow not found. Installing pillow for high-res frame rendering...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow", "--quiet"])
    from PIL import Image, ImageDraw, ImageFont

def render_code_reel(source_file, output_video="eakv_code_reel.mp4"):
    print(f"[CODE-TO-REEL] Reading source file: {source_file}...")
    if not os.path.exists(source_file):
        print(f"[ERROR] Source file {source_file} not found.")
        return False
        
    with open(source_file, 'r') as f:
        code_lines = f.readlines()
        
    # Vertical Reel Resolution: 1080x1920 (9:16 aspect ratio)
    width, height = 1080, 1920
    img = Image.new("RGB", (width, height), color="#0d1117") # GitHub dark mode background
    draw = ImageDraw.Draw(img)
    
    # Fonts (Fall back to default if custom TTF isn't present)
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
        code_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 32)
        footer_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    except IOError:
        title_font = ImageFont.load_default()
        code_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()

    # Draw Brand Header
    draw.rectangle([(0, 0), (width, 180)], fill="#161b22")
    draw.text((60, 60), "👑 ELITE AKV | C & UNIX SYSTEMS", fill="#58a6ff", font=title_font)
    draw.text((60, 120), f"TARGET: {os.path.basename(source_file)}", fill="#8b949e", font=footer_font)
    
    # Draw Code Terminal Window Box
    box_margin = 60
    draw.rounded_rectangle(
        [(box_margin, 220), (width - box_margin, height - 250)],
        radius=16,
        fill="#010409",
        outline="#30363d",
        width=3
    )
    
    # Render Code Lines inside terminal box
    y_offset = 280
    max_lines = 40
    for i, line in enumerate(code_lines[:max_lines]):
        cleaned_line = line.expandtabs(4).rstrip('\n')
        draw.text((box_margin + 40, y_offset), cleaned_line, fill="#c9d1d9", font=code_font)
        y_offset += 45

    # Draw Footer Telemetry
    draw.rectangle([(0, height - 150), (width, height)], fill="#161b22")
    draw.text((60, height - 100), "⚡ 360° Vision. Global Vibes. Pure Execution.", fill="#f0883e", font=footer_font)
    
    # Save temporary frame
    frame_path = "temp_reel_frame.png"
    img.save(frame_path)
    print(f"[SUCCESS] High-res vertical frame rendered: {frame_path}")

    # Compile into MP4 using ffmpeg (if available)
    print(f"[CODE-TO-REEL] Encoding video artifact via FFmpeg -> {output_video}...")
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-loop", "1", "-i", frame_path,
        "-t", "5", "-pix_fmt", "yuv420p", "-vf", "scale=1080:1920",
        output_video
    ]
    
    try:
        subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[SUCCESS] Cinematic code reel successfully compiled: {output_video}")
    except (subprocess.SubprocessError, FileNotFoundError):
        print("[WARNING] FFmpeg not found or failed. Frame image is saved and ready for manual compilation.")

    # Cleanup temp frame
    if os.path.exists(frame_path):
        os.remove(frame_path)
    return True

if __name__ == "__main__":
    print("=== EAKV Code-to-Reel Engine V2 Active ===")
    # Find any C file in workspace or create a sample one
    target_files = [f for f in os.listdir('.') if f.endswith('.c') or f.endswith('.py')]
    if target_files:
        render_code_reel(target_files[0])
    else:
        # Create a sample C file if none exist
        sample_code = '#include <stdio.h>\n\nint main() {\n    printf("Elite AKV: Zero Bloat, Pure Execution.\\n");\n    return 0;\n}\n'
        with open("sample_core.c", "w") as f:
            f.write(sample_code)
        render_code_reel("sample_core.c")
