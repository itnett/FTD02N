python
import sympy as sp

# Definer variabelen x
x = sp.symbols('x')

# Definer funksjonen f(x)
f = 1/x**2  # Eksempel på en monoton avtagende funksjon

# Beregn integralet fra 1 til uendelig
integral = sp.integrate(f, (x, 1, sp.oo))

# Skriv ut resultatet
print(f"Integral av f(x) fra 1 til uendelig er: {integral}")

# Sjekk om integralet er konvergent
if integral.is_finite:
    print("Rekken sum(1/n^2) er konvergent.")
else:
    print("Rekken sum(1/n^2) er divergent.")