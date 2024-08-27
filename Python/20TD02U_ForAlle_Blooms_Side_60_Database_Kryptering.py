python
# Skript for å verifisere at alle data i kolonnen er kryptert
cursor.execute("SELECT AES_DECRYPT(personnummer, %s) FROM brukere", ('hemmelignøkkel',))
resultater = cursor.fetchall()

for rad i resultater:
    hvis rad[0] er None:
        print("Feil: Funnet ukryptert data!")
    ellers:
        print("Alle data er kryptert.")