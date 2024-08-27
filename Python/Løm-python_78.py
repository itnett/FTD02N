python
     class CostControl:
         def __init__(self, budget):
             self.budget = budget
             self.actual_expenses = 0

         def add_expense(self, amount):
             self.actual_expenses += amount

         def is_over_budget(self):
             return self.actual_expenses > self.budget

     project = CostControl(50000)
     project.add_expense(20000)
     project.add_expense(35000)
     print(f"Over budget: {project.is_over_budget()}")