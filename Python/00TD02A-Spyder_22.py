python
# Importere nødvendige biblioteker
import numpy as np
import sympy as sp

# Definere variabler og funksjoner
x = sp.symbols('x')
f = 3*x + 4

# Beregne nullpunktet til funksjonen f
nullpunkt = sp.solve(f, x)[0]

# Beregne skjæringspunktet med x-aksen
skjaeringspunkt = (nullpunkt, 0)

# Beregne en tangent til f ved x = 1
tangent = sp.diff(f, x).subs(x, 1) * (x - 1) + f.subs(x, 1)

# Skrive ut resultatene
print(f"Funksjon f: f(x) = {f}")
print(f"Nullpunkt til f: x = {nullpunkt}")
print(f"Skjæringspunkt med x-aksen: A = {skjaeringspunkt}")
print(f"Tangent til f ved x = 1: t(x) = {tangent}")

# Formatere resultatene for GeoGebra
funksjon_f = f"f(x) = {f}"
nullpunkt_str = f"A = ({nullpunkt}, 0)"
tangent_str = f"t(x) = {tangent}"

print("\nGeoGebra format:")
print(funksjon_f)
print(nullpunkt_str)
print(tangent_str)