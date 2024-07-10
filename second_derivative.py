# Find out 2nd Derivative of a Function

import sympy as sp

# Define the variable 
x,y = sp.symbols('x,y')

# Define the function
f = 2* x ** 3 + sp.sin(x * y)

#Calculate the 2nd order Derivative
d2f_d2x = sp.diff(f,x,2)
print(f"Print the second derivative of fuction {f} :   ",d2f_d2x)

#Define the Point
point = {x:2,y:3}

#Calculate the 2nd order Derivative at the Point
d2f_d2x_value = d2f_d2x.subs(point)
print(f"Derivative at the Point {point} :        ",d2f_d2x_value)


