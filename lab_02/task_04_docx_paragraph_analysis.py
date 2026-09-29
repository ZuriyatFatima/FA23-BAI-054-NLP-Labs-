"""Lab 02 - Task 4: DOCX Paragraph Classification and Statistical Analysis

Usage: python task_04_docx_paragraph_analysis.py [docx_path]
"""
import sys
from pathlib import Path
from pprint import pprint

from docx import Document

DOCX_PATH = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "data" / "doc_a.docx"
doc = Document(DOCX_PATH)

# (a) text + style for each paragraph
paragraphs = [{"text": p.text, "style": p.style.name} for p in doc.paragraphs]
print("(a) Total paragraphs:", len(paragraphs))
print("    Unique style names:", sorted({p["style"] for p in paragraphs}))

# (b) classification
headings, body, other = [], [], []
for p in paragraphs:
    if not p["text"].strip():
        other.append(p)                                   # blank paragraphs always go to Other
    elif p["style"].startswith("Heading"):
        headings.append(p)
    elif p["style"] == "Normal" or "Body" in p["style"]:
        body.append(p)
    else:
        other.append(p)
print(f"\n(b) Headings: {len(headings)} | Body: {len(body)} | Other/Empty: {len(other)}")

# (c) statistics on body paragraphs with > 5 words
qualifying = []
for p in body:
    words = p["text"].split()
    if len(words) > 5:
        qualifying.append({**p, "word_count": len(words),
                           "char_count": len(p["text"].replace(" ", ""))})
if qualifying:
    top = max(qualifying, key=lambda p: p["word_count"])
    low = min(qualifying, key=lambda p: p["word_count"])
    mean = round(sum(p["word_count"] for p in qualifying) / len(qualifying), 2)
    print(f"\n(c-i)   Highest word count ({top['word_count']} words): {top['text']}")
    print(f"(c-ii)  Lowest word count above 5 ({low['word_count']} words): {low['text']}")
    print("(c-iii) Mean word count:", mean)
else:
    print("\n(c) No body paragraph has more than 5 words.")

# (d) nested dictionary by style, sorted by count (descending)
by_style = {}
for p in paragraphs:
    entry = by_style.setdefault(p["style"], {"count": 0, "texts": []})
    entry["count"] += 1
    entry["texts"].append(p["text"])
for entry in by_style.values():
    if entry["count"] > 2:
        entry["texts"] = entry["texts"][:2]               # show only the first 2 texts
by_style = dict(sorted(by_style.items(), key=lambda kv: kv[1]["count"], reverse=True))
print("\n(d) Style summary:")
pprint(by_style, width=100, sort_dicts=False)
