python
# Identifikasjon av primærnøkler (PK) og fremmednøkler (FK) i ER-diagrammet
entiteter_med_nøkler = {
    'Student': 'student_id (PK)',
    'Kurs': 'kurs_id (PK)',
    'Lærer': 'lærer_id (PK)',
    'Karakter': 'karakter_id (PK), student_id (FK), kurs_id (FK)'
}

print("Entiteter med Primær- og Fremmednøkler:")
for enhet, nøkler in entiteter_med_nøkler.items():
    print(f"- {enhet}: {nøkler}")