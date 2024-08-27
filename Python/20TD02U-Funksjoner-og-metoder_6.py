python
class Bil:
    def __init__(self, merke, modell):
        self.merke = merke
        self.modell = modell

    def kjør(self):
        print(f"Bilen {self.merke} {self.modell} kjører!")

min_bil = Bil("Tesla", "Model S")
min_bil.kjør()  # Output: Bilen Tesla Model S kjører!