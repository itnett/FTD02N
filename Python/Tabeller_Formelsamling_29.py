python
import sympy as sp

x = sp.symbols('x')

# Define elementary functions
functions = {
    'exponential': sp.exp(x),
    'logarithm': sp.log(x),
    'sine': sp.sin(x),
    'cosine': sp.cos(x)
}

# Print each function
for name, func in functions.items():
    print(f"{name.capitalize()} function: {func}")