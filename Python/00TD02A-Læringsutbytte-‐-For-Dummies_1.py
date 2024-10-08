python
# Brøk og Prosentregning - Konvertere brøk til prosent

def fraction_to_percentage(numerator, denominator):
    return (numerator / denominator) * 100

# Input
numerator = float(input("Skriv inn teller: "))
denominator = float(input("Skriv inn nevner: "))

# Convert and output
percentage = fraction_to_percentage(numerator, denominator)
print(f"{numerator}/{denominator} som prosent er: {percentage:.2f}%")