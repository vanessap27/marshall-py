# Lesson 24
condition = True
longest = ""
while condition == True:
    name = input("input a name. input 'X' to stop: ")
    if name == 'X':
        break
    elif len(name) > len(longest):
        longest = name 
    elif len(name) == len(longest):
        longest = longest
print(f"the longest name is {longest} ")

