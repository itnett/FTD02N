python
# Lagre dette som my_module.py
def greet(name):
    return f"Hei, {name}!"

# I en annen fil
import my_module

print(my_module.greet("Alice"))  # Output: Hei, Alice!