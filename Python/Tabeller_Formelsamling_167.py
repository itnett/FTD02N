python
import math

def pytagoras(a, b):
  """
  Beregner hypotenusen (c) i en rettvinklet trekant gitt katetene a og b.

  Args:
    a (float): Lengden av det ene katetet.
    b (float): Lengden av det andre katetet.

  Returns:
    float: Lengden av hypotenusen.
  """
  c = math.sqrt(a**2 + b**2)
  return c

# Eksempelbruk:
a = 3
b = 4
hypotenus = pytagoras(a, b)
print("Hypotenusen er:", hypotenus)