python
     # oop_example.py
     class Animal:
         def __init__(self, name):
             self.name = name

         def speak(self):
             raise NotImplementedError("Subclasses must implement this method")

     class Dog(Animal):
         def speak(self):
             return f"{self.name} says Woof!"

     class Cat(Animal):
         def speak(self):
             return f"{self.name} says Meow!"

     if __name__ == "__main__":
         animals = [Dog("Rex"), Cat("Whiskers")]
         for animal in animals:
             print(animal.speak())