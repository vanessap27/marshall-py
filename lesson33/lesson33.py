# Lesson 33
num_list = [1, 6, 8, 2, 10, 4]
num_list.sort()
median = 0
i = 0
sum = 0
while i < len(num_list):
    sum += num_list[i]
    median = sum/len(num_list)
    i += 1
print(median)