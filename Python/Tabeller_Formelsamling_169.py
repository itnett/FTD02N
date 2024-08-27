python
import math

def vektor_lengde(x, y):
  """
  Beregner lengden av en vektor i planet.

  Args:
    x (float): X-komponenten til vektoren.
    y (float): Y-komponenten til vektoren.

  Returns:
    float: Lengden av vektoren.
  """
  return math.sqrt(x**2 + y**2)

def vektor_addisjon(x1, y1, x2, y2):
  """
  Adderer to vektorer i planet.

  Args:
    x1 (float): X-komponenten til den første vektoren.
    y1 (float): Y-komponenten til den første vektoren.
    x2 (float): X-komponenten til den andre vektoren.
    y2 (float): Y-komponenten til den andre vektoren.

  Returns:
    tuple: Et tuppel med x- og y-komponentene til resultantvektoren.
  """
  return (x1 + x2, y1 + y2)

# Eksempelbruk:
x1, y1 = 3, 4
x2, y2 = -1, 2

lengde = vektor_lengde(x1, y1)
print("Lengde av vektor (3, 4):", lengde)

sum_vektor = vektor_addisjon(x1, y1, x2, y2)
print("Summen av vektorene (3, 4) og (-1, 2) er:", sum_vektor)