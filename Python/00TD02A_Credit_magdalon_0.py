python
import math

høyde = float(input("Skriv inn høyden objektet slippes fra (i meter): "))
tyngdeakselerasjon = 9.81  # m/s^2

tid = math.sqrt(2 * høyde / tyngdeakselerasjon)
hastighet = tyngdeakselerasjon * tid

print(f"Objektet treffer bakken etter {tid:.2f} sekunder med en hastighet på {hastighet:.2f} m/s.")