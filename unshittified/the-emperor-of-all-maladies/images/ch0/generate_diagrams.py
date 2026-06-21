#!/usr/bin/env python3
"""Generate SVG diagrams for Chapter 0 (Overview) of The Emperor of All Maladies."""

import os
import math

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Color palette
BG_DARK = "#0a0e27"
BG_MID = "#131833"
TEXT_WHITE = "#e8e8e8"
TEXT_DIM = "#8892b0"
RED = "#FF6B6B"
GREEN = "#69F0AE"
GOLD = "#FFD700"
BLUE = "#4FC3F7"
PURPLE = "#B388FF"
YELLOW = "#FFEB3B"
ORANGE = "#FF9800"
PINK = "#FF80AB"
TEAL = "#26C6DA"


def generate_timeline():
    """01: 4,000-year timeline of humanity's war on cancer."""
    w, h = 1200, 520

    # Timeline milestones: (x_position_pct, label, detail, color, y_offset_direction)
    # Manually spaced to avoid overlaps
    milestones = [
        (0.03, "~2500 BC", "Imhotep describes\nbreast tumors", TEXT_DIM, -1),
        (0.11, "~400 BC", "Hippocrates names\nit 'karkinos'", RED, 1),
        (0.19, "~168 AD", "Galen: cancer =\nblack bile excess", RED, -1),
        (0.30, "1846", "Anesthesia enables\nradical surgery", ORANGE, 1),
        (0.39, "1895", "X-rays discovered:\nradiation therapy", YELLOW, -1),
        (0.48, "1943", "Mustard gas leads\nto chemotherapy", BLUE, 1),
        (0.56, "1947", "Farber's antifolates:\nfirst chemo remissions", GREEN, -1),
        (0.65, "1971", "Nixon signs the\nNational Cancer Act", PURPLE, 1),
        (0.73, "1975", "Smoking-cancer link\ndrives prevention", ORANGE, -1),
        (0.81, "1986", "Oncogenes found:\ncancer = broken genes", PINK, 1),
        (0.89, "2000", "Six Hallmarks\nof Cancer defined", GREEN, -1),
        (0.96, "2001", "Gleevec: first\ntargeted therapy", GOLD, 1),
    ]

    margin_l = 80
    margin_r = 60
    usable_w = w - margin_l - margin_r
    timeline_y = 280

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="'Segoe UI', system-ui, sans-serif">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_MID}"/>
    </linearGradient>
    <linearGradient id="lineGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{RED}" stop-opacity="0.6"/>
      <stop offset="40%" stop-color="{ORANGE}" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="{GREEN}" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="{GOLD}" stop-opacity="1"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#bgGrad)"/>

  <!-- Title -->
  <text x="{w//2}" y="40" text-anchor="middle" fill="{TEXT_WHITE}" font-size="22" font-weight="bold">4,000 Years of Cancer</text>
  <text x="{w//2}" y="62" text-anchor="middle" fill="{TEXT_DIM}" font-size="13">From humoral theory to targeted therapy</text>

  <!-- Era backgrounds -->
  <rect x="{margin_l}" y="80" width="{usable_w * 0.24}" height="16" rx="3" fill="{RED}" opacity="0.08"/>
  <rect x="{margin_l + usable_w * 0.24}" y="80" width="{usable_w * 0.20}" height="16" rx="3" fill="{ORANGE}" opacity="0.08"/>
  <rect x="{margin_l + usable_w * 0.44}" y="80" width="{usable_w * 0.24}" height="16" rx="3" fill="{BLUE}" opacity="0.08"/>
  <rect x="{margin_l + usable_w * 0.68}" y="80" width="{usable_w * 0.32}" height="16" rx="3" fill="{PURPLE}" opacity="0.08"/>

  <!-- Era labels -->
  <text x="{margin_l + usable_w * 0.12}" y="92" text-anchor="middle" fill="{RED}" font-size="10" opacity="0.8">ANCIENT ERA</text>
  <text x="{margin_l + usable_w * 0.34}" y="92" text-anchor="middle" fill="{ORANGE}" font-size="10" opacity="0.8">SURGERY + RADIATION</text>
  <text x="{margin_l + usable_w * 0.56}" y="92" text-anchor="middle" fill="{BLUE}" font-size="10" opacity="0.8">CHEMOTHERAPY</text>
  <text x="{margin_l + usable_w * 0.84}" y="92" text-anchor="middle" fill="{PURPLE}" font-size="10" opacity="0.8">MOLECULAR ERA</text>

  <!-- Era divider lines -->
  <line x1="{margin_l + usable_w * 0.24}" y1="100" x2="{margin_l + usable_w * 0.24}" y2="{timeline_y}" stroke="{TEXT_DIM}" stroke-width="0.5" stroke-dasharray="4,4" opacity="0.2"/>
  <line x1="{margin_l + usable_w * 0.44}" y1="100" x2="{margin_l + usable_w * 0.44}" y2="{timeline_y}" stroke="{TEXT_DIM}" stroke-width="0.5" stroke-dasharray="4,4" opacity="0.2"/>
  <line x1="{margin_l + usable_w * 0.68}" y1="100" x2="{margin_l + usable_w * 0.68}" y2="{timeline_y}" stroke="{TEXT_DIM}" stroke-width="0.5" stroke-dasharray="4,4" opacity="0.2"/>

  <!-- Main timeline line -->
  <line x1="{margin_l - 10}" y1="{timeline_y}" x2="{w - margin_r + 10}" y2="{timeline_y}" stroke="url(#lineGrad)" stroke-width="3" stroke-linecap="round"/>
