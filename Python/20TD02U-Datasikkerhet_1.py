python
   import sqlite3

   conn = sqlite3.connect('example.db')
   cursor = conn.cursor()

   # Parameterisert spørring for å forhindre SQL-injeksjon
   cursor.execute("SELECT * FROM users WHERE username=?", (user_input,))