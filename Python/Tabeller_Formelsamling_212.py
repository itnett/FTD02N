python
def beregn_potens(grunn_tall, eksponent):
  """Beregner en potens.

  Args:
      grunn_tall (float): Grunntallet i potensen.
      eksponent (float): Eksponenten i potensen.

  Returns:
      float: Resultatet av potensen.
  """
  return grunn_tall ** eksponent

# Eksempelbruk:
grunn_tall = 2
eksponent = 3
resultat = beregn_potens(grunn_tall, eksponent)
print(f"{grunn_tall}^{eksponent} = {resultat}")  # Output: 2^3 = 8