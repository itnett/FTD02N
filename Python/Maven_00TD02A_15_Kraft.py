python
import matplotlib.pyplot as plt

# Initiale betingelser
v0 = 0  # startfart i m/s
a = 2  # konstant akselerasjon i m/s²
t = list(range(11))  #

 tid i sekunder

# Beregn fart og distanse over tid
velocity = [v0 + a*ti for ti in t]
distance = [v0*ti + 0.5*a*ti**2 for ti in t]

plt.plot(t, velocity, label='Fart (m/s)')
plt.plot(t, distance, label='Distanse (m)')
plt.title("Bevegelse med Konstant Akselerasjon")
plt.xlabel("Tid (s)")
plt.ylabel("Verdi")
plt.grid(True)
plt.legend()
plt.show()