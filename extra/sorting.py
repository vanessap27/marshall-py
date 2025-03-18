unsorted = [1, 5, 100, 27, 2, 3, 1]
sorted = []

while len(unsorted) > 0:    
    unsorted_min= min(unsorted)
    sorted.append(unsorted_min)
    unsorted.remove(unsorted_min)
   
print(sorted)

