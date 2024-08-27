python
def total_relativistisk_energi(m0, v):
  """
  Beregner den totale relativistiske energien E for en gitt hvilemasse m0 og hastighet v.

  Args:
      m0 (float): Hvilemassen til objektet (i kilogram).
      v (float): Hastigheten til objektet (i meter per sekund).

  Returns:
      float: Den totale relativistiske energien E (i joule).
  """
  gamma = lorentz_faktor(v)
  E = gamma * m0 * c**2
  return E

def relativistisk_kinetisk_energi(m0, v):
  """
  Beregner den relativistiske kinetiske energien K for en gitt hvilemasse m0 og hastighet v.

  Args:
      m0 (float): Hvilemassen til objektet (i kilogram).
      v (float): Hastigheten til objektet (i meter per sekund).

  Returns:
      float: Den relativistiske kinetiske energien K (i joule).
  """
  E = total_relativistisk_energi(m0, v)
  E0 = hvileenergi(m0)
  K = E - E0
  return K

# Eksempelbruk:
E = total_relativistisk_energi(m0, v)
K = relativistisk_kinetisk_energi(m0, v)
print("Total relativistisk energi E er:", E, "joule")
print("Relativistisk kinetisk energi K er:", K, "joule")