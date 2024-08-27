python
def los_linear_likning(a, b):
  """Løser en lineær likning på formen ax + b = 0.

  Args:
      a (float): Koeffisienten foran x.
      b (float): Konstantleddet.

  Returns:
      float: Løsningen x.

  Raises:
      ZeroDivisionError: Hvis a er 0 (likningen er ikke lineær).
  """
  if a == 0:
    raise ZeroDivisionError("Likningen er ikke lineær (a = 0).")
  else:
    x = -b / a
    return x

# Eksempelbruk:
a = 3
b = -9
losning = los_linear_likning(a, b)
print("Løsningen til likningen", a, "x +", b, "= 0 er:", losning)  # Output: Løsningen til likningen 3x + -9 = 0 er: 3.0