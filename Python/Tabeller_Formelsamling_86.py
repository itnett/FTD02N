python
import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users (id INT, name TEXT)''')

# Insert a row of data
c.execute("INSERT INTO users (id, name) VALUES (1, 'John Doe')")

# Commit the transaction
conn.commit()

# Optimize query using indexes
c.execute('''CREATE INDEX IF NOT EXISTS idx_user_id ON users (id)''')

# Fetch data
c.execute('SELECT * FROM users WHERE id=1')
print(c.fetchone())

# Close the connection
conn.close()