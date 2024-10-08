python
from sympy import limit, singularities

f = (x + 1)/(x - 1)

# Finn vertikale asymptoter
vertikale_asymptoter = singularities(f, x)
print(vertikale_asymptoter)  # Output: {1}

# Finn horisontale asymptoter
horisontal_asymptote = limit(f, x, oo)
print(horisontal_asymptote)  # Output: 1