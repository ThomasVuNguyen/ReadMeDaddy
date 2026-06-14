#!/usr/bin/env python3
"""Parse an epub file and output JSON with title, author, and chapters."""

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

try:
    import ebooklib
    from ebooklib import epub
except ImportError:
    print("Installing ebooklib...", file=sys.stderr)
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "ebooklib", "-q"])
    import ebooklib
    from ebooklib import epub


class HTMLTextExtractor(HTMLParser):
    """Strip HTML tags and extract plain text."""

    def __init__(self):
        super().__init__()
        self.result = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip = True
        elif tag in ("p", "div", "br", "h1", "h2", "h3", "h4", "h5", "h6", "li", "blockquote"):
            self.result.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip = False
        elif tag in ("p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "li", "blockquote"):
            self.result.append("\n")

    def handle_data(self, data):
        if not self._skip:
            self.result.append(data)

    def get_text(self):
        text = "".join(self.result)
        # Collapse multiple blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def html_to_text(html_content: str) -> str:
    extractor = HTMLTextExtractor()
    extractor.feed(html_content)
    return extractor.get_text()


def extract_title_from_html(html_content: str) -> str | None:
    """Try to extract a heading from the HTML content."""
    for pattern in [
        r"<h[1-3][^>]*>(.*?)</h[1-3]>",
        r"<title>(.*?)</title>",
    ]:
        match = re.search(pattern, html_content, re.IGNORECASE | re.DOTALL)
        if match:
            title = re.sub(r"<[^>]+>", "", match.group(1)).strip()
            if title and len(title) < 200:
                return title
    return None


def parse_epub(epub_path: str) -> dict:
    book = epub.read_epub(epub_path, options={"ignore_ncx": False})

    # Get metadata
    title = "Unknown"
    author = "Unknown"

    title_meta = book.get_metadata("DC", "title")
    if title_meta:
        title = title_meta[0][0]

    author_meta = book.get_metadata("DC", "creator")
    if author_meta:
        author = author_meta[0][0]

    # Try to use TOC for chapter ordering/naming
    toc_titles = []
    if book.toc:
        for item in book.toc:
            if isinstance(item, epub.Link):
                toc_titles.append(item.title)
            elif isinstance(item, tuple):
                section, links = item
                if hasattr(section, "title"):
                    toc_titles.append(section.title)
                for link in links:
                    if isinstance(link, epub.Link):
                        toc_titles.append(link.title)

    # Extract chapters
    chapters = []
    toc_idx = 0

    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        content = item.get_content().decode("utf-8", errors="replace")
        text = html_to_text(content)

        # Skip very short items (likely navigation, copyright, etc.)
        if len(text.strip()) < 100:
            continue

        # Determine chapter title
        chapter_title = extract_title_from_html(content)
        if not chapter_title and toc_idx < len(toc_titles):
            chapter_title = toc_titles[toc_idx]
        if not chapter_title:
            chapter_title = f"Chapter {len(chapters) + 1}"

        chapters.append({
            "title": chapter_title,
            "text": text,
            "word_count": len(text.split()),
        })
        toc_idx += 1

    return {
        "title": title,
        "author": author,
        "total_chapters": len(chapters),
        "chapters": chapters,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: parse_epub.py <path-to-epub>", file=sys.stderr)
        sys.exit(1)

    result = parse_epub(sys.argv[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
