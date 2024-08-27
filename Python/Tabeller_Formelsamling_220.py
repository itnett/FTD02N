python
from sympy import factor

def faktoriser_uttrykk(uttrykk_str):
  """
  Faktoriserer et algebraisk uttrykk.

  Args:
      uttrykk_str (str): Uttrykket som skal faktoriseres (f.eks., "x**2 + 5*x + 6").

  Returns:
      str: Det faktoriserte uttrykket.
  """
  x = symbols('x')
  uttrykk = eval(uttrykk_str)
  return str(factor(uttrykk))

# Eksempelbruk:
uttrykk = "x**2 + 5*x + 6"
faktorisert = faktoriser_uttrykk(uttrykk)
print("Faktorisert uttrykk:", faktorisert)  # Output: Faktorisert uttrykk: (x + 2)*(x + 3)