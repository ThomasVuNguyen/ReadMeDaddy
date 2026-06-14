#!/usr/bin/env python3
"""Generate SVG diagrams for Chapter 5: Grains of Space."""

import math
import os
import random

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def save(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"Saved: {path}")


# --- DIAGRAM 1: Smooth Space vs Granular Space --------------------------------

def smooth_vs_granular():
    """Side by side: GR's smooth fabric vs LQG's discrete grains."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="380" fill="url(#bg)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">IS SPACE SMOOTH OR GRANULAR?</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">Two theories, two answers, one conflict</text>

  <!-- Divider -->
  <line x1="400" y1="70" x2="400" y2="340" stroke="#ffffff15" stroke-width="2" stroke-dasharray="8,6"/>

  <!-- Left: General Relativity (smooth) -->
  <text x="200" y="85" text-anchor="middle" fill="#69F0AE" font-size="16" font-weight="bold">GENERAL RELATIVITY</text>
  <text x="200" y="103" text-anchor="middle" fill="#ffffff40" font-size="11">Space is a smooth, bendable fabric</text>
"""
    # Draw smooth curved grid
    for row in range(7):
        pts = []
        for col in range(20):
            x = 50 + col * 17
            y = 130 + row * 30
            # Add curvature (depression in center)
            dx = x - 200
            dy = y - 230
            dist = math.sqrt(dx*dx + dy*dy)
            if dist < 100:
                depth = 15 * (1 - dist/100)**2
            else:
                depth = 0
            pts.append(f"{x},{y + depth:.1f}")
        svg += f'  <polyline points="{" ".join(pts)}" fill="none" stroke="#69F0AE" stroke-width="1" opacity="0.3"/>\n'

    for col in range(20):
        pts = []
        for row in range(7):
            x = 50 + col * 17
            y = 130 + row * 30
            dx = x - 200
            dy = y - 230
            dist = math.sqrt(dx*dx + dy*dy)
            if dist < 100:
                depth = 15 * (1 - dist/100)**2
            else:
                depth = 0
            pts.append(f"{x},{y + depth:.1f}")
        svg += f'  <polyline points="{" ".join(pts)}" fill="none" stroke="#69F0AE" stroke-width="1" opacity="0.3"/>\n'

    svg += """
  <text x="200" y="345" text-anchor="middle" fill="#69F0AE80" font-size="11">Infinitely smooth, infinitely divisible</text>
  <text x="200" y="362" text-anchor="middle" fill="#69F0AE80" font-size="11">You can always zoom in more</text>

  <!-- Right: Loop Quantum Gravity (granular) -->
  <text x="600" y="85" text-anchor="middle" fill="#B388FF" font-size="16" font-weight="bold">LOOP QUANTUM GRAVITY</text>
  <text x="600" y="103" text-anchor="middle" fill="#ffffff40" font-size="11">Space is a network of discrete grains</text>
"""
    # Draw a spin network / chain mail lattice
    random.seed(42)
    nodes = []
    for i in range(35):
        nx = 450 + random.uniform(0, 300)
        ny = 120 + random.uniform(0, 210)
        nodes.append((nx, ny))

    # Connect nearby nodes
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            dx = nodes[i][0] - nodes[j][0]
            dy = nodes[i][1] - nodes[j][1]
            dist = math.sqrt(dx*dx + dy*dy)
            if dist < 65:
                opacity = max(0.08, 0.3 - dist/200)
                svg += f'  <line x1="{nodes[i][0]:.0f}" y1="{nodes[i][1]:.0f}" x2="{nodes[j][0]:.0f}" y2="{nodes[j][1]:.0f}" stroke="#B388FF" stroke-width="1" opacity="{opacity:.2f}"/>\n'

    # Draw nodes
    for nx, ny in nodes:
        size = random.uniform(2, 5)
        svg += f'  <circle cx="{nx:.0f}" cy="{ny:.0f}" r="{size:.1f}" fill="#B388FF" opacity="0.4"/>\n'

    svg += """
  <text x="600" y="345" text-anchor="middle" fill="#B388FF80" font-size="11">Atoms of space, linked in a network</text>
  <text x="600" y="362" text-anchor="middle" fill="#B388FF80" font-size="11">Zoom in far enough, the "fabric" shows its weave</text>

</svg>"""
    save("01_smooth_vs_granular.svg", svg)


