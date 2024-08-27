python
# Import necessary modules
import math  # To perform mathematical operations
import functools  # For higher-order functions like reduce
import itertools  # For creating iterators for efficient looping
import logging  # For logging information
from typing import List, Dict, Tuple  # For type annotations

# Setting up logging
logging.basicConfig(level=logging.DEBUG)

# Example 1: Using print statement to display text (Concept 1)
print("Welcome to the Python 100 Concepts Tutorial!")

# Example 2: Variables and data types (Concepts 2, 3)
a = 5  # int
b = 3.14  # float
name = "Python"  # str
is_python_fun = True  # bool

# Example 3: Type conversion (Concept 4)
a_to_str = str(a)  # Convert int to string
b_to_int = int(b)  # Convert float to int

# Example 4: String concatenation and methods (Concepts 6, 7)
welcome_message = "Hello, " + name + "! Welcome to learning Python."
print(welcome_message.upper())  # Convert to uppercase

# Example 5: Taking user input (Concept 8)
user_name = input("Enter your name: ")

# Example 6: If, elif, else statements (Concepts 17, 18, 19)
if len(user_name) > 5:
    print(f"Welcome, {user_name}! Your name is quite long.")
elif len(user_name) == 5:
    print(f"Welcome, {user_name}! Your name is exactly 5 characters long.")
else:
    print(f"Welcome, {user_name}! You have a short and sweet name.")

# Example 7: Functions with default, keyword, and variable-length arguments (Concepts 26, 28, 30)
def greet_user(name="Guest", *args, **kwargs):
    """Greets the user with optional args and kwargs."""
    greeting = f"Hello, {name}!"
    print(greeting)
    if args:
        print("Additional arguments:", args)
    if kwargs:
        print("Keyword arguments:", kwargs)

greet_user(user_name, "Python", level="beginner")

# Example 8: Lambda functions, map, filter, and reduce (Concepts 34, 35, 36, 37)
numbers = [1, 2, 3, 4, 5]

# Using lambda to square numbers
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# Using filter to get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

# Using reduce to get the product of numbers
product = functools.reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)

# Example 9: List comprehension (Concept 40)
cubes = [x ** 3 for x in numbers]
print("Cubes using list comprehension:", cubes)

# Example 10: Dictionary comprehension (Concept 41)
number_dict = {x: x ** 2 for x in numbers}
print("Dictionary of squares:", number_dict)

# Example 11: Set comprehension (Concept 42)
unique_numbers = {x for x in numbers}
print("Unique numbers using set comprehension:", unique_numbers)

# Example 12: Working with files - Reading and writing (Concepts 45, 46)
with open('example.txt', 'w') as f:
    f.write("Hello, Python learners!\nThis is an example file.")

with open('example.txt', 'r') as f:
    content = f.read()
    print("File content:", content)

# Example 13: Error handling (try, except, finally) (Concepts 48, 49)
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("Execution completed.")

# Example 14: Classes, objects, inheritance, polymorphism (Concepts 54, 55, 60, 61)
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

# Example 15: Using decorators to add functionality (Concept 66)
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Example 16: Using context managers (Concept 67)
with open('example.txt', 'a') as f:
    f.write("This line is added using a context manager.")

# Example 17: Type annotations for functions (Concept 68)
def add_numbers(x: int, y: int) -> int:
    return x + y

print("Adding 5 and 10:", add_numbers(5, 10))

# Example 18: Generators and yield (Concepts 43, 44)
def countdown(num):
    while num > 0:
        yield num
        num -= 1

for i in countdown(5):
    print(i)

# Example 19: Using assertions (Concept 53)
assert a > 0, "a should be greater than 0"

# Example 20: Logging (Concept 52)
logging.info("This is an informational message.")

# Example 21: Magic methods (Concept 64)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

book = Book("1984", "George Orwell")
print(book)

# Example 22: Properties (Concept 65)
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(f"Temperature in Fahrenheit: {temp.fahrenheit}")

# Example 23: List slicing (Concept 77)
sliced_list = numbers[1:4]
print("Sliced list:", sliced_list)

# Example 24: Zip function (Concept 75)
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]
combined = list(zip(names, scores))
print("Combined using