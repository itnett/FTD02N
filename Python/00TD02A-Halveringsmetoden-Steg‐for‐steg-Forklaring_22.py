python
noyaktighet = 0.0001
while abs(f(m)) >= noyaktighet:
    m = (a + b) / 2
    if f(a) * f(m) < 0:
        b = m
    else:
        a = m