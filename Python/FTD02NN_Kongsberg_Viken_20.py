python
import sqlite3

conn = sqlite3.connect('eksempel.db')
c = conn.cursor()

# Legge inn data
c.execute('''
          INSERT INTO kunder (navn, adresse)
          VALUES ('Ola Nordmann', 'Oslo, Norge')
          ''')

conn.commit()
conn.close()