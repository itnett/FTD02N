python
    def create_user(cursor, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute('''INSERT INTO users (username, password)
                          VALUES (?, ?)''', (username, hashed_password))

    def authenticate_user(cursor, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute('''SELECT * FROM users WHERE username=? AND password=?''', 
                       (username, hashed_password))
        return cursor.fetchone() is not None

    # Opprettelse og autentiseringseksempel
    conn = sqlite3.connect('organization.db')
    cursor = conn.cursor()

    create_user(cursor, 'admin', 'securepassword')
    authenticated = authenticate_user(cursor, 'admin', 'securepassword')

    if authenticated:
        print("Autentisering vellykket!")
    else:
        print("Autentisering mislyktes!")

    conn.commit()
    conn.close()