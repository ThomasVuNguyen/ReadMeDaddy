#!/usr/bin/env python3
"""Generate SVG diagrams for Chapter 2: 'A Monster More Insatiable Than the Guillotine'."""

import math
import os
import random

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Color palette (shared with ch1)
BG_DARK = "#0a0e27"
BG_PANEL = "#111738"
BG_PANEL_LIGHT = "#1a1e3a"
WHITE = "#ffffff"
TEXT_DIM = "#8a8fa8"
RED = "#FF6B6B"
GREEN = "#69F0AE"
GOLD = "#FFD700"
BLUE = "#4FC3F7"
PURPLE = "#B388FF"
YELLOW = "#FFEB3B"
ORANGE = "#FF9800"
PINK = "#FF80AB"


def svg_header(width, height, title=""):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <title>{title}</title>
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;display=swap');
      text {{ font-family: 'Inter', 'Segoe UI', system-ui, sans-serif; }}
    </style>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_PANEL_LIGHT}"/>
    </linearGradient>
  </defs>
  <rect width="{width}" height="{height}" fill="url(#bgGrad)" rx="12"/>
'''


def svg_footer():
    return "</svg>\n"


# ============================================================
# Diagram 1: The Great Crossover — diseases falling, cancer rising
# ============================================================
def generate_disease_crossover():
    w, h = 800, 440
    svg = svg_header(w, h, "The Great Crossover: Diseases Falling, Cancer Rising")

    svg += f'  <text x="{w/2}" y="35" text-anchor="middle" fill="{WHITE}" font-size="20" font-weight="700">The Great Crossover</text>\n'
    svg += f'  <text x="{w/2}" y="57" text-anchor="middle" fill="{TEXT_DIM}" font-size="14">As infectious diseases vanished, cancer filled the space they left</text>\n'

    # Chart area
    cx, cy = 100, 80  # chart origin (top-left of plot area)
    cw, ch = 620, 300  # chart width/height
    
    # Panel background
    svg += f'  <rect x="{cx-10}" y="{cy-5}" width="{cw+20}" height="{ch+15}" fill="{BG_PANEL}" rx="8" opacity="0.5"/>\n'

    # Axes
    svg += f'  <line x1="{cx}" y1="{cy+ch}" x2="{cx+cw}" y2="{cy+ch}" stroke="{TEXT_DIM}" stroke-width="1" opacity="0.5"/>\n'
    svg += f'  <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+ch}" stroke="{TEXT_DIM}" stroke-width="1" opacity="0.5"/>\n'

    # Y-axis label
    svg += f'  <text x="55" y="{cy + ch/2}" text-anchor="middle" fill="{TEXT_DIM}" font-size="11" transform="rotate(-90, 55, {cy + ch/2})">Deaths per 100,000</text>\n'

    # Time labels (1900-1950)
    years = [1900, 1910, 1920, 1930, 1940, 1950]
    for yr in years:
        x = cx + (yr - 1900) / 50 * cw
        svg += f'  <text x="{x:.0f}" y="{cy+ch+20}" text-anchor="middle" fill="{TEXT_DIM}" font-size="11">{yr}</text>\n'
        svg += f'  <line x1="{x:.0f}" y1="{cy+ch}" x2="{x:.0f}" y2="{cy+ch+5}" stroke="{TEXT_DIM}" stroke-width="1" opacity="0.3"/>\n'

    # TB: high → low (falling disease)
    tb_points = [
        (1900, 200), (1905, 185), (1910, 160), (1915, 145),
        (1920, 120), (1925, 100), (1930, 75), (1935, 55),
        (1940, 40), (1945, 30), (1950, 20)
    ]
    
    # Typhoid: high → near zero
    typhoid_points = [
        (1900, 130), (1905, 90), (1910, 60), (1915, 35),
        (1920, 20), (1925, 12), (1930, 8), (1935, 5),
        (1940, 3), (1945, 2), (1950, 1)
    ]
    
    # Cancer: low → high (rising)
    cancer_points = [
        (1900, 65), (1905, 75), (1910, 85), (1915, 95),
        (1920, 105), (1925, 115), (1926, 120), (1930, 130),
        (1935, 140), (1940, 150), (1945, 160), (1950, 170)
    ]

    max_val = 220  # Y-axis max

    def to_svg_coords(yr, val):
        x = cx + (yr - 1900) / 50 * cw
        y = cy + ch - (val / max_val * ch)
        return x, y

    def draw_line(points, color, label_text, label_x_offset=0, label_y_offset=0):
        path_parts = []
        for i, (yr, val) in enumerate(points):
            x, y = to_svg_coords(yr, val)
            if i == 0:
                path_parts.append(f"M{x:.1f},{y:.1f}")
            else:
                path_parts.append(f"L{x:.1f},{y:.1f}")
        path_d = " ".join(path_parts)
        nonlocal svg
        svg += f'  <path d="{path_d}" fill="none" stroke="{color}" stroke-width="2.5" opacity="0.8"/>\n'
        # End label
        last_x, last_y = to_svg_coords(*points[-1])
        svg += f'  <circle cx="{last_x:.1f}" cy="{last_y:.1f}" r="4" fill="{color}" opacity="0.9"/>\n'
        svg += f'  <text x="{last_x + 8 + label_x_offset:.1f}" y="{last_y + 4 + label_y_offset:.1f}" fill="{color}" font-size="12" font-weight="600">{label_text}</text>\n'

    draw_line(tb_points, BLUE, "Tuberculosis", 0, 0)
    draw_line(typhoid_points, PURPLE, "Typhoid", 0, 0)
    draw_line(cancer_points, RED, "Cancer", 0, 0)

    # Crossover annotation
    cross_x, cross_y = to_svg_coords(1926, 120)
    svg += f'  <circle cx="{cross_x:.1f}" cy="{cross_y:.1f}" r="12" fill="none" stroke="{YELLOW}" stroke-width="1.5" stroke-dasharray="3,3"/>\n'
    svg += f'  <text x="{cross_x:.1f}" y="{cross_y - 18:.1f}" text-anchor="middle" fill="{YELLOW}" font-size="11" font-weight="600">1926: Cancer becomes #2 killer</text>\n'

    # Bottom insight
    svg += f'  <text x="{w/2}" y="{h - 15}" text-anchor="middle" fill="{TEXT_DIM}" font-size="12">Life expectancy: 47 → 68 years in half a century. Cancer was the price of living long enough to get it.</text>\n'

    svg += svg_footer()
    return svg


# ============================================================
# Diagram 2: Hot Ray vs Cold Knife — the only two options
# ============================================================
def generate_two_options():
    w, h = 800, 350
    svg = svg_header(w, h, "Cancer Treatment in the 1940s: Two Options")

    svg += f'  <text x="{w/2}" y="35" text-anchor="middle" fill="{WHITE}" font-size="20" font-weight="700">Cancer Treatment in the 1940s</text>\n'
    svg += f'  <text x="{w/2}" y="57" text-anchor="middle" fill="{TEXT_DIM}" font-size="14">"A choice between the hot ray and the cold knife"</text>\n'

    # Left panel: Surgery (cold knife)
    lx, ly = 60, 80
    pw, ph = 300, 210
    svg += f'  <rect x="{lx}" y="{ly}" width="{pw}" height="{ph}" fill="{BG_PANEL}" rx="10" stroke="{BLUE}" stroke-width="1.5" stroke-opacity="0.4"/>\n'
    svg += f'  <text x="{lx + pw/2}" y="{ly + 30}" text-anchor="middle" fill="{BLUE}" font-size="16" font-weight="600">The Cold Knife</text>\n'
    svg += f'  <text x="{lx + pw/2}" y="{ly + 50}" text-anchor="middle" fill="{TEXT_DIM}" font-size="12">Surgery</text>\n'

    # Scalpel icon (simple line drawing)
    scx = lx + pw/2
    scy = ly + 130
    svg += f'  <line x1="{scx-40}" y1="{scy-20}" x2="{scx+40}" y2="{scy+20}" stroke="{BLUE}" stroke-width="3" stroke-linecap="round"/>\n'
    svg += f'  <ellipse cx="{scx+40}" cy="{scy+20}" rx="12" ry="6" fill="none" stroke="{BLUE}" stroke-width="2" transform="rotate(25, {scx+40}, {scy+20})"/>\n'

    svg += f'  <text x="{lx + pw/2}" y="{ly + ph - 15}" text-anchor="middle" fill="{TEXT_DIM}" font-size="11">Works only if tumor is local</text>\n'

    # Right panel: Radiation (hot ray)
    rx, ry = 440, 80
    svg += f'  <rect x="{rx}" y="{ry}" width="{pw}" height="{ph}" fill="{BG_PANEL}" rx="10" stroke="{ORANGE}" stroke-width="1.5" stroke-opacity="0.4"/>\n'
    svg += f'  <text x="{rx + pw/2}" y="{ry + 30}" text-anchor="middle" fill="{ORANGE}" font-size="16" font-weight="600">The Hot Ray</text>\n'
    svg += f'  <text x="{rx + pw/2}" y="{ry + 50}" text-anchor="middle" fill="{TEXT_DIM}" font-size="12">Radiation</text>\n'

    # Radiation rays
    rcx = rx + pw/2
    rcy = ry + 130
    for angle_deg in range(-60, 61, 20):
        angle = math.radians(angle_deg)
        x2 = rcx + math.cos(angle) * 50
        y2 = rcy - math.sin(angle) * 50
        svg += f'  <line x1="{rcx}" y1="{rcy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{ORANGE}" stroke-width="2" opacity="0.6"/>\n'
    svg += f'  <circle cx="{rcx}" cy="{rcy}" r="8" fill="{ORANGE}" opacity="0.7"/>\n'

    svg += f'  <text x="{rx + pw/2}" y="{ry + ph - 15}" text-anchor="middle" fill="{TEXT_DIM}" font-size="11">Works only near the surface</text>\n'

    # Big question mark in the middle
    svg += f'  <text x="{w/2}" y="200" text-anchor="middle" fill="{TEXT_DIM}" font-size="40" opacity="0.3">?</text>\n'

    # Bottom box
    box_y = 305
    svg += f'  <rect x="100" y="{box_y}" width="600" height="35" fill="{BG_PANEL}" rx="6" stroke="{RED}" stroke-width="1" stroke-opacity="0.4"/>\n'
    svg += f'  <text x="{w/2}" y="{box_y + 22}" text-anchor="middle" fill="{RED}" font-size="13" font-weight="600">If the cancer had spread? Nothing. No drugs. No chemicals. No options.</text>\n'

    svg += svg_footer()
    return svg


# ============================================================
# Diagram 3: Farber's Logic — folic acid → acceleration → antifolate
# ============================================================
def generate_farber_logic():
    w, h = 800, 480
    svg = svg_header(w, h, "Farber's Logic: From Disaster to Breakthrough")

    svg += f'  <text x="{w/2}" y="35" text-anchor="middle" fill="{WHITE}" font-size="20" font-weight="700">Farber\'s Logic</text>\n'
    svg += f'  <text x="{w/2}" y="57" text-anchor="middle" fill="{TEXT_DIM}" font-size="14">How a catastrophic failure became a breakthrough insight</text>\n'

    # Three stages
    stages = [
        {
            "x": 30, "label": "The Hypothesis",
            "line1": "Folic acid restores",
            "line2": "normal blood production",
            "line3": "Maybe it fixes leukemia too?",
            "color": BLUE, "icon": "?"
        },
        {
            "x": 285, "label": "The Disaster",
            "line1": "Folic acid ACCELERATED",
            "line2": "the leukemia",
            "line3": "White cells doubled. Kids died faster.",
            "color": RED, "icon": "×"
        },
        {
            "x": 540, "label": "The Insight",
            "line1": "If folic acid speeds it UP",
            "line2": "blocking it might",
            "line3": "shut it DOWN",
            "color": GREEN, "icon": "✓"
        },
    ]

    panel_w = 225
    panel_h = 280
    panel_y = 75

    for s in stages:
        sx = s["x"]
        svg += f'  <rect x="{sx}" y="{panel_y}" width="{panel_w}" height="{panel_h}" fill="{BG_PANEL}" rx="10" stroke="{s["color"]}" stroke-width="1.5" stroke-opacity="0.4"/>\n'
        svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + 30}" text-anchor="middle" fill="{s["color"]}" font-size="16" font-weight="600">{s["label"]}</text>\n'

        # Icon
        svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + 100}" text-anchor="middle" fill="{s["color"]}" font-size="48" opacity="0.5">{s["icon"]}</text>\n'

        # Description lines
        svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + 170}" text-anchor="middle" fill="{WHITE}" font-size="12">{s["line1"]}</text>\n'
        svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + 188}" text-anchor="middle" fill="{WHITE}" font-size="12">{s["line2"]}</text>\n'
        svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + 220}" text-anchor="middle" fill="{s["color"]}" font-size="11" font-weight="600">{s["line3"]}</text>\n'

    # Arrows between stages
    svg += f'''  <defs>
    <marker id="arrowhead2" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{TEXT_DIM}"/>
    </marker>
  </defs>\n'''

    arrow_y = panel_y + panel_h / 2
    svg += f'  <line x1="{30 + panel_w + 5}" y1="{arrow_y}" x2="{285 - 5}" y2="{arrow_y}" stroke="{TEXT_DIM}" stroke-width="2" marker-end="url(#arrowhead2)"/>\n'
    svg += f'  <line x1="{285 + panel_w + 5}" y1="{arrow_y}" x2="{540 - 5}" y2="{arrow_y}" stroke="{TEXT_DIM}" stroke-width="2" marker-end="url(#arrowhead2)"/>\n'

    # Bottom: the key analogy
    box_y = 380
    svg += f'  <rect x="80" y="{box_y}" width="640" height="80" fill="{BG_PANEL}" rx="8" stroke="{GREEN}" stroke-width="1" stroke-opacity="0.4"/>\n'
    svg += f'  <text x="{w/2}" y="{box_y + 25}" text-anchor="middle" fill="{WHITE}" font-size="13" font-weight="600">The Fake Key Principle</text>\n'
    svg += f'  <text x="{w/2}" y="{box_y + 48}" text-anchor="middle" fill="{TEXT_DIM}" font-size="12">An antifolate mimics folic acid closely enough to fool the cell\'s enzymes,</text>\n'
    svg += f'  <text x="{w/2}" y="{box_y + 66}" text-anchor="middle" fill="{TEXT_DIM}" font-size="12">but jams the lock instead of opening it. Like a fake key that slides in but won\'t turn.</text>\n'

    svg += svg_footer()
    return svg


# ============================================================
# Diagram 4: The Bone Marrow Factory — on/off switch
# ============================================================
def generate_marrow_factory():
    w, h = 800, 380
    svg = svg_header(w, h, "The Bone Marrow Factory: On and Off Switches")

    svg += f'  <text x="{w/2}" y="35" text-anchor="middle" fill="{WHITE}" font-size="20" font-weight="700">The Bone Marrow Factory</text>\n'
    svg += f'  <text x="{w/2}" y="57" text-anchor="middle" fill="{TEXT_DIM}" font-size="14">300 billion new blood cells per day, all dependent on folic acid</text>\n'

    # Three states
    states = [
        {
            "x": 30, "label": "Starved (Bombay)",
            "subtitle": "No folic acid",
            "color": BLUE, "cell_rate": "low",
            "desc": "Factory halted",
            "cell_count": 3
        },
        {
            "x": 285, "label": "Normal",
            "subtitle": "Folic acid present",
            "color": GREEN, "cell_rate": "normal",
            "desc": "Steady production",
            "cell_count": 8
        },
        {
            "x": 540, "label": "Leukemia",
            "subtitle": "Folic acid overdrive",
            "color": RED, "cell_rate": "overdrive",
            "desc": "Factory out of control",
            "cell_count": 20
        },
    ]

    panel_w = 225
    panel_h = 250
    panel_y = 75

    random.seed(55)

    for s in states:
        sx = s["x"]
        svg += f'  <rect x="{sx}" y="{panel_y}" width="{panel_w}" height="{panel_h}" fill="{BG_PANEL}" rx="10" stroke="{s["color"]}" stroke-width="1.5" stroke-opacity="0.4"/>\n'
        svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + 28}" text-anchor="middle" fill="{s["color"]}" font-size="14" font-weight="600">{s["label"]}</text>\n'
        svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + 46}" text-anchor="middle" fill="{TEXT_DIM}" font-size="11">{s["subtitle"]}</text>\n'

        # Draw cells
        cx_cell = sx + panel_w / 2
        cy_cell = panel_y + 140
        count = s["cell_count"]

        for i in range(count):
            if count <= 3:
                x = cx_cell + (i - 1) * 30
                y = cy_cell
                r = 12
                opacity = 0.4
            elif count <= 8:
                col = i % 4
                row = i // 4
                x = cx_cell + (col - 1.5) * 28
                y = cy_cell + (row - 0.5) * 28
                r = 10
                opacity = 0.7
            else:
                x = cx_cell + random.uniform(-85, 85)
                y = cy_cell + random.uniform(-55, 55)
                r = random.uniform(6, 11)
                opacity = random.uniform(0.4, 0.9)

            svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{s["color"]}" opacity="{opacity:.2f}"/>\n'

        svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + panel_h - 20}" text-anchor="middle" fill="{s["color"]}" font-size="12" font-weight="600">{s["desc"]}</text>\n'

    # Bottom question
    svg += f'  <text x="{w/2}" y="{h - 15}" text-anchor="middle" fill="{YELLOW}" font-size="13" font-weight="600">Farber\'s question: Can we recreate the Bombay anemia in leukemia patients, on purpose?</text>\n'

    svg += svg_footer()
    return svg


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    diagrams = [
        ("01_disease_crossover.svg", generate_disease_crossover),
        ("02_two_options.svg", generate_two_options),
        ("03_farber_logic.svg", generate_farber_logic),
        ("04_marrow_factory.svg", generate_marrow_factory),
    ]

    for filename, gen_fn in diagrams:
        path = os.path.join(OUTPUT_DIR, filename)
        svg_content = gen_fn()
        with open(path, "w") as f:
            f.write(svg_content)
        print(f"Generated: {path}")
