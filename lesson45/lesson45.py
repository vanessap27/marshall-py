# Lesson 45
words = ["apple", "banana", "cherry", "date"]
def len_dict(a_list):
    result = {}
    for word in a_list:
        if word not in result:
            result[word] = len(word)
    return result
print(len_dict(words))