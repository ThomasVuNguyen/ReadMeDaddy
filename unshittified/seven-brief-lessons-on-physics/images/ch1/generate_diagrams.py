#!/usr/bin/env python3
"""Generate SVG diagrams for Chapter 1: The Most Beautiful of Theories."""

import math
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def save(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"Saved: {path}")


# ─── DIAGRAM 1: Newton vs Einstein ───────────────────────────────────────────

def newton_vs_einstein():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
    <radialGradient id="sun1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFD700"/>
      <stop offset="100%" stop-color="#FF8C00"/>
    </radialGradient>
    <radialGradient id="sun2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFD700"/>
      <stop offset="100%" stop-color="#FF8C00"/>
    </radialGradient>
    <radialGradient id="earth" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#4FC3F7"/>
      <stop offset="100%" stop-color="#1565C0"/>
    </radialGradient>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#FF6B6B"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="900" height="420" fill="url(#bg)" rx="12"/>

  <!-- Divider -->
  <line x1="450" y1="50" x2="450" y2="390" stroke="#ffffff20" stroke-width="2" stroke-dasharray="8,6"/>

  <!-- Title -->
  <text x="225" y="45" text-anchor="middle" fill="#FF6B6B" font-size="20" font-weight="bold">NEWTON</text>
  <text x="225" y="65" text-anchor="middle" fill="#ffffff80" font-size="13">Invisible force through empty space</text>
  <text x="675" y="45" text-anchor="middle" fill="#69F0AE" font-size="20" font-weight="bold">EINSTEIN</text>
  <text x="675" y="65" text-anchor="middle" fill="#ffffff80" font-size="13">Space itself is curved by matter</text>

  <!-- ═══ NEWTON SIDE ═══ -->
  <!-- Grid (flat space) -->
  <g stroke="#ffffff15" stroke-width="1">
    <line x1="30" y1="120" x2="420" y2="120"/>
    <line x1="30" y1="160" x2="420" y2="160"/>
    <line x1="30" y1="200" x2="420" y2="200"/>
    <line x1="30" y1="240" x2="420" y2="240"/>
    <line x1="30" y1="280" x2="420" y2="280"/>
    <line x1="30" y1="320" x2="420" y2="320"/>
    <line x1="30" y1="360" x2="420" y2="360"/>
    <line x1="60" y1="90" x2="60" y2="390"/>
    <line x1="110" y1="90" x2="110" y2="390"/>
    <line x1="160" y1="90" x2="160" y2="390"/>
    <line x1="210" y1="90" x2="210" y2="390"/>
    <line x1="260" y1="90" x2="260" y2="390"/>
    <line x1="310" y1="90" x2="310" y2="390"/>
    <line x1="360" y1="90" x2="360" y2="390"/>
    <line x1="410" y1="90" x2="410" y2="390"/>
  </g>

  <!-- Sun -->
  <circle cx="225" cy="230" r="35" fill="url(#sun1)" opacity="0.95"/>
  <text x="225" y="236" text-anchor="middle" fill="#000" font-size="14" font-weight="bold">Sun</text>

  <!-- Earth -->
  <circle cx="370" cy="150" r="14" fill="url(#earth)"/>
  <text x="370" y="135" text-anchor="middle" fill="#fff" font-size="12">Earth</text>

  <!-- Force arrows -->
  <line x1="355" y1="155" x2="270" y2="220" stroke="#FF6B6B" stroke-width="2.5" marker-end="url(#arrowhead)"/>
  <text x="290" y="178" fill="#FF6B6B" font-size="11" transform="rotate(-30, 290, 178)">Mysterious Force?</text>

  <!-- Question -->
  <text x="225" y="395" text-anchor="middle" fill="#FF6B6B99" font-size="12" font-style="italic">"How does force act across empty space?"</text>

  <!-- ═══ EINSTEIN SIDE ═══ -->
  <!-- Curved grid -->
  <g stroke="#69F0AE40" stroke-width="1" fill="none">"""

    # Generate curved grid lines for Einstein's side
    cx, cy = 675, 230  # center of sun
    lines = []

    # Horizontal curved lines
    for y_base in range(120, 380, 40):
        points = []
        for x in range(480, 870, 5):
            dx = x - cx
            dy = y_base - cy
            dist = math.sqrt(dx*dx + dy*dy)
            if dist < 25:
                continue
            # Curve towards center
            pull = max(0, 8000 / (dist*dist + 100))
            y_curved = y_base + (cy - y_base) * pull * 0.15
            points.append(f"{x},{y_curved:.1f}")
        if points:
            lines.append(f'    <polyline points="{" ".join(points)}"/>')

    # Vertical curved lines
    for x_base in range(510, 870, 50):
        points = []
        for y in range(90, 390, 5):
            dx = x_base - cx
            dy = y - cy
            dist = math.sqrt(dx*dx + dy*dy)
            if dist < 25:
                continue
            pull = max(0, 8000 / (dist*dist + 100))
            x_curved = x_base + (cx - x_base) * pull * 0.15
            points.append(f"{x_curved:.1f},{y}")
        if points:
            lines.append(f'    <polyline points="{" ".join(points)}"/>')

    svg += "\n".join(lines)

    # Earth orbit path (ellipse)
    svg += """
  </g>

  <!-- Orbit path -->
  <ellipse cx="675" cy="230" rx="145" ry="100" fill="none" stroke="#4FC3F7" stroke-width="1" stroke-dasharray="6,4" opacity="0.4"/>

  <!-- Sun -->
  <circle cx="675" cy="230" r="35" fill="url(#sun2)" opacity="0.95"/>
  <text x="675" y="236" text-anchor="middle" fill="#000" font-size="14" font-weight="bold">Sun</text>

  <!-- Earth following the curve -->
  <circle cx="820" cy="200" r="14" fill="url(#earth)"/>
  <text x="820" y="185" text-anchor="middle" fill="#fff" font-size="12">Earth</text>

  <!-- Direction arrow on orbit -->
  <path d="M 810 140 Q 790 125 770 120" fill="none" stroke="#4FC3F7" stroke-width="1.5" marker-end="url(#arrowhead)"/>

  <!-- Annotation -->
  <text x="675" y="395" text-anchor="middle" fill="#69F0AE99" font-size="12" font-style="italic">"Earth follows the curve of bent space"</text>

