python
import sqlite3

conn = sqlite3.connect('eksempel.db')
c = conn.cursor()

# Hente data
c.execute('SELECT * FROM kunder')
kunder = c.fetchall()

for kunde in kunder:
    print(kunde)

conn.close()