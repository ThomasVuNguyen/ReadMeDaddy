---
description: Parse an epub, read the entire book for context, and create a chapter overview.
---

# Read Book Workflow

Parse an epub, read the entire book for context, and create a chapter overview.

## Steps

### 1. Find the epub

Look in the `epub/` folder for epub files. If there are multiple, ask which one. If there's only one, use it.

### 2. Parse the epub

Run the parser script from the project root:

```bash
python3 .gemini/skills/read-epub/scripts/parse_epub.py "epub/<filename>.epub"
```

This outputs JSON with title, author, and all chapters with their full text.

### 3. Read the full book

Read through ALL chapter content from the parser output. Internalize:
- The book's core thesis and argument
- The logical thread connecting chapters
- Which details are load-bearing vs filler
- Key recurring concepts and terms

### 4. Create the book output folder

Create the directory:

```
unshittified/<book-name-kebab-case>/
```

### 5. Write the overview file

Create `unshittified/<book-name>/00-overview.md` with:

```markdown
# <Book Title>
**Author:** <Author Name>

## What This Book Is About
<3-5 sentence summary of the book's core thesis>

## Chapter Map
1. **<Chapter Title>** — <One line: what this chapter's role is in the overall argument>
2. **<Chapter Title>** — <...>
...
```

### 6. Report back

Tell the user:
- Book has been parsed and read
- Number of chapters found
- Quick summary of what it's about
- Ask which chapter to unshittify first (they can use `/unshit` for that)