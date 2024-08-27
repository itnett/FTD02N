python
class BreakEvenPoint:
    def __init__(self, faste_kostnader, pris_per_enhet, variable_kostnader_per_enhet):
        self.faste_kostnader = faste_kostnader
        self.pris_per_enhet = pris_per_enhet
        self.variable_kostnader_per_enhet = variable_kostnader_per_enhet

    def beregn_break_even(self):
        return self.faste_kostnader / (self.pris_per_enhet - self.variable_kostnader_per_enhet)

bep = BreakEvenPoint(50000, 100, 60)
print(f"Break-Even Point (enheter): {bep.beregn_break_even()}")