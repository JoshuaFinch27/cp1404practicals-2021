"""
CP1404/CP5632 Practical - Count word occurrences in a string
This example is in the lecture notes 3 different ways
"""

# Get text string and split it
word_to_word_count = {}
text = input("Text: ")
words = text.split()
# Add the word and its corresponding frequency to the dictionary
for word in words:
    word_frequency = word_to_word_count.get(word, 0)
    word_to_word_count[word] = word_frequency + 1
# Sort (alphabetically), the unique words and the corresponding frequencies
words = list(word_to_word_count.keys())
words.sort()
# Find the max length of the largest word
max_length = max((len(word) for word in words))
# Print output
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_word_count[word]))
