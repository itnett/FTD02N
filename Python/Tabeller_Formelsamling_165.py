python
from sympy import solve

def los_for_variabel(formel, variabel):
  """
  Løser en formel for en gitt variabel.

  Args:
      formel (str): Formelen (f.eks., "F = m*a")
      variabel (str): Variabelen du vil løse for (f.eks., "a")

  Returns:
      str: Formelen løst for den gitte variabelen (f.eks., "a = F/m")
  """
  losning = solve(formel, variabel)
  if len(losning) == 1:
    return f"{variabel} = {losning[0]}"
  else:
    return "Fant flere eller ingen løsninger."

# Eksempelbruk:
formel = "F = m*a"
variabel = "a"
ny_formel = los_for_variabel(formel, variabel)
print("Formelen løst for", variabel, "er:", ny_formel)  # Output: Formelen løst for a er: a = F/m