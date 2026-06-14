#!/usr/bin/env python3
"""Generate SVG diagrams for Chapter 4: Particles."""

import math
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def save(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"Saved: {path}")


# --- DIAGRAM 1: The Particle Zoo (Standard Model) ----------------------------

def standard_model():
    """Visual table of all Standard Model particles."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="900" height="520" fill="url(#bg)" rx="12"/>

  <text x="450" y="35" text-anchor="middle" fill="#fff" font-size="22" font-weight="bold">THE STANDARD MODEL</text>
  <text x="450" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">Fewer than 20 particles build everything in the universe</text>
"""
    # Define particle groups
    # Quarks (6)
    quarks = [
        ("u", "Up", "2.2 MeV", 0), ("c", "Charm", "1.3 GeV", 1), ("t", "Top", "173 GeV", 2),
        ("d", "Down", "4.7 MeV", 0), ("s", "Strange", "96 MeV", 1), ("b", "Bottom", "4.2 GeV", 2),
    ]

    # Leptons (6)
    leptons = [
        ("e", "Electron", "0.511 MeV", 0), ("μ", "Muon", "106 MeV", 1), ("τ", "Tau", "1.78 GeV", 2),
        ("νe", "e neutrino", "< 2 eV", 0), ("νμ", "μ neutrino", "< 0.2 MeV", 1), ("ντ", "τ neutrino", "< 18 MeV", 2),
    ]

    # Force carriers (4)
    forces = [
        ("γ", "Photon", "Electromagnetic", "#FFEB3B"),
        ("g", "Gluon", "Strong force", "#FF6B6B"),
        ("W/Z", "W & Z", "Weak force", "#4FC3F7"),
        ("H", "Higgs", "Mass", "#69F0AE"),
    ]

    cell_w, cell_h = 100, 75
    start_x, start_y = 50, 80

    # Section: QUARKS
    svg += f'  <text x="{start_x}" y="{start_y - 5}" fill="#FF6B6B" font-size="14" font-weight="bold">QUARKS</text>\n'
    svg += f'  <text x="{start_x + 195}" y="{start_y - 5}" fill="#ffffff30" font-size="10">Make up protons and neutrons</text>\n'

    for i, (sym, name, mass, gen) in enumerate(quarks):
        row = i // 3
        col = i % 3
        x = start_x + col * (cell_w + 10)
        y = start_y + row * (cell_h + 8)
        svg += f'  <rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="#FF6B6B10" stroke="#FF6B6B40" stroke-width="1" rx="6"/>\n'
        svg += f'  <text x="{x + 20}" y="{y + 35}" fill="#FF6B6B" font-size="28" font-weight="bold">{sym}</text>\n'
        svg += f'  <text x="{x + cell_w - 8}" y="{y + 20}" text-anchor="end" fill="#ffffff60" font-size="10">{name}</text>\n'
        svg += f'  <text x="{x + cell_w - 8}" y="{y + cell_h - 10}" text-anchor="end" fill="#ffffff30" font-size="9">{mass}</text>\n'

    # Section: LEPTONS
    lep_y = start_y + 2 * (cell_h + 8) + 30
    svg += f'  <text x="{start_x}" y="{lep_y - 5}" fill="#B388FF" font-size="14" font-weight="bold">LEPTONS</text>\n'
    svg += f'  <text x="{start_x + 100}" y="{lep_y - 5}" fill="#ffffff30" font-size="10">Electrons and their cousins</text>\n'

    for i, (sym, name, mass, gen) in enumerate(leptons):
        row = i // 3
        col = i % 3
        x = start_x + col * (cell_w + 10)
        y = lep_y + row * (cell_h + 8)
        svg += f'  <rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="#B388FF10" stroke="#B388FF40" stroke-width="1" rx="6"/>\n'
        svg += f'  <text x="{x + 20}" y="{y + 35}" fill="#B388FF" font-size="28" font-weight="bold">{sym}</text>\n'
        svg += f'  <text x="{x + cell_w - 8}" y="{y + 20}" text-anchor="end" fill="#ffffff60" font-size="10">{name}</text>\n'
        svg += f'  <text x="{x + cell_w - 8}" y="{y + cell_h - 10}" text-anchor="end" fill="#ffffff30" font-size="9">{mass}</text>\n'

    # Generation labels across top
    for gen_i, gen_label in enumerate(["I", "II", "III"]):
        gx = start_x + gen_i * (cell_w + 10) + cell_w / 2
        svg += f'  <text x="{gx}" y="{start_y + 2 * (cell_h + 8) + 20}" text-anchor="middle" fill="#ffffff20" font-size="10">Gen {gen_label}</text>\n'

    # Section: FORCE CARRIERS
    force_x = 430
    svg += f'  <text x="{force_x}" y="{start_y - 5}" fill="#69F0AE" font-size="14" font-weight="bold">FORCE CARRIERS</text>\n'

    for i, (sym, name, desc, color) in enumerate(forces):
        y = start_y + i * (cell_h + 20)
        w = 200
        svg += f'  <rect x="{force_x}" y="{y}" width="{w}" height="{cell_h}" fill="{color}10" stroke="{color}40" stroke-width="1" rx="6"/>\n'
        svg += f'  <text x="{force_x + 20}" y="{y + 38}" fill="{color}" font-size="30" font-weight="bold">{sym}</text>\n'
        svg += f'  <text x="{force_x + w - 10}" y="{y + 22}" text-anchor="end" fill="#ffffff70" font-size="12">{name}</text>\n'
        svg += f'  <text x="{force_x + w - 10}" y="{y + cell_h - 12}" text-anchor="end" fill="#ffffff40" font-size="10">{desc}</text>\n'

    # Right side: "What's missing" box
    mx = 670
    svg += f"""
  <rect x="{mx}" y="80" width="210" height="310" fill="#ffffff06" rx="8" stroke="#ffffff15" stroke-width="1"/>
  <text x="{mx + 105}" y="110" text-anchor="middle" fill="#FF6B6B" font-size="14" font-weight="bold">WHAT'S MISSING</text>

  <text x="{mx + 15}" y="145" fill="#ffffff50" font-size="12">❌ Dark matter particle</text>
  <text x="{mx + 30}" y="163" fill="#ffffff30" font-size="10">25% of the universe,</text>
  <text x="{mx + 30}" y="178" fill="#ffffff30" font-size="10">completely unknown</text>

  <text x="{mx + 15}" y="210" fill="#ffffff50" font-size="12">❌ Graviton</text>
  <text x="{mx + 30}" y="228" fill="#ffffff30" font-size="10">Gravity isn't in this</text>
  <text x="{mx + 30}" y="243" fill="#ffffff30" font-size="10">model at all</text>

  <text x="{mx + 15}" y="275" fill="#ffffff50" font-size="12">❌ Supersymmetric partners</text>
  <text x="{mx + 30}" y="293" fill="#ffffff30" font-size="10">Predicted, searched for</text>
  <text x="{mx + 30}" y="308" fill="#ffffff30" font-size="10">decades. Never found.</text>

  <text x="{mx + 15}" y="345" fill="#ffffff50" font-size="12">❌ Underlying principle</text>
  <text x="{mx + 30}" y="363" fill="#ffffff30" font-size="10">Why THESE particles?</text>
  <text x="{mx + 30}" y="378" fill="#ffffff30" font-size="10">Nobody knows.</text>
"""

    svg += """
  <!-- Bottom -->
  <text x="450" y="500" text-anchor="middle" fill="#ffffff40" font-size="12">The whole thing fits on a poster. It describes everything we've ever measured. And physicists think it's ugly.</text>

</svg>"""
    save("01_standard_model.svg", svg)


