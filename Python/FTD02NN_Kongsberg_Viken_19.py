python
import sqlite3

# Koble til (eller opprette) en database
conn = sqlite3.connect('eksempel.db')

# Opprette en cursor
c = conn.cursor()

# Opprette en tabell
c.execute('''
          CREATE TABLE IF NOT EXISTS kunder
          (id INTEGER PRIMARY KEY,
          navn TEXT,
          adresse TEXT)
          ''')

# Lukk tilkoblingen
conn.commit()
conn.close()