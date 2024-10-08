python
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info("Program started")
        result = 10 / 0
    except ZeroDivisionError as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Program ended")

if __name__ == '__main__':
    main()