"""Lab 01 - Task 06: String Cleaning Methods"""

# (a)
text = "   MACHINE Learning is AMAZING!!!   "
step1 = text.strip()
print("(a-i)   strip()  :", repr(step1))
step2 = step1.lower()
print("(a-ii)  lower()  :", repr(step2))
step3 = step2.replace("!", "")
print("(a-iii) replace():", repr(step3))

# (b)
cleaned = step3
words = cleaned.split()
print("\n(b) Tokens        :", words)
upper_words = [w.upper() for w in words]
print("    Uppercase list:", upper_words)
print("    Joined        :", " | ".join(upper_words))

# (c)
sentence = "I love Java and Java is popular"
sentence = sentence.replace("Java", "Python")
print("\n(c) Updated sentence:", sentence)
print("    First 'Python' at index:", sentence.find("Python"))

# (d)
def normalize(text):
    """Strip whitespace, lowercase, and remove commas and full stops."""
    return text.strip().lower().replace(",", "").replace(".", "")

samples = ["   Hello, World. Welcome to NLP.   ",
           "  Natural Language Processing, is FUN.  "]
print("\n(d) normalize():")
for s in samples:
    print(f"    {s!r} -> {normalize(s)!r}")
