python
def lineær_funksjon(x, a, b):
  """
  Beregner verdien av en lineær funksjon y = ax + b.

  Args:
      x (float): x-verdien
      a (float): Stigningstallet
      b (float): Konstantleddet

  Returns:
      float: y-verdien
  """
  y = a * x + b
  return y

# Eksempelbruk:
a = 2  # Stigningstall
b = 1  # Konstantledd
x_verdier = [-2, -1, 0, 1, 2]

for x in x_verdier:
  y = lineær_funksjon(x, a, b)
  print(f"f({x}) = {y}")