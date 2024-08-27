python
import math

def areal_rektangel(lengde, bredde):
  """
  Beregner arealet av et rektangel.

  Args:
    lengde (float): Lengden til rektangelet.
    bredde (float): Bredden til rektangelet.

  Returns:
    float: Arealet av rektangelet.
  """
  return lengde * bredde

def omkrets_rektangel(lengde, bredde):
  """
  Beregner omkretsen av et rektangel.

  Args:
    lengde (float): Lengden til rektangelet.
    bredde (float): Bredden til rektangelet.

  Returns:
    float: Omkretsen av rektangelet.
  """
  return 2 * (lengde + bredde)

def areal_sirkel(radius):
  """
  Beregner arealet av en sirkel.

  Args:
    radius (float): Radiusen til sirkelen.

  Returns:
    float: Arealet av sirkelen.
  """
  return math.pi * radius**2

def omkrets_sirkel(radius):
  """
  Beregner omkretsen av en sirkel.

  Args:
    radius (float): Radiusen til sirkelen.

  Returns:
    float: Omkretsen av sirkelen.
  """
  return 2 * math.pi * radius

# Eksempelbruk:
lengde = 5
bredde = 3
radius = 2

print("Areal av rektangel:", areal_rektangel(lengde, bredde))
print("Omkrets av rektangel:", omkrets_rektangel(lengde, bredde))
print("Areal av sirkel:", areal_sirkel(radius))
print("Omkrets av sirkel:", omkrets_sirkel(radius))