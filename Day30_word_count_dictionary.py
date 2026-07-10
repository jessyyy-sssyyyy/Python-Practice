paragraph = "Python is easy and Python is powerful"

words = paragraph.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

# Output:
# {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
