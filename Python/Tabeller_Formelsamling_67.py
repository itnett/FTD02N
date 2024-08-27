python
import sympy as sp

# Definer variabelen n
n = sp.symbols('n')

# Eksempel på en alternerende rekke u_n = (-1)^n / n
u_n = (-1)**n / n

# Forholdskriteriet
u_n_plus_1 = u_n.subs(n, n + 1)
ratio = sp.limit(sp.Abs(u_n_plus_1 / u_n), n, sp.oo)
print(f"Forholdskriteriet: lim |u_(n+1) / u_n| = {ratio}")

if ratio < 1:
    print("Rekken er konvergent.")
elif ratio > 1:
    print("Rekken er divergent.")
else:
    print("Forholdskriteriet er inkonklusivt.")

# Integrasjon for å sjekke integralkriteriet
x = sp.symbols('x')
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