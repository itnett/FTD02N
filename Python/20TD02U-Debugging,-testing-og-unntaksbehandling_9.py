python
     class MyCustomError(Exception):
         pass

     try:
         raise MyCustomError("Something went wrong!")
     except MyCustomError as e:
         print(f"Custom Error: {e}")