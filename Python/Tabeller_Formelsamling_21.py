python
from scipy.stats import norm

mu = 0  # Forventningsverdi
sigma = 1  # Standardavvik

forventning = norm.mean(mu, sigma)
varians = norm.var(mu, sigma)

print("Forventningsverdi:", forventning)
print("Varians:", varians)