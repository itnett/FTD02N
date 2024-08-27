python
from sympy import symbols, Eq, solveset

B, R, T = symbols('B R T')  # Bufferstørrelse, overføringshastighet, tolerert forsinkelse

# Ligning for bufferstørrelse basert på forsinkelse
ligning = Eq(B, R * T)

# Løs for bufferstørrelse gitt overføringshastighet og tolerert forsinkelse
løsning = solveset(ligning, B)
print(løsning)