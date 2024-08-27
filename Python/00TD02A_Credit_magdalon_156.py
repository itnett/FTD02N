python
from sympy import Piecewise, Symbol

alvorlighetsgrad = Symbol('alvorlighetsgrad')
risiko = Piecewise(
    (10, alvorlighetsgrad == "kritisk"),
    (7, alvorlighetsgrad == "høy"),
    (4, alvorlighetsgrad == "middels"),
    (1, alvorlighetsgrad == "lav"),
    (0, True)  # Ingen risiko for ukjente alvorlighetsgrader
)

print(risiko.subs(alvorlighetsgrad, "høy"))  # Output: 7