</svg>"""
    save("01_newton_vs_einstein.svg", svg)


# ─── DIAGRAM 2: Marble in a Funnel ──────────────────────────────────────────

def marble_in_funnel():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 450" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFD70060"/>
      <stop offset="100%" stop-color="#FFD70000"/>
    </radialGradient>
  </defs>
  <rect width="700" height="450" fill="url(#bg2)" rx="12"/>

  <text x="350" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">THE FUNNEL ANALOGY</text>
  <text x="350" y="55" text-anchor="middle" fill="#ffffff80" font-size="13">Mass warps space — objects follow the curves</text>
"""
    # Draw the funnel as concentric ellipses getting smaller towards center
    cx, cy = 350, 260
    lines = []

    # Funnel grid - horizontal rings
    for i in range(12):
        t = i / 11.0
        rx = 280 - t * 230
        ry = 140 - t * 110
        depth = t * 120
        opacity = 0.15 + t * 0.25
        color = f"#{int(105 + t*150):02x}{int(240 - t*100):02x}{int(174 - t*50):02x}"
        lines.append(f'  <ellipse cx="{cx}" cy="{cy + depth:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" fill="none" stroke="{color}" stroke-width="1.2" opacity="{opacity:.2f}"/>')

    # Funnel grid - radial lines
    for angle_deg in range(0, 360, 20):
        angle = math.radians(angle_deg)
        points = []
        for i in range(12):
            t = i / 11.0
            rx = 280 - t * 230
            ry = 140 - t * 110
            depth = t * 120
            x = cx + rx * math.cos(angle)
            y = cy + depth + ry * math.sin(angle)
            points.append(f"{x:.1f},{y:.1f}")
        lines.append(f'  <polyline points="{" ".join(points)}" fill="none" stroke="#69F0AE20" stroke-width="0.8"/>')

    svg += "\n".join(lines)

    # Sun glow at center
    svg += f"""
  <circle cx="{cx}" cy="{cy + 120}" r="40" fill="url(#glow)"/>
  <circle cx="{cx}" cy="{cy + 120}" r="18" fill="#FFD700" opacity="0.9"/>
  <text x="{cx}" y="{cy + 125}" text-anchor="middle" fill="#000" font-size="11" font-weight="bold">Sun</text>
"""

    # Marble (Earth) on the rim
    orbit_rx = 200
    orbit_ry = 100
    orbit_depth = 2.0/11.0 * 120
    angle = math.radians(30)
    earth_x = cx + orbit_rx * math.cos(angle)
    earth_y = cy + orbit_depth + orbit_ry * math.sin(angle)

    svg += f"""
  <!-- Earth marble -->
  <circle cx="{earth_x:.0f}" cy="{earth_y:.0f}" r="12" fill="#4FC3F7"/>
  <text x="{earth_x:.0f}" y="{earth_y - 18:.0f}" text-anchor="middle" fill="#4FC3F7" font-size="12">Earth</text>

  <!-- Orbit arrow -->
  <path d="M {earth_x + 15:.0f} {earth_y - 5:.0f} Q {earth_x + 30:.0f} {earth_y - 25:.0f} {earth_x + 20:.0f} {earth_y - 40:.0f}" fill="none" stroke="#4FC3F7" stroke-width="1.5"/>

  <!-- Annotations -->
  <text x="120" y="420" fill="#ffffff60" font-size="12">No force pulling inward —</text>
  <text x="120" y="438" fill="#69F0AE" font-size="12" font-weight="bold">the shape of space does the work</text>

  <!-- Labels -->
  <text x="620" y="150" fill="#ffffff40" font-size="11">Flat space</text>
  <text x="620" y="165" fill="#ffffff40" font-size="11">(far from mass)</text>
  <line x1="600" y1="155" x2="560" y2="175" stroke="#ffffff20" stroke-width="1"/>

  <text x="420" y="400" fill="#ffffff40" font-size="11">Deep curve</text>
  <text x="420" y="415" fill="#ffffff40" font-size="11">(near the sun)</text>
  <line x1="410" y1="390" x2="380" y2="370" stroke="#ffffff20" stroke-width="1"/>

</svg>"""
    save("02_curved_spacetime_funnel.svg", svg)


