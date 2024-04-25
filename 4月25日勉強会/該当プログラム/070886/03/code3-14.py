from collections import Counter

str = """I'm studying Python to work on production management.
I often ask ChatGPT to create sample programs for me."""

char_count = Counter(str)
for char, count in char_count.items():
    print(f"文字: '{char}', 出現回数: {count}")

word_count = Counter(str.split())
for word, count in word_count.items():
    print(f"単語: '{word}', 出現回数: {count}")