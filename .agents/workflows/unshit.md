---
description: Rewrite a chapter — strip the filler, merge the fluff, keep the science.
---

# Unshit Workflow

Rewrite a chapter from the current book — strip the filler, merge the fluff, keep the science.

## Prerequisites

- The book MUST have already been read using the `/read-books` workflow
- The `unshittified/<book-name>/00-overview.md` file must exist
- If these don't exist, tell the user to run `/read-books` first

## Steps

### 1. Identify the chapter

Ask the user which chapter to unshittify (by number, title, or description). If they already specified it in their message, use that. If ambiguous, confirm.

### 2. Get the chapter content

Run the parser again (or use cached output) to get the full text of the target chapter:

```bash
python3 .gemini/skills/read-epub/scripts/parse_epub.py "epub/<filename>.epub"
```

Extract the specific chapter's content from the JSON output.

### 3. Analyze the chapter

Before rewriting, identify:
- **Core point**: What is this chapter actually trying to say?
- **Load-bearing paragraphs**: Real ideas, key concepts, essential context
- **Filler**: Padding, excessive backstory, repetitive explanations, tangential anecdotes
- **Bridging content**: Keep good transitions, cut fluffy ones

### 4. Rewrite using these rules (in priority order)

1. **Preserve the science / core ideas** — Every real concept, theory, finding MUST survive. Cut the packaging, not the product.
2. **Compress, don't delete** — If a paragraph has some value but is 80% fluff, compress it to its core sentences. Only fully delete zero-value content.
3. **Merge related paragraphs** — When 3 paragraphs circle the same point, merge them into one. Pick the best way the author said it.
4. **Cut biographical/historical filler** — "Einstein was born in Ulm..." → cut. "Einstein developed GR because..." → keep.
5. **Keep genuinely illuminating examples** — Test: would a smart reader lose understanding without this? If yes, keep.
6. **Maintain the author's logical order** — Same sequence, just tighter.
7. **Write in clear, direct prose** — Short sentences, active voice, no academic throat-clearing ("It is worth noting that...").
8. **Anchor new concepts to familiar things** — When introducing something the reader hasn't seen before, immediately compare it to something they already know. "A sort of terms and conditions notice" beats "a constitutional charter limiting royal authority."
9. **Strip names from overviews, keep them in chapters** — In summaries and chapter descriptions, replace names with roles ("a pathologist," "a surgeon") unless the name is the book's protagonist. Names matter when you're IN the chapter, not when you're scanning the map.
10. **Every fact pays off now or gets cut** — If a sentence is setup for something three paragraphs away, move the payoff closer or compress both into one sentence. The reader should never be holding unresolved information.
11. **Stakes before details** — Information only flows into the brain when the brain has a reason to receive it. Open sections with *why this matters* (the stakes, the tension, the problem), not *what things looked like* (setting, atmosphere, scene-painting). Details land after the reader is invested, never before. "Every child with leukemia died" → then describe the guy who tried to change that. Not: "In a damp basement lab..." → then explain why the lab matters.
12. **Introduce people through contradiction, not credentials** — A character becomes interesting when there's a gap between what they are and what they do. "A doctor of the dead who had never treated a living patient started injecting dying children with chemicals" makes you care. "A pathologist who graduated from Harvard and became chief of pathology at Children's Hospital" is a LinkedIn profile. Lead with the tension.
13. **One unresolved thing at a time** — The brain can hold one open question while reading. Not three. If a sentence introduces a concept, resolve it before loading the next one. Don't stack "swollen spleen" + "choked with white cells" + "white cells mean infection" + "suppuration" and then finally deliver the twist. Each sentence completes its thought before the next one opens. "Drew blood, found it thick with white cells" → done. "White cells normally mean infection, like pus from a wound" → anchored, done. "Except there was no infection" → twist, done.
14. **Once the reader gets it, stop** — If you say "there was no infection," don't follow with "No wound. No abscess. No fever." The reader understood at "no infection." Repeating it three ways doesn't make it stickier, it makes the reader feel like you don't trust them. One clean beat, then move on.

### 5. Determine compression level

Default to **medium** unless the user specifies:
- **Light**: Trim obvious filler, keep most examples. ~20-30% reduction.
- **Medium**: Cut filler, merge redundant paragraphs, tighten prose. ~40-60% reduction.
- **Heavy**: Aggressive. Only core concepts and essential examples survive. ~60-80% reduction.

### 6. Save the output

Write to `unshittified/<book-name>/XX-chapter-title.md`:

```markdown
# Chapter N: Title

<Rewritten chapter content>

---

*Original: ~X paragraphs → Unshittified: ~Y paragraphs*
```

### 7. Report back

- Give a 2-3 sentence summary of what the chapter covers
- Briefly mention what was cut and why (e.g., "cut 3 paragraphs of Einstein biography, merged 4 spacetime paragraphs into 2")
- Ask if the compression level is right (too aggressive? too gentle?)
- Ask which chapter to do next