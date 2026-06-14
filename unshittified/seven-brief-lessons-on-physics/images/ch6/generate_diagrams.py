#!/usr/bin/env python3
"""Generate SVG diagrams for Chapter 6: Probability, Time, and the Heat of Black Holes."""

import math
import os
import random

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def save(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"Saved: {path}")


# --- DIAGRAM 1: What is Heat? ------------------------------------------------

def what_is_heat():
    """Hot = fast atoms, cold = slow atoms."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 350" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="350" fill="url(#bg)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">WHAT IS HEAT?</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">Nothing more than atoms moving</text>

  <line x1="400" y1="70" x2="400" y2="310" stroke="#ffffff15" stroke-width="2" stroke-dasharray="8,6"/>

  <!-- Cold side -->
  <text x="200" y="85" text-anchor="middle" fill="#4FC3F7" font-size="16" font-weight="bold">COLD</text>
  <text x="200" y="103" text-anchor="middle" fill="#ffffff40" font-size="11">Atoms barely moving</text>

  <rect x="60" y="115" width="280" height="180" fill="#4FC3F710" rx="8" stroke="#4FC3F720" stroke-width="1"/>
"""
    random.seed(33)
    # Cold atoms: small velocities
    for _ in range(25):
        x = random.randint(80, 320)
        y = random.randint(130, 275)
        # Short velocity arrow
        angle = random.uniform(0, 2 * math.pi)
        vx = 5 * math.cos(angle)
        vy = 5 * math.sin(angle)
        svg += f'  <circle cx="{x}" cy="{y}" r="5" fill="#4FC3F7" opacity="0.5"/>\n'
        svg += f'  <line x1="{x}" y1="{y}" x2="{x + vx:.0f}" y2="{y + vy:.0f}" stroke="#4FC3F7" stroke-width="1" opacity="0.3"/>\n'

    svg += """
  <text x="200" y="320" text-anchor="middle" fill="#4FC3F780" font-size="11">Slow atoms = cold substance</text>

  <!-- Hot side -->
  <text x="600" y="85" text-anchor="middle" fill="#FF6B6B" font-size="16" font-weight="bold">HOT</text>
  <text x="600" y="103" text-anchor="middle" fill="#ffffff40" font-size="11">Atoms flying around</text>

  <rect x="460" y="115" width="280" height="180" fill="#FF6B6B10" rx="8" stroke="#FF6B6B20" stroke-width="1"/>
"""
    # Hot atoms: large velocities
    for _ in range(25):
        x = random.randint(480, 720)
        y = random.randint(130, 275)
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(15, 30)
        vx = speed * math.cos(angle)
        vy = speed * math.sin(angle)
        svg += f'  <circle cx="{x}" cy="{y}" r="5" fill="#FF6B6B" opacity="0.5"/>\n'
        svg += f'  <line x1="{x}" y1="{y}" x2="{x + vx:.0f}" y2="{y + vy:.0f}" stroke="#FF6B6B" stroke-width="1.5" opacity="0.4"/>\n'

    svg += """
  <text x="600" y="320" text-anchor="middle" fill="#FF6B6B80" font-size="11">Fast atoms = hot substance</text>
  <text x="400" y="345" text-anchor="middle" fill="#ffffff40" font-size="11">That's it. That's the whole secret. Temperature is just average atomic speed.</text>

</svg>"""
    save("01_what_is_heat.svg", svg)


# --- DIAGRAM 2: Why Heat Flows One Way (Entropy) -----------------------------

