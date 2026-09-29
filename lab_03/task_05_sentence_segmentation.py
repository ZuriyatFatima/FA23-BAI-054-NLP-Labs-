"""Lab 03 - Task 5: Sentence Segmentation (Handling Tricky Cases)"""
import spacy

# a) load trained pipeline (run: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

paragraph = ("Dr. Ahmed met Mr. Khan at the conference in Lahore. "
             "They discussed NLP tools, e.g. spaCy and NLTK, for two hours. "
             "Later, Prof. Ali joined them for lunch.")
doc = nlp(paragraph)

# b) split into sentences
print("b) Sentences:")
for i, sent in enumerate(doc.sents, 1):
    print(f"   {i}. {sent.text}")

# c) total count
sentences = list(doc.sents)
print("\nc) Total sentences detected:", len(sentences))

# d) observation
print("\nd) Observation: The abbreviations 'Dr.', 'Mr.', 'e.g.' and 'Prof.' did NOT cause "
      "incorrect breaks, because the trained parser uses context (and tokenizer exceptions) "
      "rather than just splitting on every full stop.")
