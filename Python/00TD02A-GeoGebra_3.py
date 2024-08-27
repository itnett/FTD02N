python
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# Definerer funksjonen V(x)
def V(x):
    return 2000 - 2000 * (1 - x / 40)**2

# Genererer data for å plotte grafen
x_vals = np.linspace(0, 40, 400)
y_vals = V(x_vals)

# Plotter grafen
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='V(x) = 2000 - 2000 * (1 - x/40)^2')
plt.axhline(y=1000, color='r', linestyle='--', label='y = 1000')
plt.axvline(x=40, color='g', linestyle='--', label='x = 40')
plt.scatter([0, 11.72, 40], [0, 1000, 2000], color='black')

# Legger til merkinger på spesifikke punkter
plt.text(0, 50, 'C (0, 0)', fontsize=12, ha='right')
plt.text(11.72, 1050, 'A (11.72, 1000)', fontsize=12, ha='left')
plt.text(40, 2050, 'B (40, 2000)', fontsize=12, ha='left')

# Akseetiketter og tittel
plt.xlabel('Tid (minutter)')
plt.ylabel('Volum (liter)')
plt.title('V(x) = 2000 - 2000 * (1 - x/40)^2')
plt.legend()
plt.grid(True)
plt.show()

# Beregninger og forklaringer
x = symbols('x')
V_expr = 2000 - 2000 * (1 - x / 40)**2

# Skjæringspunkt med y-aksen
y_axis_intercept = V_expr.subs(x, 0)

# Tidspunkt når volumet er 1000 liter
eq1 = Eq(V_expr, 1000)
time_for_1000_liters = solve(eq1, x)

# Maksimalt volum (når x = 40)
max_volume = V_expr.subs(x, 40)

# Forklaringer
print(f"Funksjon: V(x) = 2000 - 2000 * (1 - x/40)^2")
print(f"Skjæringspunkt med y-aksen: C (0, {y_axis_intercept})")
print(f"Tidspunkt når volumet er 1000 liter: A ({time_for_1000_liters[0]}, 1000)")
print(f"Maksimalt volum: B (40, {max_volume})")

# Statistiske analyser (eksemplifisert med dummy data)
data = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]

# Gjennomsnitt
mean_value = np.mean(data)
print(f"Gjennomsnitt: {mean_value}")

# Median
median_value = np.median(data)
print(f"Median: {median_value}")

# Kvartiler
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
print(f"Første kvartil (Q1): {q1}")
print(f"Tredje kvartil (Q3): {q3}")

# Standardavvik
std_deviation = np.std(data)
print(f"Standardavvik: {std_deviation}")

# Forklaring av begreper:
# Statistisk analyse: Å samle, organisere, analysere og tolke data.
# Hjelpemiddel for statistisk analyse: Programvare som Python, GeoGebra, Excel.
# Statistisk analyse en del av sannsynlighetsregning og statistikk: Bruk av sannsynlighetsteori i statistikk.
# Gjennomsnitt: Summen av data delt på antall observasjoner.
# Median: Den midterste verdien i en sortert datasett.
# Kvartiler: Deler datasettet i fire like store deler.
# Standardavvik: Mål på spredningen av dataene rundt gjennomsnittet.
# Fyllingsprosess: Prosess der volumet øker over tid, som vist i grafen.
# Startvolum: Volum ved t=0, som i grafen er 0 liter.
# Tidspunkt når et bestemt volum nås: Når V(x)=1000, skjer ved x≈11.72.
# Maksimalt volum: Det største volumet (2000 liter ved x=40).
# Funksjon: Relasjon mellom tid og volum, V(x).
# Akseetiketter: Tid (minutter) og Volum (liter).
# Plotter grafen til funksjonen V(x): Grafen vist ovenfor.
# Sluttidspunktet: Når x=40, fyllingen er ferdig.
# Går gjennom arrayet: Iterasjon over dataene som vist i de statistiske beregningene.
# Numerisk løsning for tidspunktet når volumet: Brukt sympy til å løse V(x)=1000.
# Væskevolumet som en funksjon av tiden: V(x) som vist i grafen.
# Numeriske beregninger og array-operasjoner: Brukt NumPy for statistikk.
# Trykk, temperatur og viskositet: Kan påvirke fyllingsprosessen, men ikke relevant her.
# Kurven i grafen representerer funksjonen V(x): V(x) grafen som vist.
# Skjæringspunktet mellom V(x) og y-aksen: C (0, 0).
# En parabel som åpner oppover: Grafen av V(x) viser en parabel som åpner oppover.