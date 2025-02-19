# Lesson 4
import math
length1 = input("enter the fence length of section one denoted by  series of 'F' for each plank:")
length2 = input("enter the fence length of section two denoted by  series of 'F' for each plank:")
length3 = input("enter the fence length of section three denoted by  series of 'F' for each plank:")
total_length = len(length1) + len(length2) + len(length3)
if total_length <= 12:
    total_cans = 12
elif total_length > 12:
    total_cans = (math.ceil(total_length/12)*12)
leftover = (total_cans - total_length)
boxes = total_cans/12
cost = boxes*14.95
print (f"you will need a total of {total_cans} cans")
print (f"you will have {leftover} cans of paint leftover")
print (f"it will cost ${cost}")