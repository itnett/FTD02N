python
     class Liquidity:
         def __init__(self, current_assets, current_liabilities):
             self.current_assets = current_assets
             self.current_liabilities = current_liabilities

         def current_ratio(self):
             return self.current_assets / self.current_liabilities

     liquidity_analysis = Liquidity(150000, 100000)
     print(f"Current Ratio: {liquidity_analysis.current_ratio()}")