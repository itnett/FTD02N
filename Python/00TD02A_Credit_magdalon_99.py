python
def logg_hendelse(hendelse, alvorlighetsgrad):
    tidspunkt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{tidspunkt} {alvorlighetsgrad}: {hendelse}")

logg_hendelse("Ugyldig innloggingsforsøk", "ADVARSEL")