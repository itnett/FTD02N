python
import sympy as sp

# Definer variabelen x
x = sp.symbols('x')

# Definer funksjonene vi vil derivere
functions = {
    "C (konstant)": sp.Symbol('C'),
    "u(x) + v(x)": sp.Function('u')(x) + sp.Function('v')(x),
    "ku(x)": sp.Symbol('k') * sp.Function('u')(x),
    "u(x) * v(x)": sp.Function('u')(x) * sp.Function('v')(x),
    "u(x) / v(x)": sp.Function('u')(x) / sp.Function('v')(x),
    "x^r": x**sp.Symbol('r'),
    "ln(x)": sp.ln(x),
    "e^x": sp.exp(x),
    "a^x": sp.Symbol('a')**x,
    "sin(x)": sp.sin(x),
    "cos(x)": sp.cos(x),
    "tan(x)": sp.tan(x),
    "arcsin(x)": sp.asin(x),
    "arctan(x)": sp.atan(x),
}

# Deriver funksjonene og skriv ut resultatene
for func_name, func in functions.items():
    derivative = sp.diff(func, x)
    print(f"Derivert av {func_name} er: {derivative}")