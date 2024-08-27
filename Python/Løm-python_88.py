python
     class Budget:
         def __init__(self, revenue, expenses):
             self.revenue = revenue
             self.expenses = expenses

         def net_income(self):
             return self.revenue - self.expenses

     annual_budget = Budget(100000, 80000)
     print(f"Net Income: {annual_budget.net_income()}")