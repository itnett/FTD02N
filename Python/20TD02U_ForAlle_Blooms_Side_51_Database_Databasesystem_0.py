python
import sqlite3

# Opprette en enkel SQLite-database og tabell
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE elever (
    id INTEGER PRIMARY KEY,
    navn TEXT,
    alder INTEGER
)
''')

connection.commit()
connection.close()