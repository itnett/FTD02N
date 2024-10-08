python
   class Person:
       def __init__(self, name, age):
           self._name = name  # Protected attribute
           self.__age = age  # Private attribute

       def get_age(self):
           return self.__age

       def set_age(self, age):
           if age > 0:
               self.__age = age

   person1 = Person("Alice", 30)
   print(person1.get_age())
   person1.set_age(35)
   print(person1.get_age())