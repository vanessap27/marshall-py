# Lesson 10
phone_num = input("enter the last four digits of the number: ")
if phone_num[0] in ('8', '9'):
    if phone_num[1] == phone_num[2]:
        if phone_num[3] in ('8', '9'):
            print("the number is a telemarketer ")
else:
    print("the number is not a telemarketer ")
