python
   class Animal:
       def speak(self):
           pass
   class Dog(Animal):
       def speak(self):
           return "Bark"
   class Cat(Animal):
       def speak(self):
           return "Meow"
   for animal in (Dog(), Cat()):
       print(animal.speak())