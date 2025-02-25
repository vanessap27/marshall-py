num = int(input("enter a number greater than 0: "))
while num != 1:    
    if num % 2 == 0:
        num = num //2
        print(num)
    elif num % 2 != 0:
        num = 3*num + 1
        print(num)
