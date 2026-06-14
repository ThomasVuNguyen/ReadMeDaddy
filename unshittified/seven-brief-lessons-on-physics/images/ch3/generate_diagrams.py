#!/usr/bin/env python3
"""Generate SVG diagrams for Chapter 3: The Architecture of the Cosmos."""

import math
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def save(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"Saved: {path}")


# --- DIAGRAM 1: Cosmic Zoom Timeline -----------------------------------------

def cosmic_zoom():
    """Timeline showing how our view of the cosmos kept expanding."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 400" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="900" height="400" fill="url(#bg)" rx="12"/>

  <text x="450" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">HOW OUR VIEW KEPT EXPANDING</text>
  <text x="450" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">Each revolution made us smaller</text>

  <!-- Timeline line -->
  <line x1="60" y1="200" x2="840" y2="200" stroke="#ffffff20" stroke-width="2"/>
"""
    stages = [
        (100, "Ancient", "~3000 BC", "Flat Earth,\nsky above", "#FF6B6B", 25),
        (260, "Anaximander", "~600 BC", "Earth floats\nin space", "#FFD700", 35),
        (420, "Copernicus", "1543", "Sun at center,\nEarth orbits", "#4FC3F7", 50),
        (580, "Milky Way", "1920s", "Sun is one of\nbillions of stars", "#B388FF", 70),
        (740, "Modern", "1990s+", "Billions of\ngalaxies, expanding", "#69F0AE", 95),
    ]

    for x, label, date, desc, color, radius in stages:
        # Circle (growing bigger for each stage)
        svg += f'  <circle cx="{x}" cy="200" r="{radius}" fill="{color}10" stroke="{color}" stroke-width="1.5" opacity="0.7"/>\n'
        # Dot on timeline
        svg += f'  <circle cx="{x}" cy="200" r="5" fill="{color}"/>\n'
        # Label above
        svg += f'  <text x="{x}" y="{200 - radius - 20}" text-anchor="middle" fill="{color}" font-size="14" font-weight="bold">{label}</text>\n'
        svg += f'  <text x="{x}" y="{200 - radius - 6}" text-anchor="middle" fill="#ffffff50" font-size="10">{date}</text>\n'
        # Description below
        lines = desc.split("\n")
        for i, line in enumerate(lines):
            svg += f'  <text x="{x}" y="{200 + radius + 20 + i * 16}" text-anchor="middle" fill="#ffffff60" font-size="11">{line}</text>\n'

    # Arrows between stages
    for i in range(len(stages) - 1):
        x1 = stages[i][0] + stages[i][5] + 8
        x2 = stages[i+1][0] - stages[i+1][5] - 8
        svg += f'  <line x1="{x1}" y1="200" x2="{x2}" y2="200" stroke="#ffffff30" stroke-width="1.5" marker-end="url(#arr)"/>\n'

    svg += """
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#ffffff30"/>
    </marker>
  </defs>

  <!-- Bottom: the punchline -->
  <text x="450" y="380" text-anchor="middle" fill="#ffffff40" font-size="12">Each step: what we thought was everything turned out to be a speck inside something bigger.</text>

</svg>"""
    save("01_cosmic_zoom.svg", svg)


# --- DIAGRAM 2: Expanding Universe (Raisin Bread) ----------------------------

