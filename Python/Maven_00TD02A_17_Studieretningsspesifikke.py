python
# Temperaturer i Celsius
temperatures = [-10, 0, 20, 100, 110]

# Faseoverganger for vann
def phase_of_water(temp):
    if temp <= 0:
        return "Fast stoff (is)"
    elif 0 < temp < 100:
        return "Væske (vann)"
    else:
        return "Gass (vanndamp)"

# Analyser temperaturene
phases = [phase_of_water(t) for t in temperatures]
for t, phase in zip(temperatures, phases):
    print(f"Ved {t} °C er vann i fase: {phase}")