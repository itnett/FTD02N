python
   class MyClass:
       def __init__(self, name):
           self.name = name
       def greet(self):
           return f"Hello, {self.name}"
   obj = MyClass("John")
   print(obj.greet())