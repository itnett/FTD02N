python
     class ManagedResource:
         def __enter__(self):
             print("Acquiring resource")
             return self

         def __exit__(self, exc_type, exc_val, exc_tb):
             print("Releasing resource")
             if exc_type:
                 print(f"Exception: {exc_val}")
                 return False  # Propagate the exception
             return True

     with ManagedResource():
         print("Using resource")
         raise ValueError("An error occurred")