def expanding_universe():
    """Space itself stretching, carrying galaxies apart."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="380" fill="url(#bg2)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">THE EXPANDING UNIVERSE</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">Space itself stretches, carrying galaxies apart</text>

  <!-- Divider -->
  <line x1="400" y1="70" x2="400" y2="340" stroke="#ffffff15" stroke-width="2" stroke-dasharray="8,6"/>

  <!-- Left: Earlier (smaller, galaxies closer) -->
  <text x="200" y="85" text-anchor="middle" fill="#4FC3F7" font-size="16" font-weight="bold">EARLIER</text>
  <text x="200" y="103" text-anchor="middle" fill="#ffffff40" font-size="11">Universe was smaller</text>
"""
    # Draw a small grid with galaxies close together
    import random
    random.seed(77)
    # Grid lines (small)
    for i in range(8):
        x = 90 + i * 30
        svg += f'  <line x1="{x}" y1="120" x2="{x}" y2="300" stroke="#ffffff08" stroke-width="1"/>\n'
    for i in range(7):
        y = 120 + i * 30
        svg += f'  <line x1="90" y1="{y}" x2="300" y2="{y}" stroke="#ffffff08" stroke-width="1"/>\n'

    # Galaxies (close together)
    gals_left = [(130, 160), (180, 150), (240, 190), (150, 240), (220, 260), (270, 170), (120, 200)]
    for gx, gy in gals_left:
        svg += f'  <circle cx="{gx}" cy="{gy}" r="6" fill="#FFD700" opacity="0.7"/>\n'
        svg += f'  <circle cx="{gx}" cy="{gy}" r="12" fill="#FFD700" opacity="0.08"/>\n'

    svg += """
  <!-- Right: Now (larger, galaxies farther apart) -->
  <text x="600" y="85" text-anchor="middle" fill="#69F0AE" font-size="16" font-weight="bold">NOW</text>
  <text x="600" y="103" text-anchor="middle" fill="#ffffff40" font-size="11">Space has stretched</text>
"""
    # Draw a larger grid with galaxies spread out
    for i in range(8):
        x = 440 + i * 42
        svg += f'  <line x1="{x}" y1="115" x2="{x}" y2="310" stroke="#ffffff08" stroke-width="1"/>\n'
    for i in range(6):
        y = 115 + i * 42
        svg += f'  <line x1="440" y1="{y}" x2="734" y2="{y}" stroke="#ffffff08" stroke-width="1"/>\n'

    # Same galaxies but spread out (multiplied distances from center)
    center = (600, 210)
    for gx, gy in gals_left:
        # Scale from center of left group to center of right group
        dx = (gx - 190) * 1.8
        dy = (gy - 210) * 1.5
        nx = center[0] + dx
        ny = center[1] + dy
        svg += f'  <circle cx="{nx:.0f}" cy="{ny:.0f}" r="6" fill="#FFD700" opacity="0.7"/>\n'
        svg += f'  <circle cx="{nx:.0f}" cy="{ny:.0f}" r="12" fill="#FFD700" opacity="0.08"/>\n'

    svg += """
  <!-- Arrow between -->
  <text x="400" y="215" text-anchor="middle" fill="#fff" font-size="28">→</text>

  <!-- Key insight -->
  <text x="400" y="348" text-anchor="middle" fill="#ffffff50" font-size="12">The galaxies aren't moving through space. Space itself is expanding, carrying them apart.</text>
  <text x="400" y="368" text-anchor="middle" fill="#ffffff40" font-size="11">Run it backward → everything converges → the Big Bang.</text>

</svg>"""
    save("02_expanding_universe.svg", svg)


# --- DIAGRAM 3: Observable Universe / Light Horizon ---------------------------

def observable_universe():
    """Our cosmic horizon: we can only see as far as light has traveled."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 500" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#4FC3F7" stop-opacity="0.15"/>
      <stop offset="70%" stop-color="#4FC3F7" stop-opacity="0.03"/>
      <stop offset="100%" stop-color="#4FC3F7" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="700" height="500" fill="url(#bg3)" rx="12"/>

  <text x="350" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">THE OBSERVABLE UNIVERSE</text>
  <text x="350" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">We can only see as far as light has had time to travel</text>
"""
    cx, cy = 350, 265

    # Outer ring: CMB (cosmic microwave background)
    svg += f'  <circle cx="{cx}" cy="{cy}" r="200" fill="none" stroke="#FF6B6B" stroke-width="2" stroke-dasharray="4,4" opacity="0.5"/>\n'
    svg += f'  <text x="{cx + 145}" y="{cy - 145}" fill="#FF6B6B" font-size="10" transform="rotate(45, {cx + 145}, {cy - 145})">Cosmic Microwave Background</text>\n'

    # Observable sphere glow
    svg += f'  <circle cx="{cx}" cy="{cy}" r="180" fill="url(#glow)"/>\n'

    # Inner regions
    svg += f'  <circle cx="{cx}" cy="{cy}" r="120" fill="none" stroke="#ffffff10" stroke-width="1" stroke-dasharray="3,5"/>\n'
    svg += f'  <text x="{cx}" y="{cy - 128}" text-anchor="middle" fill="#ffffff30" font-size="10">Distant galaxies</text>\n'

    svg += f'  <circle cx="{cx}" cy="{cy}" r="60" fill="none" stroke="#ffffff10" stroke-width="1" stroke-dasharray="3,5"/>\n'
    svg += f'  <text x="{cx}" y="{cy - 65}" text-anchor="middle" fill="#ffffff30" font-size="10">Local group</text>\n'

    # Us at center
    svg += f'  <circle cx="{cx}" cy="{cy}" r="5" fill="#4FC3F7"/>\n'
    svg += f'  <text x="{cx}" y="{cy + 18}" text-anchor="middle" fill="#4FC3F7" font-size="11" font-weight="bold">Us</text>\n'

    # Scatter some galaxies
    import random
    random.seed(55)
    for _ in range(80):
        angle = random.uniform(0, 2 * math.pi)
        r = random.uniform(20, 170)
        gx = cx + r * math.cos(angle)
        gy = cy + r * math.sin(angle)
        opacity = max(0.1, 0.5 - r / 300)
        size = random.uniform(1.5, 3)
        svg += f'  <circle cx="{gx:.0f}" cy="{gy:.0f}" r="{size:.1f}" fill="#FFD700" opacity="{opacity:.2f}"/>\n'

    # Beyond the edge: question marks
    for angle_deg in [30, 80, 150, 210, 280, 340]:
        angle = math.radians(angle_deg)
        qx = cx + 215 * math.cos(angle)
        qy = cy + 215 * math.sin(angle)
        svg += f'  <text x="{qx:.0f}" y="{qy:.0f}" text-anchor="middle" fill="#ffffff20" font-size="14">?</text>\n'

    # Radius label
    svg += f'  <line x1="{cx}" y1="{cy}" x2="{cx + 200}" y2="{cy}" stroke="#69F0AE" stroke-width="1" stroke-dasharray="4,3" opacity="0.5"/>\n'
    svg += f'  <text x="{cx + 100}" y="{cy - 8}" text-anchor="middle" fill="#69F0AE" font-size="10">~14 billion light-years</text>\n'

    svg += f"""
  <!-- Labels -->
  <rect x="40" y="430" width="620" height="55" fill="#ffffff06" rx="6"/>
  <text x="350" y="450" text-anchor="middle" fill="#ffffff60" font-size="12">Light travels at a finite speed. The universe has a finite age (~14 billion years).</text>
  <text x="350" y="468" text-anchor="middle" fill="#ffffff60" font-size="12">So we can only see objects whose light has had time to reach us. Beyond the edge: more universe, invisible to us.</text>

</svg>"""
    save("03_observable_universe.svg", svg)


