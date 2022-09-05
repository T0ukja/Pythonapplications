from random import randint
import numpy as np



#one way of making
x=0
summ = 0
#
array =[randint(1,500) for _ in range(30)]

print("Random array values are", array)
for i in range(0, len(array)):    
   summ += array[i]
print(summ)
print("Average is", summ/len(array))



'''
#second method
x = 30
summ=0
arr = []
for i in range(0,30):
   value = randint(1,500)
   arr.insert(i,value)
   summ += arr[i]

print("sum is", summ)
print("Average is", summ/len(arr))
print("Array values" , arr)
'''
