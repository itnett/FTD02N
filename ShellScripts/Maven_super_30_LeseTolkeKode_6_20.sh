bash
#!/bin/bash

# Generer en salt-verdi
generate_salt() {
    head -c 16 /dev/urandom | base64
}

# Hash et passord med SHA-256 og salt
hash_password() {
    local password=$1
    local salt=$2
    echo -n "$salt$password" | sha256sum | awk '{print $1}'
}

# Sjekk om passordet matcher hash
check_password() {
    local stored_hash=$1
    local provided_password=$2
    local salt=$3
    local hash=$(hash_password "$provided_password" "$salt")
    [ "$stored_hash" == "$hash" ]
}

# Hovedskript
main() {
    echo "Welcome to Secure Password Storage!"
    read -p "Enter a password to store: " password

    salt=$(generate_salt)
    stored_hash=$(hash_password "$password" "$salt")

    echo "Your hashed password is: $stored_hash"

    read -p "Re-enter your password to check: " test_password
    if check_password "$stored_hash" "$test_password" "$salt"; then
        echo "Password matched!"
    else
        echo "Password did not match!"
    fi
}

main