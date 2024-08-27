python
# Evaluering av en datamodell basert på ER-diagrammet
def evaluer_datamodell(cursor):
    cursor.execute('PRAGMA foreign_key_list(Karakter)')
    result = cursor.fetchall()
    if not result:
        print("Tabellen Karakter har ingen utenlandske nøkler, noe som kan tyde på dårlig design.")
    else:
        print("Tabellen Karakter har riktige relasjoner.")

connection = sqlite3.connect('universitet.db')
cursor = connection.cursor()

evaluer_datamodell(cursor)

connection.close()