python
def finn_største_tall(tall1, tall2):
  """Finner det største av to tall."""
  if tall1 > tall2:
    return tall1
  else:
    return tall2

def summer_tall(tall_liste):
  """Summerer en liste med tall."""
  sum = 0
  for tall in tall_liste:
    sum += tall
  return sum

# Eksempelbruk:
tall1 = 5
tall2 = 8
største_tall = finn_største_tall(tall1, tall2)
print("Største tall:", største_tall)  # Output: Største tall: 8

tall_liste = [1, 2, 3, 4, 5]
summen = summer_tall(tall_liste)
print("Summen av tallene er:", summen)  # Output: Summen av tallene er: 15