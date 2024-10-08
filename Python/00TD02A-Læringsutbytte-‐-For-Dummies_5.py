python
# Funksjoner - Rette linjer
# Beregner stigningstallet og skjæringspunktet til en rett linje

def line_equation(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    return slope, intercept

# Input
x1 = float(input("Skriv inn x1: "))
y1 = float(input("Skriv inn y1: "))
x2 = float(input("Skriv inn x2: "))
y2 = float(input("Skriv inn y2: "))

# Calculate and output
slope, intercept = line_equation(x1, y1, x2, y2)
print(f"Stigningstallet er: {slope}")
print(f"Skjæringspunktet er: {intercept}")