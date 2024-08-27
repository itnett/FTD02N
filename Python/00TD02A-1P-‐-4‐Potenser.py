python
# Leksjon 4.12: n-te Røtter

def calculate_nth_root(number, n):
    return number ** (1/n)

# Input
number = float(input("Skriv inn et tall: "))
n = int(input("Skriv inn rotens grad: "))

# Calculate and display
result = calculate_nth_root(number, n)
print(f"Den {n}-te roten av {number} er {result}")