# ─── DIAGRAM 3: Gravitational Lensing ───────────────────────────────────────

def gravitational_lensing():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 350" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
    <radialGradient id="starglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff"/>
      <stop offset="30%" stop-color="#E1F5FE"/>
      <stop offset="100%" stop-color="#E1F5FE00"/>
    </radialGradient>
  </defs>
  <rect width="800" height="350" fill="url(#bg3)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">LIGHT BENDING</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff80" font-size="13">Predicted 1915 · Confirmed 1919 (Eddington's eclipse expedition)</text>

  <!-- Distant star -->
  <circle cx="100" cy="175" r="15" fill="url(#starglow)"/>
  <circle cx="100" cy="175" r="6" fill="#fff"/>
  <text x="100" y="210" text-anchor="middle" fill="#E1F5FE" font-size="12">Distant Star</text>

  <!-- Massive object (Sun) -->
  <circle cx="420" cy="175" r="45" fill="#FFD700" opacity="0.15"/>
  <circle cx="420" cy="175" r="30" fill="#FFD700" opacity="0.7"/>
  <text x="420" y="180" text-anchor="middle" fill="#000" font-size="13" font-weight="bold">Sun</text>

  <!-- Observer -->
  <circle cx="720" cy="175" r="10" fill="#4FC3F7"/>
  <text x="720" y="205" text-anchor="middle" fill="#4FC3F7" font-size="12">Observer</text>
  <text x="720" y="220" text-anchor="middle" fill="#4FC3F780" font-size="11">(Earth)</text>

  <!-- Straight line (blocked) -->
  <line x1="115" y1="175" x2="390" y2="175" stroke="#ffffff30" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="250" y="165" fill="#FF6B6B80" font-size="10">Blocked path</text>

  <!-- Bent light path (top) -->
  <path d="M 115 170 Q 260 80, 420 100 Q 550 115, 710 170" fill="none" stroke="#FFEB3B" stroke-width="2.5" opacity="0.8"/>
  <!-- Bent light path (bottom) -->
  <path d="M 115 180 Q 260 270, 420 250 Q 550 235, 710 180" fill="none" stroke="#FFEB3B" stroke-width="2.5" opacity="0.8"/>

  <!-- Apparent positions -->
  <circle cx="200" cy="85" r="4" fill="#fff" opacity="0.5"/>
  <text x="200" y="75" text-anchor="middle" fill="#ffffff60" font-size="10">Apparent</text>
  <text x="200" y="63" text-anchor="middle" fill="#ffffff60" font-size="10">position ↑</text>

  <circle cx="200" cy="265" r="4" fill="#fff" opacity="0.5"/>
  <text x="200" y="290" text-anchor="middle" fill="#ffffff60" font-size="10">Apparent</text>
  <text x="200" y="302" text-anchor="middle" fill="#ffffff60" font-size="10">position ↓</text>

  <!-- Dashed lines from observer to apparent positions -->
  <line x1="710" y1="168" x2="205" y2="87" stroke="#ffffff20" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="710" y1="182" x2="205" y2="263" stroke="#ffffff20" stroke-width="1" stroke-dasharray="4,3"/>

  <!-- Label -->
  <text x="400" y="325" text-anchor="middle" fill="#FFEB3B99" font-size="12" font-style="italic">Light from the star curves around the sun — the star appears shifted</text>

