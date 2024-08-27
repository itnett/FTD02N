python
import sympy as sp

# Definer variabelen x
x = sp.symbols('x')

# Definer funksjonene vi vil integrere
functions = {
    "sin(x)": sp.sin(x),
    "cos(x)": sp.cos(x),
    "1/(1 + x**2)": 1/(1 + x**2),
    "1/sqrt(1 - x**2)": 1/sp.sqrt(1 - x**2),
    "sqrt(1 - x**2)": sp.sqrt(1 - x**2),
    "1/sqrt(1 + x**2)": 1/sp.sqrt(1 + x**2),
    "sqrt(1 + x**2)": sp.sqrt(1 + x**2),
    "1/sqrt(x**2 - 1)": 1/sp.sqrt(x**2 - 1),
    "sqrt(x**2 - 1)": sp.sqrt(x**2 - 1),
    "e^(ax) * sin(bx)": sp.exp(sp.symbols('a')*x) * sp.sin(sp.symbols('b')*x),
    "e^(ax) * cos(bx)": sp.exp(sp.symbols('a')*x) * sp.cos(sp.symbols('b')*x),
}

# Integrer funksjonene og skriv ut resultatene
for func_name, func in functions.items():
    integral = sp.integrate(func, x)
    print(f"Integral of {func_name} is: {integral} + C")