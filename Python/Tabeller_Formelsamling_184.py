python
def beregn_arbeid(kraft, strekning, vinkel=0):
  """Beregner arbeid utført av en kraft."""
  import math
  return kraft * strekning * math.cos(math.radians(vinkel))  # Konverterer vinkel til radianer

def beregn_effekt(arbeid, tid):
  """Beregner effekt utført over en gitt tid."""
  return arbeid / tid

def beregn_virkningsgrad(nyttig_energi, tilført_energi):
  """Beregner virkningsgraden til en prosess."""
  return (nyttig_energi / tilført_energi) * 100

# Eksempel:
kraft = 50  # N
strekning = 10  # m
vinkel = 30  # grader
tid = 20  # s
nyttig_energi = 200  # J
tilført_energi = 300  # J

arbeid = beregn_arbeid(kraft, strekning, vinkel)
effekt = beregn_effekt(arbeid, tid)
virkningsgrad = beregn_virkningsgrad(nyttig_energi, tilført_energi)

print("Arbeid:", arbeid, "J")
print("Effekt:", effekt, "W")
print("Virkningsgrad:", virkningsgrad, "%")