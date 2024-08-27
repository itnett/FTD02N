python
import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define functions
u = sp.Function('u')(x)
v = sp.Function('v')(x)
C = sp.symbols('C')
k = sp.symbols('k', constant=True)

# Constant
constant_diff = sp.diff(C, x)
print(f"Derivative of a constant: {constant_diff}")

# Sum of functions
sum_diff = sp.diff(u + v, x)
print(f"Derivative of the sum: {sum_diff}")

# Constant multiple
const_multiple_diff = sp.diff(k * u, x)
print(f"Derivative of a constant multiple: {const_multiple_diff}")

# Product of functions
product_diff = sp.diff(u * v, x)
print(f"Derivative of the product: {product_diff}")

# Quotient of functions
quotient_diff = sp.diff(u / v, x)
print(f"Derivative of the quotient: {quotient_diff}")

# Power of x
r = sp.symbols('r')
power_diff = sp.diff(x**r, x)
print(f"Derivative of x^r: {power_diff}")

# Logarithm
log_diff = sp.diff(sp.log(x), x)
print(f"Derivative of ln(x): {log_diff}")

# Exponential function
exp_diff = sp.diff(sp.exp(x), x)
print(f"Derivative of e^x: {exp_diff}")

# General exponential function
a = sp.symbols('a', positive=True)
general_exp_diff = sp.diff(a**x, x)
print(f"Derivative of a^x: {general_exp_diff}")

# Sine
sin_diff = sp.diff(sp.sin(x), x)
print(f"Derivative of sin(x): {sin_diff}")

# Cosine
cos_diff = sp.diff(sp.cos(x), x)
print(f"Derivative of cos(x): {cos_diff}")

# Tangent
tan_diff = sp.diff(sp.tan(x), x)
print(f"Derivative of tan(x): {tan_diff}")

# Inverse Sine
arcsin_diff = sp.diff(sp.asin(x), x)
print(f"Derivative of arcsin(x): {arcsin_diff}")

# Inverse Tangent
arctan_diff = sp.diff(sp.atan(x), x)
print(f"Derivative of arctan(x): {arctan_diff}")

# Chain rule
h = sp.Function('h')(x)
g = sp.Function('g')(h)
chain_rule_diff = sp.diff(g, x).doit()
print(f"Chain rule: {chain_rule_diff}")

# Total derivative for a multivariable function
y, z = sp.symbols('y z')
varphi = sp.Function('varphi')(x, y, z)
total_diff = sp.diff(varphi, x) * sp.diff(x, x) + sp.diff(varphi, y) * sp.diff(y, x) + sp.diff(varphi, z) * sp.diff(z, x)
print(f"Total derivative: {total_diff}")