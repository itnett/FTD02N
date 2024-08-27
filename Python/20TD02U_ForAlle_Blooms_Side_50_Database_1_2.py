python
# Eksempel på normalisering: Deling av tabellen elever for å eliminere redundans
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