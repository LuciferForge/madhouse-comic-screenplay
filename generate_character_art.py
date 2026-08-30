#!/usr/bin/env python3
"""
MAD HOUSE Character Artwork Generator & Compositor
Generates rich illustrated character art PNGs for Max, Leo, and Gupta
and composites them directly into the Naruto-style anime video trailer!
"""

import os
import sys
import math
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

CHAR_DIR = Path("/Users/apple/Documents/products/madhouse-comic-screenplay/character_assets")
CHAR_DIR.mkdir(parents=True, exist_ok=True)

# Generate Detailed Anime Character Art - Max Thornton
def generate_max_art():
    w, h = 600, 700
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = w // 2, 350

    # Glow / Energy Aura Backing
    draw.ellipse([cx - 240, cy - 240, cx + 240, cy + 240], fill=(0, 229, 255, 60))

    # Lab Coat & Body
    draw.polygon([(cx - 200, cy + 300), (cx - 130, cy + 100), (cx + 130, cy + 100), (cx + 200, cy + 300)], fill=(245, 245, 250), outline=(0, 0, 0), width=6)
    # Inner Band Tee (Black with Lightning Symbol)
    draw.polygon([(cx - 70, cy + 100), (cx + 70, cy + 100), (cx + 40, cy + 250), (cx - 40, cy + 250)], fill=(20, 20, 30))
    draw.text((cx, cy + 170), "⚡", fill=(0, 255, 102), font=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 60), anchor="mm")

    # Head / Neck
    draw.polygon([(cx - 45, cy + 50), (cx + 45, cy + 50), (cx + 35, cy + 110), (cx - 35, cy + 110)], fill=(235, 190, 150))
    # Face Oval
    draw.ellipse([cx - 100, cy - 120, cx + 100, cy + 70], fill=(245, 200, 160), outline=(0, 0, 0), width=5)

    # Messy Spiky Brown Hair
    spikes = [
        (cx - 120, cy - 60), (cx - 140, cy - 120), (cx - 90, cy - 170), 
        (cx - 50, cy - 220), (cx, cy - 240), (cx + 50, cy - 220), 
        (cx + 90, cy - 170), (cx + 140, cy - 120), (cx + 120, cy - 60)
    ]
    draw.polygon(spikes, fill=(110, 65, 35), outline=(0, 0, 0), width=5)

    # Goggles on Forehead
    draw.rectangle([cx - 85, cy - 140, cx - 15, cy - 80], fill=(0, 229, 255), outline=(40, 40, 40), width=6)
    draw.rectangle([cx + 15, cy - 140, cx + 85, cy - 80], fill=(0, 229, 255), outline=(40, 40, 40), width=6)
    draw.line([cx - 15, cy - 110, cx + 15, cy - 110], fill=(0, 0, 0), width=8)

    # Anime Eyes (Determined / Smirking)
    draw.polygon([(cx - 70, cy - 30), (cx - 20, cy - 40), (cx - 30, cy - 10)], fill=(0, 0, 0)) # Eyebrow L
    draw.polygon([(cx + 20, cy - 40), (cx + 70, cy - 30), (cx + 30, cy - 10)], fill=(0, 0, 0)) # Eyebrow R
    draw.ellipse([cx - 60, cy - 10, cx - 30, cy + 25], fill=(0, 229, 255), outline=(0, 0, 0), width=3) # Iris L
    draw.ellipse([cx + 30, cy - 10, cx + 60, cy + 25], fill=(0, 229, 255), outline=(0, 0, 0), width=3) # Iris R

    # Smirk & Soot
    draw.arc([cx - 40, cy + 15, cx + 40, cy + 50], start=10, end=170, fill=(0, 0, 0), width=6)
    draw.ellipse([cx + 40, cy + 20, cx + 65, cy + 45], fill=(80, 80, 80)) # Soot mark

    # Quantum Device in Hand
    draw.rectangle([cx + 120, cy + 100, cx + 220, cy + 220], fill=(50, 50, 70), outline=(0, 255, 102), width=5)
    draw.ellipse([cx + 145, cy + 125, cx + 195, cy + 175], fill=(0, 255, 102))

    img.save(CHAR_DIR / "max_thornton.png")
    print("✅ Created Character Art: Max Thornton")

