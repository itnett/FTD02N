python
from sympy import Symbol, diff, poly

def deriver_polynom(koeffisienter):
  """
  Deriverer en polynomfunksjon.

  Args:
      koeffisienter (list): En liste med koeffisienter, der koeffisienter[i] er koeffisienten foran x^i.

  Returns:
      list: En liste med koeffisienter for den deriverte polynomfunksjonen.
  """
  x = Symbol('x')
  polynom = poly(koeffisienter, x)
  derivert = polynom.diff(x)
  return derivert.all_coeffs()  # Returnerer koeffisienter som liste

# Eksempelbruk:
koeffisienter = [1, -3, 2]  # Koeffisienter for polynomet x^2 - 3x + 2
deriverte_koeffisienter = deriver_polynom(koeffisienter)
print("Den deriverte av polynomet er:", deriverte_koeffisienter)  # Output: Den deriverte av polynomet er: [2, -3] (som tilsvarer 2x - 3)