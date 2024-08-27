python
class Frihandel:
    def __init__(self, land1, land2, handelsverdi):
        self.land1 = land1
        self.land2 = land2
        self.handelsverdi = handelsverdi

    def vis_info(self):
        return f"Handel mellom: {self.land1} og {self.land2}\nHandelsverdi: {self.handelsverdi} millioner"

handel = Frihandel("Norge", "Sverige", 200)
print(handel.vis_info())