python
   class Dog:
       def speak(self):
           return "Woof!"

   class Cat:
       def speak(self):
           return "Meow!"

   class AnimalFactory:
       @staticmethod
       def get_animal(animal_type):
           if animal_type == 'dog':
               return Dog()
           elif animal_type == 'cat':
               return Cat()
           else:
               return None

   dog = AnimalFactory.get_animal('dog')
   print(dog.speak())
   cat = AnimalFactory.get_animal('cat')
   print(cat.speak())