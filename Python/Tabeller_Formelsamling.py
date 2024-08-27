python
import math

def los_andregradslikning(a, b, c):
  """Løser en andregradslikning på formen ax^2 + bx + c = 0.

  Args:
      a (float): Koeffisienten foran x^2.
      b (float): Koeffisienten foran x.
      c (float): Konstantleddet.

  Returns:
      tuple: Et tuppel med to løsninger (x1, x2), eller None hvis det ikke finnes reelle løsninger.
  """
  if a == 0:
    raise ZeroDivisionError("Likningen er ikke andregrads (a = 0).")

  diskriminant = b**2 - 4*a*c

  if diskriminant > 0:
    x1 = (-b + math.sqrt(diskriminant)) / (2*a)
    x2 = (-b - math.sqrt(diskriminant)) / (2*a)
    return (x1, x2)
  elif diskriminant == 0:
    x = -b / (2*a)
    return (x, x)  # To like løsninger
  else:
    return None  # Ingen reelle løsninger

# Eksempelbruk:
a = 2
b = -5
c = 3
losninger = los_andregradslikning(a, b, c)
if losninger:
  print("Løsningene til likningen", a, "x^2 +", b, "x +", c, "= 0 er:", losninger)
else:
  print("Likningen har ingen reelle løsninger.")