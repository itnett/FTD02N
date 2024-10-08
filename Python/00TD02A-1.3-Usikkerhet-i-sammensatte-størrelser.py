python
import numpy as np

# Eksempel på målinger
l_malinger = [5.78, 5.77, 5.79, 5.76, 5.80]  # Lengdemålinger i cm

# Beregninger
gjennomsnitt_l = np.mean(l_malinger)
maks_min_l = (max(l_malinger) - min(l_malinger)) / 2
standardavvik_l = np.std(l_malinger, ddof=1)
standardfeil_l = standardavvik_l / np.sqrt(len(l_malinger))

# Skriv ut resultatene
print(f"Gjennomsnitt: {gjennomsnitt_l:.2f} cm")
print(f"Maks-min-metoden: ±{maks_min_l:.2f} cm")
print(f"Standardavvik: {standardavvik_l:.2f} cm")
print(f"Standardfeil: {standardfeil_l:.2f} cm")