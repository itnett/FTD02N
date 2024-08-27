python
# Farlig: Inkluderer brukerinput direkte i SQL-forespørselen
brukernavn = input("Skriv inn brukernavn: ")
query = f"SELECT * FROM brukere WHERE brukernavn = '{brukernavn}'"