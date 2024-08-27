python
def beregn_strekning(fart, tid):
  """
  Beregner strekningen et objekt tilbakelegger ved konstant fart.

  Args:
    fart (float): Farten til objektet (i meter per sekund, m/s).
    tid (float): Tiden objektet beveger seg (i sekunder, s).

  Returns:
    float: Tilbakelagt strekning (i meter, m).
  """
  strekning = fart * tid
  return strekning

# Eksempelbruk:
fart = 5  # m/s
tid = 10  # s

strekning = beregn_strekning(fart, tid)
print("Tilbakelagt strekning er:", strekning, "m")