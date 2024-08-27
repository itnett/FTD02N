python
    class MarketingCampaign:
        def __init__(self, name, budget, revenue):
            self.name = name
            self.budget = budget
            self.revenue = revenue

        def calculate_roi(self):
            return (self.revenue - self.budget) / self.budget * 100

    campaign = MarketingCampaign("Ny Produktlansering", 50000, 120000)
    roi = campaign.calculate_roi()
    print(f"ROI for {campaign.name} er {roi:.2f}%")