python
# Define time symbol and parametric equations
t = sp.symbols('t')
x_t = sp.Function('x')(t)
y_t = sp.Function('y')(t)

# First and second derivatives with respect to t
x_dot = sp.diff(x_t, t)
y_dot = sp.diff(y_t, t)
x_double_dot = sp.diff(x_dot, t)
y_double_dot = sp.diff(y_dot, t)

# Radius of curvature formula for parametric equations
R_parametric = ((x_dot**2 + y_dot**2)**(3/2)) / sp.Abs(x_dot * y_double_dot - y_dot * x_double_dot)
print(f"Radius of curvature (parametric): {R_parametric}")