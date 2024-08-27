python
import math

# Newtons andre lov
def newtons_andre_lov(masse, akselerasjon):
    return masse * akselerasjon

# Bevegelseslikninger ved konstant fart
def bevegelse_konstant_fart(fart, tid):
    return fart * tid

# Bevegelseslikninger ved konstant akselerasjon
def sluttfart(v0, akselerasjon, tid):
    return v0 + akselerasjon * tid

def forflytning(v0, akselerasjon, tid):
    return v0 * tid + 0.5 * akselerasjon * tid**2

def sluttfart_uten_tid(v0, akselerasjon, forflytning):
    return math.sqrt(v0**2 + 2 * akselerasjon * forflytning)

# Eksempler
masse = 10  # kg
akselerasjon = 2  # m/s^2
fart = 5  # m/s
tid = 4  # s
v0 = 3  # m/s

# Newtons andre lov
kraft = newtons_andre_lov(masse, akselerasjon)
print(f"Kraft: {kraft} N")

# Bevegelse ved konstant fart
forflytning_konstant_fart = bevegelse_konstant_fart(fart, tid)
print(f"Forflytning ved konstant fart: {forflytning_konstant_fart} m")

# Bevegelse ved konstant akselerasjon
sluttfart_resultat = sluttfart(v0, akselerasjon, tid)
forflytning_resultat = forflytning(v0, akselerasjon, tid)
sluttfart_uten_tid_resultat = sluttfart_uten_tid(v0, akselerasjon, forflytning_resultat)

print(f"Sluttfart: {sluttfart_resultat} m/s")
print(f"Forflytning: {forflytning_resultat} m")
print(f"Sluttfart (uten tid): {sluttfart_uten_tid_resultat} m/s")