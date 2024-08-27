# Opprett en testbruker
sudo useradd testbruker

# Gi testbrukeren et passord
sudo passwd testbruker

# Bytt til testbrukeren
su - testbruker

# Opprett en testfil
touch testfil.txt

# Gi eieren skrivetilgang
chmod u+w testfil.txt

# Fjern skrivetilgang for gruppen og andre
chmod g-w,o-w testfil.txt