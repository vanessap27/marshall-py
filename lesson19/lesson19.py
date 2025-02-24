# Lesson 19
num =int(input("enter a number "))
prime = True 
for factor in range(2, num+1):
    if num % factor == 0: 
        print(f"{num} is not a prime number ")
        prime = False 
    break
if prime == True:
    print(f"{num} is a prime number ")