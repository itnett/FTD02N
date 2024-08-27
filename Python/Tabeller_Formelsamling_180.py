python
def beregn_strekning_med_akselerasjon(startfart, akselerasjon, tid):
  """
  Beregner strekningen et objekt tilbakelegger ved konstant akselerasjon.

  Args:
    startfart (float): Startfarten til objektet (i meter per sekund, m/s).
    akselerasjon (float): Akselerasjonen til objektet (i meter per sekund i annen, m/s^2).
    tid (float): Tiden objektet beveger seg (i sekunder, s).

  Returns:
    float: Tilbakelagt strekning (i meter, m).
  """
  strekning = startfart * tid + 0.5 * akselerasjon * tid**2
  return strekning

def beregn_sluttfart(startfart, akselerasjon, tid):
  """
  Beregner sluttfarten til et objekt ved konstant akselerasjon.

  Args:
    startfart (float): Startfarten til objektet (i meter per sekund, m/s).
    akselerasjon (float): Akselerasjonen til objektet (i meter per sekund i annen, m/s^2).
    tid (float): Tiden objektet beveger seg (i sekunder, s).

  Returns:
    float: Sluttfarten til objektet (i meter per sekund, m/s).
  """
  sluttfart = startfart + akselerasjon * tid
  return sluttfart

# Eksempelbruk:
startfart = 0  # m/s (starter fra ro)
akselerasjon = 2  # m/s^2
tid = 5  # s

strekning = beregn_strekning_med_akselerasjon(startfart, akselerasjon, tid)
sluttfart = beregn_sluttfart(startfart, akselerasjon, tid)

print("Tilbakelagt strekning er:", strekning, "m")
print("Sluttfarten er:", sluttfart, "m/s")