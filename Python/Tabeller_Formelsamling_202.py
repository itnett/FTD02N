python
def beregn_varmekapasitet(masse, spesifikk_varmekapasitet):
  """Beregner varmekapasiteten til et stoff.

  Args:
      masse (float): Massen til stoffet (i kg).
      spesifikk_varmekapasitet (float): Spesifikk varmekapasitet til stoffet (i J/(kg·K)).

  Returns:
      float: Varmekapasiteten (i J/K).
  """
  return masse * spesifikk_varmekapasitet

# Eksempel:
masse_vann = 1  # kg
spesifikk_varmekapasitet_vann = 4186  # J/(kg·K)

varmekapasitet_vann = beregn_varmekapasitet(masse_vann, spesifikk_varmekapasitet_vann)
print("Varmekapasiteten til 1 kg vann er:", varmekapasitet_vann, "J/K")