python
import matplotlib.pyplot as plt

# Liste over tilgjengelige stiler
print(plt.style.available)

# Bruk en bestemt stil
with plt.style.context('ggplot'):
    # ... (din kode for å lage grafen)