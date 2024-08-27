python
# Eksempel på normalisering til 3NF ved å eliminere transitive avhengigheter
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

# Anta at vi har en situasjon hvor lærere har en avdelingsavhengighet som er transitive
cursor.execute('''
CREATE TABLE avdelinger (
    avdeling_id INTEGER PRIMARY KEY,
    avdeling_navn TEXT
)
''')

# Oppdater lærere tabellen for å inkludere avdeling_id
cursor.execute('''
CREATE TABLE lærere_3NF (
    lærer_id INTEGER PRIMARY KEY,
    lærer_navn TEXT,
    avdeling_id INTEGER,
    FOREIGN KEY (avdeling_id) REFERENCES avdelinger (avdeling_id)
)
''')

# Opprette en normalisert elever tabell i 3NF
cursor.execute('''
CREATE TABLE elever_3NF (
    id INTEGER PRIMARY KEY,
    navn TEXT,
    klasse_id INTEGER,
    FOREIGN KEY (klasse_id) REFERENCES klasser (klasse_id)
)
''')

# Legge til data i de normaliserte tabellene
cursor.execute("INSERT INTO avdelinger (avdeling_navn) VALUES ('Matematikk')")
cursor.execute("INSERT INTO lærere_3NF (lærer_navn, avdeling_id) VALUES ('Lærer A', 1)")

cursor.execute("INSERT INTO elever_3NF (navn, klasse_id) VALUES ('Ola Nordmann', 1)")

connection.commit()
connection.close()