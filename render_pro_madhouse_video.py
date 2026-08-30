#!/usr/bin/env python3
"""
MAD HOUSE Pro Motion Graphics Video Generator
Renders a high-impact, pop-art comic book motion graphic video short (1080x1920)
featuring comic panels, speech bubbles, kinetic typography, and action effects (BOOM! POW!).
"""

import os
import math
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = Path("/Users/apple/Documents/products/madhouse-comic-screenplay/rendered_shorts")
FRAMES_DIR = OUTPUT_DIR / "pro_frames"
OUTPUT_MP4 = OUTPUT_DIR / "madhouse_pro_short.mp4"

FRAMES_DIR.mkdir(parents=True, exist_ok=True)

WIDTH, HEIGHT = 1080, 1920
FPS = 30
DURATION_SEC = 10
TOTAL_FRAMES = FPS * DURATION_SEC

# Palette
BG_COLOR = (12, 16, 26)       # Dark Navy #0C101A
ACCENT_GREEN = (0, 255, 102)   # Neon Green #00FF66
ACCENT_PINK = (255, 42, 109)   # Hot Pink #FF2A6D
ACCENT_BLUE = (0, 229, 255)   # Cyber Blue #00E5FF
YELLOW_POP = (255, 230, 0)    # Comic Yellow #FFE600

try:
    FONT_TITLE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 70)
    FONT_HEADER = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 55)
    FONT_BODY = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
    FONT_BOOM = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 110)
except Exception:
    FONT_TITLE = FONT_HEADER = FONT_BODY = FONT_BOOM = ImageFont.load_default()

def draw_comic_panel(draw, bbox, bg_col, border_col, title=""):
    """Draws a pop-art comic panel with thick borders and drop shadow"""
    x0, y0, x1, y1 = bbox
    # Drop shadow
    draw.rectangle([x0 + 12, y0 + 12, x1 + 12, y1 + 12], fill=(0, 0, 0))
    # Main panel background
    draw.rectangle([x0, y0, x1, y1], fill=bg_col, outline=border_col, width=6)
    if title:
        draw.rectangle([x0, y0, x0 + 260, y0 + 50], fill=border_col)
        draw.text((x0 + 15, y0 + 10), title, fill=(0, 0, 0), font=FONT_BODY)

