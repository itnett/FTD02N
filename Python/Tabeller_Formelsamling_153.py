python
def lengdekontraksjon(L0, v):
  """
  Beregner den relativistiske lengdekontraksjonen L for en gitt egenlengde L0 og hastighet v.

  Args:
      L0 (float): Egenlengden (lengden målt i objektets eget referansesystem).
      v (float): Hastigheten til objektet (i meter per sekund).

  Returns:
      float: Den relativistiske lengden L.
  """
  gamma = lorentz_faktor(v)
  L = L0 / gamma
  return L

# Eksempelbruk:
L0 = 1  # En meter egenlengde
L = lengdekontraksjon(L0, v)
print("Lengden L for en observatør i ro er:", L, "meter")