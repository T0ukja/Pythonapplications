a=3
b=3
c=1

#first method with if else
'''
if a>b and a>c:
    print("A is biggest")

if b>c and b>a:
    print("B is biggest")
if c>b and c>b:
    print("C is biggest")
'''

#second method using max
'''
lsita = {'a':a,'b':b,'c':c}
print ("biggest value is",max(lsita),"and it is '",max(lsita, key=lsita.get),"'variable")
'''


#third method using array and sorting
'''
values = [a,b,c]
values.sort()
print(f"The maximum value in the list is: {values[-1]}")
'''
