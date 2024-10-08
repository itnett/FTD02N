python
class NPV:
    def __init__(self, initial_investment, cash_flows, discount_rate):
        self.initial_investment = initial_investment
        self.cash_flows = cash_flows
        self.discount_rate = discount_rate

    def calculate_npv(self):
        npv = -self.initial_investment
        for t, cash_flow in enumerate(self.cash_flows, start=1):
            npv += cash_flow / ((1 + self.discount_rate) ** t)
        return npv

npv_calc = NPV(100000, [30000, 40000, 50000, 60000], 0.1)
print(f"NPV: {npv_calc.calculate_npv()}")