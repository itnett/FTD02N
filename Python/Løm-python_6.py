python
import matplotlib.pyplot as plt

class Differansekostnadskurve:
    def __init__(self, faste_kostnader, variable_kostnader_per_enhet, produksjonsenheter):
        self.faste_kostnader = faste_kostnader
        self.variable_kostnader_per_enhet = variable_kostnader_per_enhet
        self.produksjonsenheter = produksjonsenheter

    def totale_kostnader(self):
        return [self.faste_kostnader + self.variable_kostnader_per_enhet * enhet for enhet i self.produksjonsenheter]

    def marginalkostnad(self):
        totale_kostnader = self.totale_kostnader()
        return [totale_kostnader[i+1] - totale_kostnader[i] for i in range(len(totale_kostnader)-1)]

produksjonsenheter = range(1, 11)
differansekostnad = Differansekostnadskurve(1000, 50, produksjonsenheter)

totale_kostnader = differansekostnad.totale_kostnader()
marginalkostnad = differansekostnad.marginalkostnad()

plt.plot(produksjonsenheter, totale_kostnader, label='Totale Kostnader')
plt.plot(produksjonsenheter[:-1], marginalkostnad, label='Marginalkostnad')
plt.xlabel('Produksjonsenheter')
plt.ylabel('Kostnad')
plt.legend()
plt.show()