"""Lab 02 - Task 1: Multi-Page PDF Extraction with Word Frequency Analysis

Usage: python task_01_pdf_word_frequency.py [pdf_path] [keyword]
"""
import re
import sys
from collections import Counter
from pathlib import Path

import pdfplumber

PDF_PATH = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "data" / "sample_report.pdf"

STOPWORDS = {"the", "is", "a", "an", "and", "or", "of", "to", "in", "on", "for", "it", "as",
             "are", "was", "were", "be", "by", "with", "that", "this", "at", "from", "can",
             "has", "have", "their", "also", "such", "these", "which", "so", "more"}

# (a) page-wise extraction
with pdfplumber.open(PDF_PATH) as pdf:
    pages = [(page.extract_text() or "") for page in pdf.pages]
print("(a) Total pages extracted:", len(pages))

# (b) merge, clean, tokenise
full_text = " ".join(pages)
clean = re.sub(r"[^\w\s]|\d|_", "", full_text).lower()
tokens = clean.split()
print("(b) Total token count:", len(tokens))

# (c) word frequency without stopwords
freq = Counter(t for t in tokens if t not in STOPWORDS)
print(f"(c) Removed {len(STOPWORDS)} stopwords. Top 10 words:")
for word, count in freq.most_common(10):
    print(f"    {word:15} {count}")

# (d) keyword search with page numbers
keyword = (sys.argv[2] if len(sys.argv) > 2 else input("(d) Enter a keyword to search: ")).strip().lower()
found = False
for page_no, text in enumerate(pages, start=1):
    text = re.sub(r"\s+", " ", text)                    # join wrapped lines
    for sentence in re.split(r"(?<=[.!?])\s+", text):
        if keyword and keyword in sentence.lower():
            print(f"    [Page {page_no}] {sentence.strip()}")
            found = True
if not found:
    print(f"    No sentence containing '{keyword}' was found.")
