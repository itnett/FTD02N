python
def beregn_prosentandel(delverdi, helhet):
  """Beregner prosentandelen en delverdi utgjør av en helhet.

  Args:
      delverdi (float): Delverdien.
      helhet (float): Helheten.

  Returns:
      float: Prosentandelen delverdien utgjør av helheten.

  Raises:
      ZeroDivisionError: Hvis helheten er null.
  """
  if helhet == 0:
    raise ZeroDivisionError("Helheten kan ikke være null.")
  return (delverdi / helhet) * 100

# Eksempelbruk:
delverdi = 30
helhet = 120
prosentandel = beregn_prosentandel(delverdi, helhet)
print(delverdi, "er", prosentandel, "% av", helhet)  # Output: 30 er 25.0 % av 120