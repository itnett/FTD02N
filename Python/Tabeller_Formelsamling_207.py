python
from fractions import Fraction

def forenkle_brøk(teller, nevner):
  """Forenkler en brøk til sin enkleste form.

  Args:
      teller (int): Telleren i brøken.
      nevner (int): Nevneren i brøken.

  Returns:
      Fraction: Den forenklede brøken.

  Raises:
      ZeroDivisionError: Hvis nevneren er null.
  """
  if nevner == 0:
    raise ZeroDivisionError("Nevneren kan ikke være null.")
  return Fraction(teller, nevner)

# Eksempelbruk:
teller = 12
nevner = 16
forenklet_brøk = forenkle_brøk(teller, nevner)
print(f"Brøken {teller}/{nevner} forenklet er: {forenklet_brøk}")  # Output: Brøken 12/16 forenklet er: 3/4