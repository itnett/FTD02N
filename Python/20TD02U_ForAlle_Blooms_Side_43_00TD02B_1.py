python
# Automatisk generering av en møteinnkalling
def generer_møteinnkalling(tittel, dato, sted, agenda):
    return f"""
    Møteinnkalling
    Tittel: {tittel}
    Dato: {dato}
    Sted: {sted}
    Agenda:
    {agenda}
    """
tittel = "Utviklermøte"
dato = "2024-09-01"
sted = "Hovedkontoret"
agenda = """
1. Introduksjon
2. Statusoppdatering
3. Planlegging av neste sprint
4. Eventuelt
"""

print(generer_møteinnkalling(tittel, dato, sted, agenda))