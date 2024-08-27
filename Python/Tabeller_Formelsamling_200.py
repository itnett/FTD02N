python
import random

def simuler_gass(n_partikler, n_trinn):
  """Simulerer bevegelsen til gasspartikler i en boks.

  Args:
      n_partikler (int): Antall partikler.
      n_trinn (int): Antall tidssteg i simuleringen.
  """
  posisjoner = [(0, 0) for _ in range(n_partikler)]  # Startposisjoner

  for _ in range(n_trinn):
    for i in range(n_partikler):
      dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])  # Tilfeldig bevegelse
      posisjoner[i] = (posisjoner[i][0] + dx, posisjoner[i][1] + dy)

    # Visualiser posisjonene (du kan bruke matplotlib for å plotte dette)
    print(posisjoner)

# Eksempelbruk:
simuler_gass(10, 5)  # Simulerer 10 partikler over 5 tidssteg