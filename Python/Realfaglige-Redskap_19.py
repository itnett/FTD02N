python
def hilsen(navn, alder=None):
    if alder:
        print(f"Hei, {navn}! Du er {alder} år gammel.")
    else:
        print(f"Hei, {navn}!")

hilsen("Charlie")
hilsen("David", 35)