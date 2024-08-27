python
def f(x):
    return x**3 + x - 1

a = 0
b = 1
noyaktighet = 0.0001

m = (a + b) / 2

while abs(f(m)) >= noyaktighet:
    if f(a) * f(m) < 0:
        b = m
    else:
        a = m
    m = (a + b) / 2

print("Løsningen på likningen er ", round(m, 3))