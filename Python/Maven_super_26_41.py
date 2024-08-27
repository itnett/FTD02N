python
# Les en binærfil (f.eks. et bilde)
with open('bilde.png', 'rb') as fil:
    data = fil.read()
    # Gjør noe med data