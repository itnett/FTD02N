python
from sympy import symbols, solve

B, C, N = symbols('B C N')  # Båndbredde, antall kanaler, støynivå

# Shannon-Hartley-teoremet for kanal kapasitet
kapasitet = B * log(1 + S/N, 2)

# Løs for båndbredde gitt kapasitet og støynivå
løsning = solve(kapasitet - 1000, B)  # Kapasitet på 1000 bps
print(løsning)