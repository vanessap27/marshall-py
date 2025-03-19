# Lesson 38
def palindrome(text):
    return text == text[::-1]

palindromes = []
largest = ''
for num1 in range(999, 99, -1):
    for num2 in range(999, 99, -1):
        curr_num = num1 * num2
        if palindrome(str(curr_num)):
            palindromes.append(curr_num)
largest = max(palindromes)
print(largest)
