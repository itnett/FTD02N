python
# Hyperbolic functions and their identities
hyperbolic_identities = {
    "cosh(x)": sp.cosh(x),
    "sinh(x)": sp.sinh(x),
    "tanh(x)": sp.tanh(x),
    "cosh(x)^2 - sinh(x)^2": sp.cosh(x)**2 - sp.sinh(x)**2,
}

# Print hyperbolic identities
for id, expr in hyperbolic_identities.items():
    print(f"{id} = {expr}")

# Inverse hyperbolic functions
inverse_hyperbolic = {
    "cosh(y) = x => y = +- ln(x + sqrt(x^2 + 1))": (sp.cosh(x), x, sp.log(x + sp.sqrt(x**2 + 1))),
    "sinh(y) = x => y = ln(x + sqrt(x^2 + 1))": (sp.sinh(x), x, sp.log(x + sp.sqrt(x**2 + 1))),
    "tanh(y) = x => y = 1/2 ln((1 + x)/(1 - x))": (sp.tanh(x), x, 0.5 * sp.log((1 + x)/(1 - x))),
}

# Print inverse hyperbolic functions
for desc, (lhs, x, rhs) in inverse_hyperbolic.items():
    print(f"{desc}: {lhs} = {rhs}")