python
# Trinket-kode for Leksjon 2: Løse Likningssett med To Ukjente

from sympy import symbols, Eq, solve

# Definer variablene
x, y = symbols('x y')

# Likningssett: 2x + y = 10 og x - y = 2
likning1 = Eq(2*x + y, 10)
likning2 = Eq(x - y, 2)

# Løs likningssettet
losning = solve((likning1, likning2), (x, y))
print(f"Løsningen for likningssettet er: x = {losning[x]}, y = {losning[y]}")

# Visualisering av likningssett
x_vals = np.linspace(-10, 10, 400)
y_vals1 = 10 - 2*x_vals
y_vals2 = x_vals - 2

plt.plot(x_vals, y_vals1, label='2x + y = 10')
plt.plot(x_vals, y_vals2, label='x - y = 2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Likningssett: 2x + y = 10 og x - y = 2')
plt.legend()
plt.grid(True)
plt.show()