</svg>"""
    save("03_gravitational_lensing.svg", svg)


# ─── DIAGRAM 4: Time Dilation ───────────────────────────────────────────────

def time_dilation():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 420" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg4" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
    <linearGradient id="mountain" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#5D4037"/>
      <stop offset="100%" stop-color="#3E2723"/>
    </linearGradient>
  </defs>
  <rect width="700" height="420" fill="url(#bg4)" rx="12"/>

  <text x="350" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">GRAVITATIONAL TIME DILATION</text>
  <text x="350" y="55" text-anchor="middle" fill="#ffffff80" font-size="13">Closer to mass = slower time · Higher up = faster time</text>

  <!-- Earth surface -->
  <rect x="0" y="340" width="700" height="80" fill="#2E7D32" rx="0"/>
  <text x="350" y="380" text-anchor="middle" fill="#ffffff40" font-size="13">SEA LEVEL</text>

  <!-- Mountain -->
  <polygon points="300,340 400,160 500,340" fill="url(#mountain)"/>
  <polygon points="370,210 400,160 430,210" fill="#fff" opacity="0.3"/>

  <!-- Clock at sea level -->
  <g transform="translate(150, 260)">
    <circle cx="0" cy="0" r="45" fill="#1a1e3a" stroke="#FF6B6B" stroke-width="3"/>
    <text x="0" y="-55" text-anchor="middle" fill="#FF6B6B" font-size="14" font-weight="bold">Twin A</text>
    <text x="0" y="-38" text-anchor="middle" fill="#ffffff60" font-size="11">Sea Level</text>
    <!-- Clock hands -->
    <line x1="0" y1="0" x2="0" y2="-30" stroke="#FF6B6B" stroke-width="3" stroke-linecap="round"/>
    <line x1="0" y1="0" x2="20" y2="10" stroke="#FF6B6B" stroke-width="2" stroke-linecap="round"/>
    <circle cx="0" cy="0" r="3" fill="#FF6B6B"/>
    <!-- Time display -->
    <text x="0" y="65" text-anchor="middle" fill="#FF6B6B" font-size="16" font-weight="bold">10:00:00.000</text>
    <text x="0" y="82" text-anchor="middle" fill="#FF6B6B80" font-size="11">⏱ Time runs SLOWER</text>
  </g>

  <!-- Clock at mountain top -->
  <g transform="translate(550, 120)">
    <circle cx="0" cy="0" r="45" fill="#1a1e3a" stroke="#69F0AE" stroke-width="3"/>
    <text x="0" y="-55" text-anchor="middle" fill="#69F0AE" font-size="14" font-weight="bold">Twin B</text>
    <text x="0" y="-38" text-anchor="middle" fill="#ffffff60" font-size="11">Mountain Top</text>
    <!-- Clock hands (slightly ahead) -->
    <line x1="0" y1="0" x2="3" y2="-30" stroke="#69F0AE" stroke-width="3" stroke-linecap="round"/>
    <line x1="0" y1="0" x2="22" y2="8" stroke="#69F0AE" stroke-width="2" stroke-linecap="round"/>
    <circle cx="0" cy="0" r="3" fill="#69F0AE"/>
    <!-- Time display -->
    <text x="0" y="65" text-anchor="middle" fill="#69F0AE" font-size="16" font-weight="bold">10:00:00.004</text>
    <text x="0" y="82" text-anchor="middle" fill="#69F0AE80" font-size="11">⏱ Time runs FASTER</text>
  </g>

  <!-- Arrow showing altitude difference -->
  <line x1="350" y1="340" x2="350" y2="170" stroke="#ffffff30" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="360" y="255" fill="#ffffff40" font-size="11" transform="rotate(-90, 360, 255)">ALTITUDE</text>

  <!-- Gravity indicator -->
  <text x="350" y="405" text-anchor="middle" fill="#ffffff50" font-size="12">Stronger gravity → more space-time curvature → slower clocks</text>

</svg>"""
    save("04_time_dilation.svg", svg)


