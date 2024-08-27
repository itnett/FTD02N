python
# Original funksjon
def calculate_sum(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum

# Refaktorert funksjon
def calculate_sum(numbers):
    return sum(numbers)