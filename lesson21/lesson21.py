# Lesson 21
n = int(input("enter a number greater than one "))
counter = 0
result = 0
for num in range(1, n+1):
    total_factors = 0

    for divisor in range(1, num+1):
        if num % divisor == 0: 
            total_factors += 1
    
        if total_factors > counter: 
            counter = total_factors
            result = num

print(f"{result} has the most factors with {counter} factors ")


