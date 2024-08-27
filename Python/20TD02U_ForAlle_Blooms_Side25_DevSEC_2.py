python
# Sikker kode: Bruk parameteriserte spørringer
cursor.execute("SELECT * FROM brukere WHERE brukernavn = %s", (brukernavn,))