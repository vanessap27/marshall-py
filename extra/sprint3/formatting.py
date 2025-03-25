#define your function 
def selectionSort(array):
    sorted_list = []
    while len(array) > 0:
        smallest = min(array)
        sorted_list.append(smallest)
        array.remove(smallest)
    return sorted_list
def createList(size):
    result = []
    for i in range(size):
        result.append(int(input('enter a number: ')))
    return result 
a_list = createList(12)
print(selectionSort(a_list))
print(a_list)