#!/usr/bin/env python3
"""Generate SVG diagrams for Chapter 1: Prologue — 'A Suppuration of Blood'."""

import math
import os
import random

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Color palette
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

# Shared SVG header
def svg_header(width, height, title=""):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <title>{title}</title>
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;display=swap');
      text {{ font-family: 'Inter', 'Segoe UI', system-ui, sans-serif; }}
    </style>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
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
# Diagram 1: Normal Blood vs Leukemic Blood
# ============================================================
def generate_normal_vs_leukemic():
    w, h = 800, 520
    svg = svg_header(w, h, "Normal Blood vs Leukemic Blood")

    # Title
    svg += f'  <text x="{w/2}" y="40" text-anchor="middle" fill="{WHITE}" font-size="20" font-weight="700">Normal Blood vs Leukemic Blood</text>\n'

    # Two panels
    panel_w, panel_h = 340, 380
    panels = [
        {"x": 40, "y": 70, "label": "Normal Blood", "color": GREEN},
        {"x": 420, "y": 70, "label": "Leukemic Blood", "color": RED},
    ]

    random.seed(42)

    for p in panels:
        px, py = p["x"], p["y"]
        svg += f'  <rect x="{px}" y="{py}" width="{panel_w}" height="{panel_h}" fill="{BG_PANEL}" rx="10" stroke="{p["color"]}" stroke-width="1.5" stroke-opacity="0.4"/>\n'
        svg += f'  <text x="{px + panel_w/2}" y="{py + 30}" text-anchor="middle" fill="{p["color"]}" font-size="16" font-weight="600">{p["label"]}</text>\n'

    # Normal blood: mostly red cells, a few white cells
    cx_normal, cy_normal = 210, 260
    # Red blood cells (donut shapes) — constrained vertically to avoid label area
    for _ in range(50):
        x = cx_normal + random.uniform(-130, 130)
        y = cy_normal + random.uniform(-110, 100)
        r = random.uniform(8, 12)
        opacity = random.uniform(0.4, 0.8)
        svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{RED}" opacity="{opacity:.2f}"/>\n'
        svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r*0.35:.1f}" fill="{BG_PANEL}" opacity="{opacity:.2f}"/>\n'

    # A few white cells (larger, white/blue)
    for _ in range(4):
        x = cx_normal + random.uniform(-100, 100)
        y = cy_normal + random.uniform(-80, 80)
        svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="14" fill="{BLUE}" opacity="0.7"/>\n'
        svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{BG_PANEL}" opacity="0.5"/>\n'

    # Leukemic blood: overrun with white blast cells
    cx_leuk, cy_leuk = 590, 260
    # Fewer red cells, scattered — constrained vertically
    for _ in range(12):
        x = cx_leuk + random.uniform(-130, 130)
        y = cy_leuk + random.uniform(-110, 100)
        r = random.uniform(7, 10)
        opacity = random.uniform(0.2, 0.5)
        svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{RED}" opacity="{opacity:.2f}"/>\n'
        svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r*0.35:.1f}" fill="{BG_PANEL}" opacity="{opacity:.2f}"/>\n'

    # Masses of white blast cells — constrained vertically
    for _ in range(55):
        x = cx_leuk + random.uniform(-130, 130)
        y = cy_leuk + random.uniform(-110, 100)
        r = random.uniform(10, 16)
        opacity = random.uniform(0.5, 0.9)
        svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{PURPLE}" opacity="{opacity:.2f}"/>\n'
        # Immature nucleus (large, irregular)
        svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r*0.6:.1f}" fill="#7C4DFF" opacity="{opacity:.2f}"/>\n'

    # Labels at bottom — placed below cell area with clear spacing
    svg += f'  <text x="210" y="{70 + panel_h - 15}" text-anchor="middle" fill="{TEXT_DIM}" font-size="12">~5,000 white cells/mL</text>\n'
    svg += f'  <text x="590" y="{70 + panel_h - 15}" text-anchor="middle" fill="{TEXT_DIM}" font-size="12">~90,000 white cells/mL (Carla Reed)</text>\n'

    # Legend
    legend_y = 478
    items = [
        (RED, "Red blood cells"),
        (BLUE, "Normal white cells"),
        (PURPLE, "Leukemic blast cells"),
    ]
    start_x = 200
    for i, (color, label) in enumerate(items):
        lx = start_x + i * 180
        svg += f'  <circle cx="{lx}" cy="{legend_y}" r="6" fill="{color}" opacity="0.8"/>\n'
        svg += f'  <text x="{lx + 12}" y="{legend_y + 4}" fill="{TEXT_DIM}" font-size="12">{label}</text>\n'

    svg += svg_footer()
    return svg


