python
    def main():
        # Programstruktur med hovedfunksjon
        greet_user()
        number = get_number_from_user()
        result = calculate_square(number)
        print_result(result)

    def greet_user():
        print("Velkommen til programmet!")

    def get_number_from_user():
        return int(input("Skriv inn et tall: "))

    def calculate_square(n):
        return n * n

    def print_result(result):
        print(f"Kvadratet av tallet er: {result}")

    if __name__ == "__main__":
        main()