python
   def create_tables():
       cursor.execute('''
       CREATE TABLE IF NOT EXISTS Users (
           user_id INTEGER PRIMARY KEY,
           username TEXT NOT NULL,
           password TEXT NOT NULL,
           email TEXT NOT NULL
       )
       ''')
       cursor.execute('''
       CREATE TABLE IF NOT EXISTS Orders (
           order_id INTEGER PRIMARY KEY,
           user_id INTEGER,
           product TEXT NOT NULL,
           amount INTEGER,
           FOREIGN KEY(user_id) REFERENCES Users(user_id)
       )
       ''')
       conn.commit()