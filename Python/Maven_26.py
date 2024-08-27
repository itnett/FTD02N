python
import sqlite3

# Koble til databasen
conn = sqlite3.connect('Okonomistyring.db')
cursor = conn.cursor()

# Utføre en SQL-spørring
cursor.execute("SELECT AccountName, BudgetAmount FROM Budget WHERE Year = 2024;")

# Hente alle resultater
rows = cursor.fetchall()

# Vise resultatene
for row in rows:
    print(f"Account: {row[0]}, Budget: {row[1]}")

# Lukk forbindelsen
conn.close()