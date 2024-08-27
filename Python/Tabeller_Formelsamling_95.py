python
import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS users (id INT, name TEXT)''')

# Insert data
c.execute("INSERT INTO users (id, name) VALUES (1, 'John Doe')")
c.execute("INSERT INTO users (id, name) VALUES (2, 'Jane Smith')")

# Commit the transaction
conn.commit()

# Create an index to optimize queries
c.execute('''CREATE INDEX IF NOT EXISTS idx_user_id ON users (id)''')

# Perform an optimized query
c.execute('SELECT * FROM users WHERE id=1')
print(c.fetchone())

# Close the connection
conn.close()