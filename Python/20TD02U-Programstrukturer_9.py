python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hei, jeg heter {self.name} og jeg er {self.age} år gammel.")

# Opprette et objekt
person1 = Person("Alice", 25)
person1.greet()  # Output: Hei, jeg heter Alice og jeg er 25 år gammel.