python
class Sikkerhetslogg:
    def __init__(self, filnavn):
        self.filnavn = filnavn
        self.oppføringer = []  # Liste for å lagre loggoppføringer

    def les_logg(self):
        with open(self.filnavn, "r") as f:
            self.oppføringer = f.readlines()

    def søk_etter_hendelse(self, søkeord):
        resultater = []
        for oppføring in self.oppføringer:
            if søkeord in oppføring:
                resultater.append(oppføring)
        return resultater

    def __repr__(self):
        return f"<Sikkerhetslogg: {self.filnavn}>"