a_list = [4, 6, 7, 1, 3]
#bubble 
def bubble(array): # mutates given array
    if len(array) <= 1:
        return array
    swap = True 
    while swap:
        swap = False
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                swap = True
    return array 
def insertion(array):
    if len(array) <= 1:
        return array
    else:
        for i in range(1, len(array)):
            for j in range(i, -1, -1):
                # starts at i goes down to 0 down by 1
                if array[j-1] > array[j]:
                    array[j-1], array[j] = array[j], array[j-1]
                else: 
                    break
    return array 

#destructive 
def select(array):
    result = []
    while array:
        smol = min(array)
        result.append(smol)
        array.remove(smol)
    return result 

#mutatuion based selection sort 
def select2(array):
    def smol_finder(array, start=0):

        if len(array) < 2:
            return array
        else:
            for i in range(1, len(array)):
                next_smallest = smol_finder(array, start-1)
                if array(next_smallest) < array[i-1]:
                array[i-1], array(next_smallest) = array(next_smallest), array[i-1]
        # if not array:
        #     return None
        # elif len(array) == 1:
        #     return array[0]:
        # else:
        #     smallest = array[start]
        #     location = start
        #     for in range(start+1, len(array)):
        #         if array[i] < smallest:
        #             smallest = array[i]
        #             location = i
        #     return location
