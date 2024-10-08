python
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

# Opprette en indeks for å forbedre ytelsen til spørringer
cursor.execute('CREATE INDEX idx_navn ON elever (navn)')

# Sammenligne ytelsen med og uten indeks ved hjelp av EXPLAIN
cursor.execute('EXPLAIN QUERY PLAN SELECT * FROM elever WHERE navn = "Ola Nordmann"')
print(cursor.fetchall())

connection.close()