def nthorder(n):
    if n<= 0:
        print("wrong input")

    elif n == 1:
        return 0

    elif n == 2:
        return 1
    else:
        return nthorder(n-1)+nthorder(n-2)
 

 
print(nthorder(3))
 
