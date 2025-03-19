# Lesson 35
argument = ['a', 'a', 'b', 'c', 'hii', 'cat', 'bat' , 'cat']
argument.sort()
single = []
i = 0
current_var = argument[i]
count = argument.count(current_var)
while i < len(argument):
    if argument[i] not in single:
        single.append(argument[i])
    i += 1
print(single)