'''

    for pct, label, detail, color, direction in milestones:
        x = margin_l + pct * usable_w
        stem_len = 68
        stem_end_y = timeline_y + direction * stem_len
        text_y = stem_end_y + direction * 4

        # Dot on timeline
        svg += f'  <circle cx="{x:.0f}" cy="{timeline_y}" r="5" fill="{color}" filter="url(#glow)"/>\n'
        # Stem
        svg += f'  <line x1="{x:.0f}" y1="{timeline_y}" x2="{x:.0f}" y2="{stem_end_y:.0f}" stroke="{color}" stroke-width="1.5" opacity="0.5"/>\n'

        # Year label
        if direction == -1:
            year_y = text_y - 2
        else:
            year_y = text_y + 12
        svg += f'  <text x="{x:.0f}" y="{year_y:.0f}" text-anchor="middle" fill="{color}" font-size="11" font-weight="bold">{label}</text>\n'

        # Detail lines
        lines = detail.split('\n')
        for i, line in enumerate(lines):
            if direction == -1:
                ly = year_y - (len(lines) - i) * 13
            else:
                ly = year_y + (i + 1) * 13
            svg += f'  <text x="{x:.0f}" y="{ly:.0f}" text-anchor="middle" fill="{TEXT_DIM}" font-size="10">{line}</text>\n'

    # Arrow at end
    ax = w - margin_r + 10
    svg += f'  <polygon points="{ax:.0f},{timeline_y - 6} {ax + 12:.0f},{timeline_y} {ax:.0f},{timeline_y + 6}" fill="{GOLD}" opacity="0.8"/>\n'

    # Bottom note
    svg += f'  <text x="{w//2}" y="{h - 30}" text-anchor="middle" fill="{TEXT_DIM}" font-size="11" font-style="italic">"Cancer is not one disease but many. And each has its own biography." </text>\n'

    svg += '</svg>'

    with open(os.path.join(OUTPUT_DIR, "01_cancer_timeline.svg"), "w") as f:
        f.write(svg)
    print("  Created 01_cancer_timeline.svg")


def generate_book_structure():
    """02: Book structure showing how the 6 parts build on each other."""
    w, h = 1100, 450

    parts = [
        ("Part I", "Origins", "Ancient history\n+ first chemo", RED, "1947"),
        ("Part II", "The War", "Political crusade\n+ combo chemo", ORANGE, "1950s-70s"),
        ("Part III", "Reckoning", "Evidence-based\nmedicine", YELLOW, "1970s-80s"),
        ("Part IV", "Prevention", "Tobacco wars\n+ screening", GREEN, "1950s-90s"),
        ("Part V", "Molecular", "Oncogenes\n+ tumor suppressors", BLUE, "1970s-2000"),
        ("Part VI", "Targeted", "Gleevec, Herceptin\n+ precision drugs", PURPLE, "2000s"),
    ]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="'Segoe UI', system-ui, sans-serif">
  <defs>
    <linearGradient id="bgGrad2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_MID}"/>
    </linearGradient>
    <filter id="glow2">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#bgGrad2)"/>

  <!-- Title -->
  <text x="{w//2}" y="38" text-anchor="middle" fill="{TEXT_WHITE}" font-size="22" font-weight="bold">Book Structure: Six Fronts of the Cancer War</text>
  <text x="{w//2}" y="58" text-anchor="middle" fill="{TEXT_DIM}" font-size="13">Each part opens a new front while earlier battles continue</text>
'''

    box_w = 145
    box_h = 185
    gap = 20
    total_w = len(parts) * box_w + (len(parts) - 1) * gap
    start_x = (w - total_w) / 2
    box_y = 85

    for i, (part_label, title, detail, color, era) in enumerate(parts):
        x = start_x + i * (box_w + gap)

        # Box with rounded corners
        svg += f'  <rect x="{x:.0f}" y="{box_y}" width="{box_w}" height="{box_h}" rx="10" fill="{BG_MID}" stroke="{color}" stroke-width="2" opacity="0.9"/>\n'

        # Colored top accent bar
        svg += f'  <rect x="{x:.0f}" y="{box_y}" width="{box_w}" height="4" rx="2" fill="{color}"/>\n'

        # Part label
        svg += f'  <text x="{x + box_w/2:.0f}" y="{box_y + 28}" text-anchor="middle" fill="{color}" font-size="12" font-weight="bold">{part_label}</text>\n'

        # Title
        svg += f'  <text x="{x + box_w/2:.0f}" y="{box_y + 55}" text-anchor="middle" fill="{TEXT_WHITE}" font-size="18" font-weight="bold">{title}</text>\n'

        # Separator line
        svg += f'  <line x1="{x + 15:.0f}" y1="{box_y + 68}" x2="{x + box_w - 15:.0f}" y2="{box_y + 68}" stroke="{color}" stroke-width="0.5" opacity="0.4"/>\n'

        # Detail text
        lines = detail.split('\n')
        for j, line in enumerate(lines):
            svg += f'  <text x="{x + box_w/2:.0f}" y="{box_y + 90 + j * 16}" text-anchor="middle" fill="{TEXT_DIM}" font-size="11">{line}</text>\n'

        # Era label at bottom
        svg += f'  <text x="{x + box_w/2:.0f}" y="{box_y + box_h - 12}" text-anchor="middle" fill="{color}" font-size="10" opacity="0.6">{era}</text>\n'

        # Arrow to next box
        if i < len(parts) - 1:
            ax = x + box_w + 2
            ay = box_y + box_h / 2
            svg += f'  <line x1="{ax:.0f}" y1="{ay:.0f}" x2="{ax + gap - 4:.0f}" y2="{ay:.0f}" stroke="{TEXT_DIM}" stroke-width="1.5" opacity="0.5"/>\n'
            svg += f'  <polygon points="{ax + gap - 4:.0f},{ay - 4:.0f} {ax + gap + 2:.0f},{ay:.0f} {ax + gap - 4:.0f},{ay + 4:.0f}" fill="{TEXT_DIM}" opacity="0.5"/>\n'

    # Carla Reed thread running underneath
    thread_y = box_y + box_h + 40
    svg += f'  <line x1="{start_x:.0f}" y1="{thread_y}" x2="{start_x + total_w:.0f}" y2="{thread_y}" stroke="{PINK}" stroke-width="2" stroke-dasharray="8,4" opacity="0.6"/>\n'

    # Dots along the thread
    for i in range(len(parts)):
        dx = start_x + i * (box_w + gap) + box_w / 2
        svg += f'  <circle cx="{dx:.0f}" cy="{thread_y}" r="4" fill="{PINK}" opacity="0.8"/>\n'

    # Vertical connectors from boxes to thread
    for i in range(len(parts)):
        dx = start_x + i * (box_w + gap) + box_w / 2
        svg += f'  <line x1="{dx:.0f}" y1="{box_y + box_h}" x2="{dx:.0f}" y2="{thread_y}" stroke="{PINK}" stroke-width="1" stroke-dasharray="3,3" opacity="0.3"/>\n'

    svg += f'  <text x="{start_x - 10:.0f}" y="{thread_y + 5}" text-anchor="end" fill="{PINK}" font-size="12" font-weight="bold">Carla Reed</text>\n'
    svg += f'  <text x="{start_x - 10:.0f}" y="{thread_y + 20}" text-anchor="end" fill="{TEXT_DIM}" font-size="10">present-day patient thread</text>\n'

    svg += '</svg>'

    with open(os.path.join(OUTPUT_DIR, "02_book_structure.svg"), "w") as f:
        f.write(svg)
    print("  Created 02_book_structure.svg")


