#!/usr/bin/env python3
"""
generate_puzzle.py

Generates a "Crack the Code" puzzle image similar to the provided reference.
Requires: Pillow (pip install pillow)

Output: puzzle_output.png
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
from textwrap import wrap

# Canvas size (adjustable)
W, H = 868, 1024

# Try to load nice fonts; fall back to default if not available.
def load_font(name_list, size):
    for name in name_list:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()

# Common fonts to attempt (you can add local font file paths here)
TITLE_FONT = load_font(["Montserrat-Bold.ttf", "Arial-Bold.ttf", "DejaVuSans-Bold.ttf"], 56)
CLUE_FONT = load_font(["Montserrat-Regular.ttf", "Arial.ttf", "DejaVuSans.ttf"], 32)
DIGIT_FONT = load_font(["Montserrat-Bold.ttf", "Arial-Bold.ttf", "DejaVuSans-Bold.ttf"], 36)
SMALL_FONT = load_font(["Montserrat-Regular.ttf", "DejaVuSans.ttf", "Arial.ttf"], 16)

# Colors
BG_TOP = (250, 251, 252)
BG_BOTTOM = (237, 240, 242)
TILE_COLOR = (255, 255, 255, 255)
SHADOW_COLOR = (0, 0, 0, 180)
# GOLD_TILE = (212, 171, 114, 255)  # for question marks
GOLD_TILE = (212, 151, 124, 255)  # for question marks
TEXT_COLOR = (20, 20, 20)
SUBTEXT_COLOR = (90, 95, 100)

# Clues and digits to draw
guesses = ["5730", "9513", "2591", "4960", "4673"]
# clue_texts = [
#     "3 digits correct: 1 well placed, 2 in wrong place",
#     "2 digits correct: 1 well placed, 1 in wrong place",
#     "1 digit is correct & well placed",
#     "2 digits are correct but in wrong place",
# ]
clue_texts = [
    "2 digits correct but in wrong places",
    "Only 1 digit is correct",
    "2 digits correct: 1 well placed",
    "Only 1 digit is correct",
    "Only 1 digit is correct but it is well placed",
]

# Utility: draw vertical gradient
def draw_vertical_gradient(width, height, top_color, bottom_color):
    base = Image.new("RGB", (width, height), top_color)
    top = Image.new("RGB", (width, height), bottom_color)
    mask = Image.new("L", (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / (height - 1)))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

# Get text size helper (works across Pillow versions)
def get_text_size(draw, text, font):
    # Try draw.textbbox (newer Pillow)
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]
    except Exception:
        try:
            return font.getsize(text)
        except Exception:
            # last-resort
            return draw.textsize(text, font=font)

# Draw a rounded rectangle by pasting a masked block
def rounded_rectangle(target_image, xy, radius, fill):
    x0, y0, x1, y1 = xy
    w = x1 - x0
    h = y1 - y0
    if w <= 0 or h <= 0:
        return
    mask = Image.new("L", (w, h), 0)
    mdraw = ImageDraw.Draw(mask)
    # Use rounded_rectangle if available, otherwise draw by hand
    try:
        mdraw.rounded_rectangle((0, 0, w, h), radius=radius, fill=255)
    except Exception:
        # fallback: draw rectangle and four circles
        mdraw.rectangle((radius, 0, w - radius, h), fill=255)
        mdraw.rectangle((0, radius, w, h - radius), fill=255)
        mdraw.pieslice((0, 0, radius * 2, radius * 2), 180, 270, fill=255)
        mdraw.pieslice((w - radius * 2, 0, w, radius * 2), 270, 360, fill=255)
        mdraw.pieslice((0, h - radius * 2, radius * 2, h), 90, 180, fill=255)
        mdraw.pieslice((w - radius * 2, h - radius * 2, w, h), 0, 90, fill=255)
    colored = Image.new("RGBA", (w, h), fill)
    target_image.paste(colored, (x0, y0), mask)

# Draw a tile with drop shadow
def draw_tile(canvas, pos, size, radius=12, color=(255, 255, 255, 255), shadow=True, shadow_offset=(6, 8), shadow_blur=8):
    x, y = pos
    w, h = size
    if shadow:
        shadow_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        # draw shadow rounded rectangle onto shadow_layer (as a dark filled rect)
        rounded_rectangle(shadow_layer, (x + shadow_offset[0], y + shadow_offset[1], x + w + shadow_offset[0], y + h + shadow_offset[1]), radius, SHADOW_COLOR)
        shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=shadow_blur))
        canvas.alpha_composite(shadow_layer)
    # draw main tile
    rounded_rectangle(canvas, (x, y, x + w, y + h), radius, color)

# Centered text draw helper
def draw_centered_text(draw, text, bbox, font, fill):
    x0, y0, x1, y1 = bbox
    w = x1 - x0
    h = y1 - y0
    tw, th = get_text_size(draw, text, font)
    tx = x0 + (w - tw) / 2
    ty = y0 + (h - th) / 2
    draw.text((tx, ty), text, font=font, fill=fill)

def generate_image(output_path="puzzle_output.png"):
    # Background gradient
    bg = draw_vertical_gradient(W, H, BG_TOP, BG_BOTTOM)

    # Create RGBA canvas for easy compositing
    canvas = Image.new("RGBA", (W, H))
    canvas.paste(bg, (0, 0))

    draw = ImageDraw.Draw(canvas)

    # Title
    title = "CRACK THE CODE?"
    draw.text((40, 40), title, font=TITLE_FONT, fill=TEXT_COLOR)

    left_x = 40
    top_y = 240
    tile_w = 72
    tile_h = 72
    tile_gap_x = 18
    tile_gap_y = 24

    # bottom_y = top_y + 4 * (tile_h + tile_gap_y) + 60
    bottom_y = top_y
    q_tile_w = 72
    q_tile_h = 72
    q_gap = 18
    q_x_start = left_x
    for i in range(4):
        x = q_x_start + i * (q_tile_w + q_gap)
        draw_tile(canvas, (x, bottom_y), (q_tile_w, q_tile_h), radius=12, color=GOLD_TILE, shadow=True)
        bbox = (x, bottom_y, x + q_tile_w, bottom_y + q_tile_h)
        draw_centered_text(draw, "*", bbox, DIGIT_FONT, TEXT_COLOR)

    # Left starting position for tiles
    # left_x = 40
    top_y += (tile_h + tile_gap_y) + 60
    # tile_w = 72
    # tile_h = 72
    # tile_gap_x = 18
    # tile_gap_y = 24

    # Draw the four guess rows (large white tiles with digits)
    for row, guess in enumerate(guesses):
        y = top_y + row * (tile_h + tile_gap_y)
        for col, ch in enumerate(guess):
            x = left_x + col * (tile_w + tile_gap_x)
            # tile shadow + tile
            draw_tile(canvas, (x, y), (tile_w, tile_h), radius=12, color=TILE_COLOR, shadow=True)
            # digit
            bbox = (x, y, x + tile_w, y + tile_h)
            draw_centered_text(draw, ch, bbox, DIGIT_FONT, TEXT_COLOR)

    # Right column for clue texts
    # clue_x = 320
    clue_x = 400
    clue_y = top_y
    for i, text in enumerate(clue_texts):
        max_width = W - clue_x - 40
        wrapped = wrap(text, width=30)
        text_y = clue_y + i * (tile_h + tile_gap_y) + 6
        for j, line in enumerate(wrapped):
            draw.text((clue_x, text_y + j * 30), line, font=CLUE_FONT, fill=TEXT_COLOR)

    # Draw the gold question tiles at bottom
    # bottom_y = top_y + 4 * (tile_h + tile_gap_y) + 60
    # q_tile_w = 72
    # q_tile_h = 72
    # q_gap = 18
    # q_x_start = left_x
    # for i in range(4):
    #     x = q_x_start + i * (q_tile_w + q_gap)
    #     draw_tile(canvas, (x, bottom_y), (q_tile_w, q_tile_h), radius=12, color=GOLD_TILE, shadow=True)
    #     bbox = (x, bottom_y, x + q_tile_w, bottom_y + q_tile_h)
    #     draw_centered_text(draw, "*", bbox, DIGIT_FONT, TEXT_COLOR)

    # Bottom caption text
    # caption = "DOWNLOAD THE BRAIN CODE APP FOR MORE"
    # caption_w, caption_h = get_text_size(draw, caption, SMALL_FONT)
    # draw.text(((W - caption_w) / 2, H - 60), caption, font=SMALL_FONT, fill=SUBTEXT_COLOR)

    # Optional: translucent panel behind right-side clues to mimic original
    # overlay = Image.new("RGBA", (W, H), (255, 255, 255, 0))
    # odraw = ImageDraw.Draw(overlay)
    # odraw.rectangle((clue_x - 10, top_y - 10, W - 30, top_y + 4 * (tile_h + tile_gap_y) + 20), fill=(255, 255, 255, 220))
    # canvas = Image.alpha_composite(canvas, overlay)

    canvas.convert("RGB").save(output_path, quality=95)
    print(f"Saved puzzle image to {output_path}")

if __name__ == "__main__":
    out = "puzzle_output.png"
    if len(sys.argv) > 1:
        out = sys.argv[1]
    generate_image(out)
