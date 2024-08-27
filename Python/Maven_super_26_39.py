python
# Les en tekstfil og skriv ut innholdet
with open('eksempel.txt', 'r', encoding='utf-8') as fil:
    innhold = fil.read()
    print(innhold)