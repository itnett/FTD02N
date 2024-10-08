python
# Leksjon 3.9: Prosentpoeng

def calculate_percentage_point_change(old_percent, new_percent):
    return new_percent - old_percent

# Input
old_percent = float(input("Skriv inn gammel prosent: "))
new_percent = float(input("Skriv inn ny prosent: "))

# Calculate and display
percentage_point_change = calculate_percentage_point_change(old_percent, new_percent)
print(f"Endringen i prosentpoeng fra {old_percent}% til {new_percent}% er: {percentage_point_change} prosentpoeng")