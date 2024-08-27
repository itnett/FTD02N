python
import os

# Sett miljøvariabler (gjerne gjort i systemet, ikke i koden)
# export DATABASE_URL="postgresql://bruker:passord@localhost/db"

database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise ValueError("DATABASE_URL miljøvariabel er ikke satt")

# Bruk database_url i applikasjonen
print(database_url)