python
  class Animal:
      def sound(self):
          return "Some sound"
  class Cat(Animal):
      def sound(self):
          return "Meow"
  my_cat = Cat()
  print(my_cat.sound())