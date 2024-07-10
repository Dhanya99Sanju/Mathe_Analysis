# Partial derivative calculation
import sympy as sp

# Define the variables
x , y = sp.symbols('x,y')

# Define the function
f = x ** 3 + 2 * x * y + y ** 2 + x - 3 * y

# Partial derivative w.r.to x
df_dx = sp.diff(f,x)

# Partial derivative w.r.to y
df_dy = sp.diff(f,y)

# Define the point at where to calculate Partial Derivative
point = {x : 2, y : 3}

# Evaluate the Partial Derivatine at the given point
df_dx_value = df_dx.subs(point)
df_dy_value = df_dy.subs(point)

# Print the Partial Derivatives
print(" the Partial Derivatives df_dx",df_dx)
print(" the Partial Derivatives df_dy",df_dy)

# Print the Partial Derivatives at a given Point
print("the Partial Derivatives at a given Point",df_dx_value)
print("the Partial Derivatives at a given Point",df_dy_value)