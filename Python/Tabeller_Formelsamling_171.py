python
def polynomfunksjon(x, koeffisienter):
  """
  Beregner verdien av en polynomfunksjon.

  Args:
      x (float): x-verdien
      koeffisienter (list): En liste med koeffisienter, der koeffisienter[i] er koeffisienten foran x^i.

  Returns:
      float: y-verdien
  """
  y = 0
  for i, koeff in enumerate(koeffisienter):
    y += koeff * x**i
  return y

# Eksempelbruk:
koeffisienter = [1, -3, 2]  # Koeffisienter for polynomet x^2 - 3x + 2
x_verdier = [-1, 0, 1, 2, 3]

for x in x_verdier:
  y = polynomfunksjon(x, koeffisienter)
  print(f"f({x}) = {y}")