num = input("enter any natural number: ")
string_num = str(num)

steps = 0
while len(string_num) > 1:
    i = 0
    sum = 0
    while i < len(string_num):
        sum += int(string_num[i])
        i += 1 
    steps += 1
    string_num = str(sum)
print(f"it takes {steps} steps to become a single digit" )
