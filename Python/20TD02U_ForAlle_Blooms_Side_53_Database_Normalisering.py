python
# Evaluerer om en database er riktig normalisert
def evaluer_normalisering(cursor):
    cursor.execute('PRAGMA foreign_key_list(elever_3NF)')
    result = cursor.fetchall()
    if not result:
        print("Tabellen elever_3NF har ingen utenlandske nøkler, mulig mangel på normalisering.")
    else:
        print("Tabellen elever_3NF har riktige relasjoner.")
        
connection = sqlite3.connect('skole.db')
cursor = connection.cursor()

evaluer_normalisering(cursor)

connection.close()