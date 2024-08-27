python
class Bil:
    def __init__(self, merke):
        self.merke = merke

    def kjør(self):
        print(f"{self.merke} kjører!")

min_bil = Bil("Tesla")
min_bil.kjør()