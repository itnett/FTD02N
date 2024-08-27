python
import sympy as sp

# Define symbols
x, y = sp.symbols('x y')
z = sp.Function('z')(x, y)

# Define the function f(x, y)
f = x**3 + y**3 - 3*x*y

# Compute the first derivatives
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

# Find the critical points where the first derivatives are zero
critical_points = sp.solve([df_dx, df_dy], (x, y))
print(f"Critical points: {critical_points}")

# Compute the second derivatives
d2f_dx2 = sp.diff(df_dx, x)
d2f_dy2 = sp.diff(df_dy, y)
d2f_dxdy = sp.diff(df_dx, y)

# Evaluate the second derivatives at the critical points
for point in critical_points:
    a, b = point
    H = d2f_dx2.subs({x: a, y: b}) * d2f_dy2.subs({x: a, y: b}) - (d2f_dxdy.subs({x: a, y: b}))**2
    
    if H > 0:
        if d2f_dx2.subs({x: a, y: b}) > 0:
            print(f"Point {point} is a local minimum")
        elif d2f_dx2.subs({x: a, y: b}) < 0:
            print(f"Point {point} is a local maximum")
    elif H < 0:
        print(f"Point {point} is a saddle point")
    else:
        print(f"Point {point} requires further investigation")