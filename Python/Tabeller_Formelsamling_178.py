python
def beregn_akselerasjon(kraft, masse):
  """
  Beregner akselerasjonen til et objekt gitt kraft og masse.

  Args:
    kraft (float): Kraften som virker på objektet (i newton, N).
    masse (float): Massen til objektet (i kilogram, kg).

  Returns:
    float: Akselerasjonen til objektet (i meter per sekund i annen, m/s^2).
  """
  akselerasjon = kraft / masse
  return akselerasjon

# Eksempelbruk:
kraft = 10  # N
masse = 2  # kg

akselerasjon = beregn_akselerasjon(kraft, masse)
print("Akselerasjonen er:", akselerasjon, "m/s^2")