# Generate Detailed Anime Character Art - Leo Vance
def generate_leo_art():
    w, h = 600, 700
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = w // 2, 350

    # Glow / Shadow Aura Backing
    draw.ellipse([cx - 240, cy - 240, cx + 240, cy + 240], fill=(255, 42, 109, 60))

    # Bathrobe & Body
    draw.polygon([(cx - 210, cy + 300), (cx - 140, cy + 100), (cx + 140, cy + 100), (cx + 210, cy + 300)], fill=(30, 35, 55), outline=(0, 0, 0), width=6)
    # Bathrobe Lapels
    draw.polygon([(cx - 140, cy + 100), (cx, cy + 280), (cx - 40, cy + 300)], fill=(200, 40, 80))
    draw.polygon([(cx + 140, cy + 100), (cx, cy + 280), (cx + 40, cy + 300)], fill=(200, 40, 80))

    # Head & Neck
    draw.polygon([(cx - 45, cy + 50), (cx + 45, cy + 50), (cx + 35, cy + 110), (cx - 35, cy + 110)], fill=(230, 180, 140))
    draw.ellipse([cx - 95, cy - 110, cx + 95, cy + 70], fill=(240, 190, 150), outline=(0, 0, 0), width=5)

    # Sleek Dark Anime Hair
    hair_points = [
        (cx - 110, cy - 40), (cx - 130, cy - 110), (cx - 80, cy - 160), 
        (cx, cy - 180), (cx + 80, cy - 160), (cx + 130, cy - 110), (cx + 110, cy - 40)
    ]
    draw.polygon(hair_points, fill=(25, 25, 30), outline=(0, 0, 0), width=5)

    # Cool Black Sunglasses
    draw.polygon([(cx - 80, cy - 35), (cx - 10, cy - 35), (cx - 20, cy + 15), (cx - 75, cy + 15)], fill=(10, 10, 15), outline=(0, 0, 0), width=4)
    draw.polygon([(cx + 10, cy - 35), (cx + 80, cy - 35), (cx + 75, cy + 15), (cx + 20, cy + 15)], fill=(10, 10, 15), outline=(0, 0, 0), width=4)
    draw.line([cx - 10, cy - 25, cx + 10, cy - 25], fill=(0, 0, 0), width=6)

    # Deadpan Mouth
    draw.line([cx - 35, cy + 35, cx + 35, cy + 35], fill=(0, 0, 0), width=6)

    # Espresso Cup
    draw.rectangle([cx - 180, cy + 120, cx - 100, cy + 200], fill=(255, 255, 255), outline=(0, 0, 0), width=5)
    draw.text((cx - 140, cy + 160), "☕", fill=(100, 50, 20), font=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40), anchor="mm")

    img.save(CHAR_DIR / "leo_vance.png")
    print("✅ Created Character Art: Leo Vance")

# Generate Detailed Anime Character Art - Mr. Baldev Gupta
def generate_gupta_art():
    w, h = 600, 700
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = w // 2, 350

    # Flame Red Aura Backing
    draw.ellipse([cx - 250, cy - 250, cx + 250, cy + 250], fill=(255, 51, 51, 70))

    # Cardigan & Body
    draw.polygon([(cx - 220, cy + 300), (cx - 150, cy + 100), (cx + 150, cy + 100), (cx + 220, cy + 300)], fill=(140, 40, 30), outline=(0, 0, 0), width=6)
    
    # Head & Neck
    draw.ellipse([cx - 105, cy - 100, cx + 105, cy + 80], fill=(245, 180, 140), outline=(0, 0, 0), width=5)

    # Flying Crooked Toupee
    draw.ellipse([cx - 80, cy - 170, cx + 40, cy - 90], fill=(60, 40, 30), outline=(0, 0, 0), width=5)

    # Angry Vein on Forehead
    draw.text((cx + 45, cy - 60), "💢", fill=(255, 0, 0), font=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 50), anchor="mm")

    # Angry Eyes
    draw.line([cx - 70, cy - 30, cx - 15, cy - 5], fill=(0, 0, 0), width=8) # Eyebrow L
    draw.line([cx + 15, cy - 5, cx + 70, cy - 30], fill=(0, 0, 0), width=8) # Eyebrow R
    draw.ellipse([cx - 55, cy - 5, cx - 30, cy + 20], fill=(255, 51, 51), outline=(0, 0, 0), width=3)
    draw.ellipse([cx + 30, cy - 5, cx + 55, cy + 20], fill=(255, 51, 51), outline=(0, 0, 0), width=3)

    # Yelling Open Mouth
    draw.ellipse([cx - 45, cy + 25, cx + 45, cy + 70], fill=(160, 20, 20), outline=(0, 0, 0), width=5)

    # Rent Clipboard
    draw.rectangle([cx + 110, cy + 100, cx + 220, cy + 250], fill=(160, 110, 60), outline=(0, 0, 0), width=5)
    draw.text((cx + 165, cy + 175), "RENT\n$$$", fill=(255, 255, 255), font=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 30), anchor="mm")

    img.save(CHAR_DIR / "mr_gupta.png")
    print("✅ Created Character Art: Mr. Baldev Gupta")

if __name__ == "__main__":
    generate_max_art()
    generate_leo_art()
    generate_gupta_art()
