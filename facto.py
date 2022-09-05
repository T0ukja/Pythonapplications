def facto(number):
      
    if number == 0:
        return 1
     
    return number * facto(number-1)
  
number = 7;
print("Factorial of", number, "is",
facto(number))
