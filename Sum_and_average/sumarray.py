#First method
import numpy as np
def sumarr():
    arr=[1+5+6+7+8+9+10]
    print(np.sum(arr))


def sumarrsecond():
    #Second method
    arr=[1+5+6+7+8+9+10]
    sum=0
    for i in arr:
        sum = sum + i
        print(sum)


sumarr()
sumarrsecond()
