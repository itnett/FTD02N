python
# Trinket-kode for Leksjon 6.1: Figurtall

def trekanttall(n):
    return n * (n + 1) // 2

def kvadrattall(n):
    return n * n

# Eksempelbruk
print("Leksjon 6.1: Figurtall")
n = int(input("Skriv inn n for trekanttall: "))
print(f"Trekanttall T_{n} = {trekanttall(n)}")

n = int(input("Skriv inn n for kvadrattall: "))
print(f"Kvadrattall Q_{n} = {kvadrattall(n)}")