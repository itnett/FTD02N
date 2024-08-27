python
from scipy.special import comb

n = 5  # Antall elementer
k = 3  # Antall elementer i hver kombinasjon

antall_kombinasjoner = comb(n, k, exact=True)
print("Antall kombinasjoner:", antall_kombinasjoner)