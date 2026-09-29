"""Lab 01 - Task 03: Dictionaries for Word Mapping"""

# (a)
word_freq = {"machine": 4, "learning": 7, "data": 5, "model": 3, "text": 6}
print("(a) word_freq            :", word_freq)
print("    Frequency of learning:", word_freq["learning"])
word_freq["data"] = 9
print("    After updating data  :", word_freq)

# (b)
word_freq["neural"] = 8
word_freq["network"] = 5
del word_freq["model"]
print("\n(b) After add/delete:", word_freq)
if "text" in word_freq:
    print('    The key "text" exists in the dictionary.')
else:
    print('    The key "text" does NOT exist in the dictionary.')

# (c)
vocab = {"nlp": 0, "python": 1, "token": 2, "vector": 3, "corpus": 4}
id_to_word = {idx: word for word, idx in vocab.items()}
print("\n(c) vocab     :", vocab)
print("    id_to_word:", id_to_word)

# (d)
print("\n(d) Word-frequency pairs:")
for word, freq in word_freq.items():
    print(f'Word: "{word}" → Frequency: {freq}')
print("Total unique words:", len(word_freq))
