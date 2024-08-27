python
from Crypto.Cipher import AES
import base64
import mysql.connector
import matplotlib.pyplot as plt

def encrypt(data, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    padded_data = data + (16 - len(data) % 16) * ' '
    encrypted = base64.b64encode(cipher.encrypt(padded_data.encode('utf-8')))
    return encrypted.decode('utf-8')

# Kryptering av sensitiv data og lagring i MySQL
cnx = mysql.connector.connect(user='root', password='yourpassword', host='localhost', database='skole')
cursor = cnx.cursor()
key = "ThisIsASecretKey"

cursor.execute("INSERT INTO elever (navn, alder, personnummer) VALUES (%s, %s, %s)", 
               ("Ola Nordmann", 16, encrypt("12345678910", key)))

cnx.commit()
cursor.close()
cnx.close()

# Datavisualisering av elevdata
def fetch_elev_data():
    cnx = mysql.connector.connect(user='root', password='yourpassword', host='localhost', database='skole')
    cursor = cnx.cursor()
    cursor.execute("SELECT navn, alder FROM elever")
    data = cursor.fetchall()
    cursor.close()
    cnx.close()
    return data

elev_data = fetch_elev_data()
navn, alder = zip(*elev_data)
plt.bar(navn, alder)
plt.xlabel('Navn')
plt.ylabel('Alder')
plt.title('Elev Alder Visualisering')
plt.show()