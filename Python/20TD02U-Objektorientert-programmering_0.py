python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

       def greet(self):
           return f"Hello, my name is {self.name} and I am {self.age} years old."

   # Opprette et objekt av klassen Person
   person1 = Person("Alice", 30)
   print(person1.greet())