# --- DIAGRAM 2: Time Disappears at the Bottom --------------------------------

def time_disappears():
    """At the fundamental level, there's no time variable."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 400" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="700" height="400" fill="url(#bg2)" rx="12"/>

  <text x="350" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">WHERE DOES TIME GO?</text>
  <text x="350" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">Zoom in far enough and the clock disappears</text>
"""
    # Three layers, top to bottom: our experience → GR → LQG
    layers = [
        (100, "#4FC3F7", "OUR EXPERIENCE", "Smooth flow of time, clocks tick, events happen in order"),
        (210, "#69F0AE", "GENERAL RELATIVITY", "Time is stretchy (slows near mass, speeds up in space) but still flows"),
        (320, "#B388FF", "LOOP QUANTUM GRAVITY", "No time variable in the equations. Change without a clock."),
    ]

    for y, color, title, desc in layers:
        svg += f'  <rect x="60" y="{y - 30}" width="580" height="70" fill="{color}08" stroke="{color}30" stroke-width="1" rx="8"/>\n'
        svg += f'  <text x="80" y="{y}" fill="{color}" font-size="14" font-weight="bold">{title}</text>\n'
        svg += f'  <text x="80" y="{y + 20}" fill="#ffffff50" font-size="11">{desc}</text>\n'

    # Arrows going down
    for y in [140, 250]:
        svg += f'  <line x1="350" y1="{y}" x2="350" y2="{y + 30}" stroke="#ffffff20" stroke-width="1.5"/>\n'
        svg += f'  <polygon points="346,{y + 28} 350,{y + 35} 354,{y + 28}" fill="#ffffff20"/>\n'
        svg += f'  <text x="365" y="{y + 20}" fill="#ffffff20" font-size="10">zoom in</text>\n'

    # Clock icons that fade
    # Layer 1: solid clock
    svg += '  <circle cx="640" cy="100" r="18" fill="none" stroke="#4FC3F7" stroke-width="2" opacity="0.7"/>\n'
    svg += '  <line x1="640" y1="100" x2="640" y2="88" stroke="#4FC3F7" stroke-width="2" opacity="0.7"/>\n'
    svg += '  <line x1="640" y1="100" x2="650" y2="100" stroke="#4FC3F7" stroke-width="1.5" opacity="0.7"/>\n'

    # Layer 2: wobbly clock
    svg += '  <ellipse cx="640" cy="210" rx="18" ry="15" fill="none" stroke="#69F0AE" stroke-width="2" opacity="0.4" transform="rotate(10, 640, 210)"/>\n'
    svg += '  <line x1="640" y1="210" x2="640" y2="198" stroke="#69F0AE" stroke-width="1.5" opacity="0.4"/>\n'
    svg += '  <line x1="640" y1="210" x2="650" y2="207" stroke="#69F0AE" stroke-width="1.5" opacity="0.4"/>\n'

    # Layer 3: broken / dissolved clock
    for angle in range(0, 360, 45):
        a = math.radians(angle)
        fx = 640 + 18 * math.cos(a)
        fy = 320 + 18 * math.sin(a)
        # Scatter outward
        fx2 = 640 + 25 * math.cos(a) + random.uniform(-3, 3)
        fy2 = 320 + 25 * math.sin(a) + random.uniform(-3, 3)
        svg += f'  <circle cx="{fx2:.0f}" cy="{fy2:.0f}" r="2" fill="#B388FF" opacity="0.3"/>\n'

    svg += """
  <text x="640" y="325" text-anchor="middle" fill="#B388FF" font-size="8" opacity="0.4">dissolved</text>

  <!-- Punchline -->
  <text x="350" y="385" text-anchor="middle" fill="#ffffff40" font-size="12">Time isn't fundamental. It's what change looks like when you're too big to see the grains.</text>

</svg>"""
    save("02_time_disappears.svg", svg)


# --- DIAGRAM 3: Black Hole → Planck Star Bounce -------------------------------

