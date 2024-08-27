python
   try:
       print(10 / 0)
   except ZeroDivisionError:
       print("You cannot divide by zero!")
   finally:
       print("This block is always executed.")