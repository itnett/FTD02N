python
from sympy import symbols, Eq, linsolve

x, y = symbols('x y')  # Båndbredde for applikasjon 1 og 2

# Ligninger basert på båndbreddekrav og tilgjengelig kapasitet
ligning1 = Eq(x + y, 100)  # Total båndbredde på 100 Mbps
ligning2 = Eq(2*x + y, 150)  # Applikasjon 1 trenger dobbelt så mye båndbredde som applikasjon 2

løsning = linsolve([ligning1, ligning2], (x, y))
print(løsning)  # Output: {(50, 50)}