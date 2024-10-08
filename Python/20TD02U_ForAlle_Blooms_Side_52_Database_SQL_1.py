python
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

# Filtrere data med WHERE
cursor.execute("SELECT * FROM elever WHERE alder > 16")

# Sortere data med ORDER BY
cursor.execute("SELECT * FROM elever ORDER BY navn ASC")

# Begrense resultater med LIMIT
cursor.execute("SELECT * FROM elever ORDER BY alder DESC LIMIT 1")

print(cursor.fetchall())

connection.close()