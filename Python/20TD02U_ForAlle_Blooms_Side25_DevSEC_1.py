python
# Farlig kode: Brukerinput inkludert direkte i SQL-spørringen
brukernavn = input("Skriv inn brukernavn: ")
query = f"SELECT * FROM brukere WHERE brukernavn = '{brukernavn}'"