python
hendelse = "Ugyldig innloggingsforsøk"

if "innlogging" in hendelse.lower():
    type = "Autentisering"
elif "filtilgang" in hendelse.lower():
    type = "Tilgangskontroll"
else:
    type = "Annet"

print(f"Hendelsestype: {type}")