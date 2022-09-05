

list1 = [10, 20, 1, 45, 99]

def sorting(arraylist):
    print("before sorting", list1)
    arr=[]
    for i in range (len(arraylist)):
        value = min(arraylist)
        list1.remove(value)
        arr.append(value)
    return arr




print(sorting(list1))
