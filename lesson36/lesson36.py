# Lesson 36


def factors(num):
    ''' checks the number of factors of num 
    '''
    ctr = 0
    for i in range(1, num+1):
        if num % i == 0:    
            ctr += 1
            i += 1
    return ctr

num = int(input("enter a number to find it's prime: "))

if factors(num) == 2:
    print("prime. ")
else:
    print('not prime. ')