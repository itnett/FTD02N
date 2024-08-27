python
def generer_prosjektrapport(tittel, forfatter, innholdsliste):
    rapport = f"""
    Prosjektrapport
    Tittel: {tittel}
    Forfatter: {forfatter}
    
    Innhold:
    """
    for innhold in innholdsliste:
        rapport += f"\n- {innhold}"
    return rapport

tittel = "Teknologiutvikling i 2024"
forfatter = "Utviklerteamet"
innholdsliste = ["Introduksjon", "Metodikk", "Resultater", "Diskusjon", "Konklusjon"]

print(generer_prosjektrapport(tittel, forfatter, innholdsliste))