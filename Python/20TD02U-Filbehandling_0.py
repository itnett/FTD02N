python
# Skrive til en fil
with open("test.txt", "w") as f:
    f.write("Hei, dette er en testfil!\n")

# Lese fra en fil
with open("test.txt", "r") as f:
    innhold = f.read()
    print(innhold)

# Append til en fil
with open("test.txt", "a") as f:
    f.write("Dette er en ny linje.\n")