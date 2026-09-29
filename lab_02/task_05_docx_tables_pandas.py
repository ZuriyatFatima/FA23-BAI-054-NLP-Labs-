"""Lab 02 - Task 5: DOCX Table Extraction and Pandas Integration

Usage: python task_05_docx_tables_pandas.py [docx_path]
"""
import sys
from pathlib import Path

import pandas as pd
from docx import Document
from docx.text.paragraph import Paragraph

HERE = Path(__file__).parent
DOCX_PATH = sys.argv[1] if len(sys.argv) > 1 else HERE / "data" / "doc_a.docx"
doc = Document(DOCX_PATH)

# (a) tables as list of lists
tables = [[[cell.text for cell in row.cells] for row in table.rows] for table in doc.tables]
print("(a) Total tables found:", len(tables))
for i, t in enumerate(tables, start=1):
    print(f"    Table {i}: {len(t)} rows x {len(t[0]) if t else 0} columns")
if not tables:
    sys.exit("No tables found in the document.")

# (b) DataFrame from the first table
first = tables[0]
df = pd.DataFrame(first[1:], columns=first[0])
print("\n(b) DataFrame:\n", df.to_string())
empty_per_col = df.apply(lambda col: col.map(lambda v: v is None or str(v).strip() == "").sum())
print("\n    Empty/None cells per column:\n", empty_per_col.to_string())

# (c) paragraphs before the first table
pre_table = []
for child in doc.element.body.iterchildren():
    if child.tag.endswith("}tbl"):
        break
    if child.tag.endswith("}p"):
        pre_table.append(Paragraph(child, doc).text)
print("\n(c) Paragraphs before the first table:", len(pre_table))

# (d) write both to a labelled text file
out_path = HERE / "docx_extracted.txt"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("--- PRE-TABLE PARAGRAPHS ---\n")
    for text in pre_table:
        if text.strip():                       # skip blank paragraphs in the file
            f.write(text + "\n")
    f.write("\n--- TABLE DATA ---\n")
    for row in first:
        f.write(" | ".join(row) + "\n")
print(f"\n(d) Written to {out_path.name}:\n")
print(out_path.read_text(encoding="utf-8"))
