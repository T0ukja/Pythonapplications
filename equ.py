import cmath
import math

a=3
b=-4
c=9
d=5
r =-27*d+b*(9*c-2*b**2)

q = ((3*c) - (b)**2) / 9
discriminant= q**3 + (r**2 * -1)
s = r + cmath.sqrt((discriminant))
t = r - cmath.sqrt((discriminant))
term = 1.7320508075688772935274463415059*((-(t)+s)/2)
r13= 2*cmath.sqrt(q)

x1=((-1*term)+r13*math.cos(q**3/3))
x2=(-term + r13*math.cos(q**3+(2*math.pi)/3))
x3=(-term + r13*math.cos(q**3+(4*math.pi)/3))

print(x1)
print(x2)
print(x3)


