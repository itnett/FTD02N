python
    def calculate_npv(cash_flows, discount_rate):
        npv = sum([cf / (1 + discount_rate) ** i for i, cf in enumerate(cash_flows)])
        return npv

    cash_flows = [-100000, 30000, 40000, 50000, 60000]
    discount_rate = 0.1
    npv = calculate_npv(cash_flows, discount_rate)
    print(f"NPV: {npv}")