python
import sympy as sp
import math

# Areal og Omkrets
def areal_rektangel(l, b):
    return l * b

def omkrets_rektangel(l, b):
    return 2 * (l + b)

def areal_sirkel(r):
    return math.pi * r**2

def omkrets_sirkel(r):
    return 2 * math.pi * r

# Volum og Overflate
def volum_kube(s):
    return s**3

def overflate_kube(s):
    return 6 * s**2

def volum_kule(r):
    return (4/3) * math.pi * r**3

def overflate_kule(r):
    return 4 * math.pi * r**2

# Pytagoras' setning
def pytagoras(a, b):
    return math.sqrt(a**2 + b**2)

# Trigonometri i rettvinklede trekanter
def sin_theta(opposite, hypotenuse):
    return opposite / hypotenuse

def cos_theta(adjacent, hypotenuse):
    return adjacent / hypotenuse

def tan_theta(opposite, adjacent):
    return opposite / adjacent

# Vektorer i planet
def add_vectors(u, v):
    return (u[0] + v[0], u[1] + v[1])

def scalar_multiply_vector(k, v):
    return (k * v[0], k * v[1])

def vector_norm(v):
    return math.sqrt(v[0]**2 + v[1]**2)

# Eksempler
print(f"Areal av rektangel (l=5, b=3): {areal_rektangel(5, 3)}")
print(f"Omkrets av rektangel (l=5, b=3): {omkrets_rektangel(5, 3)}")
print(f"Areal av sirkel (r=4): {areal_sirkel(4)}")
print(f"Omkrets av sirkel (r=4): {omkrets_sirkel(4)}")
print(f"Volum av kube (s=2): {volum_kube(2)}")
print(f"Overflate av kube (s=2): {overflate_kube(2)}")
print(f"Volum av kule (r=3): {volum_kule(3)}")
print(f"Overflate av kule (r=3): {overflate_kule(3)}")
print(f"Hypotenusen i rettvinklet trekant (a=3, b=4): {pytagoras(3, 4)}")
print(f"Sinus til vinkel θ med motstående katet 3 og hypotenuse 5: {sin_theta(3, 5)}")
print(f"Kosinus til vinkel θ med hosliggende katet 4 og hypotenuse 5: {cos_theta(4, 5)}")
print(f"Tangens til vinkel θ med motstående katet 3 og hosliggende katet 4: {tan_theta(3, 4)}")
print(f"Addisjon av vektorene (2, 3) og (1, 4): {add_vectors((2, 3), (1, 4))}")
print(f"Skalarmultiplikasjon av vektor (2, 3) med skalar 3: {scalar_multiply_vector(3, (2, 3))}")
print(f"Normen av vektoren (3, 4): {vector_norm((3, 4))}")