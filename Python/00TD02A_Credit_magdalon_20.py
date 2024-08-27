python
import numpy as np
import scipy.stats as st

data = [1.5, 2.3, 1.8, 2.1, 1.9]
konfidensnivå = 0.95

gjennomsnitt = np.mean(data)
standardfeil = st.sem(data)
konfidensintervall = st.t.interval(konfidensnivå, len(data) - 1, loc=gjennomsnitt, scale=standardfeil)

print(f"Gjennomsnitt: {gjennomsnitt:.2f}")
print(f"{konfidensnivå * 100}% konfidensintervall: {konfidensintervall}")