# ─── DIAGRAM 5: Black Hole Formation ────────────────────────────────────────

def black_hole():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 320" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg5" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
    <radialGradient id="star_alive" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF9C4"/>
      <stop offset="60%" stop-color="#FFD700"/>
      <stop offset="100%" stop-color="#FF8C00"/>
    </radialGradient>
    <radialGradient id="star_dying" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF8A80"/>
      <stop offset="100%" stop-color="#B71C1C"/>
    </radialGradient>
    <radialGradient id="accretion" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#000"/>
      <stop offset="40%" stop-color="#000"/>
      <stop offset="70%" stop-color="#FF6D0080"/>
      <stop offset="100%" stop-color="#FF6D0000"/>
    </radialGradient>
  </defs>
  <rect width="900" height="320" fill="url(#bg5)" rx="12"/>

  <text x="450" y="30" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">BLACK HOLE: DEATH OF A MASSIVE STAR</text>

  <!-- Stage 1: Living star -->
  <g transform="translate(120, 170)">
    <circle cx="0" cy="0" r="50" fill="url(#star_alive)" opacity="0.9"/>
    <text x="0" y="5" text-anchor="middle" fill="#000" font-size="12" font-weight="bold">Burning</text>
    <text x="0" y="-60" text-anchor="middle" fill="#FFD700" font-size="13" font-weight="bold">1. Massive Star</text>
    <text x="0" y="75" text-anchor="middle" fill="#ffffff50" font-size="10">Hydrogen fusion</text>
    <text x="0" y="88" text-anchor="middle" fill="#ffffff50" font-size="10">pushes outward</text>
  </g>

  <!-- Arrow -->
  <text x="225" y="175" fill="#ffffff40" font-size="24">→</text>

  <!-- Stage 2: Fuel exhausted -->
  <g transform="translate(330, 170)">
    <circle cx="0" cy="0" r="45" fill="url(#star_dying)" opacity="0.8"/>
    <circle cx="0" cy="0" r="20" fill="#424242"/>
    <text x="0" y="5" text-anchor="middle" fill="#fff" font-size="10">Iron</text>
    <text x="0" y="16" text-anchor="middle" fill="#fff" font-size="10">core</text>
    <text x="0" y="-55" text-anchor="middle" fill="#FF8A80" font-size="13" font-weight="bold">2. Fuel Exhausted</text>
    <text x="0" y="70" text-anchor="middle" fill="#ffffff50" font-size="10">No more outward</text>
    <text x="0" y="83" text-anchor="middle" fill="#ffffff50" font-size="10">pressure</text>
  </g>

  <!-- Arrow -->
  <text x="435" y="175" fill="#ffffff40" font-size="24">→</text>

  <!-- Stage 3: Collapse -->
  <g transform="translate(540, 170)">
    <!-- Inward arrows -->
    <line x1="-55" y1="0" x2="-20" y2="0" stroke="#FF6B6B" stroke-width="2"/>
    <line x1="55" y1="0" x2="20" y2="0" stroke="#FF6B6B" stroke-width="2"/>
    <line x1="0" y1="-55" x2="0" y2="-20" stroke="#FF6B6B" stroke-width="2"/>
    <line x1="0" y1="55" x2="0" y2="20" stroke="#FF6B6B" stroke-width="2"/>
    <line x1="-40" y1="-40" x2="-14" y2="-14" stroke="#FF6B6B" stroke-width="2"/>
    <line x1="40" y1="-40" x2="14" y2="-14" stroke="#FF6B6B" stroke-width="2"/>
    <line x1="-40" y1="40" x2="-14" y2="14" stroke="#FF6B6B" stroke-width="2"/>
    <line x1="40" y1="40" x2="14" y2="14" stroke="#FF6B6B" stroke-width="2"/>
    <circle cx="0" cy="0" r="12" fill="#333"/>
    <text x="0" y="-60" text-anchor="middle" fill="#FF6B6B" font-size="13" font-weight="bold">3. Collapse</text>
    <text x="0" y="75" text-anchor="middle" fill="#ffffff50" font-size="10">Gravity crushes</text>
    <text x="0" y="88" text-anchor="middle" fill="#ffffff50" font-size="10">the star inward</text>
  </g>

  <!-- Arrow -->
  <text x="640" y="175" fill="#ffffff40" font-size="24">→</text>

  <!-- Stage 4: Black hole -->
  <g transform="translate(750, 170)">
    <circle cx="0" cy="0" r="55" fill="url(#accretion)"/>
    <circle cx="0" cy="0" r="22" fill="#000" stroke="#ffffff30" stroke-width="1"/>
    <text x="0" y="3" text-anchor="middle" fill="#ffffff60" font-size="9">Event</text>
    <text x="0" y="14" text-anchor="middle" fill="#ffffff60" font-size="9">Horizon</text>
    <text x="0" y="-65" text-anchor="middle" fill="#fff" font-size="13" font-weight="bold">4. Black Hole</text>
    <text x="0" y="75" text-anchor="middle" fill="#ffffff50" font-size="10">Space bent so deeply</text>
    <text x="0" y="88" text-anchor="middle" fill="#ffffff50" font-size="10">nothing escapes</text>
  </g>

