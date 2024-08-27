python
# Bruk parameterisert SQL for å unngå SQL Injection
cursor.execute("SELECT * FROM brukere WHERE brukernavn = %s", (brukernavn,))