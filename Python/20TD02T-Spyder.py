python
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import hashlib

# --- KONFIGURASJON OG DATABASEOPPRETTELSE ---
database_name = 'fagplan.db'

# Opprette en forbindelse til databasen (oppretter databasen hvis den ikke finnes)
conn = sqlite3.connect(database_name)
cursor = conn.cursor()

# --- OPPRETTELSE AV TABELLER OG INNSKYTING AV DATA ---
# Funksjon for å opprette tabeller
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

# Funksjon for å legge til data
def insert_data():
    # Legger til brukere
    users = [
        ('alice', hashlib.sha256('password123'.encode()).hexdigest(), 'alice@example.com'),
        ('bob', hashlib.sha256('password456'.encode()).hexdigest(), 'bob@example.com')
    ]
    cursor.executemany('INSERT INTO Users (username, password, email) VALUES (?, ?, ?)', users)

    # Legger til ordre
    orders = [
        (1, 'Laptop', 1),
        (2, 'Smartphone', 2),
        (1, 'Tablet', 3)
    ]
    cursor.executemany('INSERT INTO Orders (user_id, product, amount) VALUES (?, ?, ?)', orders)
    conn.commit()

# --- DATABASEVISUALISERING ---
# Funksjon for å hente og visualisere data
def visualize_data():
    query = '''
    SELECT Users.username, Orders.product, Orders.amount
    FROM Users
    JOIN Orders ON Users.user_id = Orders.user_id
    '''
    df = pd.read_sql_query(query, conn)

    # Visualiser data
    df.groupby('username').sum()['amount'].plot(kind='bar')
    plt.title('Total Orders by User')
    plt.xlabel('User')
    plt.ylabel('Total Orders')
    plt.show()

# --- BACKUP OG RESTORE ---
def backup_database():
    with open('backup.sql', 'w') as f:
        for line in conn.iterdump():
            f.write(f'{line}\n')

def restore_database():
    with open('backup.sql', 'r') as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()

# --- INDEKSERING OG OPTIMALISERING ---
def create_index():
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_user_id ON Orders(user_id)')
    conn.commit()

# --- SIKKERHET OG KRYPTIERING ---
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- EKSEKVERING AV FUNKSJONER ---
create_tables()
insert_data()
visualize_data()
backup_database()
create_index()

# Avslutt forbindelse
conn.close()