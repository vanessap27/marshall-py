# Lesson 12
angle1 = int(input("enter angle one "))
angle2 = int(input("enter angle two "))
angle3 = int(input("enter angle three "))
triangle = (angle1 + angle2 + angle3)
if triangle != 180:
    print("not a triangle")
if triangle == 180:
    if angle1 == angle2 == angle3:
        print("it is an equilateral triangle ")
    if angle1 == angle2 and  angle1 != angle3 or angle1 == angle3 and angle1 != angle2 or angle2 == angle3 and angle2 != angle1:
        print("it is an isosceles triangle ")
    else: 
        print("it is a scalene triangle ")
