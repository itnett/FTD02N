python
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, sqrt, expand

# --- FYSIKK: KONSTANTER OG VARIABLER ---
gravitasjonskonstant = 9.81  # m/s^2 (kan endres)

# --- FUNKSJONER ---
def V(x, fyllingshastighet=2000/40):  # Væskevolum (liter) som funksjon av tid (minutter), med justerbar fyllingshastighet
    return 2000 - 2000 * (1 - x / 40)**2

def rett_linje(x, stigningstall=2, konstantledd=3):  # Rett linje med justerbare parametere
    return stigningstall * x + konstantledd

def eksponentiell_funksjon(x, startverdi=100, vekstfaktor=1.05):  # Eksponentiell funksjon med justerbare parametere
    return startverdi * vekstfaktor**x

def kinetisk_energi(m, v):
    return 0.5 * m * v**2

def potensiell_energi(m, h, g=gravitasjonskonstant):  # Potensiell energi med tyngdeakselerasjon som standardparameter
    return m * g * h

# --- VÆSKEVOLUM-ANALYSE ---
# Tidsparametere (kan endres)
starttid = 0
sluttid = 40
antall_punkter = 400

x_verdier = np.linspace(starttid, sluttid, antall_punkter)  # Array med tidspunkter
volum_verdier = V(x_verdier)  # Array med tilsvarende volumer

# Numerisk løsning for når volumet når 1000 liter
maal_volum = 1000  # Liter (kan endres)
tid_1000_liter = np.interp(maal_volum, volum_verdier, x_verdier)  # Bruker interpolasjon for å finne tidspunktet

# Maksimalt volum
maks_volum = V(sluttid)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_verdier, volum_verdier, label=f'V(x) = {2000} - {2000} * (1 - x/{40})^2')  # Dynamisk label
plt.axhline(y=maal_volum, color='r', linestyle='--', label=f'y = {maal_volum}')  # Dynamisk label
plt.axvline(x=sluttid, color='g', linestyle='--', label=f'x = {sluttid}')  # Dynamisk label
plt.scatter([starttid, tid_1000_liter, sluttid], [V(starttid), maal_volum, maks_volum], color='black')
# ... (rest av plottekoden er uendret)

# --- STATISTISK ANALYSE AV VOLUMDATA ---
# Dummydata (kan erstattes med reelle data)
volumdata = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]

gjennomsnitt = np.mean(volumdata)
median = np.median(volumdata)
q1 = np.percentile(volumdata, 25)
q3 = np.percentile(volumdata, 75)
stdavvik = np.std(volumdata)

# --- ALGEBRA: LØSE KVADRATISK LIKNING ---
# ... (uendret)

# --- TRIGONOMETRI: PYTHAGORAS ---
# ... (uendret)

# --- FYSIKK: ENERGIBEREGNINGER ---
masse = 10  # kg (kan endres)
hastighet = 5  # m/s (kan endres)
høyde = 10  # meter (kan endres)

kinetisk_energi_resultat = kinetisk_energi(masse, hastighet)
potensiell_energi_resultat = potensiell_energi(masse, høyde)

# --- FORKLARING OG SAMMENHENG ---
print(f"""
Forklaring av begreper og sammenhenger:

**Fyllingsprosess:**
Væskevolumet øker over tid, modellert av funksjonen V(x) = {2000} - {2000} * (1 - x/{40})^2. 
Startvolumet er {V(starttid)} liter, og det maksimale volumet er {maks_volum} liter etter {sluttid} minutter.
Volumet når {maal_volum} liter etter omtrent {round(tid_1000_liter, 2)} minutter.

**Statistisk analyse:**
Vi kan analysere volumdataene for å få innsikt i fordelingen. 
Gjennomsnittet er {gjennomsnitt} liter, medianen er {median} liter, 
første kvartil (Q1) er {q1} liter, og tredje kvartil (Q3) er {q3} liter. 
Standardavviket er {stdavvik} liter, som indikerer spredningen rundt gjennomsnittet.

**Algebra:**
Vi kan bruke algebra til å løse likninger, som å finne tidspunktet når et bestemt volum nås.

**Trigonometri:**
Vi kan bruke trigonometri til å beregne avstander og vinkler, for eksempel i konstruksjoner eller problemer med kraft og bevegelse.

**Fysikk:**
Vi kan beregne kinetisk energi ({kinetisk_energi_resultat:.2f} Joule) og potensiell energi ({potensiell_energi_resultat:.2f} Joule) for et objekt med masse {masse} kg, 
hastighet {hastighet} m/s, og høyde {høyde} meter. 
Tyngdeakselerasjonen er satt til {gravitasjonskonstant} m/s^2.

**Sammenhenger:**
Alle disse områdene henger sammen i realfaglige problemer. For eksempel kan vi bruke algebra til å løse likninger som oppstår i fysikk, eller bruke statistikk til å analysere data fra et fysikkforsøk.
""")