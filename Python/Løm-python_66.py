python
    class Leder:
        def __init__(self, navn):
            self.navn = navn

        def motiver_ansatte(self):
            print(f"{self.navn} motiverer ansatte gjennom anerkjennelse og belønninger.")

    leder = Leder("Ola")
    leder.motiver_ansatte()