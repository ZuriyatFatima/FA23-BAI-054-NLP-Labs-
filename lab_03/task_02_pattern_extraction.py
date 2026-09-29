"""Lab 03 - Task 2: Pattern-Based Extraction (Real World Data)"""
import re

paragraph = """
Order ORD-1042 was placed by ali.khan@example.com on 15/03/2024 with a 12.5% discount.
Call 0300-1234567 or 0345-7654321 for support. Sara (sara_ahmed99@mail.co.pk) ordered
ORD-2077 on 02/11/2023; her refund of 45% was approved on 30/11/2023.
Reach billing at billing.dept@company.org or 0312-9998887. Invalid: 13/13/20 and 0400-123.
"""

# a) e-mail addresses
emails = re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", paragraph)
print("a) Emails:", emails)

# b) phone numbers 03XX-XXXXXXX
phones = re.findall(r"\b03\d{2}-\d{7}\b", paragraph)
print("b) Phones:", phones)

# c) dates DD/MM/YYYY
dates = re.findall(r"\b(?:0[1-9]|[12]\d|3[01])/(?:0[1-9]|1[0-2])/\d{4}\b", paragraph)
print("c) Dates :", dates)

# d) percentages e.g. 45%, 12.5%
percentages = re.findall(r"\b\d+(?:\.\d+)?%", paragraph)
print("d) Percentages:", percentages)
