python
     try:
         result = 10 / 2
     except ZeroDivisionError as e:
         print(f"Error: {e}")
     else:
         print(f"Result: {result}")
     finally:
         print("This will always execute")