def planck_star():
    """Star collapses but bounces back instead of crushing to a singularity."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 350" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="900" height="350" fill="url(#bg3)" rx="12"/>

  <text x="450" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">PLANCK STAR: THE BOUNCE</text>
  <text x="450" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">Loop quantum gravity says nothing can crush to a point</text>
"""
    stages = [
        (100, "Star", "#FFD700", 50),
        (280, "Collapse", "#FF6B6B", 30),
        (450, "Planck Star", "#B388FF", 8),
        (620, "Bounce", "#69F0AE", 25),
        (800, "Explosion", "#FFEB3B", 50),
    ]

    # Draw each stage
    for x, label, color, radius in stages:
        svg += f'  <circle cx="{x}" cy="175" r="{radius}" fill="{color}" opacity="0.2"/>\n'
        svg += f'  <circle cx="{x}" cy="175" r="{radius}" fill="none" stroke="{color}" stroke-width="2" opacity="0.6"/>\n'
        svg += f'  <text x="{x}" y="{175 + radius + 25}" text-anchor="middle" fill="{color}" font-size="13" font-weight="bold">{label}</text>\n'

    # Collapse arrows (shrinking)
    svg += '  <line x1="155" y1="175" x2="245" y2="175" stroke="#FF6B6B" stroke-width="1.5" opacity="0.4"/>\n'
    svg += '  <polygon points="243,171 250,175 243,179" fill="#FF6B6B" opacity="0.4"/>\n'

    svg += '  <line x1="315" y1="175" x2="435" y2="175" stroke="#B388FF" stroke-width="1.5" opacity="0.4"/>\n'
    svg += '  <polygon points="433,171 440,175 433,179" fill="#B388FF" opacity="0.4"/>\n'

    # Bounce arrows (expanding)
    svg += '  <line x1="465" y1="175" x2="590" y2="175" stroke="#69F0AE" stroke-width="1.5" opacity="0.4"/>\n'
    svg += '  <polygon points="588,171 595,175 588,179" fill="#69F0AE" opacity="0.4"/>\n'

    svg += '  <line x1="650" y1="175" x2="745" y2="175" stroke="#FFEB3B" stroke-width="1.5" opacity="0.4"/>\n'
    svg += '  <polygon points="743,171 750,175 743,179" fill="#FFEB3B" opacity="0.4"/>\n'

    # Add Planck star glow
    svg += '  <circle cx="450" cy="175" r="20" fill="#B388FF" opacity="0.08"/>\n'

    # Quantum repulsion text
    svg += '  <text x="450" y="240" text-anchor="middle" fill="#B388FF80" font-size="10">Quantum repulsion prevents</text>\n'
    svg += '  <text x="450" y="254" text-anchor="middle" fill="#B388FF80" font-size="10">infinite compression</text>\n'

    # Explosion rays
    for angle_deg in range(0, 360, 30):
        a = math.radians(angle_deg)
        rx1 = 800 + 50 * math.cos(a)
        ry1 = 175 + 50 * math.sin(a)
        rx2 = 800 + 70 * math.cos(a)
        ry2 = 175 + 70 * math.sin(a)
        svg += f'  <line x1="{rx1:.0f}" y1="{ry1:.0f}" x2="{rx2:.0f}" y2="{ry2:.0f}" stroke="#FFEB3B" stroke-width="1" opacity="0.3"/>\n'

    svg += """
  <!-- Comparison -->
  <rect x="60" y="280" width="780" height="50" fill="#ffffff06" rx="6"/>
  <text x="250" y="305" text-anchor="middle" fill="#FF6B6B80" font-size="11">General Relativity: collapses to a singularity (infinite density, equations break)</text>
  <text x="650" y="305" text-anchor="middle" fill="#69F0AE80" font-size="11">Loop QG: bounces at the Planck scale (no infinities)</text>
  <text x="450" y="322" text-anchor="middle" fill="#ffffff30" font-size="10">A black hole is a rebounding star viewed in extreme slow motion.</text>

</svg>"""
    save("03_planck_star.svg", svg)


# --- DIAGRAM 4: Big Bounce ---------------------------------------------------

