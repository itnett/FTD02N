python
import math

def lorentz_faktor(v):
  """
  Beregner Lorentz-faktoren γ for en gitt hastighet v.

  Args:
      v (float): Hastigheten til objektet (i meter per sekund).

  Returns:
      float: Lorentz-faktoren γ.

  Raises:
      ValueError: Hvis hastigheten v er større enn eller lik lyshastigheten.
  """
  c = 299792458  # Lyshastigheten i vakuum (m/s)

  if v >= c:
    raise ValueError("Hastigheten kan ikke være større enn eller lik lyshastigheten.")

  gamma = 1 / math.sqrt(1 - (v ** 2) / (c ** 2))
  return gamma

# Eksempelbruk:
v = 0.5 * 299792458  # Halvparten av lyshastigheten
gamma = lorentz_faktor(v)
print("Lorentz-faktoren γ for v =", v, "m/s er:", gamma)