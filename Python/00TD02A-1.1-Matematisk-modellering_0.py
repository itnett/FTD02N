python
from vpython import *

# Definer konstanter
g = 9.81  # Tyngdeakselerasjonen i m/s^2
l = 1.0   # Lengden av pendelen i meter
theta_0 = 0.2  # Maksimalt vinkelutslag i radianer

# Opprett en pendel
pendel = simple_sphere(pos=vector(l*sin(theta_0), -l*cos(theta_0), 0), radius=0.05)

# Tidsvariabler
t = 0
dt = 0.01

# Animasjonsløkke
while True:
    rate(100)  # Oppdateringshastighet
    theta = theta_0 * cos(sqrt(g/l) * t)
    pendel.pos = vector(l*sin(theta), -l*cos(theta), 0)
    t += dt