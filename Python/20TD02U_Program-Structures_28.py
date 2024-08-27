python
# Import necessary libraries
import math

# Define functions for specific tasks
def calculate_area(radius):
    """Calculate the area of a circle given the radius."""
    return math.pi * radius ** 2

def calculate_circumference(radius):
    """Calculate the circumference of a circle given the radius."""
    return 2 * math.pi * radius

# Main function to execute the program
def main():
    radius = 5  # Radius of the circle
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)

    print(f"For a circle with radius {radius}:")
    print(f"Area is {area}")
    print(f"Circumference is {circumference}")

# Call the main function
if __name__ == "__main__":
    main()