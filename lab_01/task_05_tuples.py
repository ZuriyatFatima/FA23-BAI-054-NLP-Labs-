"""Lab 01 - Task 05: Tuples for Fixed Linguistic Data"""

# (a)
pos_tags = [("language", "NOUN"), ("processes", "VERB"), ("human", "ADJ"),
            ("text", "NOUN"), ("quickly", "ADV")]
print("(a) pos_tags:", pos_tags)
print("    Second tuple - word:", pos_tags[1][0])
print("    Second tuple - tag :", pos_tags[1][1])

# (b)
word, tag = pos_tags[0]
print("\n(b) word:", word)
print("    tag :", tag)
try:
    pos_tags[0][1] = "VERB"
except TypeError as e:
    print("    Error message:", e)

# (c)
def extract_nouns(pos_list):
    """Return only the words whose tag is NOUN."""
    return [w for w, t in pos_list if t == "NOUN"]

print("\n(c) Nouns:", extract_nouns(pos_tags))

# (d)
pipeline_steps = ("load_data", "clean_text", "tokenize", "remove_stopwords", "vectorize")
print("\n(d) Pipeline        :", pipeline_steps)
print("    Index of tokenize:", pipeline_steps.index("tokenize"))
print("    Total steps      :", len(pipeline_steps))
try:
    del pipeline_steps[1]
except TypeError as e:
    print("    Cannot modify tuple ->", e)
