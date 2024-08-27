python
# Analyser denne koden for å identifisere ineffektivitet
def finn_sum(liste):
    sum = 0
    for tall i liste:
        sum += tall
    return sum

# Analysert: Denne koden er effektiv for små lister, men hvis listen blir svært stor, kan det være mer effektivt å bruke innebygde funksjoner som sum(liste).