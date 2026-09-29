"""Lab 01 - Task 07: String Validation Methods"""

# (a)
text = "NLP is the future of AI research"
print("(a) Starts with 'NLP'     :", "Yes" if text.startswith("NLP") else "No")
print("    Ends with 'research'  :", "Yes" if text.endswith("research") else "No")
print("    Position of 'future'  :", text.find("future"))

# (b)
tokens = ["hello", "123", "world", "456abc", "python", "789", "NLP3"]
print("\n(b) Token classification:")
for t in tokens:
    if t.isalpha():
        label = "purely alphabetic"
    elif t.isdigit():
        label = "purely numeric"
    else:
        label = "mixed"
    print(f"    {t!r:10} -> {label}")

# (c)
words = ["running", "jumped", "NLP", "ai2025", "data", "42"]
pure_words, pure_numbers, mixed_tokens = [], [], []
for w in words:
    if w.isalpha():
        pure_words.append(w)
    elif w.isdigit():
        pure_numbers.append(w)
    else:
        mixed_tokens.append(w)
print("\n(c) pure_words   :", pure_words)
print("    pure_numbers :", pure_numbers)
print("    mixed_tokens :", mixed_tokens)

# (d)
def validate_token(token):
    if token.isalpha():
        return "WORD"
    if token.isdigit():
        return "NUMBER"
    return "MIXED"

print("\n(d) validate_token():")
for t in ["chat", "99", "gpt4", "bert", "2024", "nlp!"]:
    print(f"    {t:6} -> {validate_token(t)}")
