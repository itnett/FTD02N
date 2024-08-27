python
from sympy import symbols, Eq, solve

def los_likningssett(eq1, eq2):
  """
  Løser et likningssett med to ukjente.

  Args:
      eq1 (str): Den første likningen (f.eks., "2*x + 3*y = 7")
      eq2 (str): Den andre likningen (f.eks., "x - y = 1")

  Returns:
      dict: En ordbok med løsningene (f.eks., {x: 2, y: 1})
  """
  x, y = symbols('x y')
  likning1 = Eq(eval(eq1.replace('=', ',')))  # Konverterer strengen til en SymPy-likning
  likning2 = Eq(eval(eq2.replace('=', ',')))
  losning = solve((likning1, likning2), (x, y))
  return losning

# Eksempelbruk:
likning1 = "2*x + 3*y = 7"
likning2 = "x - y = 1"
losning = los_likningssett(likning1, likning2)
print("Løsningen på likningssettet er:", losning)  # Output: Løsningen på likningssettet er: {x: 2, y: 1}