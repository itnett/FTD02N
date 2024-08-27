python
   class MyClass:
       def __init__(self, name):
           self.__name = name
       def get_name(self):
           return self.__name
   obj = MyClass("John")
   print(obj.get_name())