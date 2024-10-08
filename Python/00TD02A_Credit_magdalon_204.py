python
   import math

   def calculate_free_fall(height):
       """Calculate the time and speed of an object in free fall."""
       g = 9.81  # Acceleration due to gravity in m/s^2
       if height < 0:
           raise ValueError("Height cannot be negative.")
       time = math.sqrt(2 * height / g)
       speed = g * time
       return time, speed

   try:
       height = float(input("Enter the height (in meters): "))
       time, speed = calculate_free_fall(height)
       print(f"The object will hit the ground in {time:.2f} seconds at a speed of {speed:.2f} m/s.")
   except ValueError as e:
       print(f"Invalid input: {e}")