python
from fractions import Fraction

# Brøkregning
brøk1 = Fraction(3, 4)
brøk2 = Fraction(1, 2)
sum = brøk1 + brøk2
print("Summen av brøkene:", sum)

# Prosentregning
pris = 500
rabatt = 20  # Prosent
ny_pris = pris * (1 - rabatt/100)
print("Ny pris etter rabatt:", ny_pris)