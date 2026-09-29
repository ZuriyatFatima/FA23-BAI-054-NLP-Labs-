"""Lab 02 - Task 2: Structured Page Metadata Extraction and CSV Export

Usage: python task_02_pdf_metadata_csv.py [pdf_path] [phrase]
"""
import csv
import sys
from pathlib import Path

import pdfplumber

HERE = Path(__file__).parent
PDF_PATH = sys.argv[1] if len(sys.argv) > 1 else HERE / "data" / "sample_report.pdf"


class PhraseNotFoundError(Exception):
    """Raised when a search phrase does not occur on any page."""


# (a) build pages_data
pages_data = []
with pdfplumber.open(PDF_PATH) as pdf:
    for i, page in enumerate(pdf.pages, start=1):
        text = page.extract_text() or ""
        pages_data.append({
            "page_number": i,
            "raw_text": text,
            "word_count": len(text.split()),
            "char_count": len(text.replace(" ", "").replace("\n", "")),   # excluding spaces
        })
print(f"(a) {len(pages_data)} pages read. First 2 entries:")
for entry in pages_data[:2]:
    print("   ", entry)

# (b) statistics
non_zero = [p for p in pages_data if p["word_count"] > 0]
if non_zero:
    highest = max(pages_data, key=lambda p: p["word_count"])
    lowest = min(non_zero, key=lambda p: p["word_count"])
    print(f"\n(b-i)  Highest word count: page {highest['page_number']} ({highest['word_count']} words)")
    print("       Content:", highest["raw_text"])
    print(f"(b-ii) Lowest non-zero word count: page {lowest['page_number']} ({lowest['word_count']} words)")
else:
    print("\n(b) All pages are empty - no statistics available.")
average = round(sum(p["word_count"] for p in pages_data) / len(pages_data), 2) if pages_data else 0
print("(b-iii) Average word count:", average)

# (c) case-insensitive phrase search
phrase = (sys.argv[2] if len(sys.argv) > 2 else input("\n(c) Enter a search phrase: ")).strip()
try:
    hits = [(p["page_number"], p["raw_text"].lower().count(phrase.lower()))
            for p in pages_data if phrase and phrase.lower() in p["raw_text"].lower()]
    if not hits:
        raise PhraseNotFoundError(f"The phrase '{phrase}' was not found on any page.")
    for page_no, count in hits:
        print(f"    Page {page_no}: '{phrase}' appears {count} time(s)")
except PhraseNotFoundError as err:
    print("    PhraseNotFoundError caught:", err)

# (d) write and re-read CSV (csv module only)
csv_path = HERE / "pdf_summary.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["page_number", "word_count", "char_count"])
    for p in pages_data:
        writer.writerow([p["page_number"], p["word_count"], p["char_count"]])

print(f"\n(d) Contents of {csv_path.name}:")
with open(csv_path, newline="", encoding="utf-8") as f:
    for row in csv.reader(f):
        print("   ", row)
