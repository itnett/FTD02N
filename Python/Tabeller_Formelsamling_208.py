python
def addere_brøker(teller1, nevner1, teller2, nevner2):
  """Adderer to brøker.

  Args:
      teller1 (int): Telleren i den første brøken.
      nevner1 (int): Nevneren i den første brøken.
      teller2 (int): Telleren i den andre brøken.
      nevner2 (int): Nevneren i den andre brøken.

  Returns:
      Fraction: Summen av de to brøkene, forenklet.
  """
  return forenkle_brøk(teller1 * nevner2 + teller2 * nevner1, nevner1 * nevner2)

def subtrahere_brøker(teller1, nevner1, teller2, nevner2):
  """Subtraherer to brøker.

  Args:
      teller1 (int): Telleren i den første brøken.
      nevner1 (int): Nevneren i den første brøken.
      teller2 (int): Telleren i den andre brøken.
      nevner2 (int): Nevneren i den andre brøken.

  Returns:
      Fraction: Differansen mellom de to brøkene, forenklet.
  """
  return forenkle_brøk(teller1 * nevner2 - teller2 * nevner1, nevner1 * nevner2)

# Eksempelbruk:
print("1/2 + 2/3 =", addere_brøker(1, 2, 2, 3))  # Output: 1/2 + 2/3 = 7/6
print("3/4 - 1/2 =", subtrahere_brøker(3, 4, 1, 2))  # Output: 3/4 - 1/2 = 1/4