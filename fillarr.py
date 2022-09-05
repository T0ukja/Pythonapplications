from random import randint
array =[randint(1,500) for _ in range(30)]
array1 =[randint(1,500) for _ in range(30)]
summ=0
summ1=0
sumof=array+array1
if len(array) == len(array1):
    for i in range(0, len(array)):
        summ += array[i]
        summ1 += array1[i]
else:
       for i in range(0, len(array)):
           summ += array[i]
       for i in range(0, len(array)):
           summ1 += array1[i]
print(array)
print("First Array \n")
print(array1)
print("Second Array \n")
print(sumof, "\nall values are summed")
print("Sum of 2 arrays",summ+summ1)
