python
# Fullstendig normalisering for en kompleks datamodell
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

# Definerer tabeller og deres relasjoner
cursor.execute('''
CREATE TABLE studenter (
    student_id INTEGER PRIMARY KEY,
    navn TEXT
)
''')

cursor.execute('''
CREATE TABLE kurs (
    kurs_id INTEGER PRIMARY KEY,
    kurs_navn TEXT,
    lærer_id INTEGER,
    FOREIGN KEY (lærer_id) REFERENCES lærere_3NF (

lærer_id)
)
''')

cursor.execute('''
CREATE TABLE student_kurs (
    student_id INTEGER,
    kurs_id INTEGER,
    PRIMARY KEY (student_id, kurs_id),
    FOREIGN KEY (student_id) REFERENCES studenter (student_id),
    FOREIGN KEY (kurs_id) REFERENCES kurs (kurs_id)
)
''')

# Legge til data i de normaliserte tabellene
cursor.execute("INSERT INTO studenter (navn) VALUES ('Ola Nordmann')")
cursor.execute("INSERT INTO kurs (kurs_navn, lærer_id) VALUES ('Matematikk', 1)")
cursor.execute("INSERT INTO student_kurs (student_id, kurs_id) VALUES (1, 1)")

connection.commit()
connection.close()