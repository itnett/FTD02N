python
from scipy.stats import binom

p = 0.5  # Sannsynlighet for suksess
n = 10  # Antall forsøk
k = 5  # Antall suksesser

sannsynlighet = binom.pmf(k, n, p)
print("Sannsynlighet for 5 suksesser på 10 forsøk:", sannsynlighet)