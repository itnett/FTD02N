python
   def get_user_input():
       """Get and validate user input as an integer."""
       while True:
           try:
               value = int(input("Enter an integer: "))
               return value
           except ValueError:
               print("Invalid input. Please enter a valid integer.")

   user_input = get_user_input()
   print("You entered:", user_input)