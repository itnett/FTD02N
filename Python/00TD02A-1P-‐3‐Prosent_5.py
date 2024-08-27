python
# Leksjon 3.6: Finne Prosenten

def find_percentage(part, total):
    return (part / total) * 100

# Input
part = float(input("Skriv inn delen: "))
total = float(input("Skriv inn total verdi: "))

# Calculate and display
percentage = find_percentage(part, total)
print(f"{part} er {percentage}% av {total}")