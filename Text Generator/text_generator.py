import random

text = """
Artificial intelligence is transforming industries.
AI helps machines learn from data.
Machine learning improves decision making.
Artificial intelligence will shape the future.
"""

words = text.split()

chain = {}

for i in range(len(words)-1):
    word = words[i]
    next_word = words[i+1]

    if word not in chain:
        chain[word] = []

    chain[word].append(next_word)

word = random.choice(words)

generated = word

for i in range(20):
    if word in chain:
        word = random.choice(chain[word])
        generated += " " + word
    else:
        break

print("Generated Text:\n")
print(generated)