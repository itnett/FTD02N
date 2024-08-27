python
# Leksjon 3.5: Prosentdelen av et Tall med Formel

def calculate_percentage_with_formula(percent, total):
    return (percent / 100) * total

# Input
percent = int(input("Skriv inn prosent: "))
total = float(input("Skriv inn total verdi: "))

# Calculate and display
percentage_value = calculate_percentage_with_formula(percent, total)
print(f"{percent}% av {total} er: {percentage_value}")