# ============================================================
# Diagram 2: Hypertrophy vs Hyperplasia
# ============================================================
def generate_hypertrophy_vs_hyperplasia():
    w, h = 800, 420
    svg = svg_header(w, h, "Two Types of Growth: Hypertrophy vs Hyperplasia")

    svg += f'  <text x="{w/2}" y="40" text-anchor="middle" fill="{WHITE}" font-size="20" font-weight="700">Two Types of Growth</text>\n'
    svg += f'  <text x="{w/2}" y="62" text-anchor="middle" fill="{TEXT_DIM}" font-size="14">How tissues get bigger (Virchow\'s framework)</text>\n'

    # Three stages: Normal → Hypertrophy, Normal → Hyperplasia
    sections = [
        {"x": 30, "label": "Normal", "color": GREEN},
        {"x": 290, "label": "Hypertrophy", "subtitle": "Cells get BIGGER", "color": GOLD},
        {"x": 550, "label": "Hyperplasia", "subtitle": "Cells MULTIPLY", "color": BLUE},
    ]

    panel_w = 220
    panel_h = 260
    panel_y = 90

    for s in sections:
        sx = s["x"]
        svg += f'  <rect x="{sx}" y="{panel_y}" width="{panel_w}" height="{panel_h}" fill="{BG_PANEL}" rx="10" stroke="{s["color"]}" stroke-width="1.5" stroke-opacity="0.4"/>\n'
        svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + 28}" text-anchor="middle" fill="{s["color"]}" font-size="16" font-weight="600">{s["label"]}</text>\n'
        if "subtitle" in s:
            svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + 48}" text-anchor="middle" fill="{TEXT_DIM}" font-size="12">{s["subtitle"]}</text>\n'

    # Normal: 4 cells in a 2x2 grid
    def draw_cells(cx, cy, count_x, count_y, radius, color, opacity=0.7):
        cells = ""
        for i in range(count_x):
            for j in range(count_y):
                x = cx + (i - (count_x-1)/2) * (radius * 2.5)
                y = cy + (j - (count_y-1)/2) * (radius * 2.5)
                cells += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{radius}" fill="{color}" opacity="{opacity}"/>\n'
                cells += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{radius*0.4}" fill="{BG_PANEL}" opacity="0.6"/>\n'
        return cells

    # Normal: 4 medium cells — positioned lower to avoid subtitle overlap
    svg += draw_cells(140, 230, 2, 2, 22, GREEN)
    svg += f'  <text x="140" y="330" text-anchor="middle" fill="{TEXT_DIM}" font-size="11">4 cells, normal size</text>\n'

    # Hypertrophy: 4 large cells — pushed further down, label below cells
    svg += draw_cells(400, 235, 2, 2, 30, GOLD)
    svg += f'  <text x="400" y="330" text-anchor="middle" fill="{TEXT_DIM}" font-size="11">4 cells, each BIGGER</text>\n'

    # Hyperplasia: many small cells
    svg += draw_cells(660, 225, 4, 4, 14, BLUE)
    svg += f'  <text x="660" y="330" text-anchor="middle" fill="{TEXT_DIM}" font-size="11">16 cells, same size</text>\n'

    # Arrows
    for ax in [(252, 290), (512, 550)]:
        svg += f'  <line x1="{ax[0]}" y1="220" x2="{ax[1]}" y2="220" stroke="{TEXT_DIM}" stroke-width="2" marker-end="url(#arrowhead)"/>\n'

    svg += f'''  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{TEXT_DIM}"/>
    </marker>
  </defs>\n'''

    # Bottom note
    svg += f'  <text x="{w/2}" y="390" text-anchor="middle" fill="{TEXT_DIM}" font-size="13">Muscle &amp; fat → hypertrophy  |  Blood, liver, gut, skin → hyperplasia</text>\n'

    svg += svg_footer()
    return svg