</svg>"""
    save("05_black_hole_formation.svg", svg)


# ─── DIAGRAM 6: Gravitational Waves ─────────────────────────────────────────

def gravitational_waves():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg6" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg6)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">GRAVITATIONAL WAVES</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff80" font-size="13">Space itself ripples — like waves on a lake</text>
"""
    # Binary stars at center
    cx, cy = 250, 210
    lines = []

    # Ripple circles emanating outward
    for i in range(12):
        r = 40 + i * 35
        opacity = max(0.05, 0.35 - i * 0.025)
        lines.append(f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#B388FF" stroke-width="1.5" opacity="{opacity:.2f}"/>')

    svg += "\n".join(lines)

    # Binary star system
    svg += f"""
  <!-- Binary stars -->
  <circle cx="{cx - 20}" cy="{cy}" r="15" fill="#FFD700" opacity="0.9"/>
  <circle cx="{cx + 20}" cy="{cy}" r="12" fill="#FF8C00" opacity="0.9"/>

  <!-- Orbit indicator -->
  <ellipse cx="{cx}" cy="{cy}" rx="28" ry="12" fill="none" stroke="#ffffff30" stroke-width="1" stroke-dasharray="3,3"/>

  <text x="{cx}" y="{cy + 50}" text-anchor="middle" fill="#FFD700" font-size="12">Binary star system</text>
  <text x="{cx}" y="{cy + 65}" text-anchor="middle" fill="#ffffff50" font-size="11">spiraling inward</text>

  <!-- Right side: wave pattern (signal) -->
  <rect x="480" y="80" width="300" height="230" fill="#ffffff08" rx="8" stroke="#ffffff15" stroke-width="1"/>
  <text x="630" y="105" text-anchor="middle" fill="#B388FF" font-size="14" font-weight="bold">Detected Signal</text>
  <text x="630" y="120" text-anchor="middle" fill="#ffffff50" font-size="10">(like LIGO observed in 2015)</text>

  <!-- Axes -->
  <line x1="500" y1="200" x2="760" y2="200" stroke="#ffffff30" stroke-width="1"/>
  <line x1="500" y1="140" x2="500" y2="260" stroke="#ffffff30" stroke-width="1"/>
  <text x="760" y="215" fill="#ffffff40" font-size="10">time →</text>
  <text x="485" y="143" fill="#ffffff40" font-size="10">strain</text>
"""
    # Draw a chirp signal (increasing frequency and amplitude)
    wave_points = []
    for x_px in range(510, 750):
        t = (x_px - 510) / 240.0  # 0 to 1
        freq = 2 + t * 12  # increasing frequency
        amp = 10 + t * 40   # increasing amplitude
        y_val = 200 + amp * math.sin(freq * t * math.pi * 2)
        wave_points.append(f"{x_px},{y_val:.1f}")

    svg += f'  <polyline points="{" ".join(wave_points)}" fill="none" stroke="#B388FF" stroke-width="2"/>\n'

    svg += """
  <!-- Annotations -->
  <text x="540" y="280" fill="#ffffff40" font-size="10">Low frequency</text>
  <text x="700" y="280" fill="#ffffff40" font-size="10">Chirp!</text>

  <text x="400" y="380" text-anchor="middle" fill="#B388FF80" font-size="12" font-style="italic">Predictions match observations to 1 part in 100,000,000,000</text>

</svg>"""
    save("06_gravitational_waves.svg", svg)


# ─── DIAGRAM 7: Einstein's Equation Annotated ───────────────────────────────

def equation_breakdown():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 350" font-family="'Segoe UI', Arial, sans-serif">
  <defs>
    <linearGradient id="bg7" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e27"/>
      <stop offset="100%" stop-color="#1a1e3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="350" fill="url(#bg7)" rx="12"/>

  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">EINSTEIN'S FIELD EQUATION — DECODED</text>
  <text x="400" y="55" text-anchor="middle" fill="#ffffff80" font-size="13">"Half a line that contains a teeming universe"</text>

  <!-- The equation -->
  <text x="400" y="130" text-anchor="middle" fill="#fff" font-size="42" font-weight="bold" font-family="'Georgia', serif">
    R<tspan font-size="24" dy="8">ab</tspan><tspan dy="-8"> − ½ R g</tspan><tspan font-size="24" dy="8">ab</tspan><tspan dy="-8"> = T</tspan><tspan font-size="24" dy="8">ab</tspan>
  </text>

  <!-- Bracket annotations -->
  <!-- R_ab -->
  <line x1="175" y1="150" x2="175" y2="185" stroke="#FF6B6B" stroke-width="2"/>
  <line x1="175" y1="185" x2="280" y2="185" stroke="#FF6B6B" stroke-width="2"/>
  <line x1="280" y1="150" x2="280" y2="185" stroke="#FF6B6B" stroke-width="2"/>
  <text x="227" y="205" text-anchor="middle" fill="#FF6B6B" font-size="13" font-weight="bold">Ricci Curvature</text>
  <text x="227" y="222" text-anchor="middle" fill="#FF6B6B80" font-size="11">How space is curved</text>

  <!-- ½ R g_ab -->
  <line x1="300" y1="150" x2="300" y2="255" stroke="#FFEB3B" stroke-width="2"/>
  <line x1="300" y1="255" x2="475" y2="255" stroke="#FFEB3B" stroke-width="2"/>
  <line x1="475" y1="150" x2="475" y2="255" stroke="#FFEB3B" stroke-width="2"/>
  <text x="387" y="275" text-anchor="middle" fill="#FFEB3B" font-size="13" font-weight="bold">Scalar Curvature × Metric</text>
  <text x="387" y="292" text-anchor="middle" fill="#FFEB3B80" font-size="11">Overall shape of space-time</text>

  <!-- = -->
  <text x="515" y="200" text-anchor="middle" fill="#69F0AE" font-size="28" font-weight="bold">=</text>

  <!-- T_ab -->
  <line x1="545" y1="150" x2="545" y2="185" stroke="#4FC3F7" stroke-width="2"/>
  <line x1="545" y1="185" x2="650" y2="185" stroke="#4FC3F7" stroke-width="2"/>
  <line x1="650" y1="150" x2="650" y2="185" stroke="#4FC3F7" stroke-width="2"/>
  <text x="597" y="205" text-anchor="middle" fill="#4FC3F7" font-size="13" font-weight="bold">Stress-Energy Tensor</text>
  <text x="597" y="222" text-anchor="middle" fill="#4FC3F780" font-size="11">Where matter and energy are</text>

  <!-- The punchline -->
  <rect x="150" y="310" width="500" height="30" fill="#69F0AE15" rx="6"/>
  <text x="400" y="330" text-anchor="middle" fill="#69F0AE" font-size="14" font-weight="bold">GEOMETRY OF SPACE = DISTRIBUTION OF MATTER</text>

</svg>"""
    save("07_equation_breakdown.svg", svg)


# ─── Run all ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    newton_vs_einstein()
    marble_in_funnel()
    gravitational_lensing()
    time_dilation()
    black_hole()
    gravitational_waves()
    equation_breakdown()
    print("\nAll diagrams generated!")
