python
def beregn_varmeoverføring(masse, spesifikk_varmekapasitet, delta_temperatur):
  """Beregner varmeoverføringen (Q) til et stoff.

  Args:
      masse (float): Massen til stoffet (i kg).
      spesifikk_varmekapasitet (float): Spesifikk varmekapasitet til stoffet (i J/(kg·K)).
      delta_temperatur (float): Temperaturendringen (i K).

  Returns:
      float: Varmeoverføringen (i J).
  """
  return masse * spesifikk_varmekapasitet * delta_temperatur

# Eksempel:
masse = 1  # kg (vann)
spesifikk_varmekapasitet = 4186  # J/(kg·K) (vann)
delta_temperatur = 10  # K

varmeoverføring = beregn_varmeoverføring(masse, spesifikk_varmekapasitet, delta_temperatur)
print("Varmeoverføringen er:", varmeoverføring, "J")