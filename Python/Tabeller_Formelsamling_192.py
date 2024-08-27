python
import math

def fakultet(n):
  """
  Beregner fakultetet til et tall n.

  Args:
      n (int): Et ikke-negativt heltall.

  Returns:
      int: n! (n fakultet).

  Raises:
      ValueError: Hvis n er negativt.
  """
  if n < 0:
    raise ValueError("Fakultet er ikke definert for negative tall.")
  return math.factorial(n)

def permutasjoner(n, r):
  """
  Beregner antall permutasjoner av r objekter valgt fra en mengde på n objekter.

  Args:
      n (int): Totalt antall objekter.
      r (int): Antall objekter som skal velges.

  Returns:
      int: nPr (antall permutasjoner).

  Raises:
      ValueError: Hvis n eller r er negative, eller hvis r er større enn n.
  """
  if n < 0 or r < 0 or r > n:
    raise ValueError("Ugyldige verdier for n og/eller r.")
  return math.factorial(n) // math.factorial(n - r)

def kombinasjoner(n, r):
  """
  Beregner antall kombinasjoner av r objekter valgt fra en mengde på n objekter.

  Args:
      n (int): Totalt antall objekter.
      r (int): Antall objekter som skal velges.

  Returns:
      int: nCr (antall kombinasjoner).

  Raises:
      ValueError: Hvis n eller r er negative, eller hvis r er større enn n.
  """
  if n < 0 or r < 0 or r > n:
    raise ValueError("Ugyldige verdier for n og/eller r.")
  return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Eksempelbruk:
n = 5
r = 3

print("Fakultet av", n, ":", fakultet(n))  # Output: Fakultet av 5 : 120
print("Permutasjoner av", r, "objekter fra", n, ":", permutasjoner(n, r))  # Output: Permutasjoner av 3 objekter fra 5 : 60
print("Kombinasjoner av", r, "objekter fra", n, ":", kombinasjoner(n, r))  # Output: Kombinasjoner av 3 objekter fra 5 : 10