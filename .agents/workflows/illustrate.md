---
description: Create programmatic diagrams and pull real-world photos to illustrate a chapter.
---

# Illustrate Workflow

Generate visual aids for a chapter, making dense physics (or any technical content) easier to digest. Uses programmatic SVG diagrams and real-world photographs, never AI-generated images.

## Prerequisites

- The chapter MUST already be unshittified (run `/unshit` first)
- The chapter file must exist at `unshittified/<book-name>/XX-chapter-title.md`
- If it doesn't exist, tell the user to run `/unshit` first

## Steps

### 1. Identify the chapter

Ask the user which chapter to illustrate (by number, title, or description). If they already specified it in their message, use that.

### 2. Read the chapter and identify key concepts

Read the unshittified chapter and list every concept that would benefit from a visual:

- **Conceptual shifts** (e.g., Newton vs Einstein, wave vs particle)
- **Physical processes** (e.g., star collapse, light bending)
- **Diagrams the author describes in words** (e.g., "like a marble in a funnel")
- **Equations** that can be annotated/decoded visually
- **Timeline/sequence** events (e.g., stages of a process)
- **Comparisons** (e.g., two clocks at different altitudes)

### 3. Create programmatic SVG diagrams

Write a Python script at `images/<chN>/generate_diagrams.py` that generates SVG files. Follow these rules:

1. **No dependencies.** Pure Python, raw SVG XML strings. No matplotlib, no PIL, no external libraries.
2. **Dark theme.** Background `#0a0e27` to `#1a1e3a`, white/colored text and elements.
3. **Math-driven where possible.** Use actual formulas for curves (e.g., `1/r²` falloff for gravity, `sin()` for waves). Don't fake physics with hand-drawn beziers when the real math is simple.
4. **Clean labels.** Every diagram should be self-explanatory without reading the chapter text.
5. **One function per diagram.** Makes it easy to tweak individual visuals later.
6. **Color coding.** Use consistent colors across diagrams:
   - `#FF6B6B` for "old/wrong/Newtonian" concepts
   - `#69F0AE` for "new/correct/Einsteinian" concepts
   - `#FFD700` for stars/sun/energy
   - `#4FC3F7` for Earth/observer/cool objects
   - `#B388FF` for waves/quantum/abstract
   - `#FFEB3B` for light/photons

Run the script to generate all SVGs:

```bash
python3 unshittified/<book-name>/images/<chN>/generate_diagrams.py
```

### 4. Pull real-world photographs

Search for real photographs that illustrate the chapter's predictions or phenomena:

1. **Prefer public domain or CC-licensed images** from NASA, ESA, ESO, Wikimedia Commons
2. **Download with curl** to `images/<chN>/`
3. **Verify each download** with `file <path>` to ensure it's actually an image (not an HTML error page)
4. **If Wikimedia blocks direct curl**, try adding `-A "Mozilla/5.0"` or use a different source (NASA, ESO, EHT)
5. **Delete failed downloads** immediately

### 5. Add source references to real-world photos

Every real-world photo MUST have a reference block directly below it in the markdown:

```markdown
![Description of the image](images/chN/filename.jpg)

> **Source:** Credit line · [License](url) · [Source link](url)
```

Programmatic SVGs do NOT need references (they're originals).

### 6. Update the chapter markdown

Weave the images into the chapter at the exact points where they aid understanding:

- Place each image **after** the paragraph that introduces the concept it illustrates
- Use descriptive alt text in `![alt text](path)` format
- For prediction sections, pair the programmatic diagram (explaining the concept) with the real photo (showing the evidence)
- Never use em dashes in alt text. Use colons instead.

### 7. Report back

- List all diagrams created with a one-line description of each
- List all real-world photos with their source/credit
- Note any images that failed to download
- Ask if the user wants diagrams for more chapters

## File structure

```
unshittified/<book-name>/
  images/
    ch1/
      generate_diagrams.py    # Generator script
      01_concept_name.svg     # Programmatic diagrams
      02_concept_name.svg
      real_photo_name.jpg     # Downloaded photos
    ch2/
      ...
```
