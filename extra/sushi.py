#There is a new conveyor belt sushi restaurant in town. Plates of sushi travel around the restaurant on a raised conveyor belt and customers choose what to eat by removing plates.
#Each red plate of sushi costs $3 each green plate of $4 sushi costs and each blue plate of sushi costs $5
cost = 0
while True:
    red = int(input("how many red plates did you take? "))
    cost += (red*3)
    green = int(input("how many green plates did you take? "))
    cost += (green*4)
    blue = int(input("how many blue plates did you take? "))
    cost += (blue*5)
    break 
print(f"the total cost  is {cost} ")