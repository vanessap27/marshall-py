# Lesson 37

a_string = input("enter a string: ")
def repeat(a_string):
    compressed = ''
    ctr = 1
    for i in range(1, len(a_string)):
        if a_string[i] == a_string[i-1]:
            ctr += 1
        else: 
            compressed += a_string[i-1]
            compressed += str(ctr)
           
            ctr = 1

    return compressed



    if len(repeat(a_string)) >= len(a_string):
        return(a_string)
    else: 
        return(compressed)
print(repeat(a_string))