def draw_speech_bubble(draw, x, y, text, tail_dir="down"):
    """Draws a comic book speech bubble"""
    w, h = 750, 140
    rect = [x - w//2, y - h//2, x + w//2, y + h//2]
    # Shadow
    draw.rounded_rectangle([rect[0]+8, rect[1]+8, rect[2]+8, rect[3]+8], radius=25, fill=(0, 0, 0))
    # Main Bubble
    draw.rounded_rectangle(rect, radius=25, fill=(255, 255, 255), outline=(0, 0, 0), width=5)
    # Speech text
    draw.text((x, y), text, fill=(0, 0, 0), font=FONT_BODY, anchor="mm")

def draw_action_burst(draw, x, y, text, scale=1.0):
    """Draws an explosive comic burst (BOOM! POW! ZAP!)"""
    num_points = 12
    outer_r = int(220 * scale)
    inner_r = int(120 * scale)
    points = []
    for i in range(num_points * 2):
        r = outer_r if i % 2 == 0 else inner_r
        angle = i * (math.pi / num_points)
        px = x + int(r * math.cos(angle))
        py = y + int(r * math.sin(angle))
        points.append((px, py))
    
    # Shadow burst
    shadow_pts = [(px+10, py+10) for px, py in points]
    draw.polygon(shadow_pts, fill=(0, 0, 0))
    # Yellow Burst
    draw.polygon(points, fill=YELLOW_POP, outline=(255, 42, 109), width=6)
    # Text
    draw.text((x, y), text, fill=(255, 42, 109), font=FONT_BOOM, anchor="mm")

def render_frame(frame_idx: int) -> Image.Image:
    t = frame_idx / FPS
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    # 1. Top Comic Banner
    draw.rectangle([0, 0, WIDTH, 160], fill=(22, 28, 44))
    draw.text((WIDTH//2, 80), "MAD HOUSE #1", fill=ACCENT_GREEN, font=FONT_TITLE, anchor="mm")
    draw.line([0, 160, WIDTH, 160], fill=ACCENT_GREEN, width=6)

    # 2. Main Animated Content Switcher
    if t < 2.5:
        # Scene 1: Apartment 4B Setup
        draw_comic_panel(draw, [80, 260, 1000, 1300], (20, 26, 40), ACCENT_BLUE, "APARTMENT 4B - 8:05 AM")
        
        # Max's Quantum Toaster Illustration Box
        draw.rectangle([140, 360, 940, 900], fill=(30, 40, 60), outline=(255, 255, 255), width=4)
        draw.text((WIDTH//2, 630), "⚡ QUANTUM TOASTER ⚡", fill=ACCENT_BLUE, font=FONT_HEADER, anchor="mm")
        
        # Speech Bubble
        draw_speech_bubble(draw, WIDTH//2, 1100, "MAX: 'I perfected the butter-spreader!'")

    elif t < 5.5:
        # Scene 2: Explosion Burst!
        draw_comic_panel(draw, [80, 260, 1000, 1300], (40, 15, 25), ACCENT_PINK, "BOOM!")
        
        # Action Burst Animation
        scale = 1.0 + 0.15 * math.sin(t * 12)
        draw_action_burst(draw, WIDTH//2, 650, "BOOM!", scale=scale)
        
        # Speech Bubble
        draw_speech_bubble(draw, WIDTH//2, 1100, "LEO: 'It shot bread through the wall!'")

    elif t < 8.0:
        # Scene 3: Landlord Stomps In
        draw_comic_panel(draw, [80, 260, 1000, 1300], (40, 35, 10), YELLOW_POP, "THE LANDLORD!")
        
        # Gupta Angry Box
        draw.rectangle([140, 360, 940, 900], fill=(60, 50, 20), outline=ACCENT_PINK, width=6)
        draw.text((WIDTH//2, 630), "😡 MR. GUPTA 😡", fill=ACCENT_PINK, font=FONT_HEADER, anchor="mm")
        
        # Speech Bubble
        draw_speech_bubble(draw, WIDTH//2, 1100, "GUPTA: 'WHAT WAS THAT NOISE?!'")

    else:
        # Scene 4: Call-to-Action (CTA)
        draw_comic_panel(draw, [80, 260, 1000, 1300], (15, 35, 25), ACCENT_GREEN, "GET THE COMIC!")
        
        # Book Cover Box
        draw.rectangle([200, 360, 880, 900], fill=(25, 50, 35), outline=ACCENT_GREEN, width=6)
        draw.text((WIDTH//2, 550), "MAD HOUSE", fill=ACCENT_GREEN, font=FONT_TITLE, anchor="mm")
        draw.text((WIDTH//2, 680), "ISSUE #1 ON KDP", fill=(255, 255, 255), font=FONT_HEADER, anchor="mm")
        
        draw_speech_bubble(draw, WIDTH//2, 1100, "READ NOW ON KDP & GUMROAD!")

    # 3. Footer Bar
    draw.rectangle([0, HEIGHT - 180, WIDTH, HEIGHT], fill=(22, 28, 44))
    draw.text((WIDTH//2, HEIGHT - 90), "🔥 ANIMATED SERIES & COMIC BOOK", fill=(255, 255, 255), font=FONT_BODY, anchor="mm")

    return img

def render_pro_video():
    print("=================================================================")
    print(" 🎬 RENDERING PRO POP-ART COMIC MOTION GRAPHIC VIDEO")
    print("=================================================================")
    
    print(f"• Generating {TOTAL_FRAMES} Pop-Art Comic Motion Frames...")
    for i in range(TOTAL_FRAMES):
        img = render_frame(i)
        img.save(FRAMES_DIR / f"frame_{i:04d}.png")

    print(f"• Encoding 1080x1920 MP4 Video using FFmpeg...")
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", str(FRAMES_DIR / "frame_%04d.png"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        str(OUTPUT_MP4)
    ]
    subprocess.run(cmd, check=True)

    # Clean frames
    for f in FRAMES_DIR.glob("*.png"):
        f.unlink()
    FRAMES_DIR.rmdir()

    print("=================================================================")
    print(f" 🏆 PRO MOTION GRAPHIC RENDER COMPLETE: {OUTPUT_MP4}")
    print(f"   Size: {os.path.getsize(OUTPUT_MP4):,} bytes")
    print("=================================================================")

if __name__ == "__main__":
    render_pro_video()
