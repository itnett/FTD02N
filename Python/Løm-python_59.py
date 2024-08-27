python
    class Økonomistyring:
        def __init__(self, inntekter, utgifter):
            self.inntekter = inntekter
            self.utgifter = utgifter

        def beregn_resultat(self):
            return self.inntekter - self.utgifter

    bedrift = Økonomistyring(1000000, 750000)
    print(f"Resultat: {bedrift.beregn_resultat()}")