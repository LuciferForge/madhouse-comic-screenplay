#!/usr/bin/env python3
"""
MAD HOUSE Animated Short Video Generator
Renders 1080x1920 vertical promo shorts using Pillow frame generation + FFmpeg video encoding
for TikTok, Instagram Reels, and YouTube Shorts!
"""

import os
import sys
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = Path("/Users/apple/Documents/products/madhouse-comic-screenplay/rendered_shorts")
FRAMES_DIR = OUTPUT_DIR / "temp_frames"
OUTPUT_MP4 = OUTPUT_DIR / "madhouse_short_01.mp4"

FRAMES_DIR.mkdir(parents=True, exist_ok=True)

WIDTH, HEIGHT = 1080, 1920
FPS = 24
DURATION_SEC = 12
TOTAL_FRAMES = FPS * DURATION_SEC

def create_frame(frame_num: int) -> Image.Image:
    t = frame_num / FPS
    img = Image.new("RGB", (WIDTH, HEIGHT), color=(7, 9, 14)) # Dark background #07090E
    draw = ImageDraw.Draw(img)

    # Decorative Neon Header Box
    draw.rectangle([50, 100, WIDTH - 50, 240], outline=(0, 255, 102), width=4)
    
    # Try system font, fallback to default
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 75)
        text_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
        sub_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
    except Exception:
        title_font = text_font = sub_font = ImageFont.load_default()

    # Title
    draw.text((WIDTH // 2, 170), "MAD HOUSE", fill=(0, 255, 102), font=title_font, anchor="mm")

    # Time-Based Scenes
    if t < 3.0:
        draw.text((WIDTH // 2, 800), "RULE #1 OF RENTING:", fill=(255, 255, 255), font=text_font, anchor="mm")
        draw.text((WIDTH // 2, 900), "Never let your roommate invent at 8 AM!", fill=(255, 42, 109), font=sub_font, anchor="mm")
    elif t < 6.0:
        draw.text((WIDTH // 2, 800), "MAX'S NEW INVENTION:", fill=(0, 229, 255), font=text_font, anchor="mm")
        draw.text((WIDTH // 2, 900), "The Quantum Butter Spreader levitated...", fill=(255, 255, 255), font=sub_font, anchor="mm")
    elif t < 9.0:
        draw.text((WIDTH // 2, 800), "THEN IT EXPLODED!", fill=(255, 51, 102), font=text_font, anchor="mm")
        draw.text((WIDTH // 2, 900), "Sourdough shot through the wall at Mach 2!", fill=(255, 255, 255), font=sub_font, anchor="mm")
    else:
        draw.text((WIDTH // 2, 800), "READ ISSUE #1 NOW!", fill=(0, 255, 102), font=text_font, anchor="mm")
        draw.text((WIDTH // 2, 900), "Published on KDP & Gumroad — Link in Bio", fill=(255, 255, 255), font=sub_font, anchor="mm")

    # Footer Card
    draw.rectangle([100, HEIGHT - 250, WIDTH - 100, HEIGHT - 150], fill=(22, 28, 44), outline=(0, 255, 102), width=2)
    draw.text((WIDTH // 2, HEIGHT - 200), "🎬 COMEDY ANIMATED SERIES & COMIC", fill=(255, 255, 255), font=sub_font, anchor="mm")

    return img

def render_vertical_short():
    print("=================================================================")
    print(" 🎬 RENDERING MAD HOUSE ANIMATED PROMO SHORT #1 (PIL + FFmpeg)")
    print("=================================================================")
    
    print(f"• Generating {TOTAL_FRAMES} 1080x1920 frames at {FPS} FPS...")
    for i in range(TOTAL_FRAMES):
        img = create_frame(i)
        img.save(FRAMES_DIR / f"frame_{i:04d}.png")

    print(f"• Compiling frames into MP4 video using FFmpeg...")
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", str(FRAMES_DIR / "frame_%04d.png"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        str(OUTPUT_MP4)
    ]
    subprocess.run(cmd, check=True)

    # Cleanup temp frames
    for f in FRAMES_DIR.glob("*.png"):
        f.unlink()
    FRAMES_DIR.rmdir()

    print("=================================================================")
    print(f" 🏆 VIDEO RENDER COMPLETE: {OUTPUT_MP4} ({os.path.getsize(OUTPUT_MP4):,} bytes)")
    print("=================================================================")
    return str(OUTPUT_MP4)

if __name__ == "__main__":
    render_vertical_short()
