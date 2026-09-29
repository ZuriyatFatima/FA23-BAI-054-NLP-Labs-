"""Lab 01 - Task 02: Lists for Token Management"""

# (a)
tokens = ["deep", "learning", "helps", "machines", "understand", "text"]
print("(a) Full list        :", tokens)
print("    Length           :", len(tokens))
print("    Element at idx 2 :", tokens[2])
print("    Last element     :", tokens[-1])

# (b)
tokens.append("efficiently")
print("\n(b-i)   After append   :", tokens)
tokens.insert(3, "computers")
print("(b-ii)  After insert   :", tokens)
tokens.remove("helps")
print("(b-iii) After remove   :", tokens)

# (c)
tokens_A = ["NLP", "uses", "Python"]
tokens_B = ["for", "text", "analysis"]
full_tokens = tokens_A + tokens_B
print("\n(c) Combined list       :", full_tokens)
print("    Last three elements :", full_tokens[-3:])

# (d)
sorted_tokens = sorted(full_tokens)              # alphabetical (uppercase sorts before lowercase)
length_sorted = sorted(full_tokens, key=len)     # by word length
print("\n(d) Alphabetical :", sorted_tokens)
print("    By length    :", length_sorted)

# Which is more useful in NLP?
# Alphabetical sorting is generally more useful: it groups identical/similar words
# together, makes vocabularies easy to look up, deduplicate and compare, and gives a
# deterministic order for building word indices. Length sorting is mainly handy for
# batching sequences or filtering very short/long tokens.
