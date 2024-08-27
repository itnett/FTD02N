python
import sqlite3

def safe_query(user_input):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Parameterisert spørring
    cursor.execute("SELECT * FROM users WHERE name=?", (user_input,))
    results = cursor.fetchall()
    
    conn.close()
    return results