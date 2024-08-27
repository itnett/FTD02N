python
def sannsynlighet(gunstige_utfall, mulige_utfall):
  """
  Beregner sannsynligheten for en hendelse.

  Args:
      gunstige_utfall (int): Antall utfall som er gunstige for hendelsen.
      mulige_utfall (int): Totalt antall mulige utfall.

  Returns:
      float: Sannsynligheten for hendelsen (mellom 0 og 1).

  Raises:
      ValueError: Hvis gunstige_utfall er større enn mulige_utfall eller noen av argumentene er negative.
  """
  if gunstige_utfall > mulige_utfall or gunstige_utfall < 0 or mulige_utfall < 0:
    raise ValueError("Ugyldige verdier for gunstige og/eller mulige utfall.")
  return gunstige_utfall / mulige_utfall

# Eksempelbruk:
gunstige_utfall = 2  # F.eks., antall røde kuler i en pose
mulige_utfall = 5  # F.eks., totalt antall kuler i posen
sannsynlighet_for_rød = sannsynlighet(gunstige_utfall, mulige_utfall)
print("Sannsynligheten for å trekke en rød kule er:", sannsynlighet_for_rød)  # Output: Sannsynligheten for å trekke en rød kule er: 0.4