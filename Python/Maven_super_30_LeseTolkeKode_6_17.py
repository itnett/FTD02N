python
import sqlite3
from datetime import datetime

def backup_database(db_name, backup_dir):
    """
    Sikkerhetskopierer en SQLite-database til en fil.
    """
    conn = sqlite3.connect(db_name)
    backup_name = f"{backup_dir}/backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.db"
    
    with open(backup_name, 'w') as backup_file:
        for line in conn.iterdump():
            backup_file.write('%s\n' % line)
    
    print(f"Backup created: {backup_name}")
    conn.close()

def create_user(db_name, username, password):
    """
    Oppretter en ny bruker i en SQLite-database.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Oppretter brukertabellen hvis den ikke eksisterer
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    ''')
    
    # Legger til brukeren
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    print(f"User {username} created.")
    conn.close()

def main():
    db_name = "example.db"
    backup_dir = "backups"
    
    # Oppretter en bruker og deretter en sikkerhetskopi
    create_user(db_name, "newuser", "password123")
    backup_database(db_name, backup_dir)

if __name__ == "__main__":
    main()