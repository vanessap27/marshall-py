# Lesson 13
month = int(input("enter numerical month "))
day = int(input("enter numerical day "))
if month == 2 and day == 18:
    print("special")
elif month == 2 and day < 18 or month == 1:
    print("before")
elif month == 2 and day > 18 or month > 2:
    print("after")
    