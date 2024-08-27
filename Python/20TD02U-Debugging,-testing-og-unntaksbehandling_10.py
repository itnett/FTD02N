python
import logging

logging.basicConfig(level=logging.DEBUG)

class Calculator:
    def add(self, a, b):
        logging.debug(f"Adding {a} and {b}")
        return a + b

    def subtract(self, a, b):
        logging.debug(f"Subtracting {b} from {a}")
        return a - b

    def multiply(self, a, b):
        logging.debug(f"Multiplying {a} and {b}")
        return a * b

    def divide(self, a, b):
        try:
            logging.debug(f"Dividing {a} by {b}")
            return a / b
        except ZeroDivisionError as e:
            logging.error(f"Error: {e}")
            return "Cannot divide by zero"

if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(1, 2))
    print(calc.subtract(4, 2))
    print(calc.multiply(3, 3))
    print(calc.divide(10, 2))
    print(calc.divide(10, 0))