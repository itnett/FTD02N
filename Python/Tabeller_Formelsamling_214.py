python
import math

def beregn_rot(tall, n):
  """
  Beregner n-te roten av et tall.

  Args:
      tall (float): Tallet du vil finne roten av.
      n (int): Rotens orden (f.eks., 2 for kvadratrot, 3 for kubikkrot).

  Returns:
      float: n-te roten av tallet.

  Raises:
      ValueError: Hvis tallet er negativt og n er partall.
  """
  if tall < 0 and n % 2 == 0:
    raise ValueError("Kan ikke ta partallsrot av et negativt tall.")
  return tall**(1/n)

# Eksempelbruk:
tall = 8
n = 3
rot = beregn_rot(tall, n)
print(f"Kubikkroten av {tall} er: {rot}")  # Output: Kubikkroten av 8 er: 2.0