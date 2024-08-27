python
import hashlib

def hash_password(password):
    # Hashes a password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(stored_hash, provided_password):
    # Checks if the provided password matches the stored hash
    return stored_hash == hash_password(provided_password)

def main():
    print("Welcome to Secure Password Storage!")
    
    # Get user password
    password = input("Enter a password to store: ")
    stored_hash = hash_password(password)
    
    print(f"Your hashed password is: {stored_hash}")
    
    # Check password
    test_password = input("Re-enter your password to check: ")
    if check_password(stored_hash, test_password):
        print("Password matched!")
    else:
        print("Password did not match!")

if __name__ == "__main__":
    main()