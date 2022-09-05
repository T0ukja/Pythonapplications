def BMI():
    weight=float(input("Give your weight"))
    height=float(input("Give your Height"))
    BMI = weight/(height/100)**2
    print(f"Your BMI is {BMI}")




BMI()


