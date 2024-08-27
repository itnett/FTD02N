python
class Bil:
    def __init__(self, merke, modell, år):
        self.merke = merke
        self.modell = modell
        self.år = år
    
    def beskrivelse(self):
        return f"{self.år} {self.merke} {self.modell}"

min_bil = Bil("Tesla", "Model S", 2020)
print(min_bil.beskrivelse())  # Utskrift: 2020 Tesla Model S