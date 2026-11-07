#!/usr/bin/env python3
import os
import sys
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1920
FPS = 30
DURATION_SEC = 5
TOTAL_FRAMES = FPS * DURATION_SEC
OUTPUT_FILE = "eakv_reel_demo.mp4"

def get_font(size):
font_paths = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    "/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"
]
for path in font_paths:
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
return ImageFont.load_default()

def draw_frame(frame_idx):
img = Image.new("RGB", (WIDTH, HEIGHT), color="#0d1117")
draw = ImageDraw.Draw(img)

font_title = get_font(52)
font_body = get_font(36)
font_sub = get_font(28)

for y in range(0, HEIGHT, 80):
    draw.line([(0, y), (WIDTH, y)], fill="#161b22", width=1)

draw.text((80, 120), "EAKV SOVEREIGN ENGINE", fill="#58a6ff", font=font_title)
draw.text((80, 190), "POSIX C / UNIX ARCHITECTURE TRACE", fill="#8b949e", font=font_sub)
draw.line([(80, 240), (WIDTH - 80, 240)], fill="#30363d", width=3)

progress = frame_idx / TOTAL_FRAMES
pulse = int(128 + 127 * math.sin(progress * math.pi * 4))
pulse_hex = f"#{pulse:02x}b950"

current_addr = 0x55f83f2ba420 + (frame_idx * 0x1000)
current_bytes = 65536 * ((frame_idx % 5) + 1)

draw.text((80, 320), f"[FRAME] {frame_idx + 1:03d} / {TOTAL_FRAMES}", fill="#f0883e", font=font_body)
draw.text((80, 400), f"[TRACE] MALLOC_ALLOC | SIZE: {current_bytes} bytes", fill="#3fb950", font=font_body)
draw.text((80, 460), f"[ADDR]  0x{current_addr:12x}", fill="#bc8cff", font=font_body)
draw.text((80, 520), f"[SYNC]  POSIX THREAD_POOL [OK]", fill="#58a6ff", font=font_body)

bar_width = int((WIDTH - 160) * progress)
draw.rectangle([(80, 620), (80 + bar_width, 650)], fill="#3fb950")
draw.rectangle([(80, 620), (WIDTH - 80, 650)], outline="#30363d", width=2)

center_y = 1000
wave_points = []
for x in range(80, WIDTH - 80, 10):
    y = center_y + int(100 * math.sin((x / 50.0) + (frame_idx * 0.2)))
    wave_points.append((x, y))

if len(wave_points) > 1:
    draw.line(wave_points, fill="#58a6ff", width=4)

draw.rectangle([(80, 1200), (WIDTH - 80, 1600)], fill="#161b22", outline="#30363d", width=2)
draw.text((120, 1240), "KERNEL ENGINE STATUS", fill="#f0883e", font=font_body)
draw.text((120, 1320), "• Memory Footprint: 1.2 MB (Zero-Bloat)", fill="#e6edf3", font=font_sub)
draw.text((120, 1380), "• CPU Overhead: < 0.01%", fill="#e6edf3", font=font_sub)
draw.text((120, 1440), "• Execution Pipeline: Pure C + PIL Pipe", fill="#e6edf3", font=font_sub)
draw.text((120, 1500), f"• Telemetry State: ONLINE", fill=pulse_hex, font=font_sub)

draw.text((80, 1750), "ENGINEERED BY EAKVISION", fill="#8b949e", font=font_sub)

return img

def run_pipeline():
print(f"[EAKV-REELS] Starting render pipeline ({WIDTH}x{HEIGHT} @ {FPS}fps)...")

ffmpeg_cmd = [
    "ffmpeg", "-y",
    "-f", "rawvideo", "-vcodec", "rawvideo",
    "-s", f"{WIDTH}x{HEIGHT}", "-pix_fmt", "rgb24",
    "-r", str(FPS), "-i", "-",
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    "-preset", "fast", "-crf", "18",
    OUTPUT_FILE
]

try:
    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
except FileNotFoundError:
    print("[ERROR] FFmpeg is missing.")
    sys.exit(1)

for i in range(TOTAL_FRAMES):
    frame = draw_frame(i)
    proc.stdin.write(frame.tobytes())
    if (i + 1) % 30 == 0 or i == TOTAL_FRAMES - 1:
        print(f"[EAKV-REELS] Rendered {i + 1}/{TOTAL_FRAMES} frames...")

proc.stdin.close()
proc.wait()

if proc.returncode == 0:
    print(f"[SUCCESS] Video rendered cleanly to: {OUTPUT_FILE}")
else:
    _, stderr = proc.communicate()
    print(f"[FAIL] FFmpeg error:\n{stderr.decode()}")

if __name__ == "__main__":
run_pipeline()
