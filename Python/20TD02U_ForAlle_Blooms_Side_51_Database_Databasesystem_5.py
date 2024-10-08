python
import matplotlib.pyplot as plt
import mysql.connector

def fetch_data():
    cnx = mysql.connector.connect(user='root', password='yourpassword', host='localhost', database='skole')
    cursor = cnx.cursor()
    cursor.execute("SELECT navn, alder FROM elever")
    data = cursor.fetchall()
    cursor.close()
    cnx.close()
    return data

data = fetch_data()
navn, alder = zip(*data)
plt.bar(navn, alder)
plt.xlabel('Navn')
plt.ylabel('Alder')
plt.title('Elev Alder Visualisering')
plt.show()