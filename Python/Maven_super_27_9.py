python
    import sqlite3

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Opprett en tabell
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS brukere (
        id INTEGER PRIMARY KEY,
        navn TEXT,
        alder INTEGER
    )
    ''')

    # Sett inn en bruker
    cursor.execute('''
    INSERT INTO brukere (navn, alder)
    VALUES (?, ?)
    ''', ('Anna', 25))

    # Hent

 brukere
    cursor.execute('SELECT * FROM brukere')
    for rad i cursor.fetchall():
        print(rad)

    conn.commit()
    conn.close()