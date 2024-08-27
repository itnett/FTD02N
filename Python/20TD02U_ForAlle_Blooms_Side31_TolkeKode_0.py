python
# Identifiser variabler, funksjoner, og løkker i koden
navn = "Alice"  # Variabeldeklarasjon
alder = 30

def skriv_informasjon(navn, alder):  # Funksjon
    for i in range(alder):  # Løkke
        print(f"{navn} er {alder} år gammel.")

skriv_informasjon(navn, alder)