python
    import sqlite3

    # Opprette en databaseforbindelse
    conn = sqlite3.connect('organization.db')
    cursor = conn.cursor()

    # Opprette en tabell
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                      (id INTEGER PRIMARY KEY, name TEXT, position TEXT, salary REAL)''')

    # Legge til en ny ansatt
    cursor.execute('''INSERT INTO employees (name, position, salary)
                      VALUES ('John Doe', 'Manager', 75000)''')

    # Hente ut data fra databasen
    cursor.execute('''SELECT * FROM employees''')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.commit()
    conn.close()