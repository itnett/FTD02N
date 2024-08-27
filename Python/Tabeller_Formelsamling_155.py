python
def hvileenergi(m0):
  """
  Beregner hvileenergien E0 for en gitt hvilemasse m0.

  Args:
      m0 (float): Hvilemassen til objektet (i kilogram).

  Returns:
      float: Hvileenergien E0 (i joule).
  """
  c = 299792458  # Lyshastigheten i vakuum (m/s)
  E0 = m0 * c**2
  return E0

# Eksempelbruk:
E0 = hvileenergi(m0)
print("Hvileenergien E0 er:", E0, "joule")