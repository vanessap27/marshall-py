# Lesson 17
num = int(input("input a positive number "))
factorial = 1
while num > 0:
    factorial = factorial * num
    num -= 1
print(factorial)