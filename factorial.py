def facto(n):
      
    if n == 0:
        return 1
     
    return n * facto(n-1)
  
num = int(input("Give Number"))
print("Factorial of", num, "is",
facto(num))
