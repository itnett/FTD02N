python
    class Rekruttering:
        def __init__(self, stilling, kandidater):
            self.stilling = stilling
            self.kandidater = kandidater

        def velg_kandidat(self):
            return f"Valgt kandidat for {self.stilling}: {self.kandidater[0]}"

    rekruttering = Rekruttering("Utvikler", ["Anne", "Kari", "Per"])
    print(rekruttering.velg_kandidat())