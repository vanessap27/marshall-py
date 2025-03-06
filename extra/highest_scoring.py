score = 0
points = 0
word = ''
counter = 0
user_input =''
while user_input != "X":
    user_input = input("enter a word to be score, enter X to exit: ")
    if user_input != "X":
        word += user_input.lower()
for i in word:
    if i.isalpha():
        if  i == 'a' or  i == 'e' or  i == 'o' or  i == 'u':
            points += 1
        else:
            points += 5
    counter += 1
score = points * (len(word))
print(score)

score_dict = {} # empty
while True:
    new_word = input("enter a word: ")
    if new_word == "X":
        break
    elif new_word not in score_dict:
        score_dict[new_word] = score(new_word)

word_score = None
best_score = None
for word, score in score_dict.items():
    if worst_score is None:
        worst_score = (word, score)
    else:
    if score <= worst_score[1]:
    if best_score is None:
        best_score = (word, score)
    else:
        if score >= best_score[1]:
            best_score = (word, score)

print(best_score)
print(worst_score)