python
def beregn_kinetisk_energi(masse, hastighet):
  """Beregner kinetisk energi til et objekt."""
  return 0.5 * masse * hastighet**2

def beregn_potensiell_energi(masse, høyde, g=9.81):
  """Beregner potensiell energi i tyngdefeltet."""
  return masse * g * høyde

# Eksempel:
masse = 2  # kg
hastighet = 5  # m/s
høyde = 10  # m

kinetisk_energi = beregn_kinetisk_energi(masse, hastighet)
potensiell_energi = beregn_potensiell_energi(masse, høyde)

print("Kinetisk energi:", kinetisk_energi, "J")
print("Potensiell energi:", potensiell_energi, "J")