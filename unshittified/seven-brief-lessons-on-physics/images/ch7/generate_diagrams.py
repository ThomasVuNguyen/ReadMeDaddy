#!/usr/bin/env python3
"""Generate SVG diagrams for Chapter 7: Ourselves."""

import math
import os
import random

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def save(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"Saved: {path}")


# --- DIAGRAM 1: We Are Made of the Same Stuff --------------------------------

def same_stuff():
    """Humans, stars, and mountains: all combinations of the same particles."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">WE ARE MADE OF STARDUST</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">Same particles, same forces, different arrangements</text>
"""
    # Show different objects all made of the same particles
    objects = [
        (120, "STAR", "#FFD700", "H, He, C, O\nfusion, gravity"),
        (290, "MOUNTAIN", "#69F0AE", "Si, O, Al, Fe\nelectromagnetism"),
        (460, "TREE", "#4FC3F7", "C, H, O, N\nphotosynthesis"),
        (630, "YOU", "#B388FF", "C, H, O, N, P, S\nconsciousness?"),
    ]

    for x, label, color, desc in objects:
        # Simple iconic shapes
        svg += f'  <circle cx="{x}" cy="140" r="40" fill="{color}" fill-opacity="0.1" stroke="{color}" stroke-width="1.5" stroke-opacity="0.4"/>\n'
        svg += f'  <text x="{x}" y="145" text-anchor="middle" fill="{color}" font-size="14" font-weight="bold">{label}</text>\n'
        lines = desc.split("\n")
        for i, line in enumerate(lines):
            svg += f'  <text x="{x}" y="{195 + i * 16}" text-anchor="middle" fill="#ffffff40" font-size="10">{line}</text>\n'

    # Arrows all pointing down to the same base
    for x, _, color, _ in objects:
        svg += f'  <line x1="{x}" y1="225" x2="{x}" y2="265" stroke="{color}" stroke-width="1" opacity="0.3"/>\n'
        svg += f'  <polygon points="{x - 4},263 {x},272 {x + 4},263" fill="{color}" opacity="0.3"/>\n'

    # Common base: the Standard Model particles
    svg += '  <rect x="60" y="280" width="680" height="90" fill="#ffffff06" rx="8" stroke="#ffffff15" stroke-width="1"/>\n'
    svg += '  <text x="400" y="310" text-anchor="middle" fill="#fff" font-size="14" font-weight="bold">THE SAME HANDFUL OF PARTICLES</text>\n'

    particles = ["e-", "u", "d", "γ", "g", "ν"]
    colors = ["#4FC3F7", "#FF6B6B", "#FF6B6B", "#FFEB3B", "#FF6B6B", "#B388FF"]
    start_x = 220
    for i, (p, c) in enumerate(zip(particles, colors)):
        px = start_x + i * 60
        svg += f'  <circle cx="{px}" cy="345" r="14" fill="{c}20" stroke="{c}" stroke-width="1.5" opacity="0.5"/>\n'
        svg += f'  <text x="{px}" y="350" text-anchor="middle" fill="{c}" font-size="12" font-weight="bold">{p}</text>\n'

    svg += """
  <text x="400" y="395" text-anchor="middle" fill="#ffffff40" font-size="12">No magic ingredient separates you from a star. Just arrangement.</text>

</svg>"""
    save("01_same_stuff.svg", svg)


# --- DIAGRAM 2: The Scale of What We Are --------------------------------------

