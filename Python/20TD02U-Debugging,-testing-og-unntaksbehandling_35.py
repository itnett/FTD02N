python
   def divide(a, b):
       try:
           return a / b
       except ZeroDivisionError:
           return "Cannot divide by zero"

   print(divide(10, 2))  # Output: 5.0
   print(divide(10, 0))  # Output: Cannot divide by zero