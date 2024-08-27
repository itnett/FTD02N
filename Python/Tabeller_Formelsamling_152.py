python
def tidsforlengelse(t0, v):
  """
  Beregner den relativistiske tidsforlengelsen t for en gitt egentid t0 og hastighet v.

  Args:
      t0 (float): Egentiden (tiden målt i objektets eget referansesystem).
      v (float): Hastigheten til objektet (i meter per sekund).

  Returns:
      float: Den relativistiske tiden t.
  """
  gamma = lorentz_faktor(v)
  t = gamma * t0
  return t

# Eksempelbruk:
t0 = 1  # Ett sekund egentid
t = tidsforlengelse(t0, v)
print("Tiden t for en observatør i ro er:", t, "sekunder")