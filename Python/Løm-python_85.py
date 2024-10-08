python
     class Employee:
         def __init__(self, name, position):
             self.name = name
             self.position = position
             self.subordinates = []

         def add_subordinate(self, subordinate):
             self.subordinates.append(subordinate)

     # Hierarchical organization example
     ceo = Employee('Alice', 'CEO')
     manager = Employee('Bob', 'Manager')
     staff1 = Employee('Charlie', 'Staff')
     staff2 = Employee('David', 'Staff')

     ceo.add_subordinate(manager)
     manager.add_subordinate(staff1)
     manager.add_subordinate(staff2)