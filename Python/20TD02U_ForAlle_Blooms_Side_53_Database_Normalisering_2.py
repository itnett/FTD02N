python
# Splitte tabellen fra 1NF til 2NF
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

# Opprette separate tabeller for klasser og lærere for å eliminere delvis avhengighet
cursor.execute('''
CREATE TABLE klasser (
    klasse_id INTEGER PRIMARY KEY,
    klasse_navn TEXT
)
''')

cursor.execute('''
CREATE TABLE lærere (
    lærer_id INTEGER PRIMARY KEY,
    lærer_navn TEXT
)
''')

cursor.execute('''
CREATE TABLE elever_2NF (
    id INTEGER PRIMARY KEY,
    navn TEXT,
    klasse_id INTEGER,
    lærer_id INTEGER,
    FOREIGN KEY (klasse_id) REFERENCES klasser (klasse_id),
    FOREIGN KEY (lærer_id) REFERENCES lærere (lærer_id)
)
''')

# Legge til data i de normaliserte tabellene
cursor.execute("INSERT INTO klasser (klasse_navn) VALUES ('10A')")
cursor.execute("INSERT INTO klasser (klasse_navn) VALUES ('10B')")
cursor.execute("INSERT INTO lærere (lærer_navn) VALUES ('Lærer A')")
cursor.execute("INSERT INTO lærere (lærer_navn) VALUES ('Lærer B')")

cursor.execute("INSERT INTO elever_2NF (navn, klasse_id, lærer_id) VALUES ('Ola Nordmann', 1, 1)")
cursor.execute("INSERT INTO elever_2NF (navn, klasse_id, lærer_id) VALUES ('Kari Nordmann', 2, 2)")
cursor.execute("INSERT INTO elever_2NF (navn, klasse_id, lærer_id) VALUES ('Per Hansen', 1, 1)")

connection.commit()
connection.close()