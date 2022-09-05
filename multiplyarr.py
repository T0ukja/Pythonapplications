list1 = [2, 5, 8,10,50]
list2 = [9,5,2,10,25]

def multiply(first,second):
    multi = []
    for first, second in zip(first, second):
        multi.append(first * second)
    return multi


print("Multiply arrays", list1, "and", list2, "is", multiply(list1,list2))
