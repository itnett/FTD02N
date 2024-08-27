python
import mysql.connector

# Kobling til MySQL-databasen
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ditt_passord",
    database="skole"
)

cursor = conn.cursor()

# Kryptere følsomme data ved innsats
kryptert_sql = "INSERT INTO brukere (id, navn, personnummer) VALUES (%s, %s, AES_ENCRYPT(%s, %s))"
data = (1, 'Kari Nordmann', '98765432101', 'hemmelignøkkel')
cursor.execute(kryptert_sql, data)
conn.commit()

# Dekryptere data ved henting
dekryptert_sql = "SELECT id, navn, AES_DECRYPT(personnummer, %s) FROM brukere"
cursor.execute(dekryptert_sql, ('hemmelignøkkel',))
resultat = cursor.fetchall()
for rad in resultat:
    print(rad)

conn.close()