python
   class Employee(Person):
       def __init__(self, name, age, employee_id):
           super().__init__(name, age)
           self.employee_id = employee_id

       def greet(self):
           return f"Hello, my name is {self.name}, I am {self.age} years old, and my employee ID is {self.employee_id}."

   employee1 = Employee("Bob", 25, "E123")
   print(employee1.greet())