python
   class Engine:
       def start(self):
           return "Engine started"

   class Car:
       def __init__(self):
           self.engine = Engine()

       def start(self):
           return self.engine.start()

   my_car = Car()
   print(my_car.start())