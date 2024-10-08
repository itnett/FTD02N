python
# Eksempel på å legge inn data i MongoDB
from pymongo import MongoClient

# Koble til MongoDB
client = MongoClient('localhost', 27017)
db = client['bedrift']
samling = db['ansatte']

# Sett inn dokumenter (tilsvarer rader i en SQL-tabell)
samling.insert_one({'ansatt_id': 1, 'navn': 'Ola Nordmann', 'stilling': 'Utvikler', 'lønn': 60000.00})

# Hent data
for ansatt in samling.find():
    print(ansatt)