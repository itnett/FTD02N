python
# Skriver til en tekstfil. Hvis filen ikke eksisterer, blir den opprettet.
with open('utdata.txt', 'w', encoding='utf-8') as fil:
    fil.write("Dette er en linje med tekst.\n")
    fil.write("Dette er en annen linje.")