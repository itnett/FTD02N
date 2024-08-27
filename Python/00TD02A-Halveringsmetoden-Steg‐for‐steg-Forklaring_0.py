python
# Importerer alle funksjoner og moduler fra pylab (unødvendig i dette tilfellet)
from pylab import *

# Definerer grensene for intervallet og ønsket nøyaktighet
a = 0
b = 1
noyaktighet = 0.0001

# Definerer funksjonen f(x) som vi vil finne nullpunktet til
def f(x):
    return x**3 + x - 1

# Beregner midtpunktet av intervallet [a, b]
m = (a + b) / 2

# Hovedløkka som utfører halveringsmetoden
while abs(f(m)) >= noyaktighet:
    if f(a) * f(m) < 0:
        b = m  # Hvis roten er i [a, m], oppdater b til m
    else:
        a = m  # Hvis roten er i [m, b], oppdater a til m
    m = (a + b) / 2  # Beregn nytt midtpunkt

# Skriver ut løsningen avrundet til 3 desimaler
print("Løsningen på likningen er ", round(m, 3))