python
import matplotlib.pyplot as plt
import numpy as np

år = [2021, 2022, 2023]
kritiske_sårbarheter = [5, 8, 12]
høye_sårbarheter = [10, 15, 20]

x = np.arange(len(år))  # Posisjonene til søylene på x-aksen
bredde = 0.35  # Bredden på hver søyle

plt.bar(x - bredde/2, kritiske_sårbarheter, bredde, label='Kritisk')
plt.bar(x + bredde/2, høye_sårbarheter, bredde, label='Høy')

plt.xticks(x, år)  # Sett årstallene på x-aksen
plt.title("Antall sårbarheter per år")
plt.ylabel("Antall sårbarheter")
plt.legend()
plt.show()