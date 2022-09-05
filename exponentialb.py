base = int(input("Give base"))
exponent= int(input("Give exponent"))
result = base
if exponent != 0:
    for i in range(exponent - 1):
       result = result * base
print("Exponential value is : ", result)



#Easier way 
'''
print("Exponential Value is: ", base ** exponent)'''
