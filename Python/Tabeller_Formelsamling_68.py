python
import sympy as sp

# Definer variabler
x, y, a, b, c, d = sp.symbols('x y a b c d')

# Eksempler på regneregler
associative_add = (a + (b + c)).expand()
associative_mult = (a * (b * c)).expand()
commutative_add = (a + b).expand()
commutative_mult = (a * b).expand()
distributive = (a * (b + c)).expand()

# Eksempler på brøkregning
fraction_add = sp.Rational(1, 2) + sp.Rational(1, 3)
fraction_mult = sp.Rational(1, 2) * sp.Rational(1, 3)
fraction_div = sp.Rational(1, 2) / sp.Rational(1, 3)

# Eksempler på potenser
power_mult = a**3 * a**2
power_div = a**3 / a**2
power_exp = (a**3)**2

# Tall på standardform
standard_form = sp.nsimplify('4500', rational=True).evalf()

# Sammentrekning og faktorisering
combine_like_terms = sp.simplify(2*a + 3*a)
factor_expr = sp.factor(x**2 - 9)
factor_common = sp.factor(3*x + 3*y)

# Skriv ut resultatene
print(f"Associativ addisjon: {associative_add}")
print(f"Associativ multiplikasjon: {associative_mult}")
print(f"Kommutativ addisjon: {commutative_add}")
print(f"Kommutativ multiplikasjon: {commutative_mult}")
print(f"Distribusjonslov: {distributive}")

print(f"Brøk addisjon: {fraction_add}")
print(f"Brøk multiplikasjon: {fraction_mult}")
print(f"Brøk divisjon: {fraction_div}")

print(f"Potenser multiplikasjon: {power_mult}")
print(f"Potenser divisjon: {power_div}")
print(f"Potenser eksponent: {power_exp}")

print(f"Tall på standardform: {standard_form}")

print(f"Sammentrekning av like ledd: {combine_like_terms}")
print(f"Faktorisering av uttrykk: {factor_expr}")
print(f"Faktorisering av felles faktorer: {factor_common}")