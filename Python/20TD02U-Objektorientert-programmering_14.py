python
   class Animal:
       def sound(self):
           pass

   class Dog(Animal):
       def sound(self):
           return "Woof"

   class Cat(Animal):
       def sound(self):
           return "Meow"

   def make_sound(animal):
       print(animal.sound())

   dog = Dog()
   cat = Cat()
   make_sound(dog)
   make_sound(cat)