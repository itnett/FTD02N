python
class Bruker:
    def __init__(self, navn, epost, passord):
        self.navn = navn
        self.epost = epost
        self._passord = passord  # Private attributt

    def endre_passord(self, nytt_passord):
        self._passord = nytt_passord

    def vis_info(self):
        print(f"Navn: {self.navn}, E-post: {self.epost}")

# Opprette en ny bruker og vise informasjon
bruker1 = Bruker("Ola Nordmann", "ola@nordmann.no", "hemmelig")
bruker1.vis_info()
bruker1.endre_passord("nytt_passord")