python
# Modifisert tabell for å oppfylle 1NF (ingen flere verdier i en enkelt celle)
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE elever_1NF (
    id INTEGER PRIMARY KEY,
    navn TEXT,
    klasse TEXT,
    lærer TEXT
)
''')

cursor.execute("INSERT INTO elever_1NF (navn, klasse, lærer) VALUES ('Ola Nordmann', '10A', 'Lærer A')")
cursor.execute("INSERT INTO elever_1NF (navn, klasse, lærer) VALUES ('Kari Nordmann', '10B', 'Lærer B')")
cursor.execute("INSERT INTO elever_1NF (navn, klasse, lærer) VALUES ('Per Hansen', '10A', 'Lærer A')")

connection.commit()
connection.close()