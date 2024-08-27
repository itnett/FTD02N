python
# Define symbols
k1, k2 = sp.symbols('k1 k2')

# Angle between two lines
angle = sp.atan((k2 - k1) / (1 + k1 * k2))

print(f"Angle between the lines: {angle} radians")

# Check for perpendicular lines
perpendicular_condition = sp.Eq(k1 * k2, -1)
print(f"Lines are perpendicular if: {perpendicular_condition}")