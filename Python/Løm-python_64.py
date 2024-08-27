python
    class Investering:
        def __init__(self, beløp, avkastning):
            self.beløp = beløp
            self.avkastning = avkastning

        def beregn_inntekt(self):
            return self.beløp * (1 + self.avkastning)

    investering = Investering(100000, 0.05)
    print(f"Fremtidig verdi: {investering.beregn_inntekt()}")