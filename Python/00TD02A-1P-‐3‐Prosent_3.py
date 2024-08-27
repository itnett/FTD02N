python
# Leksjon 3.4: Prosentdelen av et Tall uten Formel

def calculate_percentage_without_formula(percent, total):
    decimal = percent / 100
    return decimal * total

# Input
percent = int(input("Skriv inn prosent: "))
total = float(input("Skriv inn total verdi: "))

# Calculate and display
percentage_value = calculate_percentage_without_formula(percent, total)
print(f"{percent}% av {total} er: {percentage_value}")