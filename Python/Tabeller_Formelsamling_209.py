python
def multiplisere_brøker(teller1, nevner1, teller2, nevner2):
  """Multipliserer to brøker.

  Args:
      teller1 (int): Telleren i den første brøken.
      nevner1 (int): Nevneren i den første brøken.
      teller2 (int): Telleren i den andre brøken.
      nevner2 (int): Nevneren i den andre brøken.

  Returns:
      Fraction: Produktet av de to brøkene, forenklet.
  """
  return forenkle_brøk(teller1 * teller2, nevner1 * nevner2)

def dividere_brøker(teller1, nevner1, teller2, nevner2):
  """Dividerer to brøker.

  Args:
      teller1 (int): Telleren i den første brøken.
      nevner1 (int): Nevneren i den første brøken.
      teller2 (int): Telleren i den andre brøken.
      nevner2 (int): Nevneren i den andre brøken.

  Returns:
      Fraction: Kvotienten av de to brøkene, forenklet.

  Raises:
      ZeroDivisionError: Hvis teller2 eller nevner2 er null.
  """
  if teller2 == 0 or nevner2 == 0:
    raise ZeroDivisionError("Kan ikke dividere med null.")
  return forenkle_brøk(teller1 * nevner2, nevner1 * teller2)

# Eksempelbruk:
print("1/2 * 2/3 =", multiplisere_brøker(1, 2, 2, 3))  # Output: 1/2 * 2/3 = 1/3
print("3/4 / 1/2 =", dividere_brøker(3, 4, 1, 2))  # Output: 3/4 / 1/2 = 3/2