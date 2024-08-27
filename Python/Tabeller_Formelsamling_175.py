python
def konverter_si_prefiks(verdi, gammel_prefiks, ny_prefiks):
  """
  Konverterer en verdi fra en SI-prefiks til en annen.

  Args:
      verdi (float): Den numeriske verdien som skal konverteres.
      gammel_prefiks (str): Den opprinnelige SI-prefikset (f.eks., 'k' for kilo).
      ny_prefiks (str): Det nye SI-prefikset (f.eks., 'm' for milli).

  Returns:
      float: Den konverterte verdien.

  Raises:
      ValueError: Hvis ugyldige prefikser blir gitt.
  """
  prefikser = {
      'Y': 1e24, 'Z': 1e21, 'E': 1e18, 'P': 1e15, 'T': 1e12,
      'G': 1e9, 'M': 1e6, 'k': 1e3, 'h': 1e2, 'da': 1e1,
      'd': 1e-1, 'c': 1e-2, 'm': 1e-3, 'µ': 1e-6, 'n': 1e-9,
      'p': 1e-12, 'f': 1e-15, 'a': 1e-18, 'z': 1e-21, 'y': 1e-24
  }

  if gammel_prefiks not in prefikser or ny_prefiks not in prefikser:
    raise ValueError("Ugyldig SI-prefiks.")

  return verdi * prefikser[gammel_prefiks] / prefikser[ny_prefiks]

# Eksempelbruk:
verdi = 2.5  # 2.5 kilometer
gammel_prefiks = 'k'
ny_prefiks = 'm'
konvertert_verdi = konverter_si_prefiks(verdi, gammel_prefiks, ny_prefiks)
print(f"{verdi}{gammel_prefiks} = {konvertert_verdi}{ny_prefiks}")  # Output: 2.5k = 2500.0m