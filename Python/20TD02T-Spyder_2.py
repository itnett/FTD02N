python
   def insert_data():
       users = [
           ('alice', hashlib.sha256('password123'.encode()).hexdigest(), 'alice@example.com'),
           ('bob', hashlib.sha256('password456'.encode()).hexdigest(), 'bob@example.com')
       ]
       cursor.executemany('INSERT INTO Users (username, password, email) VALUES (?, ?, ?)', users)

       orders = [
           (1, 'Laptop', 1),
           (2, 'Smartphone', 2),
           (1, 'Tablet', 3)
       ]
       cursor.executemany('INSERT INTO Orders (user_id, product, amount) VALUES (?, ?, ?)', orders)
       conn.commit()