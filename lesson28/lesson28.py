# Lesson 28
word = input("enter word: ")
reverse = word[-1::-1]
if word == reverse:
    print("it's a palindrome! ")
else:
    print("it's NOT a palindrome! ")