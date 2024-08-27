python
from sympy import Sum, symbols

n = symbols('n')
feilrate = 0.01  # Sannsynlighet for feil per hendelse
antall_hendelser = 1000

forventet_antall_feil = Sum(feilrate, (n, 1, antall_hendelser)).doit()
print(f"Forventet antall feil: {forventet_antall_feil}")  # Output: Forventet antall feil: 10