def generate_hallmarks():
    """03: The Six Hallmarks of Cancer, radial diagram."""
    w, h = 900, 900

    hallmarks = [
        ("Self-Sufficient\nGrowth", "Oncogenes (ras, myc)\njam the accelerator ON", GREEN),
        ("Ignoring\nStop Signals", "Tumor suppressors (Rb)\nare knocked out", RED),
        ("Evading\nCell Death", "Apoptosis pathways\nare disabled", ORANGE),
        ("Unlimited\nReplication", "Telomerase keeps cells\nimmortally dividing", PURPLE),
        ("Growing\nBlood Vessels", "Tumors recruit their\nown blood supply", BLUE),
        ("Invasion &amp;\nMetastasis", "Cells migrate, colonize\ndistant organs", PINK),
    ]

    cx, cy = w // 2, h // 2 + 20
    radius = 280

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="'Segoe UI', system-ui, sans-serif">
  <defs>
    <linearGradient id="bgGrad3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_MID}"/>
    </linearGradient>
    <filter id="glow3">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <radialGradient id="centerGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{GOLD}" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="{GOLD}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#bgGrad3)"/>

  <!-- Title -->
  <text x="{w//2}" y="45" text-anchor="middle" fill="{TEXT_WHITE}" font-size="24" font-weight="bold">The Six Hallmarks of Cancer</text>
  <text x="{w//2}" y="70" text-anchor="middle" fill="{TEXT_DIM}" font-size="14">Weinberg &amp; Hanahan, 2000: six rules governing all cancers</text>

  <!-- Center glow -->
  <circle cx="{cx}" cy="{cy}" r="130" fill="url(#centerGlow)"/>

  <!-- Center circle -->
  <circle cx="{cx}" cy="{cy}" r="70" fill="{BG_MID}" stroke="{GOLD}" stroke-width="2" opacity="0.9"/>
  <text x="{cx}" y="{cy - 12}" text-anchor="middle" fill="{GOLD}" font-size="16" font-weight="bold">CANCER</text>
  <text x="{cx}" y="{cy + 8}" text-anchor="middle" fill="{TEXT_DIM}" font-size="11">Normal cells</text>
  <text x="{cx}" y="{cy + 22}" text-anchor="middle" fill="{TEXT_DIM}" font-size="11">gone wrong</text>