def entropy():
    """Heat flows from hot to cold because the reverse is astronomically unlikely."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg2)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">WHY DOES HEAT FLOW ONE WAY?</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">Not because it must, but because the reverse is absurdly unlikely</text>

  <!-- Before: hot + cold -->
  <text x="200" y="90" text-anchor="middle" fill="#fff" font-size="14" font-weight="bold">BEFORE</text>

  <rect x="60" y="105" width="120" height="100" fill="#FF6B6B15" stroke="#FF6B6B40" stroke-width="1" rx="6"/>
  <text x="120" y="165" text-anchor="middle" fill="#FF6B6B" font-size="12">HOT</text>

  <rect x="220" y="105" width="120" height="100" fill="#4FC3F715" stroke="#4FC3F740" stroke-width="1" rx="6"/>
  <text x="280" y="165" text-anchor="middle" fill="#4FC3F7" font-size="12">COLD</text>

  <!-- Arrow -->
  <text x="200" y="238" text-anchor="middle" fill="#ffffff30" font-size="24">↓</text>

  <!-- After: lukewarm + lukewarm -->
  <text x="200" y="275" text-anchor="middle" fill="#fff" font-size="14" font-weight="bold">AFTER</text>

  <rect x="60" y="290" width="120" height="75" fill="#FFD70015" stroke="#FFD70040" stroke-width="1" rx="6"/>
  <text x="120" y="335" text-anchor="middle" fill="#FFD700" font-size="12">WARM</text>

  <rect x="220" y="290" width="120" height="75" fill="#FFD70015" stroke="#FFD70040" stroke-width="1" rx="6"/>
  <text x="280" y="335" text-anchor="middle" fill="#FFD700" font-size="12">WARM</text>

  <!-- Right side: probability explanation -->
  <rect x="420" y="80" width="350" height="290" fill="#ffffff06" rx="8" stroke="#ffffff10" stroke-width="1"/>
  <text x="595" y="110" text-anchor="middle" fill="#B388FF" font-size="15" font-weight="bold">BOLTZMANN'S INSIGHT</text>

  <text x="440" y="145" fill="#ffffff60" font-size="12">There are VASTLY more ways to arrange</text>
  <text x="440" y="163" fill="#ffffff60" font-size="12">atoms with energy spread evenly than with</text>
  <text x="440" y="181" fill="#ffffff60" font-size="12">energy concentrated in one spot.</text>

  <text x="440" y="215" fill="#69F0AE" font-size="12" font-weight="bold">Ways to be "mixed": ~10²³⁰⁰⁰⁰⁰⁰⁰⁰⁰⁰⁰⁰⁰⁰⁰⁰⁰⁰⁰⁰</text>
  <text x="440" y="240" fill="#FF6B6B" font-size="12" font-weight="bold">Ways to be "separated": ~1</text>

  <text x="440" y="275" fill="#ffffff50" font-size="12">It's not forbidden for heat to flow</text>
  <text x="440" y="293" fill="#ffffff50" font-size="12">backward. It's just that the odds</text>
  <text x="440" y="311" fill="#ffffff50" font-size="12">against it have more zeroes than there</text>
  <text x="440" y="329" fill="#ffffff50" font-size="12">are atoms in the observable universe.</text>

  <text x="595" y="360" text-anchor="middle" fill="#B388FF80" font-size="11">The second law of thermodynamics is a bet, not a law.</text>

</svg>"""
    save("02_entropy.svg", svg)


# --- DIAGRAM 3: The Arrow of Time --------------------------------------------

def arrow_of_time():
    """Time's direction comes from heat and probability, not fundamental physics."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="380" fill="url(#bg3)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">WHERE DOES TIME'S ARROW COME FROM?</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">The fundamental equations don't care which direction time runs</text>
"""
    # Two panels: reversible vs irreversible
    # Top: reversible
    svg += '  <rect x="50" y="75" width="700" height="110" fill="#69F0AE08" rx="8" stroke="#69F0AE20" stroke-width="1"/>\n'
    svg += '  <text x="70" y="100" fill="#69F0AE" font-size="14" font-weight="bold">TIME-REVERSIBLE (no heat involved)</text>\n'

    # Bouncing ball forward
    svg += '  <text x="110" y="130" text-anchor="middle" fill="#ffffff40" font-size="10">Forward</text>\n'
    for i, x_pos in enumerate([80, 120, 160, 200, 240]):
        h = [30, 20, 10, 20, 30][i]
        svg += f'  <circle cx="{x_pos}" cy="{170 - h}" r="6" fill="#69F0AE" opacity="0.5"/>\n'
    svg += '  <line x1="80" y1="175" x2="250" y2="175" stroke="#ffffff15" stroke-width="1"/>\n'

    # Equals sign
    svg += '  <text x="310" y="155" text-anchor="middle" fill="#69F0AE" font-size="20">=</text>\n'

    # Bouncing ball backward (looks the same)
    svg += '  <text x="410" y="130" text-anchor="middle" fill="#ffffff40" font-size="10">Backward</text>\n'
    for i, x_pos in enumerate([380, 420, 460, 500, 540]):
        h = [30, 20, 10, 20, 30][i]
        svg += f'  <circle cx="{x_pos}" cy="{170 - h}" r="6" fill="#69F0AE" opacity="0.5"/>\n'
    svg += '  <line x1="380" y1="175" x2="550" y2="175" stroke="#ffffff15" stroke-width="1"/>\n'

    svg += '  <text x="680" y="155" fill="#69F0AE80" font-size="11">Looks identical</text>\n'
    svg += '  <text x="680" y="172" fill="#69F0AE80" font-size="11">either way</text>\n'

    # Bottom: irreversible (heat involved)
    svg += '  <rect x="50" y="200" width="700" height="110" fill="#FF6B6B08" rx="8" stroke="#FF6B6B20" stroke-width="1"/>\n'
    svg += '  <text x="70" y="225" fill="#FF6B6B" font-size="14" font-weight="bold">IRREVERSIBLE (heat involved)</text>\n'

    # Egg breaking forward
    svg += '  <text x="120" y="255" text-anchor="middle" fill="#ffffff40" font-size="10">Forward</text>\n'
    svg += '  <ellipse cx="90" cy="280" rx="12" ry="16" fill="#FFD700" opacity="0.4"/>\n'
    svg += '  <text x="140" y="285" fill="#ffffff30" font-size="16">→</text>\n'
    # Broken egg
    for pos in [(170, 275), (190, 280), (185, 270), (175, 285), (195, 275)]:
        svg += f'  <circle cx="{pos[0]}" cy="{pos[1]}" r="4" fill="#FFD700" opacity="0.3"/>\n'

    # Not equals
    svg += '  <text x="310" y="285" text-anchor="middle" fill="#FF6B6B" font-size="20">≠</text>\n'

    # Egg unbreaking backward (absurd)
    svg += '  <text x="420" y="255" text-anchor="middle" fill="#ffffff40" font-size="10">Backward</text>\n'
    for pos in [(390, 275), (410, 280), (405, 270), (395, 285), (415, 275)]:
        svg += f'  <circle cx="{pos[0]}" cy="{pos[1]}" r="4" fill="#FFD700" opacity="0.3"/>\n'
    svg += '  <text x="450" y="285" fill="#ffffff30" font-size="16">→</text>\n'
    svg += '  <ellipse cx="490" cy="280" rx="12" ry="16" fill="#FFD700" opacity="0.4"/>\n'
    svg += '  <text x="505" y="285" fill="#FF6B6B" font-size="14">?!</text>\n'

    svg += '  <text x="680" y="275" fill="#FF6B6B80" font-size="11">This NEVER</text>\n'
    svg += '  <text x="680" y="292" fill="#FF6B6B80" font-size="11">happens</text>\n'

    # Bottom: punchline
    svg += '  <rect x="50" y="325" width="700" height="40" fill="#ffffff06" rx="6"/>\n'
    svg += '  <text x="400" y="350" text-anchor="middle" fill="#B388FF" font-size="13">The arrow of time = the direction entropy increases = the direction heat flows.</text>\n'

    svg += "\n</svg>"
    save("03_arrow_of_time.svg", svg)


