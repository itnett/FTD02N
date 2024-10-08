python
# Trinket-kode for Leksjon 6.2: Lage Bokstavuttrykk

def lag_bokstavuttrykk(beskrivelse):
    if beskrivelse == "fem mer enn et tall":
        return "x + 5"
    elif beskrivelse == "et tall ganger tre":
        return "3x"
    else:
        return "Ukjent beskrivelse"

# Eksempelbruk
print("Leksjon 6.2: Lage Bokstavuttrykk")
beskrivelse = input("Beskrivelse (fem mer enn et tall / et tall ganger tre): ")
uttrykk = lag_bokstavuttrykk(beskrivelse)
print(f"Bokstavuttrykk: {uttrykk}")