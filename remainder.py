numbers = 1
sumofnumbers = 0
while numbers <= 40:
  for x in range (0,40):
    numbers += 1
    if(numbers % 2 == 0):
      sumofnumbers +=numbers
      print("number is", numbers)
      print("sum is", sumofnumbers)
