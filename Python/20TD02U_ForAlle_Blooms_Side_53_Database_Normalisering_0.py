python
import sqlite3

# Ikke-normalisert tabell
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE elever (
    id INTEGER PRIMARY KEY,
    navn TEXT,
    klasse TEXT,
    lærer TEXT
)
''')

cursor.execute("INSERT INTO elever (navn, klasse, lærer) VALUES ('Ola Nordmann', '10A', 'Lærer A')")
cursor.execute("INSERT INTO elever (navn, klasse, lærer) VALUES ('Kari Nordmann', '10B', 'Lærer B')")
cursor.execute("INSERT INTO elever (navn, klasse, lærer) VALUES ('Per Hansen', '10A', 'Lærer A')")

connection.commit()
connection.close()