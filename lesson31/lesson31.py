# Lesson 31
input_a = list(input("enter your first word: "))
input_b = list(input("enter your second word: "))
input_a.sort()
input_b.sort()
x = 0
if input_a == input_b:
    print("they're anagrams! ")
elif len(input_a) != len(input_b):
    print("they're not anagrams")
else: 
    for i in input_a:
        if i != input_b[x]:
            print("they're not anagrams. ")
            break 
        else:
            x += 1
            print("they're anagrams! ")