# --- DIAGRAM 2: Atom Structure (quarks inside proton inside nucleus) ----------

def atom_zoom():
    """Zoom levels: atom → nucleus → proton → quarks."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 350" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="900" height="350" fill="url(#bg2)" rx="12"/>

  <text x="450" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">ZOOM IN: WHAT MATTER IS MADE OF</text>
"""
    stages = [
        (120, 175, 70, "#4FC3F7", "ATOM", "Electron cloud\naround a nucleus"),
        (340, 175, 55, "#69F0AE", "NUCLEUS", "Protons + neutrons\npacked together"),
        (560, 175, 55, "#FF6B6B", "PROTON", "Three quarks\nbound by gluons"),
        (780, 175, 45, "#B388FF", "QUARKS", "Ripples in\nquantum fields"),
    ]

    for x, y, r, color, label, desc in stages:
        # Glow
        svg += f'  <circle cx="{x}" cy="{y}" r="{r + 15}" fill="{color}" opacity="0.04"/>\n'
        svg += f'  <circle cx="{x}" cy="{y}" r="{r}" fill="{color}10" stroke="{color}" stroke-width="2" opacity="0.6"/>\n'
        svg += f'  <text x="{x}" y="{y - r - 15}" text-anchor="middle" fill="{color}" font-size="15" font-weight="bold">{label}</text>\n'
        lines = desc.split("\n")
        for i, line in enumerate(lines):
            svg += f'  <text x="{x}" y="{y + r + 22 + i * 16}" text-anchor="middle" fill="#ffffff50" font-size="11">{line}</text>\n'

    # Atom details: electron orbit + tiny nucleus
    svg += '  <circle cx="120" cy="175" r="50" fill="none" stroke="#4FC3F750" stroke-width="1" stroke-dasharray="4,3"/>\n'
    svg += '  <circle cx="145" cy="140" r="5" fill="#4FC3F7" opacity="0.8"/>\n'  # electron
    svg += '  <circle cx="120" cy="175" r="8" fill="#69F0AE" opacity="0.5"/>\n'  # tiny nucleus

    # Nucleus details: protons + neutrons
    for angle in [0, 60, 120, 180, 240, 300]:
        a = math.radians(angle)
        nx = 340 + 20 * math.cos(a)
        ny = 175 + 20 * math.sin(a)
        color = "#FF6B6B" if angle % 120 == 0 else "#FFD700"
        svg += f'  <circle cx="{nx:.0f}" cy="{ny:.0f}" r="12" fill="{color}" opacity="0.4"/>\n'

    # Proton details: three quarks + gluon lines
    quark_angles = [90, 210, 330]
    quark_positions = []
    for a_deg in quark_angles:
        a = math.radians(a_deg)
        qx = 560 + 22 * math.cos(a)
        qy = 175 - 22 * math.sin(a)
        quark_positions.append((qx, qy))
        svg += f'  <circle cx="{qx:.0f}" cy="{qy:.0f}" r="10" fill="#FF6B6B" opacity="0.6"/>\n'
        svg += f'  <text x="{qx:.0f}" y="{qy + 4:.0f}" text-anchor="middle" fill="#fff" font-size="8" font-weight="bold">q</text>\n'

    # Gluon lines between quarks
    for i in range(3):
        j = (i + 1) % 3
        svg += f'  <line x1="{quark_positions[i][0]:.0f}" y1="{quark_positions[i][1]:.0f}" x2="{quark_positions[j][0]:.0f}" y2="{quark_positions[j][1]:.0f}" stroke="#FFD700" stroke-width="2" opacity="0.3" stroke-dasharray="3,3"/>\n'

    # Quantum field ripple for quarks stage
    for i in range(8):
        wy = 175 + (i - 4) * 12
        wave_pts = []
        for wx in range(740, 820, 3):
            dy = 5 * math.sin((wx - 740) * 0.15 + i * 0.7)
            wave_pts.append(f"{wx},{wy + dy:.1f}")
        svg += f'  <polyline points="{" ".join(wave_pts)}" fill="none" stroke="#B388FF" stroke-width="1" opacity="0.2"/>\n'

    # Zoom arrows
    for i in range(3):
        x1 = stages[i][0] + stages[i][2] + 18
        x2 = stages[i + 1][0] - stages[i + 1][2] - 18
        mid = (x1 + x2) / 2
        svg += f'  <line x1="{x1}" y1="175" x2="{x2}" y2="175" stroke="#ffffff30" stroke-width="1.5"/>\n'
        svg += f'  <polygon points="{x2 - 6},170 {x2},175 {x2 - 6},180" fill="#ffffff30"/>\n'
        svg += f'  <text x="{mid}" y="168" text-anchor="middle" fill="#ffffff25" font-size="9">zoom</text>\n'

    svg += """
  <text x="450" y="335" text-anchor="middle" fill="#ffffff40" font-size="12">At the deepest level: no solid "things." Just ripples in fields, flickering in and out of existence.</text>

</svg>"""
    save("02_atom_zoom.svg", svg)


