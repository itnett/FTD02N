python
# Leksjon 3.3: Prosent som Desimaltall

def percent_to_decimal(percent):
    return percent / 100

# Input
percent = int(input("Skriv inn en prosentverdi: "))

# Convert and display
decimal = percent_to_decimal(percent)
print(f"{percent}% som desimaltall er: {decimal}")