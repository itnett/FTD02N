bash
# Bruk sqlmap for å utføre en SQL-injeksjonstest på en applikasjon
sqlmap -u "http://localhost/sårbar_applikasjon?parameter=verdi" --dbs