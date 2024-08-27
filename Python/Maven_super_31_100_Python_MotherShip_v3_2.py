python
# ---- 1. Print Statement ----
print("Velkommen til 100 Python-konsepter!")  # Skriver ut en velkomstmelding til konsollen

# ---- 2. Variables ----
navn = "Python Lærer"  # Lagrer en tekststreng i variabelen navn
alder = 30  # Lagrer et heltall i variabelen alder

# ---- 3. Data Types ----
er_student = True  # Boolean datatype
poengsum = 95.5  # Float datatype

# ---- 4. Type Conversion ----
alder_str = str(alder)  # Konverterer alder til en tekststreng

# ---- 5. Strings ----
full_greeting = "Hei, " + navn + "! Velkommen til kurset."  # Kombinerer strenger
print(full_greeting)

# ---- 6. String Concatenation ----
hilsen = "Velkommen" + ", " + navn  # Kombinerer flere strenger
print(hilsen)

# ---- 7. String Methods ----
stor_hilsen = hilsen.upper()  # Konverterer til store bokstaver
print(stor_hilsen)

# ---- 8. User Input ----
bruker_navn = input("Hva heter du? ")  # Tar imot input fra brukeren
print(f"Hei, {bruker_navn}!")

# ---- 9. Comments ----
# Dette er en enkel kommentar som forklarer koden
# Kommentarer er viktige for å gjøre koden lesbar og forståelig

# ---- 10. Arithmetic Operations ----
summa = 5 + 3  # Legger sammen to tall
produkt = 5 * 3  # Multipliserer to tall
kvotient = 10 / 2  # Deler et tall
print(summa, produkt, kvotient)

# ---- 11. Assignment Operations ----
x = 5
x += 2  # Øker x med 2
print(x)

# ---- 12. Comparison Operations ----
lik = x == 7  # Sjekker om x er lik 7
print(lik)

# ---- 13. Logical Operations ----
og_sjekk = (x > 2) and (x < 10)  # Sjekker om x er mellom 2 og 10
print(og_sjekk)

# ---- 14. Identity Operations ----
y = x
print(x is y)  # Sjekker om x og y refererer til samme objekt

# ---- 15. Membership Operations ----
liste = [1, 2, 3, 4]
print(3 in liste)  # Sjekker om 3 er i listen

# ---- 16. Bitwise Operations ----
a = 60  # 0011 1100 i binært
b = 13  # 0000 1101 i binært
print(a & b)  # 0000 1100 (bitwise AND)

# ---- 17. If Statement ----
if x > 5:
    print("x er større enn 5")

# ---- 18. Else Statement ----
if x < 5:
    print("x er mindre enn 5")
else:
    print("x er ikke mindre enn 5")

# ---- 19. Elif Statement ----
if x > 10:
    print("x er større enn 10")
elif x == 7:
    print("x er lik 7")
else:
    print("x er verken større enn 10 eller lik 7")

# ---- 20. Nested If Statement ----
if x > 5:
    if x < 10:
        print("x er mellom 5 og 10")

# ---- 21. For Loop ----
for i in range(5):
    print(f"i er nå: {i}")

# ---- 22. While Loop ----
count = 0
while count < 5:
    print(f"Count er: {count}")
    count += 1

# ---- 23. Break Statement ----
for i in range(10):
    if i == 5:
        break
    print(i)

# ---- 24. Continue Statement ----
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# ---- 25. Pass Statement ----
for i in range(5):
    if i == 2:
        pass  # Plassholder som ikke gjør noe
    print(i)

# ---- 26. Functions ----
def si_hei():
    print("Hei!")
si_hei()

# ---- 27. Function Arguments ----
def si_hei_til(navn):
    print(f"Hei, {navn}!")
si_hei_til("Marius")

# ---- 28. Default Arguments ----
def si_hei_til(navn="Verden"):
    print(f"Hei, {navn}!")
si_hei_til()

# ---- 29. Keyword Arguments ----
def skriv_tekst(farge, tekst):
    print(f"{farge} tekst: {tekst}")
skriv_tekst(tekst="Dette er viktig!", farge="Rød")

# ---- 30. Variable-length Arguments ----
def skriv_lister(*elementer):
    for element in elementer:
        print(element)
skriv_lister(1, 2, 3, 4)

# ---- 31. Return Statement ----
def kvadrat(x):
    return x * x
print(kvadrat(4))

# ---- 32. Docstrings ----
def legg_til(x, y):
    """Legger sammen to tall og returnerer resultatet."""
    return x + y
print(legg_til(3, 4))

# ---- 33. Recursion ----
def faktorielle(n):
    if n == 1:
        return 1
    else:
        return n * faktorielle(n-1)
print(faktorielle(5))

# ---- 34. Lambda Functions ----
kvadrat = lambda x: x * x
print(kvadrat(5))

# ---- 35. Map Function ----
tall = [1, 2, 3, 4]
kvadrater = list(map(lambda x: x * x, tall))
print(kvadrater)

# ---- 36. Filter Function ----
oddetall = list(filter(lambda x: x % 2 != 0, tall))
print(oddetall)

# ---- 37. Reduce Function ----
from functools import reduce
summen = reduce(lambda x, y: x + y, tall)
print(summen)

# ---- 38. Zip Function ----
navn = ["Ole", "Dole", "Doffen"]
aldre = [5, 6, 7]
kombinasjon = list(zip(navn, aldre))
print(kombinasjon)

# ---- 39. Enumerate Function ----
for index, navn in enumerate(navn):
    print(f"{index}: {navn}")

# ---- 40. List Comprehensions ----
kvadrater = [x * x for x in range(10)]
print(kvadrater)

# ---- 41. Dictionary Comprehensions ----
kvadrater_dict = {x: x * x for x in range(10)}
print(kvadrater_dict)

# ---- 42. Set Comprehensions ----
unikke_kvadrater = {x * x for x in [1, 1, 2, 3, 3, 3]}
print(unikke_kvadrater)

# ---- 43. Generators ----
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fibonacci(10)))

# ---- 44. Yield Statement ----
def opp_til_ti():
    for i in range(1, 11):
        yield i
print(list(opp_til_ti()))

# ---- 45. File Handling - Reading ----
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# ---- 46. File Handling - Writing ----
with open("example.txt", "w") as file:
    file.write("Dette er en test")

# ---- 47. File Handling - Appending ----
with open("example.txt", "a") as file:
    file.write("\nDette er en tilleggs test")

# ---- 48. Error Handling - Try/Except ----
try:
    10 / 0
except ZeroDivisionError:
    print("Kan ikke dele på null!")

# ---- 49. Error Handling - Finally ----
try:
    10 / 0
except ZeroDivisionError:
    print("Kan ikke dele på null!")
finally:
    print("Dette kjøres alltid uansett.")

# ---- 50. Error Handling - Else ----
try:
    resultat = 10 / 2
except ZeroDivisionError:
    print("Kan ikke dele

Det ser ut som at responsen min ble avbrutt midt i prosessen med å beskrive koden og de resterende konseptene. La meg fullføre skriptet og gi en fullstendig oppsummering, detaljert kodelesning og tolkning, samt lenker og opplæring for hvert av de 100 Python-konseptene.

### **100 Grunnleggende Python-Konsepter i Ett Sammenhengende Skript**

#### **Konsept 51-100:**