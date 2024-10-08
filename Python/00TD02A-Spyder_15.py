python
# Termofysikkens første lov
Q = 100  # Varme tilført systemet (J)
W = 50  # Arbeid utført av systemet (J)
delta_U = Q - W  # Endring i indre energi (J)
print("Endring i indre energi:", delta_U, "J")

# Varmekapasitet
m = 0.5  # Masse (kg)
c = 4186  # Spesifikk varmekapasitet for vann (J/(kg*K))
delta_T = 10  # Temperaturøkning (K)
Q = m * c * delta_T
print("Varmemengde:", Q, "J")