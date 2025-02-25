user_input = input("input your caesar cipher: ")
message = ""
index = 0
current_char = ""

while user_input:
    current_char = ord(user_input[index])
    message = message + chr(current_char-1)
    index += 1
    if len(message) == len(user_input):
        break
print(message)