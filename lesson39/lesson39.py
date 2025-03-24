# Lesson 39
def gcd(num1, num2):
    fact1 = []
    fact2 = []
    gcd = 0
    
    for i in range(1, num1+1):
        if num1 % i == 0:
            fact1.append(i)
    for j in range(1, num2+1):
        if num2 % j == 0:
            fact2.append(j)  
    for x in range(len(fact1)):
        curr_num = fact1[x]
        if fact1[x] in fact2:
            if int(curr_num)> gcd:
                gcd = curr_num

    return gcd

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

print(f"the gcd of {num1} and {num2} is {gcd(num1, num2)} ")



    