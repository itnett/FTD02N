python
import math

def briggsk_logaritme(x):
  """
  Beregner den Briggske logaritmen (log₁₀) til et tall.

  Args:
      x (float): Tallet du vil finne logaritmen til.

  Returns:
      float: Den Briggske logaritmen til tallet.

  Raises:
      ValueError: Hvis tallet er mindre enn eller lik 0.
  """
  if x <= 0:
    raise ValueError("Tallet må være positivt.")
  return math.log10(x)

# Eksempelbruk:
tall = 100
logaritme = briggsk_logaritme(tall)
print("log₁₀(", tall, ") =", logaritme)  # Output: log₁₀( 100 ) = 2.0