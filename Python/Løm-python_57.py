python
class FriKonkurranse:
    def __init__(self, antall_selgere, antall_kjøpere):
        self.antall_selgere = antall_selgere
        self.antall_kjøpere = antall_kjøpere

    def vis_info(self):
        return f"Antall Selgere: {self.antall_selgere}\nAntall Kjøpere: {self.antall_kjøpere}"

konkurranse = FriKonkurranse(100, 1000)
print(konkurranse.vis_info())