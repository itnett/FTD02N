python
class MyClass:
    def method(self):
        pass

# Inspiser metoder
print(dir(MyClass))

# Dynamisk legge til en metode
def new_method(self):
    return "New Method"

MyClass.new_method = new_method

instance = MyClass()
print(instance.new_method())