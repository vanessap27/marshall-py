# Lesson 3
tiles = input("Enter the number of tiles: ") 
#reads as string 
tiles = int(tiles)
#square root is ^ 1/2
calculation = int((tiles ** 0.5) // 1)
print(f"the max side length is: {calculation}")
