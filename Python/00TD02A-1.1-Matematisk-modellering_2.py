python
import math

# Definer konstanter
g = 9.81  # Tyngdeakselerasjonen i m/s^2
l = 1.0   # Lengden av pendelen i meter

# Funksjon for å beregne svingetiden T
def beregn_svingetid(l):
    T = 2 * math.pi * math.sqrt(l / g)
    return T

# Test funksjonen med forskjellige lengder
lengder = [0.5, 1.0, 1.5]  # Eksempellengder i meter
for l in lengder:
    T = beregn_svingetid(l)
    print(f"Lengde: {l} m, Svingetid: {T:.2f} s")

# Legg til kode her for å samle inn data, utføre regresjonsanalyse, etc.