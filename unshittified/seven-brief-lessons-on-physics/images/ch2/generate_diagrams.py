#!/usr/bin/env python3
"""Generate SVG diagrams for Chapter 2: Quanta."""

import math
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def save(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"Saved: {path}")


# --- DIAGRAM 1: Classical vs Quantum Energy -----------------------------------

def classical_vs_quantum():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 380" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="900" height="380" fill="url(#bg)" rx="12"/>

  <!-- Divider -->
  <line x1="450" y1="50" x2="450" y2="350" stroke="#ffffff20" stroke-width="2" stroke-dasharray="8,6"/>

  <!-- Left: Classical (continuous) -->
  <text x="225" y="40" text-anchor="middle" fill="#FF6B6B" font-size="20" font-weight="bold">CLASSICAL</text>
  <text x="225" y="60" text-anchor="middle" fill="#ffffff60" font-size="13">Energy flows like water</text>
"""
    # Draw a smooth sine wave (continuous energy)
    wave_points = []
    for x in range(30, 420, 2):
        t = (x - 30) / 390.0
        y = 200 + 80 * math.sin(t * math.pi * 6)
        wave_points.append(f"{x},{y:.1f}")
    svg += f'  <polyline points="{" ".join(wave_points)}" fill="none" stroke="#FF6B6B" stroke-width="3" opacity="0.8"/>\n'

    # Fill under the wave
    fill_points = [f"30,280"] + wave_points + [f"420,280"]
    svg += f'  <polyline points="{" ".join(fill_points)}" fill="#FF6B6B10" stroke="none"/>\n'

    svg += """
  <text x="225" y="320" text-anchor="middle" fill="#FF6B6B80" font-size="12">Any amount of energy is possible</text>
  <text x="225" y="338" text-anchor="middle" fill="#FF6B6B80" font-size="12">Smooth, continuous spectrum</text>

  <!-- Right: Quantum (discrete) -->
  <text x="675" y="40" text-anchor="middle" fill="#B388FF" font-size="20" font-weight="bold">QUANTUM</text>
  <text x="675" y="60" text-anchor="middle" fill="#ffffff60" font-size="13">Energy comes in packets (quanta)</text>
"""
    # Draw discrete energy bars (like a histogram/staircase)
    bar_heights = [50, 90, 130, 160, 130, 90, 50, 30, 15]
    bar_width = 35
    start_x = 490
    for i, h in enumerate(bar_heights):
        x = start_x + i * (bar_width + 8)
        y = 280 - h
        # Glow effect
        svg += f'  <rect x="{x}" y="{y}" width="{bar_width}" height="{h}" fill="#B388FF" opacity="0.15" rx="3"/>\n'
        svg += f'  <rect x="{x}" y="{y}" width="{bar_width}" height="{h}" fill="none" stroke="#B388FF" stroke-width="2" rx="3" opacity="0.7"/>\n'
        # Photon dot at top
        svg += f'  <circle cx="{x + bar_width/2}" cy="{y - 8}" r="4" fill="#FFEB3B" opacity="0.8"/>\n'

    svg += """
  <text x="675" y="320" text-anchor="middle" fill="#B388FF80" font-size="12">Only specific energy levels allowed</text>
  <text x="675" y="338" text-anchor="middle" fill="#B388FF80" font-size="12">Discrete packets: E = h x f</text>

  <!-- Labels -->
  <text x="60" y="165" fill="#ffffff30" font-size="11">Energy</text>
  <text x="380" y="290" fill="#ffffff30" font-size="11">frequency</text>
  <text x="500" y="165" fill="#ffffff30" font-size="11">Energy</text>
  <text x="830" y="290" fill="#ffffff30" font-size="11">frequency</text>

</svg>"""
    save("01_classical_vs_quantum.svg", svg)


# --- DIAGRAM 2: Bohr Model / Quantum Leaps -----------------------------------

def bohr_model():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 450" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
    <radialGradient id="nucleus" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF6B6B"/>
      <stop offset="100%" stop-color="#D32F2F"/>
    </radialGradient>
  </defs>
  <rect width="700" height="450" fill="url(#bg2)" rx="12"/>

  <text x="350" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">BOHR MODEL: QUANTUM LEAPS</text>
  <text x="350" y="55" text-anchor="middle" fill="#ffffff80" font-size="13">Electrons can only exist at specific energy levels</text>
"""
    cx, cy = 280, 250

    # Draw allowed orbits (concentric circles)
    orbits = [
        (60, "n=1", "#B388FF", 1.0),
        (100, "n=2", "#B388FF", 0.7),
        (145, "n=3", "#B388FF", 0.5),
        (190, "n=4", "#B388FF", 0.35),
    ]

    for r, label, color, opacity in orbits:
        svg += f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="1.5" opacity="{opacity}" stroke-dasharray="6,4"/>\n'
        svg += f'  <text x="{cx + r + 8}" y="{cy - 5}" fill="{color}" font-size="11" opacity="{opacity + 0.2}">{label}</text>\n'

    # Nucleus
    svg += f'  <circle cx="{cx}" cy="{cy}" r="18" fill="url(#nucleus)"/>\n'
    svg += f'  <text x="{cx}" y="{cy + 5}" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">nucleus</text>\n'

    # Electron on n=3
    e_angle = math.radians(210)
    e_x = cx + 145 * math.cos(e_angle)
    e_y = cy + 145 * math.sin(e_angle)
    svg += f'  <circle cx="{e_x:.0f}" cy="{e_y:.0f}" r="10" fill="#4FC3F7"/>\n'
    svg += f'  <text x="{e_x:.0f}" y="{e_y + 4:.0f}" text-anchor="middle" fill="#000" font-size="9" font-weight="bold">e-</text>\n'

    # Quantum leap arrow (n=3 -> n=1)
    e2_angle = math.radians(330)
    e2_x = cx + 60 * math.cos(e2_angle)
    e2_y = cy + 60 * math.sin(e2_angle)

    svg += f"""
  <!-- Quantum leap arrow -->
  <path d="M {e_x:.0f} {e_y:.0f} Q {cx - 30} {cy + 40} {e2_x:.0f} {e2_y:.0f}" fill="none" stroke="#FFEB3B" stroke-width="2.5" stroke-dasharray="6,3"/>

  <!-- Photon emitted -->
  <circle cx="{cx - 50}" cy="{cy + 80}" r="8" fill="#FFEB3B" opacity="0.9"/>
"""
    # Wavy line from the leap (photon emission)
    wave_pts = []
    for i in range(30):
        wx = cx - 60 - i * 5
        wy = cy + 85 + 8 * math.sin(i * 0.8)
        wave_pts.append(f"{wx:.0f},{wy:.0f}")
    svg += f'  <polyline points="{" ".join(wave_pts)}" fill="none" stroke="#FFEB3B" stroke-width="2" opacity="0.6"/>\n'

    svg += f"""
  <text x="{cx - 110}" y="{cy + 115}" fill="#FFEB3B" font-size="12">photon emitted</text>

  <!-- Right side: energy level diagram -->
  <rect x="490" y="80" width="190" height="340" fill="#ffffff06" rx="8" stroke="#ffffff15" stroke-width="1"/>
  <text x="585" y="105" text-anchor="middle" fill="#fff" font-size="14" font-weight="bold">Energy Levels</text>

  <!-- Energy levels -->
  <line x1="510" y1="360" x2="660" y2="360" stroke="#B388FF" stroke-width="2"/>
  <text x="670" y="365" fill="#B388FF" font-size="11">n=1 (ground)</text>

  <line x1="510" y1="290" x2="660" y2="290" stroke="#B388FF" stroke-width="2" opacity="0.7"/>
  <text x="670" y="295" fill="#B388FF" font-size="11" opacity="0.7">n=2</text>

  <line x1="510" y1="230" x2="660" y2="230" stroke="#B388FF" stroke-width="2" opacity="0.5"/>
  <text x="670" y="235" fill="#B388FF" font-size="11" opacity="0.5">n=3</text>

  <line x1="510" y1="180" x2="660" y2="180" stroke="#B388FF" stroke-width="2" opacity="0.35"/>
  <text x="670" y="185" fill="#B388FF" font-size="11" opacity="0.35">n=4</text>

  <!-- Jump arrow -->
  <line x1="550" y1="225" x2="550" y2="365" stroke="#FFEB3B" stroke-width="2.5"/>
  <polygon points="546,365 550,375 554,365" fill="#FFEB3B"/>
  <text x="530" y="300" fill="#FFEB3B" font-size="11" transform="rotate(-90, 530, 300)">LEAP</text>

  <!-- No in-between label -->
  <text x="585" y="420" text-anchor="middle" fill="#ffffff50" font-size="12">No orbits exist between the lines.</text>
  <text x="585" y="436" text-anchor="middle" fill="#ffffff50" font-size="12">Jump or nothing.</text>

</svg>"""
    save("02_bohr_quantum_leaps.svg", svg)


# --- DIAGRAM 3: Electron Probability Cloud -----------------------------------

def probability_cloud():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
    <radialGradient id="cloud" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#B388FF" stop-opacity="0.6"/>
      <stop offset="30%" stop-color="#B388FF" stop-opacity="0.3"/>
      <stop offset="60%" stop-color="#B388FF" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#B388FF" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg3)" rx="12"/>

  <!-- Divider -->
  <line x1="400" y1="60" x2="400" y2="360" stroke="#ffffff20" stroke-width="2" stroke-dasharray="8,6"/>

  <!-- Left: Classical electron (definite position) -->
  <text x="200" y="40" text-anchor="middle" fill="#FF6B6B" font-size="20" font-weight="bold">CLASSICAL VIEW</text>
  <text x="200" y="60" text-anchor="middle" fill="#ffffff60" font-size="13">"The electron IS here"</text>

  <!-- Orbit circle -->
  <circle cx="200" cy="210" r="90" fill="none" stroke="#ffffff20" stroke-width="1"/>
  <!-- Nucleus -->
  <circle cx="200" cy="210" r="12" fill="#FF6B6B80"/>
  <!-- Electron as a definite dot -->
  <circle cx="268" cy="150" r="10" fill="#4FC3F7"/>
  <text x="268" y="154" text-anchor="middle" fill="#000" font-size="9" font-weight="bold">e-</text>
  <!-- Orbit path -->
  <circle cx="200" cy="210" r="90" fill="none" stroke="#4FC3F7" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.5"/>
  <!-- Arrow showing orbit direction -->
  <text x="200" y="330" text-anchor="middle" fill="#FF6B6B80" font-size="12">Electron follows a definite path</text>
  <text x="200" y="348" text-anchor="middle" fill="#FF6B6B80" font-size="12">like a tiny planet</text>

  <!-- Right: Quantum electron (probability cloud) -->
  <text x="600" y="40" text-anchor="middle" fill="#B388FF" font-size="20" font-weight="bold">QUANTUM VIEW</text>
  <text x="600" y="60" text-anchor="middle" fill="#ffffff60" font-size="13">"The electron MIGHT be here, here, or here"</text>

  <!-- Nucleus -->
  <circle cx="600" cy="210" r="12" fill="#B388FF40"/>

  <!-- Probability cloud (concentric fuzzy circles) -->
  <circle cx="600" cy="210" r="120" fill="url(#cloud)"/>
  <circle cx="600" cy="210" r="80" fill="url(#cloud)"/>
"""

    # Scatter random dots with density falling off with distance
    import random
    random.seed(42)
    for _ in range(200):
        angle = random.uniform(0, 2 * math.pi)
        # Use gaussian-like distribution for radius
        r = abs(random.gauss(60, 30))
        if r > 120:
            continue
        x = 600 + r * math.cos(angle)
        y = 210 + r * math.sin(angle)
        # Opacity falls off with distance
        opacity = max(0.05, 0.5 - r / 200)
        size = random.uniform(1, 3)
        svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{size:.1f}" fill="#B388FF" opacity="{opacity:.2f}"/>\n'

    svg += """
  <!-- Question marks at potential positions -->
  <text x="560" y="160" fill="#B388FF" font-size="14" opacity="0.6">?</text>
  <text x="650" y="180" fill="#B388FF" font-size="14" opacity="0.4">?</text>
  <text x="580" y="270" fill="#B388FF" font-size="14" opacity="0.5">?</text>
  <text x="640" y="240" fill="#B388FF" font-size="14" opacity="0.3">?</text>

  <text x="600" y="330" text-anchor="middle" fill="#B388FF80" font-size="12">No definite position until measured.</text>
  <text x="600" y="348" text-anchor="middle" fill="#B388FF80" font-size="12">Only a cloud of probabilities.</text>

  <!-- Bottom annotation -->
  <text x="400" y="385" text-anchor="middle" fill="#ffffff40" font-size="12">Heisenberg: "Electrons don't always exist. They only exist when they interact with something."</text>

</svg>"""
    save("03_probability_cloud.svg", svg)


# --- DIAGRAM 4: Wave-Particle Duality ----------------------------------------

def wave_particle():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 350" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg4" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="350" fill="url(#bg4)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">THE DOUBLE NATURE OF LIGHT</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff80" font-size="13">Is it a wave? Is it a particle? Both, depending on how you look.</text>

  <!-- Divider -->
  <line x1="400" y1="70" x2="400" y2="310" stroke="#ffffff20" stroke-width="2" stroke-dasharray="8,6"/>

  <!-- Left: Wave behavior -->
  <text x="200" y="90" text-anchor="middle" fill="#FFEB3B" font-size="16" font-weight="bold">WAVE</text>
  <text x="200" y="108" text-anchor="middle" fill="#ffffff50" font-size="11">Interference, diffraction, spread</text>
"""
    # Draw interference pattern
    for i in range(7):
        y_center = 140 + i * 25
        # Alternating bright/dark bands
        opacity = 0.5 if i % 2 == 0 else 0.08
        svg += f'  <rect x="80" y="{y_center}" width="240" height="20" fill="#FFEB3B" opacity="{opacity}" rx="2"/>\n'

    svg += """
  <text x="200" y="330" text-anchor="middle" fill="#FFEB3B80" font-size="11">Interference bands on a screen</text>

  <!-- Right: Particle behavior -->
  <text x="600" y="90" text-anchor="middle" fill="#FFEB3B" font-size="16" font-weight="bold">PARTICLE</text>
  <text x="600" y="108" text-anchor="middle" fill="#ffffff50" font-size="11">Photoelectric effect, discrete hits</text>
"""
    # Draw individual photon hits (dots scattered with pattern)
    import random
    random.seed(123)
    for _ in range(120):
        # Cluster around certain y-values to show wave-like distribution
        band = random.choice([0, 0, 0, 1, 2, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6])
        y = 150 + band * 25 + random.gauss(0, 4)
        x = 500 + random.uniform(0, 200)
        svg += f'  <circle cx="{x:.0f}" cy="{y:.0f}" r="2" fill="#FFEB3B" opacity="0.7"/>\n'

    svg += """
  <text x="600" y="330" text-anchor="middle" fill="#FFEB3B80" font-size="11">Individual photon hits build up the pattern</text>

  <!-- Center annotation -->
  <text x="400" y="195" text-anchor="middle" fill="#69F0AE" font-size="13" font-weight="bold" transform="rotate(-90, 400, 195)">SAME THING</text>

</svg>"""
    save("04_wave_particle_duality.svg", svg)


# --- DIAGRAM 5: Einstein vs Bohr Debate --------------------------------------

def einstein_vs_bohr():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg5" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="380" fill="url(#bg5)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">THE GREAT DEBATE</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff80" font-size="13">Two giants, decades of argument, still unresolved</text>

  <!-- Einstein side -->
  <rect x="30" y="75" width="340" height="250" fill="#FF6B6B08" rx="10" stroke="#FF6B6B30" stroke-width="1"/>
  <text x="200" y="105" text-anchor="middle" fill="#FF6B6B" font-size="18" font-weight="bold">EINSTEIN</text>

  <!-- Einstein's position -->
  <text x="50" y="140" fill="#ffffff80" font-size="13">"God does not play dice."</text>
  <text x="50" y="170" fill="#ffffff60" font-size="12">The theory works, but it can't be</text>
  <text x="50" y="188" fill="#ffffff60" font-size="12">the full story. Something deeper and</text>
  <text x="50" y="206" fill="#ffffff60" font-size="12">more deterministic must lurk beneath.</text>

  <text x="50" y="240" fill="#FF6B6B" font-size="12" font-weight="bold">Key arguments:</text>
  <text x="50" y="260" fill="#ffffff50" font-size="11">- Thought experiments to find contradictions</text>
  <text x="50" y="278" fill="#ffffff50" font-size="11">- "Box of light" paradox</text>
  <text x="50" y="296" fill="#ffffff50" font-size="11">- EPR paradox (hidden variables)</text>

  <!-- Bohr side -->
  <rect x="430" y="75" width="340" height="250" fill="#B388FF08" rx="10" stroke="#B388FF30" stroke-width="1"/>
  <text x="600" y="105" text-anchor="middle" fill="#B388FF" font-size="18" font-weight="bold">BOHR</text>

  <!-- Bohr's position -->
  <text x="450" y="140" fill="#ffffff80" font-size="13">"Stop telling God what to do."</text>
  <text x="450" y="170" fill="#ffffff60" font-size="12">The theory IS the reality. Nature is</text>
  <text x="450" y="188" fill="#ffffff60" font-size="12">genuinely probabilistic at its core.</text>
  <text x="450" y="206" fill="#ffffff60" font-size="12">There's nothing "deeper" to find.</text>

  <text x="450" y="240" fill="#B388FF" font-size="12" font-weight="bold">Key arguments:</text>
  <text x="450" y="260" fill="#ffffff50" font-size="11">- Rebutted every thought experiment</text>
  <text x="450" y="278" fill="#ffffff50" font-size="11">- Complementarity principle</text>
  <text x="450" y="296" fill="#ffffff50" font-size="11">- "We can only describe observations"</text>

  <!-- VS in center -->
  <circle cx="400" cy="200" r="25" fill="#1a1e3a" stroke="#ffffff30" stroke-width="2"/>
  <text x="400" y="207" text-anchor="middle" fill="#fff" font-size="16" font-weight="bold">VS</text>

  <!-- Bottom: verdict -->
  <rect x="150" y="340" width="500" height="30" fill="#ffffff08" rx="6"/>
  <text x="400" y="360" text-anchor="middle" fill="#69F0AE" font-size="13">A century later: Bohr's equations work perfectly. Nobody knows if he was right about reality.</text>

</svg>"""
    save("05_einstein_vs_bohr.svg", svg)


# --- Run all ------------------------------------------------------------------

if __name__ == "__main__":
    classical_vs_quantum()
    bohr_model()
    probability_cloud()
    wave_particle()
    einstein_vs_bohr()
    print("\nAll Chapter 2 diagrams generated!")
