python
def relativistisk_bevegelsesmengde(m0, v):
  """
  Beregner den relativistiske bevegelsesmengden p for en gitt hvilemasse m0 og hastighet v.

  Args:
      m0 (float): Hvilemassen til objektet (i kilogram).
      v (float): Hastigheten til objektet (i meter per sekund).

  Returns:
      float: Den relativistiske bevegelsesmengden p.
  """
  if v < 0.1 * 299792458:  # Sjekk om hastigheten er under 10% av lyshastigheten
    print("Hastigheten er lav, bruk klassisk mekanikk for bevegelsesmengde.")
    return m0 * v  # Klassisk bevegelsesmengde

  gamma = lorentz_faktor(v)
  p = gamma * m0 * v
  return p

# Eksempelbruk:
m0 = 1  # Ett kilogram hvilemasse
p = relativistisk_bevegelsesmengde(m0, v)
print("Den relativistiske bevegelsesmengden p er:", p, "kg*m/s")