python
import hashlib
import os

def generate_salt():
    """
    Generer en salt-verdi for å sikre at like passord ikke får samme hash.
    """
    return os.urandom(16)  # Genererer 16 bytes med tilfeldig data

def hash_password(password, salt):
    """
    Hash et passord med SHA-256 og en salt-verdi.
    """
    return hashlib.sha256(salt + password.encode()).hexdigest()

def check_password(stored_hash, provided_password, salt):
    """
    Sjekk om det oppgitte passordet matcher den lagrede hash-verdien.
    """
    return stored_hash == hash_password(provided_password, salt)

def main():
    print("Welcome to Secure Password Storage!")
    
    # Få brukerpassord og generer salt
    password = input("Enter a password to store: ")
    salt = generate_salt()  # Generer en salt-verdi
    stored_hash = hash_password(password, salt)  # Hash passordet med saltet
    
    print(f"Your hashed password is: {stored_hash}")
    
    # Sjekk passord
    test_password = input("Re-enter your password to check: ")
    if check_password(stored_hash, test_password, salt):
        print("Password matched!")
    else:
        print("Password did not match!")

if __name__ == "__main__":
    main()