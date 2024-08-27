python
def tyngde(masse):
  """
  Beregner tyngden til et objekt med gitt masse på jorden.

  Args:
      masse (float): Massen til objektet (i kg).

  Returns:
      float: Tyngden til objektet (i N).
  """
  g = 9.81  # Tyngdeakselerasjonen på jorden (m/s^2)
  return masse * g

def massetetthet(masse, volum):
  """
  Beregner massetettheten til et objekt med gitt masse og volum.

  Args:
      masse (float): Massen til objektet (i kg).
      volum (float): Volumet til objektet (i m^3).

  Returns:
      float: Massetettheten til objektet (i kg/m^3).

  Raises:
      ZeroDivisionError: Hvis volumet er 0.
  """
  if volum == 0:
    raise ZeroDivisionError("Volumet kan ikke være 0.")
  return masse / volum

# Eksempelbruk:
masse = 5  # 5 kg
volum = 0.01  # 0.01 m^3

print("Tyngde:", tyngde(masse), "N")
print("Massetetthet:", massetetthet(masse, volum), "kg/m^3")