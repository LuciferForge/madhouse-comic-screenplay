#!/usr/bin/env python3
"""
MAD HOUSE Naruto-Style Anime Character Intro Video Generator
Renders a high-energy anime/comic character intro (1080x1920 MP4) featuring:
- Radial speed lines & dynamic slash transitions
- Full character portraits (Max, Leo, Mr. Gupta) with glowing aura energy
- Character intro freeze-frame cards with bold impact badges
- High-FPS kinetic motion graphics
"""

import os
import math
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = Path("/Users/apple/Documents/products/madhouse-comic-screenplay/rendered_shorts")
FRAMES_DIR = OUTPUT_DIR / "naruto_frames"
OUTPUT_MP4 = OUTPUT_DIR / "madhouse_naruto_intro.mp4"

FRAMES_DIR.mkdir(parents=True, exist_ok=True)

WIDTH, HEIGHT = 1080, 1920
FPS = 30
DURATION_SEC = 15
TOTAL_FRAMES = FPS * DURATION_SEC

# Color Palette
BG_DARK = (8, 10, 18)
NEON_GREEN = (0, 255, 102)
NEON_CYAN = (0, 229, 255)
NEON_PINK = (255, 42, 109)
CHAKRA_YELLOW = (255, 230, 0)
FLAME_RED = (255, 51, 51)

try:
    FONT_HUGE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 110)
    FONT_TITLE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 80)
    FONT_SUB = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 45)
    FONT_BADGE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 38)
except Exception:
    FONT_HUGE = FONT_TITLE = FONT_SUB = FONT_BADGE = ImageFont.load_default()

def draw_speed_lines(draw, cx, cy, num_lines=36, color=(255, 255, 255, 40)):
    """Draws Naruto-style radial speed lines converging on (cx, cy)"""
    for i in range(num_lines):
        angle = i * (2 * math.pi / num_lines)
        r_outer = 1400
        r_inner = 350 + (i % 3) * 50
        x1 = cx + int(r_inner * math.cos(angle))
        y1 = cy + int(r_inner * math.sin(angle))
        x2 = cx + int(r_outer * math.cos(angle))
        y2 = cy + int(r_outer * math.sin(angle))
        draw.line([x1, y1, x2, y2], fill=(255, 255, 255), width=3)

# Character Art PNG Paths
CHAR_MAX_PATH = Path("/Users/apple/Documents/products/madhouse-comic-screenplay/character_assets/max_thornton.png")
CHAR_LEO_PATH = Path("/Users/apple/Documents/products/madhouse-comic-screenplay/character_assets/leo_vance.png")
CHAR_GUPTA_PATH = Path("/Users/apple/Documents/products/madhouse-comic-screenplay/character_assets/mr_gupta.png")

IMG_MAX = Image.open(CHAR_MAX_PATH).convert("RGBA") if CHAR_MAX_PATH.exists() else None
IMG_LEO = Image.open(CHAR_LEO_PATH).convert("RGBA") if CHAR_LEO_PATH.exists() else None
IMG_GUPTA = Image.open(CHAR_GUPTA_PATH).convert("RGBA") if CHAR_GUPTA_PATH.exists() else None