'''

    for i, (title, detail, color) in enumerate(hallmarks):
        angle = -math.pi / 2 + i * (2 * math.pi / 6)
        # Node position
        nx = cx + radius * math.cos(angle)
        ny = cy + radius * math.sin(angle)

        # Inner connection point
        ix = cx + 75 * math.cos(angle)
        iy = cy + 75 * math.sin(angle)

        # Line from center to node
        svg += f'  <line x1="{ix:.0f}" y1="{iy:.0f}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="{color}" stroke-width="2" opacity="0.3"/>\n'

        # Outer circle
        svg += f'  <circle cx="{nx:.0f}" cy="{ny:.0f}" r="58" fill="{BG_MID}" stroke="{color}" stroke-width="2.5" filter="url(#glow3)"/>\n'

        # Number badge
        badge_angle = angle - 0.35
        bx = nx + 50 * math.cos(badge_angle)
        by = ny + 50 * math.sin(badge_angle)
        svg += f'  <circle cx="{bx:.0f}" cy="{by:.0f}" r="14" fill="{color}"/>\n'
        svg += f'  <text x="{bx:.0f}" y="{by + 5:.0f}" text-anchor="middle" fill="{BG_DARK}" font-size="14" font-weight="bold">{i+1}</text>\n'

        # Title inside circle
        title_lines = title.split('\n')
        for j, line in enumerate(title_lines):
            ty = ny - 6 + j * 16
            svg += f'  <text x="{nx:.0f}" y="{ty:.0f}" text-anchor="middle" fill="{TEXT_WHITE}" font-size="12" font-weight="bold">{line}</text>\n'

        # Detail text outside circle
        detail_lines = detail.split('\n')
        detail_offset = 75
        for j, line in enumerate(detail_lines):
            dx = cx + (radius + detail_offset) * math.cos(angle)
            dy = cy + (radius + detail_offset) * math.sin(angle) - 6 + j * 14
            svg += f'  <text x="{dx:.0f}" y="{dy:.0f}" text-anchor="middle" fill="{TEXT_DIM}" font-size="10">{line}</text>\n'

    # Connecting arcs between adjacent hallmarks
    for i in range(6):
        angle1 = -math.pi / 2 + i * (2 * math.pi / 6)
        angle2 = -math.pi / 2 + ((i + 1) % 6) * (2 * math.pi / 6)
        x1 = cx + (radius - 25) * math.cos(angle1 + 0.18)
        y1 = cy + (radius - 25) * math.sin(angle1 + 0.18)
        x2 = cx + (radius - 25) * math.cos(angle2 - 0.18)
        y2 = cy + (radius - 25) * math.sin(angle2 - 0.18)
        svg += f'  <line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{TEXT_DIM}" stroke-width="0.5" stroke-dasharray="3,3" opacity="0.2"/>\n'

    # Bottom note
    svg += f'  <text x="{w//2}" y="{h - 25}" text-anchor="middle" fill="{TEXT_DIM}" font-size="11" font-style="italic">"A distorted version of our normal selves"</text>\n'

    svg += '</svg>'

    with open(os.path.join(OUTPUT_DIR, "03_hallmarks_of_cancer.svg"), "w") as f:
        f.write(svg)
    print("  Created 03_hallmarks_of_cancer.svg")


if __name__ == "__main__":
    print("Generating Chapter 0 diagrams...")
    generate_timeline()
    generate_book_structure()
    generate_hallmarks()
    print("Done!")
