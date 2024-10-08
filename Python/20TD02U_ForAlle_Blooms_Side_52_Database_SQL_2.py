python
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

# Opprette flere tabeller og relasjoner
cursor.execute('''
CREATE TABLE klasser (
    klasse_id INTEGER PRIMARY KEY,
    klasse_navn TEXT
)
''')

cursor.execute('''
CREATE TABLE fag (
    fag_id INTEGER PRIMARY KEY,
    fag_navn TEXT
)
''')

cursor.execute('''
CREATE TABLE elever (
    id INTEGER PRIMARY KEY,
    navn TEXT,
    alder INTEGER,
    klasse_id INTEGER,
    fag_id INTEGER,
    FOREIGN KEY (klasse_id) REFERENCES klasser (klasse_id),
    FOREIGN KEY (fag_id) REFERENCES fag (fag_id)
)
''')

# Koble tabellene sammen med INNER JOIN
cursor.execute('''
SELECT elever.navn, klasser.klasse_navn, fag.fag_navn
FROM elever
INNER JOIN klasser ON elever.klasse_id = klasser.klasse_id
INNER JOIN fag ON elever.fag_id = fag.fag_id
''')

print(cursor.fetchall())

connection.close()