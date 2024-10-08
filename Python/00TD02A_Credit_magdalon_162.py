python
from sympy import Function, dsolve, Eq, symbols

t = symbols('t')
I = Function('I')  # Antall infiserte enheter
beta = 0.1  # Smitterate
gamma = 0.05  # Helbredelsesrate

diffeq = Eq(I(t).diff(t), beta * I(t) * (1 - I(t)) - gamma * I(t))  # SIR-modellen
løsning = dsolve(diffeq, I(t), ics={I(0): 0.01})  # Initialbetingelse: 1% infiserte enheter ved t=0

print(løsning)