# Lesson 30
num = int(input('enter a random number: '))
pattern = ''
i = 1

while i <= num:
    if i%2 == 0:
        pattern += '1'
    else:
        pattern += '0'
    i += 1
print(pattern)