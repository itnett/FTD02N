python
import turtle
import math

# Definer konstanter
g = 9.81  # Tyngdeakselerasjonen i m/s^2
l = 1.0   # Lengden av pendelen i meter
theta_0 = 0.2  # Maksimalt vinkelutslag i radianer

# Opprett skjerm og pendel
skjerm = turtle.Screen()
pendel = turtle.Turtle()

# Funksjon for å oppdatere pendelens posisjon
def oppdater_pendel(t):
    theta = theta_0 * math.cos(math.sqrt(g/l) * t)
    x = l * math.sin(theta)
    y = -l * math.cos(theta)
    pendel.goto(x, y)

# Initialiser pendelen
pendel.penup()
oppdater_pendel(0)
pendel.pendown()

# Tidsvariabler
t = 0
dt = 0.01

# Animasjonsløkke
while True:
    oppdater_pendel(t)
    t += dt

# Lukk vinduet når du er ferdig
skjerm.mainloop()