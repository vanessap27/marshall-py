# def factorial(num):
# # base case
#     if num in (0,1): #0! and 1! are both 1
#         return 1
#     else: 
#         return num * factorial(num-1)
#         # work towards base case
#         #do recursive function call (calling itself)

# result = factorial(5)
# print(result)

# def power(base, exp)
#     if base == 0 and exp == 0:
#         return base
#     elif base = 0:
#         return 1
#     elif exp == 0:
#         return 1
#     else: 
#         return(base * power(base, exp-1))

# def palindrome(word):
#     if len(word) in (0, 1): 
#         return True
#     elif len(word) in (2, 3):
#         return word[0] == word[-1]
#     else: 
#         condition1 = word[0] == word[-1]
#         condition2 = palindrome(word[1: -1])
#         return condition1 and condition2 

def palindrome(word):
    def helper(text, i , j):
        if i >= j:
            return True
        elif text[i] != text[j]
            return False
        else:
            return helper(text, i+1, j-1)
    if len(word) in (0, 1): 
        return True
    elif len(word) in (2, 3):
        return word[0] == word[-1]
    else: 
       return helper(word, 0, len(word)-1)

result = palindrome("tacocat")
print(result)