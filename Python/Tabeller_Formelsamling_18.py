python
from sympy import symbols, I, exp, log

z = 2 + 3*I
print("z =", z)
print("Re(z) =", sp.re(z))
print("Im(z) =", sp.im(z))
print("|z| =", abs(z))
print("z* =", sp.conjugate(z))
print("exp(i*pi) =", exp(I*sp.pi))  # Eulers formel