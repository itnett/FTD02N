python
# Trinket-kode for Leksjon 7.11: Andregradsfunksjoner i Praktiske Situasjoner

def s(t):
    return -4.9*t**2 + 19.6*t

# Eksempelbruk
print("Leksjon 7.11: Andregradsfunksjoner i Praktiske Situasjoner")
t = float(input("Skriv inn verdien av t: "))
print(f"s({t}) = {s(t)}")

# Tegn grafen til funksjonen s(t)
import matplotlib.pyplot as plt
import numpy as np

t_values = np.linspace(0, 5, 100)
s_values = s(t_values)

plt.plot(t_values, s_values, label='s(t) = -4.9t^2 + 19.6t')
plt.title('Grafen til funksjonen s(t) = -4.9t^2 + 19.6t')
plt.xlabel('t')
plt.ylabel('s(t)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()