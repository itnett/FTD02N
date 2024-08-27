python
class Motor:
    def start(self):
        return "Motoren starter..."

class Bil:
    def __init__(self, merke, modell):
        self.merke = merke
        self.modell = modell
        self.motor = Motor()  # Bil inneholder en Motor

    def start(self):
        return self.motor.start()

min_bil = Bil("Tesla", "Model S")
print(min_bil.start())  # Utdata: Motoren starter...