# ============================================================
# Diagram 3: The Neoplasia Spectrum
# ============================================================
def generate_neoplasia_spectrum():
    w, h = 800, 440
    svg = svg_header(w, h, "From Normal Growth to Neoplasia")

    svg += f'  <text x="{w/2}" y="40" text-anchor="middle" fill="{WHITE}" font-size="20" font-weight="700">The Spectrum of Cell Growth</text>\n'
    svg += f'  <text x="{w/2}" y="62" text-anchor="middle" fill="{TEXT_DIM}" font-size="14">Normal hyperplasia → Pathological hyperplasia → Neoplasia (cancer)</text>\n'

    # Three stages as panels along a gradient bar
    stages = [
        {
            "x": 30, "label": "Normal Hyperplasia",
            "desc": "Controlled multiplication",
            "detail": "Cells divide when needed,\nthen stop on signal",
            "color": GREEN, "cell_count": 6, "radius": 16, "orderly": True
        },
        {
            "x": 280, "label": "Pathological\nHyperplasia",
            "desc": "Excessive but responsive",
            "detail": "Too many cells, but still\nrespond to stop signals",
            "color": GOLD, "cell_count": 12, "radius": 14, "orderly": True
        },
        {
            "x": 530, "label": "Neoplasia",
            "desc": "Autonomous, uncontrolled",
            "detail": "Cells ignore all stop signals.\nGrowth has its own will.",
            "color": RED, "cell_count": 24, "radius": 12, "orderly": False
        },
    ]

    panel_w = 230
    panel_h = 280
    panel_y = 85

    random.seed(99)

    for s in stages:
        sx = s["x"]
        svg += f'  <rect x="{sx}" y="{panel_y}" width="{panel_w}" height="{panel_h}" fill="{BG_PANEL}" rx="10" stroke="{s["color"]}" stroke-width="1.5" stroke-opacity="0.4"/>\n'

        # Label (handle multiline)
        lines = s["label"].split("\n")
        for li, line in enumerate(lines):
            svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + 26 + li*18}" text-anchor="middle" fill="{s["color"]}" font-size="15" font-weight="600">{line}</text>\n'

        svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + 26 + len(lines)*18 + 4}" text-anchor="middle" fill="{TEXT_DIM}" font-size="11">{s["desc"]}</text>\n'

        # Draw cells
        cx = sx + panel_w / 2
        cy = panel_y + 170
        count = s["cell_count"]
        r = s["radius"]

        if s["orderly"]:
            cols = min(count, 6)
            rows = math.ceil(count / cols)
            for i in range(count):
                col = i % cols
                row = i // cols
                x = cx + (col - (cols-1)/2) * (r * 2.3)
                y = cy + (row - (rows-1)/2) * (r * 2.3)
                svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{s["color"]}" opacity="0.6"/>\n'
                svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r*0.35}" fill="{BG_PANEL}" opacity="0.5"/>\n'
        else:
            for i in range(count):
                x = cx + random.uniform(-80, 80)
                y = cy + random.uniform(-60, 60)
                r_var = r + random.uniform(-3, 5)
                svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r_var:.1f}" fill="{s["color"]}" opacity="{random.uniform(0.4, 0.8):.2f}"/>\n'
                svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r_var*0.35:.1f}" fill="{BG_PANEL}" opacity="0.5"/>\n'

        # Detail text at bottom
        detail_lines = s["detail"].split("\n")
        for di, dl in enumerate(detail_lines):
            svg += f'  <text x="{sx + panel_w/2}" y="{panel_y + panel_h - 20 + di*15}" text-anchor="middle" fill="{TEXT_DIM}" font-size="11">{dl}</text>\n'

    # Gradient bar at bottom
    bar_y = 395
    svg += f'  <defs><linearGradient id="spectrumGrad" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="{GREEN}"/><stop offset="50%" stop-color="{GOLD}"/><stop offset="100%" stop-color="{RED}"/></linearGradient></defs>\n'
    svg += f'  <rect x="80" y="{bar_y}" width="640" height="8" fill="url(#spectrumGrad)" rx="4"/>\n'
    svg += f'  <text x="80" y="{bar_y + 25}" fill="{GREEN}" font-size="11">Controlled</text>\n'
    svg += f'  <text x="720" y="{bar_y + 25}" text-anchor="end" fill="{RED}" font-size="11">Uncontrolled</text>\n'

    svg += svg_footer()
    return svg


