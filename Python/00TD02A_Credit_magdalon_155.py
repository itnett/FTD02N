python
from sympy import Piecewise, Symbol

port = Symbol('port')
handling = Piecewise(
    ("blokker", port < 1024),
    ("tillat", port >= 1024 and port <= 65535),
    ("blokker", True)  # Blokker alle andre porter
)

print(handling.subs(port, 80))    # Output: blokker
print(handling.subs(port, 8080))  # Output: tillat
print(handling.subs(port, 65536)) # Output: blokker