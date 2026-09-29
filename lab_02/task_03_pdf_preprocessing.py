"""Lab 02 - Task 3: PDF Text Preprocessing Pipeline for NLP

Usage: python task_03_pdf_preprocessing.py [pdf_path]
"""
import re
import sys
from pathlib import Path

import nltk
import pdfplumber
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)

HERE = Path(__file__).parent
PDF_PATH = sys.argv[1] if len(sys.argv) > 1 else HERE / "data" / "sample_report.pdf"

# (a) extract and clean
with pdfplumber.open(PDF_PATH) as pdf:
    text = "\n".join((p.extract_text() or "") for p in pdf.pages)
before = len(text)

text = re.sub(r"(https?://\S+|www\.\S+)", "", text)      # (i) remove URLs
text = re.sub(r"\d", "", text)                           # (ii) remove digits
text = re.sub(r"[^A-Za-z. ]", " ", text)                 # (iii) keep letters, spaces, full stops
#   (newlines become spaces here so that words on adjacent lines are not glued together)
text = re.sub(r" {2,}", " ", text)                       # (iv) collapse multiple spaces
print(f"(a) Characters before cleaning: {before}\n    Characters after cleaning : {len(text)}")

# (b) sentences
text = text.lower()
raw_sentences = [s.strip() for s in re.split(r"[.!?]", text)]
sentences = [s for s in raw_sentences if s]
print(f"\n(b) Sentence count before removing empties: {len(raw_sentences)}")
print(f"    Sentence count after removing empties : {len(sentences)}")

# (c) tokenise, remove stopwords, filter short sentences
stop_set = set(stopwords.words("english"))
processed = []
for s in sentences:
    tokens = [w for w in re.findall(r"[a-z]+", s) if w not in stop_set]
    if len(tokens) >= 5:
        processed.append(s)
print(f"\n(c) Sentences before filter: {len(sentences)}\n    Sentences after filter : {len(processed)}")
print("    Sample sentences:")
for s in processed[:3]:
    print("     -", s)

# (d) write, re-read, report
out_path = HERE / "nlp_ready_output.txt"
out_path.write_text("\n".join(processed) + "\n", encoding="utf-8")
lines = [ln.rstrip("\n") for ln in out_path.read_text(encoding="utf-8").splitlines()]
print(f"\n(d) Total lines written  : {len(lines)}")
print("    Longest sentence     :", max(lines, key=len))
print("    Shortest sentence    :", min(lines, key=len))
