python
loggoppføringer = [
    {"tidspunkt": "2023-06-13 10:22:31", "alvorlighetsgrad": "INFO", "melding": "Bruker logget inn"},
    {"tidspunkt": "2023-06-13 10:25:14", "alvorlighetsgrad": "ADVARSEL", "melding": "Ugyldig innloggingsforsøk"},
    {"tidspunkt": "2023-06-13 10:30:05", "alvorlighetsgrad": "FEIL", "melding": "Serverfeil"},
]

alvorlighetsgrader = ["INFO", "ADVARSEL", "FEIL"]

def filtrer_loggoppføringer(oppføringer, minimum_alvorlighetsgrad):
    filtrerte_oppføringer = []
    for oppføring in oppføringer:
        if alvorlighetsgrader.index(oppføring["alvorlighetsgrad"]) >= alvorlighetsgrader.index(minimum_alvorlighetsgrad):
            filtrerte_oppføringer.append(oppføring)
    return filtrerte_oppføringer

filtrerte_oppføringer = filtrer_loggoppføringer(loggoppføringer, "ADVARSEL")
print(filtrerte_oppføringer)