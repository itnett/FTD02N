python
import sqlite3

def finn_bruker(conn, brukernavn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM brukere WHERE brukernavn = ?", (brukernavn,))
    return cursor.fetchone()

# Eksempel på bruk
conn = sqlite3.connect('database.db')
bruker = finn_bruker(conn, 'admin')
print(bruker)