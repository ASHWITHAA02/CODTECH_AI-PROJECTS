import re
from collections import Counter

# Read text from file
with open("sample_input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split into sentences
sentences = re.split(r'(?<=[.!?]) +', text)

# Clean words
words = re.findall(r'\w+', text.lower())

# Count word frequency
freq = Counter(words)

# Score sentences
sentence_scores = {}

for sentence in sentences:
    for word in re.findall(r'\w+', sentence.lower()):
        if word in freq:
            sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq[word]

# Select top 2 sentences
summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]

print("\nSummary:\n")
for s in summary:
    print(s)

# Save summary
with open("summary.txt", "w", encoding="utf-8") as f:
    for s in summary:
        f.write(s + "\n")