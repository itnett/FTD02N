python
def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError("Invalid input: must be a string")
    return user_input

try:
    user_data = validate_input(123)  # Dette vil kaste en feil
except ValueError as e:
    print(e)