python
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

# Telle antall elever i hver klasse
cursor.execute('''
SELECT klasser.klasse_navn, COUNT(elever.id) AS antall_elever
FROM elever
INNER JOIN klasser ON elever.klasse_id = klasser.klasse_id
GROUP BY klasser.klasse_navn
''')

# Beregne gjennomsnittsalder per klasse
cursor.execute('''
SELECT klasser.klasse_navn, AVG(elever.alder) AS gjennomsnittsalder
FROM elever
INNER JOIN klasser ON elever.klasse_id = klasser.klasse_id
GROUP BY klasser.klasse_navn
''')

# Finne den eldste eleven i hver klasse
cursor.execute('''
SELECT klasser.klasse_navn, MAX(elever.alder) AS eldste_elev
FROM elever
INNER JOIN klasser ON elever.klasse_id = klasser.klasse_id
GROUP BY klasser.klasse_navn
''')

print(cursor.fetchall())

connection.close()