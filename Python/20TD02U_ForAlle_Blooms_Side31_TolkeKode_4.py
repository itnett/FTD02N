python
# Kombiner flere funksjoner for å lage et program som beregner summen av alle partall i en liste
def sjekk_partall(tall):
    return tall % 2 == 0

def finn_sum(liste):
    sum = 0
    for tall i liste:
        if sjekk_partall(tall):
            sum += tall
    return sum

tall_liste = [1, 2, 3, 4, 5, 6]
print(f"Summen av partallene er: {finn_sum(tall_liste)}")