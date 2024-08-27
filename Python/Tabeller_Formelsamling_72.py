python
import math

# Beregning av tyngde
def beregn_tyngde(masse, gravitasjon=9.81):
    return masse * gravitasjon

# Beregning av massetetthet
def beregn_massetetthet(masse, volum):
    return masse / volum

# Beregning av usikkerhet
def relativ_usikkerhet(verdi, usikkerhet):
    return (usikkerhet / verdi) * 100

# Eksempler
masse = 5.0  # kg
volum = 0.002  # m^3
usikkerhet_masse = 0.1  # kg

# Tyngde
tyngde = beregn_tyngde(masse)
print(f"Tyngde: {tyngde} N")

# Massetetthet
massetetthet = beregn_massetetthet(masse, volum)
print(f"Massetetthet: {massetetthet} kg/m^3")

# Relativ usikkerhet
rel_usikkerhet_masse = relativ_usikkerhet(masse, usikkerhet_masse)
print(f"Relativ usikkerhet i masse: {rel_usikkerhet_masse}%")