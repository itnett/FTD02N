python
# Kommutativ lov
a = 5
b = 3

print("Kommutativ lov (addisjon):")
print(f"{a} + {b} = {b} + {a} ({a + b})")  # Output: 5 + 3 = 3 + 5 (8)

print("\nKommutativ lov (multiplikasjon):")
print(f"{a} * {b} = {b} * {a} ({a * b})")  # Output: 5 * 3 = 3 * 5 (15)

# Assosiativ lov
c = 2

print("\nAssosiativ lov (addisjon):")
print(f"({a} + {b}) + {c} = {a} + ({b} + {c}) ({(a + b) + c})")  # Output: (5 + 3) + 2 = 5 + (3 + 2) (10)

print("\nAssosiativ lov (multiplikasjon):")
print(f"({a} * {b}) * {c} = {a} * ({b} * {c}) ({(a * b) * c})")  # Output: (5 * 3) * 2 = 5 * (3 * 2) (30)

# Distributiv lov
print("\nDistributiv lov:")
print(f"{a} * ({b} + {c}) = {a} * {b} + {a} * {c} ({a * (b + c)})")  # Output: 5 * (3 + 2) = 5 * 3 + 5 * 2 (25)