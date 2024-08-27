python
# Define symbols for heat (Q) and temperature (T)
T = sp.symbols('T')

# Entropy change
delta_S = Q / T
print(f"Entropy change: ΔS = {delta_S}")