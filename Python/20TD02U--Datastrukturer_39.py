python
def process_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
        else:
            total -= num
    return total

numbers = [1, 2, 3, 4, 5]
result = process_numbers(numbers)
print(result)  # Output: -3