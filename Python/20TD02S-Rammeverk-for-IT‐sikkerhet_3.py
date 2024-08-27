python
endringer = []

def registrer_endring(beskrivelse, påvirkning):
    endring = {"beskrivelse": beskrivelse, "påvirkning": påvirkning}
    endringer.append(endring)

# Eksempel på registrering av en endring
registrer_endring("Oppdatering av brannmurregler", "Medium")
print(endringer)