python
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

# Legge til data
cursor.execute("INSERT INTO elever (navn, alder) VALUES ('Ola Nordmann', 16)")
cursor.execute("INSERT INTO elever (navn, alder) VALUES ('Kari Nordmann', 17)")

# Hente ut data
cursor.execute("SELECT * FROM elever")
print(cursor.fetchall())

connection.commit()
connection.close()