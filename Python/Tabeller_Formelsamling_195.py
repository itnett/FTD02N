python
import numpy as np

def gjennomsnitt(data):
  """
  Beregner gjennomsnittet av en liste med tall.

  Args:
      data (list): En liste med tall.

  Returns:
      float: Gjennomsnittet av tallene.
  """
  return np.mean(data)

def standardavvik(data):
  """
  Beregner standardavviket til en liste med tall.

  Args:
      data (list): En liste med tall.

  Returns:
      float: Standardavviket til tallene.
  """
  return np.std(data)

# Eksempelbruk:
data = [1, 2, 3, 4, 5]
gjennomsnitt_verdi = gjennomsnitt(data)
standardavvik_verdi = standardavvik(data)
print("Gjennomsnitt:", gjennomsnitt_verdi)  # Output: Gjennomsnitt: 3.0
print("Standardavvik:", standardavvik_verdi)  # Output: Standardavvik: 1.4142135623730951