def big_bounce():
    """The Big Bang as a bounce from a prior contracting universe."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 350" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg4" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="350" fill="url(#bg4)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">THE BIG BOUNCE</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">What if the Big Bang wasn't the beginning, but a transition?</text>
"""
    # Draw two funnels meeting at a pinch point
    cx = 400
    pinch_y = 200

    # Left funnel (prior universe contracting)
    for i in range(30):
        t = i / 30.0
        x_offset = 150 * (1 - t**0.5)
        y = 80 + t * (pinch_y - 80)
        opacity = 0.1 + 0.15 * (1 - t)
        svg += f'  <line x1="{cx - x_offset:.0f}" y1="{y:.0f}" x2="{cx + x_offset:.0f}" y2="{y:.0f}" stroke="#FF6B6B" stroke-width="1" opacity="{opacity:.2f}"/>\n'

    # Right funnel (our universe expanding)
    for i in range(30):
        t = i / 30.0
        x_offset = 150 * (t**0.5)
        y = pinch_y + t * (320 - pinch_y)
        opacity = 0.1 + 0.15 * t
        svg += f'  <line x1="{cx - x_offset:.0f}" y1="{y:.0f}" x2="{cx + x_offset:.0f}" y2="{y:.0f}" stroke="#69F0AE" stroke-width="1" opacity="{opacity:.2f}"/>\n'

    # Outline curves
    # Left side
    pts_left = []
    pts_right = []
    for i in range(60):
        t = i / 59.0
        if t < 0.5:
            # Contracting
            t2 = t * 2
            x_off = 150 * (1 - t2**0.5)
            y = 80 + t2 * (pinch_y - 80)
        else:
            # Expanding
            t2 = (t - 0.5) * 2
            x_off = 150 * (t2**0.5)
            y = pinch_y + t2 * (320 - pinch_y)
        pts_left.append(f"{cx - x_off:.0f},{y:.0f}")
        pts_right.append(f"{cx + x_off:.0f},{y:.0f}")

    svg += f'  <polyline points="{" ".join(pts_left)}" fill="none" stroke="#ffffff30" stroke-width="1.5"/>\n'
    svg += f'  <polyline points="{" ".join(pts_right)}" fill="none" stroke="#ffffff30" stroke-width="1.5"/>\n'

    # Pinch point glow
    svg += f'  <circle cx="{cx}" cy="{pinch_y}" r="12" fill="#B388FF" opacity="0.15"/>\n'
    svg += f'  <circle cx="{cx}" cy="{pinch_y}" r="5" fill="#B388FF" opacity="0.4"/>\n'

    # Labels
    svg += f'  <text x="180" y="100" fill="#FF6B6B" font-size="14" font-weight="bold">PRIOR UNIVERSE</text>\n'
    svg += f'  <text x="180" y="118" fill="#FF6B6B80" font-size="11">contracting</text>\n'

    svg += f'  <text x="{cx + 70}" y="{pinch_y + 5}" fill="#B388FF" font-size="12" font-weight="bold">BOUNCE</text>\n'
    svg += f'  <text x="{cx + 70}" y="{pinch_y + 20}" fill="#B388FF80" font-size="10">quantum repulsion</text>\n'

    svg += f'  <text x="540" y="305" fill="#69F0AE" font-size="14" font-weight="bold">OUR UNIVERSE</text>\n'
    svg += f'  <text x="540" y="323" fill="#69F0AE80" font-size="11">expanding</text>\n'

    # Arrows
    svg += f'  <line x1="{cx - 20}" y1="85" x2="{cx - 5}" y2="{pinch_y - 15}" stroke="#FF6B6B" stroke-width="1.5" opacity="0.4"/>\n'
    svg += f'  <polygon points="{cx - 8},{pinch_y - 20} {cx - 3},{pinch_y - 13} {cx - 1},{pinch_y - 22}" fill="#FF6B6B" opacity="0.4"/>\n'

    svg += f'  <line x1="{cx + 5}" y1="{pinch_y + 15}" x2="{cx + 20}" y2="315" stroke="#69F0AE" stroke-width="1.5" opacity="0.4"/>\n'
    svg += f'  <polygon points="{cx + 17},310 {cx + 22},318 {cx + 24},308" fill="#69F0AE" opacity="0.4"/>\n'

    svg += """
</svg>"""
    save("04_big_bounce.svg", svg)


# --- Run all ------------------------------------------------------------------

if __name__ == "__main__":
    smooth_vs_granular()
    time_disappears()
    planck_star()
    big_bounce()
    print("\nAll Chapter 5 diagrams generated!")
