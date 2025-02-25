# Lesson 23
condition = True
sum = 0
counter = 0

while condition == True:
    num = input("enter a number to be added to the average ")
    if num == "X":
        condition = False 
    else:
        sum = sum + int(num)
        counter += 1

average = sum / counter
print(f"the average is {average} ")

