a_list = [1, 5, 100, 27, 2, 3, 1]

#1 destructive version (simplest)
# sorted = []
# while len(a_list) > 0:  # or while a_list:  
#     a_list_min= min(a_list)
#     sorted.append(a_list_min)
#     a_list.remove(a_list_min)  
# print(sorted)


# 2 without distruction

# for i in range(0, len(a_list)-1):
#     small = a_list[i]
#     location = None #havent found a min
#     for j in range(i+1, len(a_list)):
#         if a_list[j] < small:
#             small = a_list[j]
#             location = j
#     if location is not None:
#         a_list[i], a_list[location] = a_list[location], a_list[i]
# print(a_list)


#3 bubble sort

# swapped = True
# while swapped:
#     swapped = False
#     for i in range(1, len(a_list)):
#         left = a_list[i - 1]
#         right = a_list[i]
#         if left > right:
#             swapped = True
#             a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
# print(a_list)

#4 insertion 
for i in range(1, len(a_list)):
    for j in range( i, 0, -1):
        if a_list[j] < a_list[j-1]
        a_list[j-1], a_list[j] = a_list[j], a_list[j]
print(a_list)