python
# Define symbols
c, m, delta_T = sp.symbols('c m delta_T')

# Heat transferred
Q = m * c * delta_T
print(f"Heat transferred: Q = {Q}")