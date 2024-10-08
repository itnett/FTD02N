python
import mysql.connector

# Koble til MySQL-databasen
conn = mysql.connector.connect(
    host="localhost",
    user="begrenset_bruker",
    password="sterkt_passord",
    database="skole"
)

cursor = conn.cursor()

# Bruk parameterisert SQL for å beskytte mot SQL-injeksjon
student_id = 1
cursor.execute("SELECT navn, fødselsdato FROM studenter WHERE id = %s", (student_id,))
resultat = cursor.fetchall()

for rad in resultat:
    print(rad)

conn.close()