# --- DIAGRAM 4: Dark Matter / Dark Energy Pie Chart ---------------------------

def dark_universe():
    """The universe's composition: 5% normal matter, 25% dark matter, 70% dark energy."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 420" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg4" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="700" height="420" fill="url(#bg4)" rx="12"/>

  <text x="350" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">WHAT THE UNIVERSE IS MADE OF</text>
  <text x="350" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">We only understand 5% of it</text>
"""
    cx, cy = 280, 230
    r = 140

    # Pie slices: dark energy (70%), dark matter (25%), normal matter (5%)
    slices = [
        (0.70, "#B388FF", "Dark Energy", "~70%"),
        (0.25, "#FF6B6B", "Dark Matter", "~25%"),
        (0.05, "#FFD700", "Normal Matter", "~5%"),
    ]

    start_angle = -math.pi / 2  # Start from top
    for frac, color, label, pct in slices:
        end_angle = start_angle + 2 * math.pi * frac
        # SVG arc
        x1 = cx + r * math.cos(start_angle)
        y1 = cy + r * math.sin(start_angle)
        x2 = cx + r * math.cos(end_angle)
        y2 = cy + r * math.sin(end_angle)
        large_arc = 1 if frac > 0.5 else 0

        svg += f'  <path d="M {cx} {cy} L {x1:.1f} {y1:.1f} A {r} {r} 0 {large_arc} 1 {x2:.1f} {y2:.1f} Z" fill="{color}" opacity="0.25" stroke="{color}" stroke-width="2"/>\n'

        # Label at midpoint of arc
        mid_angle = start_angle + math.pi * frac
        lx = cx + (r + 25) * math.cos(mid_angle)
        ly = cy + (r + 25) * math.sin(mid_angle)
        svg += f'  <text x="{lx:.0f}" y="{ly:.0f}" text-anchor="middle" fill="{color}" font-size="13" font-weight="bold">{pct}</text>\n'

        start_angle = end_angle

    # Legend on the right
    legend_items = [
        ("#B388FF", "Dark Energy (~70%)", "Mysterious force accelerating\nthe expansion of space.\nWe have no idea what it is."),
        ("#FF6B6B", "Dark Matter (~25%)", "Invisible, detectable only\nthrough its gravity.\nUnknown composition."),
        ("#FFD700", "Normal Matter (~5%)", "Stars, planets, gas, us.\nEverything we can see\nand touch."),
    ]

    ly = 110
    for color, title, desc in legend_items:
        svg += f'  <rect x="470" y="{ly}" width="16" height="16" fill="{color}" opacity="0.5" rx="3"/>\n'
        svg += f'  <text x="495" y="{ly + 13}" fill="{color}" font-size="13" font-weight="bold">{title}</text>\n'
        for i, line in enumerate(desc.split("\n")):
            svg += f'  <text x="495" y="{ly + 30 + i * 15}" fill="#ffffff50" font-size="11">{line}</text>\n'
        ly += 90

    svg += """
  <!-- Punchline -->
  <text x="350" y="405" text-anchor="middle" fill="#ffffff40" font-size="12">95% of the universe is stuff we can't see, can't touch, and can't explain.</text>

</svg>"""
    save("04_dark_universe.svg", svg)


# --- Run all ------------------------------------------------------------------

if __name__ == "__main__":
    cosmic_zoom()
    expanding_universe()
    observable_universe()
    dark_universe()
    print("\nAll Chapter 3 diagrams generated!")
