python
# Åpne en fil i lesemodus
fil = open('eksempel.txt', 'r')

# Lese innholdet
innhold = fil.read()
print(innhold)

# Lukke filen
fil.close()