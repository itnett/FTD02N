python
import numpy as np
import matplotlib.pyplot as plt
from sympy import fourier_transform, symbols, pi

t, f = symbols('t f')
signal = sin(2*pi*5*t) + 0.5*sin(2*pi*10*t)  # Et enkelt signal med to frekvenser

# Beregn Fourier-transformasjonen
signal_fft = fourier_transform(signal, t, f)

# Plot signalet og dets Fourier-transform
p1 = sy.plot(signal, (t, 0, 1), show=False)
p2 = sy.plot(abs(signal_fft), (f, 0, 15), show=False)
p1.append(p2[0])
p1.show()