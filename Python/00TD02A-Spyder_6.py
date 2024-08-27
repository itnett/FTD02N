python
# Briggske logaritmer
import math

x = 100
log_x = math.log10(x)
print("Briggsk logaritme av 100:", log_x)

# Kombinatorikk
from scipy.special import comb

n = 5  # Antall elementer
k = 3  # Antall elementer i hver kombinasjon
kombinasjoner = comb(n, k)
print("Antall kombinasjoner:", kombinasjoner)