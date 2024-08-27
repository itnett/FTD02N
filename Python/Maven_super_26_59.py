python
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

brukernavn = input("Brukernavn: ")
passord = input("Passord: ")

# Unngå SQL-injeksjon ved å bruke parametere
cursor.execute("SELECT * FROM brukere WHERE brukernavn=? AND passord=?", (brukernavn, passord))
resultat = cursor.fetchone()

if resultat:
    print("Innlogging vellykket")
else:
    print("Innlogging mislyktes")

conn.close()