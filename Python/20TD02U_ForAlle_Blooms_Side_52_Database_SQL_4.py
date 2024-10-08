python
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

# Finne elever som er eldre enn gjennomsnittsalderen i klassen deres
cursor.execute('''
SELECT navn, alder
FROM elever
WHERE alder > (
    SELECT AVG(alder)
    FROM elever AS e
    WHERE e.klasse_id = elever.klasse_id
)
''')

print(cursor.fetchall())

connection.close()