import sympy as sp
x , y = sp.symbols('x,y')
f = x ** 3 + 2 * x * y + y ** 2 + x - 3 * y
df_dx = sp.diff(f,x)
df_dy = sp.diff(f,y)
point = {x : 2, y : 3}
df_dx_value = df_dx.subs(point)
df_dy_value = df_dy.subs(point)
print("df_dx",df_dx)
print("df_dy",df_dy)
print(df_dx_value)
print(df_dy_value)