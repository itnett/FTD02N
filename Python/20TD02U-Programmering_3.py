python
# En enkel løkke for å skrive ut tall fra 1 til 5
for i in range(1, 6):
    print(i)

# If-else for å sjekke om et tall er positivt, negativt eller null
num = int(input("Skriv inn et tall: "))
if num > 0:
    print("Positivt tall")
elif num == 0:
    print("Null")
else:
    print("Negativt tall")