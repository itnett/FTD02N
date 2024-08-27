python
import numpy as np

class Sinusfunksjon:
    def __init__(self, amplitude, periode, faseforskyvning, likevektslinje):
        self.amplitude = amplitude
        self.periode = periode
        self.faseforskyvning = faseforskyvning
        self.likevektslinje = likevektslinje

    def __call__(self, t):
        return self.amplitude * np.sin(2 * np.pi * t / self.periode + self.faseforskyvning) + self.likevektslinje