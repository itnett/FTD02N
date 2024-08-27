python
def is_valid_username(username):
    import re
    # Bruk regex for å validere brukernavn
    pattern = r'^[a-zA-Z0-9_]+$'
    return re.match(pattern, username)

user_input = "valid_username123"
if is_valid_username(user_input):
    print("Valid username")
else:
    print("Invalid username")