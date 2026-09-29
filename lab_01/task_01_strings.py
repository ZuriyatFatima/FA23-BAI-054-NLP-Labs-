"""Lab 01 - Task 01: Strings as Text Storage"""

# (a)
sentence = "Artificial Intelligence is transforming Natural Language Processing"
print("(a) Sentence :", sentence)
print("    Type     :", type(sentence))
print("    Length   :", len(sentence))

# (b)
first_word = sentence[:10]          # "Artificial" occupies indices 0-9
last_char = sentence[-1]
lang_start = sentence.find("Language")
language = sentence[lang_start:lang_start + len("Language")]
print("\n(b) First word (slice)      :", first_word)
print("    Last char (neg. index)  :", last_char)
print("    'Language' (slice range):", language)

# (c)
exists = "Intelligence" in sentence
print("\n(c) 'Intelligence' exists:", exists)
print("    Starting index       :", sentence.find("Intelligence"))

# (d)
paragraph = """Natural Language Processing enables computers to understand text.
Tokenization splits raw text into smaller units called tokens.
Word embeddings capture the semantic meaning of words."""
sentences = paragraph.split("\n")
print("\n(d) Sentences in paragraph:")
for s in sentences:
    print("   ", s)
