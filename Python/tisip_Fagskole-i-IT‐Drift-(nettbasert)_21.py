python
# Lese fra en fil
with open('fil.txt', 'r') as fil:
    innhold = fil.read()
    print(innhold)

# Skrive til en fil
with open('fil.txt', 'w') as fil:
    fil.write("Dette er en test.")