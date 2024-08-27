python
class Bil:
    def __init__(self, merke, modell, årgang):
        self.merke = merke
        self.modell = modell
        self.årgang = årgang
    
    def beskrivelse(self):
        return f"{self.årgang} {self.merke} {self.modell}"

min_bil = Bil("Tesla", "Model S", 2020)
print(min_bil.beskrivelse())  # Utdata: 2020 Tesla Model S