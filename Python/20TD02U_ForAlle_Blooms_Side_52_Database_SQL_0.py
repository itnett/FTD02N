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

# Legge til data
cursor.execute("INSERT INTO elever (navn, alder) VALUES ('Ola Nordmann', 16)")
cursor.execute("INSERT INTO elever (navn, alder) VALUES ('Kari Nordmann', 17)")

# Hente ut data
cursor.execute("SELECT * FROM elever")
print(cursor.fetchall())

# Oppdatere data
cursor.execute("UPDATE elever SET alder = 18 WHERE navn = 'Ola Nordmann'")

# Slette data
cursor.execute("DELETE FROM elever WHERE navn = 'Kari Nordmann'")

connection.commit()
connection.close()