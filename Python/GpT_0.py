python
import openai

# Sett opp OpenAI API-nøkkel
openai.api_key = 'din_api_nokkel'

# Funksjon for å generere svar
def generer_svar(sporsmal):
    response = openai.Completion.create(
      engine="davinci-codex",
      prompt=f"Du er en ekspert i IT-drift og sikkerhet. Svar på følgende spørsmål: {sporsmal}",
      max_tokens=150
    )
    return response.choices[0].text.strip()

# Eksempelspørsmål
sporsmal = "Hvordan konfigurerer jeg en sikker VPN-forbindelse?"
svar = generer_svar(sporsmal)
print(svar)