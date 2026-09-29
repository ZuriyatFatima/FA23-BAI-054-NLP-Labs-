"""Lab 03 - Task 1: Regex Fundamentals (Character Classes & Quantifiers)"""
import re

text = ("In 2023, Ali scored 95 marks and Sara scored 88 in Lahore. "
        "The event started in 1999 & ended in 2024! Contact: Dr. Khan @ office #42. "
        "Prices rose 15% by 2025; costs were $120 for Python books.")
print("Text:", text, "\n")

# a) all digits
print("a) Digits:", re.findall(r"\d", text))

# b) words starting with a capital letter
print("b) Capitalised words:", re.findall(r"\b[A-Z][a-zA-Z]*\b", text))

# c) sequences of exactly 4 digits (not part of a longer number)
print("c) 4-digit sequences:", re.findall(r"(?<!\d)\d{4}(?!\d)", text))

# d) words that are 3 to 6 characters long
print("d) Words of 3-6 chars:", re.findall(r"\b[A-Za-z]{3,6}\b", text))
