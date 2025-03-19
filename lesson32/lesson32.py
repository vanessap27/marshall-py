# Lesson 32
wordA = input("input the first word: ")
wordB = input('input the second word: ')
joined = list(wordA + wordB)
for i in joined:
    if joined.count(i) > 1:
        joined.remove(i)
print(joined)