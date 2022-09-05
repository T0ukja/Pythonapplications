
import sympy as sym
from sympy import *
x = sym.symbols('x')

exp=3*x**3-4*x**2+9*x+5


sol = solve(Eq(3*x**3-4*x**2+9*x+5, 0), x)
print(sol)

'''
equ =solve(Eq(exp,0),x)
print(sym.solve(equ))
'''







'''
from sympy import var, Eq, solve

x = var('x')
sol = solve(Eq(3*x**3-4*x**2+9*x+5, 0), x)
print(sol)

'''



'''


# Equation: x^3+b*x^2+c*x+d=x^3+(B−r)x^2+(C−B*r)x−C*r


print(sympy.solve(equation,"b"))
print(sympy.solve(equation,"c"))    
print(sympy.solve(equation,"d"))
'''
