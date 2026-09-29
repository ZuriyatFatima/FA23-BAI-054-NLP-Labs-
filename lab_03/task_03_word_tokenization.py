"""Lab 03 - Task 3: Word Tokenization (NLTK vs spaCy)"""
import nltk
import spacy
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

paragraph = ("I don't think it's easy to build a chatbot. "
             "Dr. Smith's team can't finish it by 5 p.m. today, isn't that odd? "
             "They'll email me at team@lab.com or visit https://lab.com for $50.")

# a) NLTK
nltk_tokens = word_tokenize(paragraph)
print("a) NLTK tokens:\n  ", nltk_tokens)

# b) blank spaCy pipeline
nlp = spacy.blank("en")
spacy_tokens = [t.text for t in nlp(paragraph)]
print("\nb) spaCy tokens:\n  ", spacy_tokens)

# c) Differences observed between the two outputs
# 1. E-mail addresses: spaCy keeps "team@lab.com" as ONE token (its tokenizer has an
#    e-mail/URL-aware rule set), whereas NLTK breaks it into "team", "@", "lab.com".
# 2. URLs: spaCy keeps "https://lab.com" as ONE token, while NLTK splits it into
#    "https", ":" and "//lab.com".
# 3. (Similarity) Contractions such as "don't", "it's", "can't" are split the same way by
#    both ("do" + "n't", "it" + "'s"); abbreviations like "Dr." and "p.m." are also kept
#    whole by both. As a result NLTK produces more tokens than spaCy on this paragraph.
print("\nc) See comments in the code for the differences.")
print("   Tokens only in NLTK :", sorted(set(nltk_tokens) - set(spacy_tokens)))
print("   Tokens only in spaCy:", sorted(set(spacy_tokens) - set(nltk_tokens)))

# d) counts
print("\nd) NLTK token count :", len(nltk_tokens))
print("   spaCy token count:", len(spacy_tokens))
