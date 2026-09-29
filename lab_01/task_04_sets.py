"""Lab 01 - Task 04: Sets for Unique Vocabulary"""

# (a)
raw = ["nlp", "ai", "nlp", "deep", "learning", "ai", "nlp", "python"]
vocab = set(raw)
print("(a) raw   :", raw)
print("    vocab :", vocab)
print("    Unique words:", len(vocab))
# A set is backed by a hash table and stores each element at most once: when an
# element that is already present (same hash and equal value) is added again, the
# set simply ignores it, so duplicates disappear automatically.

# (b)
set_A = {"machine", "learning", "data", "model"}
set_B = {"deep", "learning", "neural", "data"}
print("\n(b-i)   Union        :", set_A | set_B)
print("(b-ii)  Intersection :", set_A & set_B)
print("(b-iii) A - B        :", set_A - set_B)

# (c)
stopwords = {"is", "the", "a", "in", "of", "and", "to"}
tokens = ["nlp", "is", "a", "field", "of", "ai", "and", "the", "future"]
# Set difference removes stopwords but loses order/duplicates, so restore order after.
remaining = set(tokens) - stopwords
cleaned = [t for t in tokens if t in remaining]
print("\n(c) Cleaned tokens:", cleaned)

# (d)
vocab.add("transformer")
vocab.add("bert")
vocab.discard("python")
print("\n(d) 'ai' still present:", "ai" in vocab)
print("    Final set        :", vocab)
