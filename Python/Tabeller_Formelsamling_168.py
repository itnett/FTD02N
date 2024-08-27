python
import math

def sinus(motstående, hypotenus):
  """
  Beregner sinus til en vinkel i en rettvinklet trekant.

  Args:
    motstående (float): Lengden av den motstående kateten til vinkelen.
    hypotenus (float): Lengden av hypotenusen.

  Returns:
    float: Sinusverdien til vinkelen.
  """
  return motstående / hypotenus

def cosinus(hosliggende, hypotenus):
  """
  Beregner cosinus til en vinkel i en rettvinklet trekant.

  Args:
    hosliggende (float): Lengden av den hosliggende kateten til vinkelen.
    hypotenus (float): Lengden av hypotenusen.

  Returns:
    float: Cosinusverdien til vinkelen.
  """
  return hosliggende / hypotenus

def tangens(motstående, hosliggende):
  """
  Beregner tangens til en vinkel i en rettvinklet trekant.

  Args:
    motstående (float): Lengden av den motstående kateten til vinkelen.
    hosliggende (float): Lengden av den hosliggende kateten til vinkelen.

  Returns:
    float: Tangensverdien til vinkelen.
  """
  return motstående / hosliggende

# Eksempelbruk:
motstående = 3
hosliggende = 4
hypotenus = pytagoras(motstående, hosliggende)  # Bruker pytagoras-funksjonen fra tidligere

print("Sinus:", sinus(motstående, hypotenus))
print("Cosinus:", cosinus(hosliggende, hypotenus))
print("Tangens:", tangens(motstående, hosliggende))