# --- DIAGRAM 3: Quantum Field Vacuum Fluctuations ----------------------------

def vacuum_fluctuations():
    """Even empty space isn't empty: virtual particles pop in and out."""
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 350" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="350" fill="url(#bg3)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">"EMPTY" SPACE ISN'T EMPTY</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff60" font-size="13">Virtual particles constantly appear and disappear</text>

  <!-- Divider -->
  <line x1="400" y1="70" x2="400" y2="310" stroke="#ffffff15" stroke-width="2" stroke-dasharray="8,6"/>

  <!-- Left: what we imagine -->
  <text x="200" y="85" text-anchor="middle" fill="#FF6B6B" font-size="16" font-weight="bold">WHAT WE IMAGINE</text>
  <text x="200" y="103" text-anchor="middle" fill="#ffffff40" font-size="11">"Empty" = nothing there</text>

  <rect x="60" y="120" width="280" height="170" fill="#00000030" rx="8" stroke="#ffffff10" stroke-width="1"/>
  <text x="200" y="210" text-anchor="middle" fill="#ffffff15" font-size="24">nothing</text>

  <!-- Right: what's actually there -->
  <text x="600" y="85" text-anchor="middle" fill="#69F0AE" font-size="16" font-weight="bold">WHAT'S ACTUALLY THERE</text>
  <text x="600" y="103" text-anchor="middle" fill="#ffffff40" font-size="11">Seething with quantum fluctuations</text>

  <rect x="460" y="120" width="280" height="170" fill="#00000030" rx="8" stroke="#ffffff10" stroke-width="1"/>
"""
    # Draw virtual particle pairs appearing and annihilating
    import random
    random.seed(99)
    pairs = [
        (510, 170, "e+", "e-", "#B388FF"),
        (620, 200, "q", "q̄", "#FF6B6B"),
        (560, 250, "γ", "γ", "#FFEB3B"),
        (690, 160, "e+", "e-", "#B388FF"),
        (530, 180, "q", "q̄", "#FF6B6B"),
        (660, 240, "γ", "γ", "#FFEB3B"),
        (700, 200, "e+", "e-", "#B388FF"),
        (490, 230, "q", "q̄", "#FF6B6B"),
    ]

    for x, y, p1, p2, color in pairs:
        # Two particles curving away from each other
        opacity = random.uniform(0.2, 0.5)
        svg += f'  <circle cx="{x - 8}" cy="{y}" r="4" fill="{color}" opacity="{opacity:.2f}"/>\n'
        svg += f'  <circle cx="{x + 8}" cy="{y}" r="4" fill="{color}" opacity="{opacity:.2f}"/>\n'
        svg += f'  <text x="{x - 8}" y="{y - 7}" text-anchor="middle" fill="{color}" font-size="7" opacity="{opacity + 0.2:.2f}">{p1}</text>\n'
        svg += f'  <text x="{x + 8}" y="{y - 7}" text-anchor="middle" fill="{color}" font-size="7" opacity="{opacity + 0.2:.2f}">{p2}</text>\n'
        # Curved path
        svg += f'  <path d="M {x - 8} {y} Q {x} {y - 15} {x + 8} {y}" fill="none" stroke="{color}" stroke-width="0.8" opacity="{opacity:.2f}"/>\n'

    # Add some random field ripples
    for _ in range(15):
        rx = random.randint(470, 730)
        ry = random.randint(130, 280)
        rr = random.randint(3, 8)
        svg += f'  <circle cx="{rx}" cy="{ry}" r="{rr}" fill="none" stroke="#ffffff" stroke-width="0.5" opacity="0.06"/>\n'

    svg += """
  <text x="200" y="325" text-anchor="middle" fill="#FF6B6B80" font-size="11">Static. Dead. Silent.</text>
  <text x="600" y="325" text-anchor="middle" fill="#69F0AE80" font-size="11">A roiling sea of virtual particles.</text>

</svg>"""
    save("03_vacuum_fluctuations.svg", svg)


# --- Run all ------------------------------------------------------------------

if __name__ == "__main__":
    standard_model()
    atom_zoom()
    vacuum_fluctuations()
    print("\nAll Chapter 4 diagrams generated!")
