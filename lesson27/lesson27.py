# Lesson 27
user_input = input("enter anything: ")
alpha = []
if user_input.isalpha():
    print(user_input)
else: 
    for i in user_input:
        if i.isalpha():
            alpha.append(i)
    print(alpha)
