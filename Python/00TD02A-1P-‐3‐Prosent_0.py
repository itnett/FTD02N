python
# Leksjon 3.1: Hva er Prosent?

def percent_to_fraction(percent):
    return f"{percent}/100"

def fraction_to_percent(numerator, denominator):
    return (numerator / denominator) * 100

# Input
percent = int(input("Skriv inn en prosentverdi: "))

# Convert and display
fraction = percent_to_fraction(percent)
print(f"{percent}% som brøk er: {fraction}")

# Practice problem
numerator = int(input("Skriv inn teller: "))
denominator = int(input("Skriv inn nevner: "))

# Convert and display
percentage = fraction_to_percent(numerator, denominator)
print(f"{numerator}/{denominator} som prosent er: {percentage}%")