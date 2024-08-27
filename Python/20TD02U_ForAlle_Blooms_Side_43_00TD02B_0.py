python
import language_tool_python

# Bruk LanguageTool for å sjekke grammatikkfeil i norsk tekst
tool = language_tool_python.LanguageTool('no')
tekst = "Dette er en eksempel tekst som inneholder noen grammatiske feil."
feil = tool.check(tekst)

for feil_i_tekst in feil:
    print(f"Feil: {feil_i_tekst.message} - {feil_i_tekst.sentence}")