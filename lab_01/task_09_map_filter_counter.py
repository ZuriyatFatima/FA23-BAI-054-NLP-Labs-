"""Lab 01 - Task 09: map(), filter(), sorted() and Counter"""
from collections import Counter

words = ["Python", "NLP", "is", "a", "powerful", "tool", "for", "text"]

# (a)
print("(a-i)  Lowercase:", list(map(lambda w: w.lower(), words)))
print("(a-ii) Lengths  :", list(map(lambda w: len(w), words)))

# (b)
words_long = list(filter(lambda w: len(w) > 3, words))
words_with_t = list(filter(lambda w: "t" in w.lower(), words))
print("\n(b-i)  words_long   :", words_long)
print("(b-ii) words_with_t :", words_with_t)

# (c)
print("\n(c-i)   Alphabetical      :", sorted(words))
print("(c-ii)  Length ascending  :", sorted(words, key=len))
print("(c-iii) Length descending :", sorted(words, key=len, reverse=True))

# (d)
sentence = "nlp nlp python ai nlp python text ai nlp python text"
tokens = sentence.split()
freq = Counter(tokens)
print("\n(d) Counter            :", freq)
print("(i)   3 most common     :", freq.most_common(3))
print("(ii)  Freq of 'python'  :", freq["python"])
print("(iii) Total words       :", len(tokens), "| Unique vocabulary:", len(freq))
