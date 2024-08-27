python
import matplotlib.pyplot as plt
import sqlite3

# Koble til databasen
conn = sqlite3.connect('min_database.db')
cursor = conn.cursor()

# Hent data
cursor.execute('SELECT år, salg FROM salgstall')
data = cursor.fetchall()

# Forbered data for plotting
år = [row[0] for row in data]
salg = [row[1] for row in data]

# Lag visualiseringen
plt.figure(figsize=(10, 6))
plt.bar(år, salg, color='skyblue')
plt.xlabel('År')
plt.ylabel('Salg')
plt.title('Salgstall per år')
plt.grid(axis='y', alpha=0.75)

# Vis visualiseringen
plt.show()

# Lukk databaseforbindelsen
conn.close()