python
    class Kostnadskontroll:
        def __init__(self, faktiske_kostnader, budsjett):
            self.faktiske_kostnader = faktiske_kostnader
            self.budsjett = budsjett

        def kontroller_kostnader(self):
            return self.budsjett - self.faktiske_kostnader

    kontroll = Kostnadskontroll(75000, 80000)
    print(f"Tilgjengelig budsjett: {kontroll.kontroller_kostnader()}")