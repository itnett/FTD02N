python
from sympy import symbols, solve, S

R, T = symbols('R T')  # Responstid, terskelverdi

# Ulikhet for akseptabel responstid
ulikhet = R < T

# Løs for responstid gitt en terskelverdi
løsning = solveset(ulikhet, R, domain=S.Reals)
print(løsning)