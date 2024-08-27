python
     # Beskytte mot SQL-injeksjon
     import sqlite3

     def get_user(username):
       conn = sqlite3.connect('example.db')
       cursor = conn.cursor()
       cursor.execute("SELECT * FROM users WHERE username=?", (username,))
       return cursor.fetchone()