python
loggoppføringer = ["INFO: Bruker logget inn", "FEIL: Ugyldig passord", "INFO: Fil lastet ned"]

for oppføring in loggoppføringer:
    if oppføring.startswith("FEIL"):
        print(f"Feilmelding: {oppføring}")