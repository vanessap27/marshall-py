# Lesson 22
Nth = int(input("enter a number greater than 0: "))
fib_0 = 0
fib_nth = 1
next_fib = 0
final_fib = 0
for term in range(2, Nth):
    next_fib = fib_0 + fib_nth
    fib_0 = fib_nth
    fib_nth = next_fib

print(next_fib)