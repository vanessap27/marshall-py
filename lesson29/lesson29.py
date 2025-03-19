# Lesson 29
user_input = list(input('enter a phrase/word: '))
counter = 0
i = 0
while i < len(user_input):
    if user_input[i] == 'a' or user_input[i] == 'e' or user_input[i] == 'i' or user_input[i] == 'o' or user_input[i] == 'u':
        counter += 0
    else:
        counter += 1
    i += 1
print(counter)
