# Lesson 16
num = int(input("enter a number between 1 and 50 "))
if 1 <= num <= 50:
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    if  num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)