def cosmic_humility():
    """Our place: one species, one planet, one star, one galaxy."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="380" fill="url(#bg2)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">WHERE WE STAND</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">Not at the center of anything</text>
"""
    # Concentric rings, each bigger, us at center
    cx, cy = 400, 210
    rings = [
        (20, "#B388FF", "You", "100 billion neurons"),
        (60, "#4FC3F7", "Earth", "8 billion humans"),
        (110, "#69F0AE", "Solar System", "1 ordinary star"),
        (170, "#FFD700", "Milky Way", "200 billion stars"),
        (240, "#FF6B6B", "Observable Universe", "200 billion galaxies"),
    ]

    for r, color, label, desc in reversed(rings):
        svg += f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" fill-opacity="0.06" stroke="{color}" stroke-width="1" stroke-opacity="0.25"/>\n'

    # Labels (offset to right side)
    for r, color, label, desc in rings:
        lx = cx + r + 15
        ly = cy - r + 10 if r > 60 else cy
        if r == 20:
            ly = cy - 25
            lx = cx + 35
        svg += f'  <text x="{lx}" y="{ly}" fill="{color}" font-size="11" font-weight="bold">{label}</text>\n'
        svg += f'  <text x="{lx}" y="{ly + 14}" fill="#ffffff30" font-size="9">{desc}</text>\n'
        # Connector line
        svg += f'  <line x1="{cx + r}" y1="{cy}" x2="{lx - 5}" y2="{ly - 5}" stroke="{color}" stroke-width="0.5" opacity="0.3"/>\n'

    # Center dot
    svg += f'  <circle cx="{cx}" cy="{cy}" r="3" fill="#B388FF"/>\n'

    svg += """
  <text x="400" y="370" text-anchor="middle" fill="#ffffff40" font-size="12">We're not homeless. We're home. This strange world is the only one we've got.</text>

</svg>"""
    save("02_cosmic_humility.svg", svg)


# --- DIAGRAM 3: The Frontier of Knowledge ------------------------------------

def frontier():
    """What we know vs what we don't."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 350" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
    <radialGradient id="known" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#69F0AE" stop-opacity="0.15"/>
      <stop offset="80%" stop-color="#69F0AE" stop-opacity="0.03"/>
      <stop offset="100%" stop-color="#69F0AE" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="700" height="350" fill="url(#bg3)" rx="12"/>

  <text x="350" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">THE EDGE OF KNOWLEDGE</text>
  <text x="350" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">"On the edge of what we know, shines the mystery and the beauty of the world."</text>
"""
    cx, cy = 350, 200

    # Known: bright island
    svg += f'  <circle cx="{cx}" cy="{cy}" r="80" fill="url(#known)"/>\n'
    svg += f'  <circle cx="{cx}" cy="{cy}" r="80" fill="none" stroke="#69F0AE" stroke-width="1.5" opacity="0.3" stroke-dasharray="4,4"/>\n'
    svg += f'  <text x="{cx}" y="{cy - 5}" text-anchor="middle" fill="#69F0AE" font-size="14" font-weight="bold">WHAT WE KNOW</text>\n'

    # Items inside the known circle
    known_items = ["GR", "QM", "Standard\nModel", "Thermo", "Evolution"]
    known_angles = [45, 135, 225, 315, 0]
    for item, angle_deg in zip(known_items, known_angles):
        a = math.radians(angle_deg)
        ix = cx + 45 * math.cos(a)
        iy = cy + 45 * math.sin(a)
        lines = item.split("\n")
        for j, line in enumerate(lines):
            svg += f'  <text x="{ix:.0f}" y="{iy + j * 12:.0f}" text-anchor="middle" fill="#69F0AE80" font-size="9">{line}</text>\n'

    # Unknown: question marks scattered around the edge
    unknowns = [
        (140, 120, "Dark matter?"),
        (530, 130, "Dark energy?"),
        (150, 280, "Quantum gravity?"),
        (550, 250, "Consciousness?"),
        (350, 80, "Before the Big Bang?"),
        (350, 320, "What is time?"),
        (180, 190, "Other universes?"),
        (520, 190, "Why these constants?"),
    ]

    for qx, qy, label in unknowns:
        svg += f'  <text x="{qx}" y="{qy}" text-anchor="middle" fill="#B388FF" font-size="11" opacity="0.5">{label}</text>\n'
        # Faint connecting line to the known circle edge
        dx = qx - cx
        dy = qy - cy
        dist = math.sqrt(dx*dx + dy*dy)
        if dist > 0:
            ex = cx + 80 * dx / dist
            ey = cy + 80 * dy / dist
            svg += f'  <line x1="{ex:.0f}" y1="{ey:.0f}" x2="{qx}" y2="{qy}" stroke="#B388FF" stroke-width="0.5" opacity="0.15" stroke-dasharray="3,5"/>\n'

    svg += """
  <text x="350" y="345" text-anchor="middle" fill="#ffffff35" font-size="11">The island of knowledge grows, but so does the shoreline of mystery.</text>

</svg>"""
    save("03_frontier.svg", svg)


# --- Run all ------------------------------------------------------------------

if __name__ == "__main__":
    same_stuff()
    cosmic_humility()
    frontier()
    print("\nAll Chapter 7 diagrams generated!")
