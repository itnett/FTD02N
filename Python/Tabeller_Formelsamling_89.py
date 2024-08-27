python
# Eksempel på beregning av sannsynlighet for pålitelighet
import math

p = 0.95  # Sannsynlighet for at en komponent fungerer
n = 10  # Antall komponenter
system_p = p ** n
print(f"Sannsynlighet for at hele systemet fungerer: {system_p}")