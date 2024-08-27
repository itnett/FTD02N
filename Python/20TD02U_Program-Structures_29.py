python
def is_prime(num):
    """
    Checks if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    """
    The main function of the program.
    """
    numbers = [2, 3, 4, 5, 6, 7, 8, 9]
    prime_numbers = [num for num in numbers if is_prime(num)]
    print(f"Prime numbers in the list: {prime_numbers}")

if __name__ == "__main__":
    main()