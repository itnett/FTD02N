python
# Leksjon 3.8: Promille

def promille_to_decimal(promille):
    return promille / 1000

def promille_to_percent(promille):
    return promille / 10

# Input
promille = int(input("Skriv inn promilleverdi: "))

# Convert and display
decimal = promille_to_decimal(promille)
percent = promille_to_percent(promille)
print(f"{promille}‰ som desimaltall er: {decimal}")
print(f"{promille}‰ som prosent er: {percent}%")