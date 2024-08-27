python
import math

def eksponentialfunksjon(x, a):
  """
  Beregner verdien av en eksponentialfunksjon y = a^x.

  Args:
      x (float): x-verdien
      a (float): Grunntallet (må være positivt)

  Returns:
      float: y-verdien

  Raises:
      ValueError: Hvis grunntallet a er mindre enn eller lik 0.
  """
  if a <= 0:
    raise ValueError("Grunntallet må være positivt.")
  y = a**x
  return y

# Eksempelbruk:
a = 2  # Grunntall
x_verdier = [-2, -1, 0, 1, 2]

for x in x_verdier:
  y = eksponentialfunksjon(x, a)
  print(f"f({x}) = {y}")