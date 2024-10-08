python
class Finansieringsplan:
    def __init__(self, egenkapital, lån, andre_kilder):
        self.egenkapital = egenkapital
        self.lån = lån
        self.andre_kilder = andre_kilder

    def total_finansiering(self):
        return self.egenkapital + self.lån + self.andre_kilder

plan = Finansieringsplan(300000, 200000, 50000)
print(f"Total Finansiering: {plan.total_finansiering()}")