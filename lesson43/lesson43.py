# Lesson 43
Alist = ['hello', 'world', 'cat', 'dog', 'blueberry', 'hello']
Blist = ["hello",  'blueberry', 'strawberry', 'cat']
def duplicates(a_list):
    result = set(a_list)
    return(list(result))
print(duplicates(Alist))
def intersect(a_list, b_list):
    x= set(Alist)
    y =set(Blist)
    return x.intersection(y)
print(intersect(Alist, Blist))
