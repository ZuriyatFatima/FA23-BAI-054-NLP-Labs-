# NLP Labs (Lab 01 – Lab 05)

Solutions for the "Python Essentials for NLP" lab series. Every task is a separate, runnable script
with the sub-parts (a), (b), (c), (d) labelled in the output.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -c "import nltk; [nltk.download(p) for p in ('punkt','punkt_tab','stopwords')]"
```

## Structure
| Folder | Contents |
|---|---|
| `lab_01/` | Python essentials: strings, lists, dicts, sets, tuples, string methods, functions/lambda, map/filter/Counter (9 tasks) |
| `lab_02/` | PDF & DOCX extraction, preprocessing, REST API joins and analysis (9 tasks) |
| `lab_03/` | Regex, NLTK vs spaCy tokenization, token attributes, sentence segmentation (5 tasks) |
| `lab_04/` | Text preprocessing: lowercasing, noise removal, stop-words, stemming, lemmatization, pipeline, edit distance, spelling correction (9 tasks, notebook) |
| `lab_05/` | N-gram language models: unigram/bigram/trigram, MLE, smoothing, perplexity (9 tasks, notebook, standard library only) |

## Running
```bash
python lab_01/task_01_strings.py

# Lab 02 - sample input files live in lab_02/data (regenerate with create_sample_data.py).
# Pass your own file as an argument, and the keyword/phrase to skip the input() prompt:
python lab_02/task_01_pdf_word_frequency.py lab_02/data/sample_report.pdf nlp
python lab_02/task_02_pdf_metadata_csv.py
python lab_02/task_06_docx_comparison.py lab_02/data/doc_a.docx lab_02/data/doc_b.docx

# Lab 02 tasks 7-9 need internet access (jsonplaceholder.typicode.com)
python lab_02/task_07_api_join.py

python lab_03/task_05_sentence_segmentation.py
```

## Notes
- Lab 02 tasks 1–6 use generated sample files (`lab_02/data`); swap in your own PDF/DOCX files if required by your instructor.
- Files produced by the scripts (`pdf_summary.csv`, `nlp_ready_output.txt`, `docx_extracted.txt`) are committed as sample output.