def draw_character_max(img, cx, cy, pulse=1.0):
    """Pastes Max Thornton PNG character artwork onto frame"""
    if IMG_MAX:
        w, h = int(550 * pulse), int(640 * pulse)
        resized = IMG_MAX.resize((w, h), Image.Resampling.LANCZOS)
        img.paste(resized, (cx - w//2, cy - h//2), resized)

def draw_character_leo(img, cx, cy, pulse=1.0):
    """Pastes Leo Vance PNG character artwork onto frame"""
    if IMG_LEO:
        w, h = int(550 * pulse), int(640 * pulse)
        resized = IMG_LEO.resize((w, h), Image.Resampling.LANCZOS)
        img.paste(resized, (cx - w//2, cy - h//2), resized)

def draw_character_gupta(img, cx, cy, pulse=1.0):
    """Pastes Mr. Baldev Gupta PNG character artwork onto frame"""
    if IMG_GUPTA:
        w, h = int(550 * pulse), int(640 * pulse)
        resized = IMG_GUPTA.resize((w, h), Image.Resampling.LANCZOS)
        img.paste(resized, (cx - w//2, cy - h//2), resized)

def render_frame(frame_idx: int) -> Image.Image:
    t = frame_idx / FPS
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)

    cx, cy = WIDTH // 2, 750
    pulse = 1.0 + 0.08 * math.sin(t * 10)

    # 1. INTRO TITLE SEQUENCE (0.0s - 3.0s)
    if t < 3.0:
        draw_speed_lines(draw, cx, cy)
        # Giant Impact Badge
        draw.rectangle([100, 500, 980, 850], fill=(22, 28, 44), outline=NEON_GREEN, width=8)
        draw.text((cx, 620), "MAD HOUSE", fill=NEON_GREEN, font=FONT_HUGE, anchor="mm")
        draw.text((cx, 750), "THE UNHINGED TENANTS", fill=(255, 255, 255), font=FONT_SUB, anchor="mm")

        # Diagonal Slash Banner
        draw.polygon([(0, 1100), (WIDTH, 1000), (WIDTH, 1220), (0, 1320)], fill=NEON_PINK)
        draw.text((cx, 1160), "OFFICIAL CHARACTER INTRO", fill=(255, 255, 255), font=FONT_TITLE, anchor="mm")

    # 2. CHARACTER 1: MAX THORNTON (3.0s - 6.0s)
    elif t < 6.0:
        draw_speed_lines(draw, cx, cy, color=NEON_CYAN)
        draw_character_max(img, cx, cy, pulse=pulse)

        # Character Card Overlay
        draw.polygon([(0, 1250), (WIDTH, 1180), (WIDTH, 1550), (0, 1620)], fill=(16, 24, 40), outline=NEON_CYAN, width=6)
        draw.text((100, 1320), "NAME: MAX THORNTON", fill=NEON_CYAN, font=FONT_TITLE)
        draw.text((100, 1420), "ROLE: HYPERACTIVE GENIUS INVENTOR", fill=(255, 255, 255), font=FONT_SUB)
        draw.text((100, 1490), "ABILITY: QUANTUM BUTTER SPREADING (MACH 2)", fill=CHAKRA_YELLOW, font=FONT_BADGE)

    # 3. CHARACTER 2: LEO VANCE (6.0s - 9.0s)
    elif t < 9.0:
        draw_speed_lines(draw, cx, cy, color=NEON_PINK)
        draw_character_leo(img, cx, cy, pulse=pulse)

        # Character Card Overlay
        draw.polygon([(0, 1250), (WIDTH, 1180), (WIDTH, 1550), (0, 1620)], fill=(30, 18, 32), outline=NEON_PINK, width=6)
        draw.text((100, 1320), "NAME: LEO VANCE", fill=NEON_PINK, font=FONT_TITLE)
        draw.text((100, 1420), "ROLE: DEADPAN PRAGMATIST", fill=(255, 255, 255), font=FONT_SUB)
        draw.text((100, 1490), "ABILITY: IMMUNE TO LIVING ROOM EXPLOSIONS", fill=NEON_CYAN, font=FONT_BADGE)

    # 4. CHARACTER 3: MR. BALDEV GUPTA (9.0s - 12.0s)
    elif t < 12.0:
        draw_speed_lines(draw, cx, cy, color=FLAME_RED)
        draw_character_gupta(img, cx, cy, pulse=pulse)

        # Character Card Overlay
        draw.polygon([(0, 1250), (WIDTH, 1180), (WIDTH, 1550), (0, 1620)], fill=(45, 15, 15), outline=FLAME_RED, width=6)
        draw.text((100, 1320), "NAME: MR. BALDEV GUPTA", fill=FLAME_RED, font=FONT_TITLE)
        draw.text((100, 1420), "ROLE: FURIOUS LANDLORD", fill=(255, 255, 255), font=FONT_SUB)
        draw.text((100, 1490), "ABILITY: RENT INCREASE & TOUPEE LEVITATION", fill=CHAKRA_YELLOW, font=FONT_BADGE)

    # 5. ENSEMBLE SHOWCASE & CALL TO ACTION (12.0s - 15.0s)
    else:
        # Triple Split Screen Showcase
        draw.rectangle([50, 250, 330, 1000], fill=(20, 40, 60), outline=NEON_CYAN, width=4)
        draw_character_max(img, 190, 500, pulse=0.45)
        draw.text((190, 920), "MAX", fill=NEON_CYAN, font=FONT_SUB, anchor="mm")

        draw.rectangle([390, 250, 670, 1000], fill=(50, 20, 40), outline=NEON_PINK, width=4)
        draw_character_leo(img, 530, 500, pulse=0.45)
        draw.text((530, 920), "LEO", fill=NEON_PINK, font=FONT_SUB, anchor="mm")

        draw.rectangle([730, 250, 1010, 1000], fill=(60, 30, 20), outline=FLAME_RED, width=4)
        draw_character_gupta(img, 870, 500, pulse=0.45)
        draw.text((870, 920), "GUPTA", fill=FLAME_RED, font=FONT_SUB, anchor="mm")

        # CTA Card
        draw.rectangle([80, 1150, 1000, 1600], fill=(22, 28, 44), outline=NEON_GREEN, width=8)
        draw.text((cx, 1260), "MAD HOUSE ISSUE #1", fill=NEON_GREEN, font=FONT_TITLE, anchor="mm")
        draw.text((cx, 1370), "READ THE COMIC ON KDP & GUMROAD", fill=(255, 255, 255), font=FONT_SUB, anchor="mm")
        draw.text((cx, 1470), "🔥 ANIMATED SERIES COMING SOON!", fill=CHAKRA_YELLOW, font=FONT_BADGE, anchor="mm")

    # Header & Footer Bars
    draw.rectangle([0, 0, WIDTH, 120], fill=(16, 20, 30))
    draw.text((cx, 60), "⚡ MAD HOUSE ANIME CHARACTER TRAILER ⚡", fill=NEON_GREEN, font=FONT_BADGE, anchor="mm")

    draw.rectangle([0, HEIGHT - 140, WIDTH, HEIGHT], fill=(16, 20, 30))
    draw.text((cx, HEIGHT - 70), "SUBSCRIBE FOR ANIMATED EPISODES & COMIC RELEASES", fill=(255, 255, 255), font=FONT_BADGE, anchor="mm")

    return img

def render_naruto_intro():
    print("=================================================================")
    print(" ⚡ RENDERING NARUTO-STYLE ANIME CHARACTER INTRO VIDEO")
    print("=================================================================")
    print(f"• Generating {TOTAL_FRAMES} High-FPS Anime Frames at {FPS} FPS...")
    
    for i in range(TOTAL_FRAMES):
        img = render_frame(i)
        img.save(FRAMES_DIR / f"frame_{i:04d}.png")

    print(f"• Compiling 1080x1920 MP4 Video using FFmpeg...")
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
    print(f" 🏆 NARUTO ANIME INTRO RENDER COMPLETE: {OUTPUT_MP4}")
    print(f"   Size: {os.path.getsize(OUTPUT_MP4):,} bytes")
    print("=================================================================")
    return str(OUTPUT_MP4)

if __name__ == "__main__":
    render_naruto_intro()
