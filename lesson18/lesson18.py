# Lesson 18
num = int(input("input a number "))
for factor in range(1, num+1):
    if num % factor == 0:
        print(f"{factor} is a factor of {num} ")

