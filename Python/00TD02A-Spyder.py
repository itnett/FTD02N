python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from sympy import symbols, Eq, solve, sqrt

# --- FYSIKK: KONSTANTER OG VARIABLER ---
gravitasjonskonstant = 9.81  # m/s^2 (kan endres)

# --- FUNKSJONER ---
def V(x, fyllingshastighet=2000/40, maks_volum=2000):
    """Beregner væskevolum (liter) som funksjon av tid (minutter)."""
    return maks_volum * (1 - (1 - x / 40)**2)

def rett_linje(x, stigningstall=2, konstantledd=3):
    """Definerer en rett linje."""
    return stigningstall * x + konstantledd

def eksponentiell_funksjon(x, startverdi=100, vekstfaktor=1.05):
    """Definerer en eksponentiell funksjon."""
    return startverdi * vekstfaktor**x

def kinetisk_energi(m, v):
    """Beregner kinetisk energi."""
    return 0.5 * m * v**2

def potensiell_energi(m, h, g=gravitasjonskonstant):
    """Beregner potensiell energi."""
    return m * g * h

# --- VÆSKEVOLUM-ANALYSE ---
# Tidsparametere (kan endres)
starttid = 0
sluttid = 40
antall_punkter = 400

# Fyllingshastighet (liter per minutt)
fyllingshastighet = 50  # Kan endres for å se effekten på fyllingsprosessen

# Målvolum (kan endres)
maal_volum = 1500  # Liter

# Maks kapasitet på beholderen (liter)
maks_volum = 2000  # Kan endres for å se effekten på fyllingsprosessen

x_verdier = np.linspace(starttid, sluttid, antall_punkter)
volum_verdier = V(x_verdier, fyllingshastighet, maks_volum)

# Numerisk løsning for når volumet når målvolum
def likning_for_maal_volum(x):
    return V(x, fyllingshastighet, maks_volum) - maal_volum

tid_maal_volum = fsolve(likning_for_maal_volum, x0=sluttid/2)[0]  # Antar at beholderen fylles opp i løpet av tidsintervallet

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_verdier, volum_verdier, label=f'V(x) = {maks_volum} * (1 - (1 - x/{40})^2)')
plt.axhline(y=maal_volum, color='r', linestyle='--', label=f'y = {maal_volum}')
plt.axvline(x=tid_maal_volum, color='g', linestyle='--', label=f'x = {round(tid_maal_volum, 2)}')
plt.scatter([starttid, tid_maal_volum, sluttid], [V(starttid, fyllingshastighet, maks_volum), maal_volum, V(sluttid, fyllingshastighet, maks_volum)], color='black')
plt.text(starttid, V(starttid, fyllingshastighet, maks_volum) + 50, 'C (0, 0)', fontsize=12, ha='right')
plt.text(tid_maal_volum, maal_volum + 50, f'A ({round(tid_maal_volum, 2)}, {maal_volum})', fontsize=12, ha='left')
plt.text(sluttid, V(sluttid, fyllingshastighet, maks_volum) + 50, f'B ({sluttid}, {V(sluttid, fyllingshastighet, maks_volum)})', fontsize=12, ha='left')

plt.xlabel('Tid (minutter)')
plt.ylabel('Volum (liter)')
plt.title(f'Fyllingshastighet: {fyllingshastighet} liter/minutt, Maks volum: {maks_volum} liter')  # Oppdatert tittel
plt.legend()
plt.grid(True)
plt.show()

# --- STATISTISK ANALYSE AV VOLUMDATA ---
# Simulerte data (kan erstattes med reelle data)
np.random.seed(0)  # For å få reproducerbare resultater
volumdata = V(np.random.uniform(starttid, sluttid, 100), fyllingshastighet, maks_volum)  # 100 tilfeldige tidspunkter

gjennomsnitt = np.mean(volumdata)
median = np.median(volumdata)
q1 = np.percentile(volumdata, 25)
q3 = np.percentile(volumdata, 75)
stdavvik = np.std(volumdata)

# --- ALGEBRA: LØSE KVADRATISK LIKNING ---
x = symbols('x')
kvadratisk_likning = Eq(x**2 - 5*x + 6, 0)
løsninger_kvadratisk = solve(kvadratisk_likning, x)

# --- TRIGONOMETRI: PYTHAGORAS ---
a = 3
b = 4
hypotenus = sqrt(a**2 + b**2)

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
Væskevolumet øker over tid, modellert av funksjonen V(x) = {maks_volum} * (1 - (1 - x/{40})^2).
Med en fyllingshastighet på {fyllingshastighet} liter/minutt, tar det {round(tid_maal_volum, 2)} minutter å nå {maal_volum} liter.
Startvolumet er {V(starttid, fyllingshastighet, maks_volum)} liter, og det maksimale volumet er {maks_volum} liter etter {sluttid} minutter.

**Statistisk analyse av fyllingsprosessen:**
Vi simulerte 100 tilfeldige fyllinger og analyserte volumdataene:
* Gjennomsnittlig volum: {gjennomsnitt:.2f} liter
* Medianvolum: {median:.2f} liter
* 25% av fyllingene hadde et volum under {q1:.2f} liter (Q1)
* 75% av fyllingene hadde et volum under {q3:.2f} liter (Q3)
* Standardavviket er {stdavvik:.2f} liter, som indikerer spredningen i volumene.

**Algebra:**
Vi kan bruke algebra til å løse likninger, som å finne tidspunktet når et bestemt volum nås.
Eksempel: Løsningene for kvadratisk likning x^2 - 5x + 6 = 0 er {løsninger_kvadratisk}.

**Trigonometri:**
Vi kan bruke trigonometri til å beregne avstander og vinkler, for eksempel i konstruksjoner eller problemer med kraft og bevegelse.
Hypotenusen for en trekant med katetene a=3 og b=4 er {hypotenus}.

**Fysikk:**
Vi kan beregne kinetisk energi ({kinetisk_energi_resultat:.2f} Joule) og potensiell energi ({potensiell_energi_resultat:.2f} Joule) for et objekt med masse {masse} kg, 
hastighet {hastighet} m/s, og høyde {høyde} meter. 
Tyngdeakselerasjonen er satt til {gravitasjonskonstant} m/s^2.

**Sammenhenger:**
Alle disse områdene henger sammen i realfaglige problemer. For eksempel:
* Fyllingsprosessen kan modelleres matematisk (funksjonen V(x)) og analyseres statistisk.
* Algebra og trigonometri kan brukes til å løse praktiske problemer i fysikk.
* Fysikkens lover og prinsipper kan brukes til å forstå og forutsi bevegelse og energi.
""")