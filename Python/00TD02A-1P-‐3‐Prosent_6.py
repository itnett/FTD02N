python
# Leksjon 3.7: Prosentvis Endring

def calculate_percentage_change(original, new):
    change = new - original
    return (change / original) * 100

# Input
original_value = float(input("Skriv inn opprinnelig verdi: "))
new_value = float(input("Skriv inn ny verdi: "))

# Calculate and display
percentage_change = calculate_percentage_change(original_value, new_value)
print(f"Prosentvis endring fra {original_value} til {new_value} er: {percentage_change}%")