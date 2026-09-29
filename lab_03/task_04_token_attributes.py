"""Lab 03 - Task 4: Token Attributes (Categorizing Tokens)"""
import spacy

nlp = spacy.blank("en")

# a) load the sentence into a Doc
sentence = "Ali paid $50 for 3 books, then emailed ali.khan@example.com about Rs. 500 more."
doc = nlp(sentence)
print("Sentence:", sentence, "\n")

# b) is_alpha
print("b) is_alpha:")
for token in doc:
    print(f"   {token.text:22} is_alpha={token.is_alpha}")

# c) like_num and like_email
print("\nc) like_num / like_email:")
for token in doc:
    print(f"   {token.text:22} like_num={token.like_num!s:6} like_email={token.like_email}")

# d) currency tokens
currency_tokens = [token.text for token in doc if token.is_currency]
print("\nd) Currency tokens:", currency_tokens)