# --- DIAGRAM 4: The Rosetta Stone (Three Pillars Meet) ------------------------

def rosetta_stone():
    """Black hole heat sits at the intersection of QM, GR, and thermodynamics."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 450" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg4" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="700" height="450" fill="url(#bg4)" rx="12"/>

  <text x="350" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">THE ROSETTA STONE OF PHYSICS</text>
  <text x="350" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">Hawking radiation: where all three pillars meet</text>
"""
    # Three overlapping circles (Venn diagram)
    cx, cy = 350, 240
    r = 120
    offset = 80

    circles = [
        (cx, cy - offset, "#B388FF", "QUANTUM\nMECHANICS", "The radiation is\na quantum effect"),
        (cx - offset * 0.87, cy + offset * 0.5, "#69F0AE", "GENERAL\nRELATIVITY", "The black hole is\na spacetime object"),
        (cx + offset * 0.87, cy + offset * 0.5, "#FF6B6B", "THERMO-\nDYNAMICS", "It produces\nheat"),
    ]

    for x, y, color, label, desc in circles:
        svg += f'  <circle cx="{x}" cy="{y}" r="{r}" fill="{color}" fill-opacity="0.08" stroke="{color}" stroke-width="2" stroke-opacity="0.3"/>\n'
        lines = label.split("\n")
        for i, line in enumerate(lines):
            svg += f'  <text x="{x}" y="{y - 30 + i * 18}" text-anchor="middle" fill="{color}" font-size="14" font-weight="bold">{line}</text>\n'
        dlines = desc.split("\n")
        for i, line in enumerate(dlines):
            svg += f'  <text x="{x}" y="{y + 10 + i * 15}" text-anchor="middle" fill="{color}80" font-size="10">{line}</text>\n'

    # Center: HAWKING RADIATION
    svg += f'  <circle cx="{cx}" cy="{cy}" r="30" fill="#FFD700" opacity="0.1"/>\n'
    svg += f'  <text x="{cx}" y="{cy - 5}" text-anchor="middle" fill="#FFD700" font-size="11" font-weight="bold">HAWKING</text>\n'
    svg += f'  <text x="{cx}" y="{cy + 10}" text-anchor="middle" fill="#FFD700" font-size="11" font-weight="bold">RADIATION</text>\n'

    svg += """
  <!-- Punchline -->
  <text x="350" y="420" text-anchor="middle" fill="#ffffff50" font-size="12">Whoever cracks this puzzle will understand the true nature of time, space, and reality.</text>
  <text x="350" y="438" text-anchor="middle" fill="#ffffff35" font-size="11">The clue is sitting right here. Nobody's solved it yet.</text>

</svg>"""
    save("04_rosetta_stone.svg", svg)


# --- Run all ------------------------------------------------------------------

if __name__ == "__main__":
    what_is_heat()
    entropy()
    arrow_of_time()
    rosetta_stone()
    print("\nAll Chapter 6 diagrams generated!")
