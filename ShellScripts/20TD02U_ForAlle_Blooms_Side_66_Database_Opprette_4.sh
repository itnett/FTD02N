bash
# Logg inn på MongoDB-serveren
mongo

# Opprett en database
use bibliotek;

# Opprett en samling
db.createCollection("bøker");

# Sett inn data i samlingen
db.bøker.insert({tittel: "Moby Dick", forfatter: "Herman Melville", publisert: 1851});

# Sjekk innholdet i samlingen
db.bøker.find();