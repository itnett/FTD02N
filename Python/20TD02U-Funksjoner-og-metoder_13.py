python
     def validate_input(data):
         if isinstance(data, str) and data.isalnum():
             return True
         return False

     print(validate_input("safe_input123"))  # Output: True
     print(validate_input("unsafe_input!@#"))  # Output: False