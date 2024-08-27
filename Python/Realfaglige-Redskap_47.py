python
# Lese fra fil
with open("fil.txt", "r") as fil:
    innhold = fil.read()

# Skrive til fil
with open("ny_fil.txt", "w") as fil:
    fil.write("Dette er nytt innhold.")