python
from sympy import simplify, Symbol

def sammentrekk_uttrykk(uttrykk_str):
  """
  Sammentrekker et algebraisk uttrykk.

  Args:
      uttrykk_str (str): Uttrykket som skal sammentrekkes (f.eks., "3*x + 5*x - 2*y + 4*y").

  Returns:
      str: Det sammentrukne uttrykket.
  """
  x, y = symbols('x y')  # Definerer symbolene x og y
  uttrykk = eval(uttrykk_str)  # Konverterer strengen til et SymPy-uttrykk
  return str(simplify(uttrykk))  # Forenkler uttrykket og returnerer det som en streng

# Eksempelbruk:
uttrykk = "3*x + 5*x - 2*y + 4*y"
sammentrukket = sammentrekk_uttrykk(uttrykk)
print("Sammentrukket uttrykk:", sammentrukket)  # Output: Sammentrukket uttrykk: 8*x + 2*y