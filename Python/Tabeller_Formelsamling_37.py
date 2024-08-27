python
import sympy as sp

# Define symbols
a, x, y, p, q = sp.symbols('a x y p q')

# Basic exponential and logarithmic properties
properties = {
    "a^0": a**0,
    "a^1": a**1,
    "a^n": a**n,
    "a^(p/q)": a**(p/q),
    "a^-x": a**-x,
    "(ab)^x": (a*b)**x,
    "(a/b)^x": (a/b)**x,
    "a^x * a^y": a**x * a**y,
    "a^x / a^y": a**x / a**y,
    "(a^x)^y": (a**x)**y,
    "ln(y)": sp.log(y),
    "ln(U*V)": sp.log(sp.symbols('U') * sp.symbols('V')),
    "ln(U/V)": sp.log(sp.symbols('U') / sp.symbols('V')),
    "ln(U^x)": sp.log(sp.symbols('U')**x),
}

# Print properties
for prop, expr in properties.items():
    print(f"{prop} = {expr}")

# Trigonometric functions and identities
t = sp.symbols('t')
trig_identities = {
    "cos(t)": sp.cos(t),
    "sin(t)": sp.sin(t),
    "tan(t)": sp.tan(t),
    "cot(t)": 1/sp.tan(t),
    "(sin(t))^2 + (cos(t))^2": sp.sin(t)**2 + sp.cos(t)**2,
    "tan(t) = sin(t)/cos(t)": sp.sin(t)/sp.cos(t),
    "cot(t) = 1/tan(t)": 1/sp.tan(t),
    "sin(x +- y)": sp.sin(x + y),
    "cos(x +- y)": sp.cos(x + y),
    "tan(x +- y)": sp.tan(x + y),
}

# Print trigonometric identities
for id, expr in trig_identities.items():
    print(f"{id} = {expr}")