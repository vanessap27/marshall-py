# Lesson 20
num = int(input( "enter a number less than 10 000 "))
sum_of_factors = 0
if num < 10000:
    for factor in range(1, num):
        if num % factor == 0:
            sum_of_factors += factor
else: 
    print("that is not a number below 10 000 ")
if sum_of_factors == num:
    print(f"{num} is a perfect number ")
else: 
    print(f"{num} is not a perfect number ")