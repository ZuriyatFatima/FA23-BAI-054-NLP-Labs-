"""Lab 01 - Task 08: Functions and Lambda for NLP Pipelines"""

# (a)
def clean(text):
    text = text.strip()
    return text.lower()

clean_lambda = lambda text: text.strip().lower()

sample = "  HELLO Natural Language Processing  "
print("(a) clean()        :", repr(clean(sample)))
print("    clean_lambda() :", repr(clean_lambda(sample)))

# (b)
def tokenize(text):
    return text.split()

def remove_short(tokens, n):
    return [t for t in tokens if len(t) > n]

sentence = "I love working with NLP tools in Python daily"
print("\n(b) Chained result:", remove_short(tokenize(sentence), 3))

# (c)
def word_lengths(tokens):
    return {word: len(word) for word in tokens}

print("\n(c) word_lengths:", word_lengths(["language", "model", "ai", "processing", "deep"]))

# (d)
def nlp_pipeline(text, min_len):
    cleaned = clean(text)
    tokens = tokenize(cleaned)
    tokens = remove_short(tokens, min_len)
    return word_lengths(tokens)

print("\n(d) Pipeline outputs:")
print("   ", nlp_pipeline("  Natural Language Processing is FUN and Powerful  ", 3))
print("   ", nlp_pipeline("Transformers changed the field of NLP completely", 4))
