# Lesson 11
user_input = input("enter the x and y coordinates of the point: ")
coords = user_input.split(" ")
x = int(coords[0])
y = int(coords[1])
if x > 0:
    if y > 1:
        print(f"the point ({x}, {y}) is in quadrant one ")
    else: 
        print(f"the point ({x}, {y}) is in quadrant four ")
if x < 0:
    if y > 1:
        print(f"the point ({x}, {y}) is in quadrant two ")
    else: 
        print(f"the point ({x}, {y}) is in quadrant three ")
