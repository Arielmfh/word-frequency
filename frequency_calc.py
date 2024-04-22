import re
import os
from collections import Counter


def count_word_frequency(filename, top_n=10):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text.lower())

    word_count = Counter(words)

    most_common = word_count.most_common(top_n)

    return most_common


txt_files = [f for f in os.listdir() if f.endswith('.txt')]

print("Available files:")
for txt_file in txt_files:
    print(f" - {txt_file}")

filename = input("Which file do you want to scan? ")

if not filename.endswith('.txt'):
    filename += '.txt'

top_n = 10
common_words = count_word_frequency(filename, top_n)

print("Top", top_n, "most common words:")
for word, count in common_words:
    print(f"{word}: {count}")
