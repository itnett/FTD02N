python
   from abc import ABC, abstractmethod
   class Animal(ABC):
       @abstractmethod
       def sound(self):
           pass
   class Dog(Animal):
       def sound(self):
           return "Bark"
   dog = Dog()
   print(dog.sound())