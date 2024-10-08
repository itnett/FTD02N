python
from sympy import symbols, And, solveset, S

antall_regler, falske_positiver, falske_negativer = symbols('antall_regler falske_positiver falske_negativer')

# Ulikheter for å balansere sikkerhet og ytelse
ulikhet1 = antall_regler < 1000  # Begrense antall regler for å unngå ytelsesproblemer
ulikhet2 = falske_positiver < 0.01  # Begrense antall falske positiver
ulikhet3 = falske_negativer < 0.001  # Begrense antall falske negativer

løsning = solveset(And(ulikhet1, ulikhet2, ulikhet3), (antall_regler, falske_positiver, falske_negativer), domain=S.Reals)
print(løsning)