# ============================================================
# Diagram 4: Why Farber Chose Leukemia (Measurability)
# ============================================================
def generate_measurability():
    w, h = 800, 520
    svg = svg_header(w, h, "Why Farber Chose Leukemia: The Measurability Advantage")

    svg += f'  <text x="{w/2}" y="40" text-anchor="middle" fill="{WHITE}" font-size="20" font-weight="700">Why Leukemia? Because You Can Count It.</text>\n'
    svg += f'  <text x="{w/2}" y="62" text-anchor="middle" fill="{TEXT_DIM}" font-size="14">Farber\'s key insight: choose the cancer you can measure</text>\n'

    # Left panel: Solid tumor (invisible)
    lx, ly = 40, 90
    pw, ph = 340, 340
    svg += f'  <rect x="{lx}" y="{ly}" width="{pw}" height="{ph}" fill="{BG_PANEL}" rx="10" stroke="{RED}" stroke-width="1.5" stroke-opacity="0.3"/>\n'
    svg += f'  <text x="{lx + pw/2}" y="{ly + 30}" text-anchor="middle" fill="{RED}" font-size="16" font-weight="600">Solid Tumor (1940s)</text>\n'

    # Body outline (simple torso)
    body_cx, body_cy = lx + pw/2, ly + 170
    svg += f'  <ellipse cx="{body_cx}" cy="{body_cy}" rx="80" ry="110" fill="none" stroke="{TEXT_DIM}" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.5"/>\n'

    # Hidden tumor inside
    svg += f'  <circle cx="{body_cx - 20}" cy="{body_cy - 20}" r="25" fill="{RED}" opacity="0.3"/>\n'
    svg += f'  <text x="{body_cx - 20}" y="{body_cy - 16}" text-anchor="middle" fill="{RED}" font-size="10" opacity="0.7">tumor</text>\n'

    # Question marks
    for qx, qy in [(body_cx + 40, body_cy - 50), (body_cx - 60, body_cy + 30), (body_cx + 50, body_cy + 20)]:
        svg += f'  <text x="{qx}" y="{qy}" text-anchor="middle" fill="{TEXT_DIM}" font-size="20" opacity="0.4">?</text>\n'

    svg += f'  <text x="{lx + pw/2}" y="{ly + ph - 35}" text-anchor="middle" fill="{TEXT_DIM}" font-size="12">No CT scans. No MRIs.</text>\n'
    svg += f'  <text x="{lx + pw/2}" y="{ly + ph - 15}" text-anchor="middle" fill="{RED}" font-size="13" font-weight="600">Can\'t see it. Can\'t measure it.</text>\n'

    # Right panel: Leukemia (visible in blood)
    rx_panel, ry = 420, 90
    svg += f'  <rect x="{rx_panel}" y="{ry}" width="{pw}" height="{ph}" fill="{BG_PANEL}" rx="10" stroke="{GREEN}" stroke-width="1.5" stroke-opacity="0.3"/>\n'
    svg += f'  <text x="{rx_panel + pw/2}" y="{ry + 30}" text-anchor="middle" fill="{GREEN}" font-size="16" font-weight="600">Leukemia (1940s)</text>\n'

    # Blood sample / microscope view — moved up to avoid label collision
    scope_cx, scope_cy = rx_panel + pw/2, ry + 150
    svg += f'  <circle cx="{scope_cx}" cy="{scope_cy}" r="80" fill="none" stroke="{GREEN}" stroke-width="2" opacity="0.4"/>\n'
    svg += f'  <text x="{scope_cx + 90}" y="{scope_cy - 65}" fill="{TEXT_DIM}" font-size="10">microscope view</text>\n'

    # Countable cells
    random.seed(77)
    cell_count = 0
    for _ in range(18):
        angle = random.uniform(0, 2 * math.pi)
        dist = random.uniform(5, 65)
        x = scope_cx + math.cos(angle) * dist
        y = scope_cy + math.sin(angle) * dist
        r = random.uniform(8, 13)
        svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{PURPLE}" opacity="0.6"/>\n'
        svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r*0.4:.1f}" fill="{BG_PANEL}" opacity="0.5"/>\n'
        cell_count += 1

    # Count label — placed below microscope circle with gap
    svg += f'  <text x="{scope_cx}" y="{scope_cy + 100}" text-anchor="middle" fill="{GREEN}" font-size="14" font-weight="600">Count = {cell_count} blast cells</text>\n'

    # Description labels — placed at bottom of panel, well below count
    svg += f'  <text x="{rx_panel + pw/2}" y="{ry + ph - 35}" text-anchor="middle" fill="{TEXT_DIM}" font-size="12">Draw blood. Look under microscope.</text>\n'
    svg += f'  <text x="{rx_panel + pw/2}" y="{ry + ph - 15}" text-anchor="middle" fill="{GREEN}" font-size="13" font-weight="600">Can see it. Can count it. Can test drugs.</text>\n'

    # Bottom insight box
    box_y = 450
    svg += f'  <rect x="100" y="{box_y}" width="600" height="50" fill="{BG_PANEL}" rx="8" stroke="{YELLOW}" stroke-width="1" stroke-opacity="0.4"/>\n'
    svg += f'  <text x="{w/2}" y="{box_y + 22}" text-anchor="middle" fill="{YELLOW}" font-size="14" font-weight="600">"Science begins with counting."</text>\n'
    svg += f'  <text x="{w/2}" y="{box_y + 40}" text-anchor="middle" fill="{TEXT_DIM}" font-size="12">Give a drug → draw blood → count cells → measure success or failure</text>\n'

    svg += svg_footer()
    return svg



# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    diagrams = [
        ("01_normal_vs_leukemic_blood.svg", generate_normal_vs_leukemic),
        ("02_hypertrophy_vs_hyperplasia.svg", generate_hypertrophy_vs_hyperplasia),
        ("03_neoplasia_spectrum.svg", generate_neoplasia_spectrum),
        ("04_measurability.svg", generate_measurability),
    ]

    for filename, gen_fn in diagrams:
        path = os.path.join(OUTPUT_DIR, filename)
        svg_content = gen_fn()
        with open(path, "w") as f:
            f.write(svg_content)
        print(f"Generated: {path}")
