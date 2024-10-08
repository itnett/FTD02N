python
# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    """
    This function takes a list of numbers as input 
    and returns the average.
    """
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

# Main part of the program
if __name__ == "__main__":
    # Get user input (a list of numbers)
    data = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(x) for x in data.split()]

    # Calculate and print the average
    result = calculate_average(numbers)
    print(f"The average of the numbers is: {result}")