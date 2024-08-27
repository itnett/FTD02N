python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subklasser må implementere denne metoden")

class Dog(Animal):
    def speak(self):
        return f"{self.name} sier woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} sier meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())