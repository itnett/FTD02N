python
# Lesson 1.2: Estimation

# Rounding to nearest ten
def round_to_nearest_ten(number):
    return round(number / 10) * 10

# Rounding to nearest hundred
def round_to_nearest_hundred(number):
    return round(number / 100) * 100

# Input
number = int(input("Enter a number: "))

# Perform rounding
print(f"Rounded to nearest ten: {round_to_nearest_ten(number)}")
print(f"Rounded to nearest hundred: {round_to_nearest_hundred(number)}")